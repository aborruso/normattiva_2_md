#!/usr/bin/env python3
"""
Script per scaricare e convertire documenti da URL Normattiva
Estrae i parametri dalla pagina e scarica il documento in formato Akoma Ntoso
"""

import argparse
import sys
import os
import re
import requests
from datetime import datetime
from convert_akomantoso import convert_akomantoso_to_markdown_improved

def extract_params_from_normattiva_url(url, session=None):
    """
    Scarica la pagina normattiva e estrae i parametri necessari per il download

    Args:
        url: URL della norma su normattiva.it
        session: sessione requests da usare (opzionale)

    Returns:
        tuple: (params dict, session)
    """
    print(f"Caricamento pagina {url}...")

    if session is None:
        session = requests.Session()

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'it-IT,it;q=0.9,en;q=0.8'
    }

    try:
        response = session.get(url, headers=headers, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Errore nel caricamento della pagina: {e}")
        return None, session

    html = response.text

    # Estrai parametri dagli input hidden usando regex
    params = {}

    # Cerca atto.dataPubblicazioneGazzetta
    match_gu = re.search(r'name="atto\.dataPubblicazioneGazzetta"[^>]*value="([^"]+)"', html)
    if match_gu:
        # Converti da formato YYYY-MM-DD a YYYYMMDD
        date_str = match_gu.group(1).replace('-', '')
        params['dataGU'] = date_str

    # Cerca atto.codiceRedazionale
    match_codice = re.search(r'name="atto\.codiceRedazionale"[^>]*value="([^"]+)"', html)
    if match_codice:
        params['codiceRedaz'] = match_codice.group(1)

    # Cerca la data di vigenza dall'input visibile
    match_vigenza = re.search(r'<input[^>]*value="(\d{2}/\d{2}/\d{4})"[^>]*>', html)
    if match_vigenza:
        # Converti da formato DD/MM/YYYY a YYYYMMDD
        date_parts = match_vigenza.group(1).split('/')
        params['dataVigenza'] = f"{date_parts[2]}{date_parts[1]}{date_parts[0]}"
    else:
        # Usa data odierna se non trovata
        params['dataVigenza'] = datetime.now().strftime('%Y%m%d')

    if not all(k in params for k in ['dataGU', 'codiceRedaz', 'dataVigenza']):
        print("Errore: impossibile estrarre tutti i parametri necessari")
        print(f"Parametri trovati: {params}")
        return None, session

    return params, session

def download_akoma_ntoso(params, output_path, session=None):
    """
    Scarica il documento Akoma Ntoso usando i parametri estratti

    Args:
        params: dizionario con dataGU, codiceRedaz, dataVigenza
        output_path: percorso dove salvare il file XML
        session: sessione requests da usare (opzionale)

    Returns:
        bool: True se il download è riuscito
    """
    url = f"https://www.normattiva.it/do/atto/caricaAKN?dataGU={params['dataGU']}&codiceRedaz={params['codiceRedaz']}&dataVigenza={params['dataVigenza']}"

    print(f"Download Akoma Ntoso da: {url}")

    if session is None:
        session = requests.Session()

    # Simula un browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'it-IT,it;q=0.9,en;q=0.8',
        'Referer': 'https://www.normattiva.it/'
    }

    try:
        response = session.get(url, headers=headers, timeout=30, allow_redirects=True)
        response.raise_for_status()

        # Verifica che sia XML
        if response.content[:5] == b'<?xml' or b'<akomaNtoso' in response.content[:500]:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"✅ File XML salvato in: {output_path}")
            return True
        else:
            print(f"❌ Errore: la risposta non è un file XML valido")
            # Salva comunque per debug
            debug_path = output_path + '.debug.html'
            with open(debug_path, 'wb') as f:
                f.write(response.content)
            print(f"   Risposta salvata in: {debug_path}")
            return False

    except requests.RequestException as e:
        print(f"❌ Errore durante il download: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description='Scarica e converte documenti Normattiva da URL',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Esempi d'uso:

  # Conversione diretta a Markdown
  python fetch_from_url.py "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2022;53" -o output.md

  # Salva solo XML
  python fetch_from_url.py "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2022;53" --xml-only -o document.xml
        """
    )

    parser.add_argument('url', help='URL della norma su normattiva.it')
    parser.add_argument('-o', '--output', required=True, help='File di output (MD o XML)')
    parser.add_argument('--xml-only', action='store_true',
                       help='Salva solo il file XML senza convertire in Markdown')
    parser.add_argument('--keep-xml', action='store_true',
                       help='Mantieni il file XML temporaneo dopo la conversione')

    args = parser.parse_args()

    # Estrai parametri dalla pagina (usa una sessione condivisa)
    params, session = extract_params_from_normattiva_url(args.url)
    if not params:
        sys.exit(1)

    print(f"\nParametri estratti:")
    print(f"  dataGU: {params['dataGU']}")
    print(f"  codiceRedaz: {params['codiceRedaz']}")
    print(f"  dataVigenza: {params['dataVigenza']}\n")

    # Determina il percorso del file XML
    if args.xml_only:
        xml_path = args.output
    else:
        # Crea un file temporaneo
        xml_path = f"temp_{params['codiceRedaz']}.xml"

    # Scarica il file Akoma Ntoso usando la stessa sessione
    if not download_akoma_ntoso(params, xml_path, session):
        sys.exit(1)

    # Converti in Markdown se richiesto
    if not args.xml_only:
        print(f"\nConversione in Markdown...")
        success = convert_akomantoso_to_markdown_improved(xml_path, args.output)

        if success:
            print(f"✅ Conversione completata: {args.output}")

            # Rimuovi il file XML temporaneo se non richiesto di mantenerlo
            if not args.keep_xml:
                try:
                    os.remove(xml_path)
                    print(f"File XML temporaneo rimosso")
                except OSError as e:
                    print(f"Attenzione: impossibile rimuovere il file temporaneo: {e}")
        else:
            print(f"❌ Errore durante la conversione")
            sys.exit(1)

    print("\n✅ Operazione completata con successo!")

if __name__ == "__main__":
    main()

# VERIFICATION_TASKS.md - Task di Verifica per l'Output Markdown

Questo documento elenca i task di verifica e i punti da controllare nell'output Markdown generato dal tool, al fine di assicurare la massima fedeltà al testo consolidato delle norme su Normattiva.it.

## Punti da Verificare nell'Output Markdown

### 1. Intestazioni "Capo" e "Sezione"

- **Problema:** Le intestazioni come "Capo I PRINCIPI GENERALI" o "Sezione II" appaiono nel Markdown, ma potrebbero non essere presenti o essere presentate diversamente nella visualizzazione consolidata di Normattiva. Questo è dovuto al fatto che il file Akoma Ntoso include una struttura più dettagliata rispetto alla visualizzazione web.
- **Task:** Valutare se queste intestazioni debbano essere rimosse, modificate (es. rimuovendo "Capo" o "Sezione" dal testo dell'intestazione) o gestite in modo diverso per allinearsi alla leggibilità del testo consolidato.

### 2. Testo Abrogato/Non Consolidato (es. "Ai fini del presente codice si intende")

- **Problema:** Frasi o blocchi di testo che non sono presenti nella versione consolidata della norma su Normattiva (perché abrogati o modificati) appaiono ancora nel Markdown. L'esempio specifico è "Ai fini del presente codice si intende per: 0a) AgID: ...". Questo indica che la logica di filtraggio attuale non è sufficientemente robusta per tutti i casi di testo non consolidato.
- **Task:** Migliorare la funzione `clean_text_content` in `convert_akomantoso.py` per identificare e filtrare in modo più efficace il testo abrogato o non pertinente alla versione consolidata. Potrebbe essere necessario analizzare pattern più complessi o la struttura circostante nel file Akoma Ntoso.

### 3. Testo Mancante (es. "Sulla proposta del Ministro per le politiche comunitarie")

- **Problema:** Alcune parti del preambolo o altri blocchi di testo visibili sulla pagina web di Normattiva non sono presenti nell'output Markdown. L'esempio specifico è "Sulla proposta del Ministro per le politiche comunitarie". Questo suggerisce che il parser Akoma Ntoso di `tulit` (o la nostra logica di estrazione dal XML) potrebbe non catturare tutti gli elementi del preambolo o altri blocchi di testo che Normattiva include nella sua visualizzazione.
- **Task:** Indagare se questi elementi mancanti sono presenti nel file Akoma Ntoso scaricato e, in caso affermativo, modificare `convert_akomantoso.py` per estrarli e includerli correttamente nel Markdown. Se non sono presenti nell'Akoma Ntoso, potrebbe essere una limitazione del formato o del parser di `tulit`.

## Priorità

Si consiglia di affrontare i task nell'ordine elencato, partendo dalle modifiche più semplici e dirette per poi passare a quelle che richiedono un'analisi più approfondita della struttura del documento.

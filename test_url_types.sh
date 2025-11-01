#!/bin/bash

# Script di test per verificare fetch_from_url.py con diversi tipi di atti normativi

set -e

echo "🧪 Test Fetch da URL Normattiva.it"
echo "=================================="
echo ""

# Crea directory per output test
mkdir -p test_output

# Test 1: Legge
echo "Test 1: Legge 53/2022"
python3 fetch_from_url.py \
  "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2022;53" \
  -o test_output/legge_53_2022.md
echo "✅ Legge convertita"
echo ""

# Test 2: Decreto Legislativo (versione vigente)
echo "Test 2: Decreto Legislativo 36/2006 (vigente)"
python3 fetch_from_url.py \
  "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2006-01-24;36!vig" \
  -o test_output/dlgs_36_2006.md
echo "✅ Decreto Legislativo convertito"
echo ""

# Test 3: Decreto Legge
echo "Test 3: Decreto Legge 93/2013"
python3 fetch_from_url.py \
  "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2013-08-14;93" \
  -o test_output/dl_93_2013.md
echo "✅ Decreto Legge convertito"
echo ""

# Test 4: Salva solo XML
echo "Test 4: Salva solo XML (CAD - Decreto Legislativo 82/2005)"
python3 fetch_from_url.py \
  "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82" \
  --xml-only -o test_output/cad.xml
echo "✅ XML salvato"
echo ""

# Test 5: Mantieni XML
echo "Test 5: Converti mantenendo XML"
python3 fetch_from_url.py \
  "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2013-10-15;119" \
  -o test_output/legge_119_2013.md --keep-xml
echo "✅ Markdown e XML salvati"
echo ""

# Statistiche
echo "📊 Statistiche dei test"
echo "======================"
echo ""

for file in test_output/*.md; do
  if [ -f "$file" ]; then
    filename=$(basename "$file")
    lines=$(wc -l < "$file")
    articles=$(grep -c "^# Art\." "$file" || echo "0")
    echo "$filename: $lines righe, $articles articoli"
  fi
done

echo ""
echo "✅ Tutti i test completati con successo!"
echo ""
echo "Output salvati in: test_output/"

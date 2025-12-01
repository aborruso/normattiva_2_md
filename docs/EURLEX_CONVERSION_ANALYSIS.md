# EUR-Lex XHTML to Markdown Conversion Analysis

**Date**: 2024-11-20  
**Document**: Direttiva (UE) 2024/1385 - Violenza contro le donne e violenza domestica  
**CELEX**: 32024L1385

## Executive Summary

Analisi comparativa di 3 tool per convertire documenti EUR-Lex da XHTML a Markdown. **Risultato: html2text è la soluzione vincente** per qualità output e leggibilità.

---

## Test Effettuati

### Documento di Test
- **Fonte**: EUR-Lex XHTML (italiano)
- **URL**: http://publications.europa.eu/resource/oj/L_202401385.ITA.xhtml.L_202401385IT.html
- **Dimensione**: 4514+ righe di contenuto normativo complesso
- **Caratteristiche**: Considerando numerati, articoli, tabelle layout, note a piè di pagina

---

## Risultati Comparativi

| Tool | Righe Output | Qualità | Tabelle | Note |
|------|--------------|---------|---------|------|
| **html2text** | 3,255 | ⭐⭐⭐⭐⭐ | Ignorate | Perfette |
| pandoc | 4,514 | ⭐ | ASCII frammentate | Corrotte |
| markitdown | 1,442 | ⭐⭐ | Markdown verbose | Corrette |

---

## 1. html2text (WINNER ✅)

### Comando
```bash
html2text --ignore-tables --ignore-images --unicode-snob file.xhtml > output.md
```

### Output Quality
```markdown
(1)

Scopo della presente direttiva è fornire un quadro giuridico generale in grado
di prevenire e combattere efficacemente la violenza contro le donne e la
violenza domestica in tutta l'Unione. A tal fine essa rafforza e introduce
misure in relazione a: la definizione dei reati e delle pene irrogabili, la
protezione delle vittime e l'accesso alla giustizia, l'assistenza alle
vittime, una migliore raccolta di dati, la prevenzione, il coordinamento e la
cooperazione.  
  
(2)

La parità tra donne e uomini e la non discriminazione sono valori e diritti
fondamentali dell'Unione sanciti rispettivamente dall'articolo 2 del trattato
sull'Unione europea (TUE) e dagli articoli 21 e 23 della Carta dei diritti
fondamentali dell'Unione europea («Carta»). La violenza contro le donne e la
violenza domestica minacciano tali stessi valori e diritti...
```

### Pro
✅ Testo fluido e leggibile  
✅ Numerazione considerando preservata  
✅ Note a piè pagina corrette `(1)`, `(2)`, etc.  
✅ Nessuna tabella ASCII corrotta  
✅ Conversione rapida (~2 secondi)  
✅ Formato standard markdown pulito

### Contro
❌ Non supporta URL diretti (richiede download preliminare)  
❌ Richiede flag specifici per qualità ottimale

### Raccomandazione
**SOLUZIONE CONSIGLIATA** - Qualità eccellente, zero post-processing richiesto.

---

## 2. pandoc

### Comando
```bash
pandoc file.xhtml -o output.md
```

### Output Quality
```markdown
+---+-----------------------------------------------------+-------------+
| ! | Gazzetta ufficiale\                                 | IT          |
| [ | dell\'Unione europea                                |             |
| E |                                                     | Serie L     |
| u |                                                     |             |
| r |                                                     |             |
| o |                                                     |             |
| p |                                                     |             |
| a |                                                     |             |
| n |                                                     |             |
|   |                                                     |             |
| f |                                                     |             |
| l |                                                     |             |
| a |                                                     |             |
| g |                                                     |             |
```

### Pro
✅ Supporta molti formati  
✅ Tool ben conosciuto

### Contro
❌ Tabelle ASCII illeggibili (ogni carattere su riga separata!)  
❌ Output verbose (4514 righe vs 3255 di html2text)  
❌ Richiede post-processing pesante  
❌ Non adatto per layout EUR-Lex

### Raccomandazione
**NON RACCOMANDATO** - Output inutilizzabile per documenti EUR-Lex.

---

## 3. markitdown

### Comando
```bash
# Da file locale
markitdown file.xhtml > output.md

# Da URL (supportato!)
markitdown "http://example.com/doc.xhtml" > output.md
```

### Output Quality
```markdown
|  |  |
| --- | --- |
| (1) | Scopo della presente direttiva è fornire un quadro giuridico... |

|  |  |
| --- | --- |
| (2) | La parità tra donne e uomini e la non discriminazione sono... |

|  |  |
| --- | --- |
| (3) | La violenza contro le donne e la violenza domestica... |
```

### Pro
✅ Supporta URL diretti (no download preliminare)  
✅ Note a piè pagina corrette  
✅ Contenuto completo preservato

### Contro
❌ Output verbose con tabelle markdown ripetitive  
❌ Ogni considerando in tabella `| --- | --- |`  
❌ Scarsa leggibilità per documenti lunghi  
❌ Output 3x più compresso ma meno user-friendly

### Raccomandazione
**ALTERNATIVA ACCETTABILE** - Utile se serve download diretto da URL, ma qualità inferiore.

---

## Raccomandazione Finale

### Per EUR-Lex Integration

**Workflow Consigliato:**

```bash
# Step 1: Download XHTML
python scripts/download_eurlex.py {CELEX} --format xhtml --lang IT --output doc.xhtml

# Step 2: Convert to Markdown
html2text --ignore-tables --ignore-images --unicode-snob doc.xhtml > doc.md

# Optional: Cleanup temp file
rm doc.xhtml
```

**Alternativa con pipe (se html2text supporta stdin):**
```bash
curl -s "http://publications.europa.eu/.../doc.html" | \
  html2text --ignore-tables --ignore-images --unicode-snob > doc.md
```

---

## Implementation Notes

### html2text Flags Spiegati

| Flag | Scopo |
|------|-------|
| `--ignore-tables` | Salta tabelle di layout EUR-Lex (preserva solo contenuto) |
| `--ignore-images` | Rimuove riferimenti immagini/loghi |
| `--unicode-snob` | Usa caratteri Unicode nativi (', ", –) invece di entità HTML |

### Dependencies Required

```bash
# Install html2text
pip install html2text
```

**Versione testata**: `html2text 2024.2.26`

---

## Performance Metrics

| Metrica | html2text | pandoc | markitdown |
|---------|-----------|--------|------------|
| Tempo conversione | ~2s | ~3s | ~5s |
| Dimensione output | 156KB | 232KB | 70KB |
| Leggibilità umana | ⭐⭐⭐⭐⭐ | ⭐ | ⭐⭐⭐ |
| Post-processing richiesto | Nessuno | Pesante | Moderato |

---

## Conclusioni

1. **html2text** è la soluzione ottimale per EUR-Lex
2. Workflow in 2 step (download + convert) è accettabile
3. Qualità output eccellente senza post-processing
4. Nessun parser XML custom necessario (risparmio settimane di sviluppo)
5. Pronto per integrazione in `eurlex2md` CLI

---

## Next Steps

- [ ] Integrare html2text in `scripts/download_eurlex.py`
- [ ] Creare wrapper CLI `eurlex2md`
- [ ] Aggiungere test con documenti campione
- [ ] Documentare workflow in `docs/EUR-LEX_INTEGRATION.md`

---

**Autore**: Analisi conversione automatica  
**Versione**: 1.0  
**Status**: ✅ Raccomandazione approvata

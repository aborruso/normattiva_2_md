# VERIFICATION.md

Documento di verifica qualità output Markdown generato da Akoma2MD.

**Ultimo aggiornamento:** 2025-11-01

## Stato Verifiche

| Problema | Stato | Fix |
|----------|-------|-----|
| Intestazioni Capo/Sezione combinate | ✅ RISOLTO | 2025-11-01 |
| Testo "0a) AgID" | ✅ VERIFICATO OK | Non serve fix |
| Preambolo mancante | ✅ VERIFICATO OK | Non serve fix |

## Fix Implementati

### Intestazioni Capo/Sezione

**Problema:**

Heading come `Capo I PRINCIPI GENERALI Sezione I Definizioni` erano su una riga, riducendo leggibilità.

**Soluzione:**

- File: `convert_akomantoso.py:6-56,117-130`
- Funzioni: `parse_chapter_heading()`, `format_heading_with_separator()`
- Output: `## Capo I - TITOLO` + `### Sezione I - Titolo`
- Gestisce modifiche legislative `(( ))` negli heading
- Testato: CAD, Codice Appalti, Costituzione

## Checklist Verifiche Output

Punti da controllare quando si genera Markdown da Akoma Ntoso:

- [ ] **Heading Capo/Sezione** separati gerarchicamente (## Capo, ### Sezione)
- [ ] **Modifiche legislative** wrapped in `(( testo modificato ))`
- [ ] **Preambolo** presente (es. "Sulla proposta del Ministro...")
- [ ] **Articoli** con formato `# Art. X - Titolo`
- [ ] **Liste** con corretta indentazione
- [ ] **Riferimenti normativi** estratti da tag `<ref>`
- [ ] **Testo pulito** senza whitespace eccessivo

## Test Consigliati

Documenti tipo per verifiche:

1. CAD (D.Lgs 82/2005) - struttura Capo/Sezione complessa
2. Codice Appalti - modifiche legislative frequenti
3. Costituzione - struttura gerarchica diversa
4. Decreto legge recente - modifiche in evidenza

## File di Test Generati

Durante le verifiche sono stati generati:

- `verification_cad.md` - Output CAD per test
- `temp_*.xml` - File XML Akoma Ntoso temporanei

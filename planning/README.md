# 📁 Planning Directory

Questa directory contiene la pianificazione dettagliata per le feature future di normattiva2md.

## 📂 Contenuto

### api-programmabile/
**Status**: ✅ Pianificazione completa  
**Data**: 2025-12-04  
**Effort**: 14-21 ore  

Pianificazione completa per rendere normattiva2md usabile come libreria Python da notebook e script, mantenendo 100% compatibilità CLI.

**Quick Start**: Leggi [`api-programmabile/SUMMARY.md`](api-programmabile/SUMMARY.md)

**Documenti**:
- 📄 [SUMMARY.md](api-programmabile/SUMMARY.md) - Executive summary
- 📚 [INDEX.md](api-programmabile/INDEX.md) - Indice navigazione completo
- 🏗️ [01-architecture.md](api-programmabile/01-architecture.md) - Design architetturale
- 📝 [02-api-specification.md](api-programmabile/02-api-specification.md) - Specifiche API
- 📦 [03-models.md](api-programmabile/03-models.md) - Dataclasses
- ⚠️ [04-exceptions.md](api-programmabile/04-exceptions.md) - Sistema eccezioni
- 🚀 [05-implementation-plan.md](api-programmabile/05-implementation-plan.md) - Piano 6 fasi
- 💡 [06-examples.md](api-programmabile/06-examples.md) - 11 esempi completi

**Deliverables**:
- 3 nuovi file Python (exceptions, models, api)
- 3 file test
- 4 esempi + Jupyter notebook
- Documentazione completa

**Next**: Review → Implementazione Fase 1

---

## 🗂️ Struttura Planning

```
planning/
├── README.md                    # Questo file
└── api-programmabile/           # API Python usabile da notebook
    ├── SUMMARY.md               # Executive summary
    ├── INDEX.md                 # Indice navigazione
    ├── README.md                # Overview
    ├── 01-architecture.md       # Architettura
    ├── 02-api-specification.md  # Specifiche API
    ├── 03-models.md             # Dataclasses
    ├── 04-exceptions.md         # Eccezioni
    ├── 05-implementation-plan.md # Piano 6 fasi
    └── 06-examples.md           # Esempi completi
```

---

## 📊 Status Overview

| Feature | Status | Docs | Effort | Priority |
|---------|--------|------|--------|----------|
| API Programmabile | ✅ Planned | 9 files, 3279 righe | 14-21h | Alta |

---

## 🎯 Prossime Feature da Pianificare

Idee future (da discutere):

- [ ] **Supporto EUR-Lex** - Conversione documenti UE
- [ ] **CLI interattivo** - TUI con selezione documenti
- [ ] **Cache intelligente** - Ridurre download ripetuti
- [ ] **Diff tra versioni** - Confronto versioni normative
- [ ] **Export formati multipli** - PDF, DOCX, HTML
- [ ] **Plugin system** - Estensioni custom

---

## 📝 Template Pianificazione

Quando pianifichi una nuova feature, usa questa struttura:

```
planning/<feature-name>/
├── SUMMARY.md              # Executive summary
├── INDEX.md                # Navigazione
├── README.md               # Overview
├── 01-requirements.md      # Requisiti
├── 02-design.md            # Design
├── 03-architecture.md      # Architettura
├── 04-implementation.md    # Piano implementazione
└── 05-examples.md          # Esempi
```

---

## 🔗 Link Utili

- **Progetto**: [normattiva_2_md](../)
- **Docs**: [../docs/](../docs/)
- **Source**: [../src/normattiva2md/](../src/normattiva2md/)
- **Tests**: [../tests/](../tests/)
- **Changelog**: [../LOG.md](../LOG.md)

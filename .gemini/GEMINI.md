# Metodologia di Lavoro con Gemini CLI

Questo documento descrive la metodologia di lavoro adottata durante l'interazione con l'agente Gemini CLI per lo sviluppo del progetto `normattiva_2_md`.

## 1. Agente CLI Interattivo

L'interazione avviene tramite un'interfaccia a riga di comando, dove l'agente risponde a richieste specifiche, esegue operazioni e fornisce feedback in tempo reale.

## 2. Workflow Orientato al Task

Il processo di sviluppo segue un ciclo iterativo:

- Comprensione: L'agente analizza la richiesta dell'utente e il contesto del progetto (file esistenti, obiettivi).

- Pianificazione: Viene formulato un piano conciso per affrontare il task, spesso includendo l'uso di strumenti specifici.

- Implementazione: L'agente esegue le azioni pianificate utilizzando gli strumenti disponibili (operazioni su file, comandi shell, interazioni Git).

- Verifica: I risultati vengono verificati, spesso con il feedback diretto dell'utente o tramite l'analisi dell'output generato.

- Iterazione/Raffinamento: Sulla base della verifica, il processo si ripete per affinare la soluzione o affrontare nuovi task.

## 3. Utilizzo degli Strumenti

L'agente utilizza una suite di strumenti per interagire con il filesystem, eseguire comandi shell, e gestire il controllo versione:

- Operazioni su File: Lettura, scrittura, modifica e ridenominazione di file (`read_file`, `write_file`, `replace`, `mv`).

- Comandi Shell: Esecuzione di comandi di sistema (`run_shell_command`) per operazioni come la creazione di directory, la rimozione di file, o l'interazione con Git.

- Operazioni Git: Gestione del repository (`git init`, `git add`, `git commit`, `git push`, `git status`, `git log`).

- Web Fetching: Recupero di contenuti da URL (`web_fetch`) per analisi o download (es. `tulit` per Normattiva).

## 4. Collaborazione con l'Utente

La collaborazione è un aspetto centrale. L'agente si basa sulle istruzioni esplicite dell'utente e sul feedback per guidare lo sviluppo. Le decisioni chiave e i cambiamenti di strategia vengono discussi e approvati dall'utente.

## 5. Specificità e Adattabilità

L'agente si adatta alle esigenze specifiche del progetto, come dimostrato dalla capacità di:

- Rifinire la qualità dell'output Markdown basandosi su requisiti dettagliati (es. gestione delle righe vuote, filtraggio del testo abrogato).

- Modificare la pipeline di elaborazione (es. passaggio da XML diretto a JSON intermedio e poi ritorno a XML diretto) per ottimizzare i risultati.

## 6. Documentazione del Progetto

Durante lo sviluppo, viene mantenuta una documentazione aggiornata per tracciare i progressi e le decisioni:

- `LOG.md`: Registro cronologico degli avanzamenti e delle modifiche significative. **Nota: I log dovrebbero essere concisi, focalizzandosi sui punti chiave e sulle decisioni, evitando dettagli eccessivi.**

- `README.md`: Descrizione generale del progetto, istruzioni di installazione e utilizzo.

- `PRD.md`: Documento dei requisiti di prodotto, che evolve con la comprensione degli obiettivi.

- `VERIFICATION.md`: Checklist e stato verifiche qualità output Markdown.
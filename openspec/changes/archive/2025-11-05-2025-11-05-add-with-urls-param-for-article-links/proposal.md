# Aggiunta parametro with_urls per link markdown agli articoli citati su normattiva.it

## Descrizione
In corrispondenza di una legge citata e di un determinato articolo, inserisce il link markdown http alla pagina con l’articolo della legge su normattiva.it. La struttura degli URL è documentata in docs/URL_NORMATTIVA.md. Il link viene generato per ogni citazione di legge e articolo.

## Motivazione
Permette di arricchire la conversione con riferimenti diretti agli articoli citati, migliorando la navigabilità e la verifica delle fonti.

## Esempio
Se nel testo viene citato "art. 2 della legge 53/2022", il markdown generato sarà:

[art. 2 della legge 53/2022](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2022;53~art2)

## Note
- La generazione degli URL segue le regole di docs/URL_NORMATTIVA.md
- Il parametro sarà opzionale (with_urls)

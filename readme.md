# Secure Hash Algorithms aka SHA

Le funzioni **SHA** sono una famiglia di funzioni hash crittografiche utilizzate principalmente nell'ambito della **crittografia**, per validare se i dati sono stati modificati e quindi nel contesto della sicurezza. Sono anche impiegate in **protocolli di criptovaluta**, come la blockchain di Bitcoin, per generare la chiave privata del wallet. Sono usate anche per le **password**, in modo che il server contenga solo l'hash della password: in questo modo, se un aggressore rubasse il contenuto del database, non potrebbe ricavare la password originale.
Viene usata anche nel processo di **hadshake** nei protocolli della crittografia TLS/SSL cosi che si possano condividere le chiavi tra i partecipanti.
Questo algoritmo è quindi molto utilizzato e importante al giorno d'oggi.

![](https://www.simplilearn.com/ice9/free_resources_article_thumb/hashing1.PNG)

## cosa è una funzione hash 
una funzione hash è una funzione che si comporta come una funzione **one way** cioè che per ottenere l'output da questa funzione è facile ma ottenere l'input dall'output è difficile senza conoscere altre informazioni.
La funzione hash modifica il testo utilizzato come input rendendolo senza senso agli occhi umani, questo è chiamato **digest** (di solito l'output è sotto forma esadecimale).
 altre tre caratteristiche dell'hash function sono:
  1. **Comportarsi come un algoritmo deterministico** cioè che a meno che non si cambia il testo dell'input il digest rimmarrà sempre lo stesso.
  2. **Non Linearità** cioè che se si cambiasse anche solo un carattere dell'input, **il digest deve cambiare completamente**. 
  3. **Il digest della funzione sha deve sempre avere una lunghezza fissa** questova in  base a quale SHA si è usato.

  all'interno della funzione i blocchi vengono processati sempre il doppio della lunghezza del digest 

### links 

- https://en.wikipedia.org/wiki/SHA-2#Pseudocode

- https://stackoverflow.com/questions/7321694/sha-256-implementation-in-python

- https://medium.com/@domspaulo/python-implementation-of-sha-256-from-scratch-924f660c5d57
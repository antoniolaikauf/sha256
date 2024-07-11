# Secure Hash Algorithms aka sha

L a funzione **sha** sono una famiglia di funzioni hash crittografiche usate sopratutto nell'ambito della crittografia, nel validare se i dati sono stati modificati quindi nell'ambito della sicurezza, ma anche in portocolli di cripto come nella blockchain in bitcoin per generare la chiave privata del wallet, può essere utilizzata anche nelle password in modo tale che il server contenga solo l'hash della password cosi che se un aggressore rubi il contenuto dal database non potra ricavare la password.
quindi questo algoritmo è molto utilizzato e importante al giorno d'oggi 

## cosa è una funzione hash 
una funzione hash è una funzione che si comporta come una funzione **one way** cioè che ottenere l'output da questa funzione è facile ma ottenere l'input dall'output è difficile senza sapere altre informazioni.
la funzione hash modifica il testo che viene messo come input rendendolo senza senso ad occhio umano chiamato **digest** (di solito l'output è sotto forma esadecimale) altre due caratteristiche dell'hash function è che si comporta come un **algoritmo deterministico** cioè che a meno che non si cambia il testo dell'input il digest rimmarrà sempre quello, l'altra caratteristica è che deve fornira la **non linearità** cioè che se si cambiasse anche solo un carattere dell'input, **il digest deve cambiare completaente**



### links 

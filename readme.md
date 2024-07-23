# Secure Hash Algorithms aka SHA

Le funzioni **SHA** sono una famiglia di funzioni hash crittografiche utilizzate principalmente nell'ambito della **crittografia**, per validare se i dati sono stati modificati e quindi nel contesto della sicurezza. Sono anche impiegate in **protocolli di criptovaluta**, come la blockchain di Bitcoin, per generare la chiave privata del wallet. Sono usate anche per le **password**, in modo che il server contenga solo l'hash della password: in questo modo, se un aggressore rubasse il contenuto del database, non potrebbe ricavare la password originale.
Viene usata anche nel processo di **hadshake** nei protocolli della crittografia TLS/SSL cosi che si possano condividere le chiavi tra i partecipanti.
Questo algoritmo è quindi molto utilizzato e importante al giorno d'oggi.

![](https://www.simplilearn.com/ice9/free_resources_article_thumb/hashing1.PNG)

## Cosa è una funzione hash 
una funzione hash è una funzione che si comporta come una funzione **one way** cioè che per ottenere l'output da questa funzione è facile ma ottenere l'input dall'output è difficile senza conoscere altre informazioni.
La funzione hash modifica il testo utilizzato come input rendendolo senza senso agli occhi umani, questo è chiamato **digest** (di solito l'output è sotto forma esadecimale).
 altre tre caratteristiche dell'hash function sono:
  1. **Comportarsi come un algoritmo deterministico** cioè che a meno che non si cambia il testo dell'input il digest rimmarrà sempre lo stesso.
  2. **Non Linearità** cioè che se si cambiasse anche solo un carattere dell'input, **il digest deve cambiare completamente**.\
  ![](img/Screenshot%202024-07-17%20151940.png)

  3. **Il digest della funzione sha deve sempre avere una lunghezza fissa** questova in  base a quale SHA si è usato.
  4. **resistenza alle collisioni** è una caratteristica molto importante questa perchè esiste un possibile attacco che si basa su un paradosso della matematica chiamato **paradosso del compleanno** [qui](https://it.wikipedia.org/wiki/Paradosso_del_compleanno).
  Questa è la formula del paradosso del compleanno
 ![](img/Screenshot%202024-07-11%20155229.png) 
 in cui 1 sarebbe la prima persona quindi avrà una probabilita di 365/365 e il blocco di destra calcola la probabilità che nessuna persona compi gli anni lo stesso giorno e sfrutta il **calcolo combinato** se si fa fatica a capire questo pezzo immaginatelo cosi\
 ![](img/Screenshot%202024-07-11%20161235.png) \
 in questo caso non è l'unga l'operazione ma se vorremmo fare un gruppo con più persone risulterebbe lunga . \
Quindi si usa questo paradosso del compleanno per indicare che le funzioni hash siano resistenti alle collisioni che significa che non ci deve essere nesun algoritmo efficiente che riesca a trovare una collisioni, le collisioni si hanno quando dati due input diversi si hanno lo stesso output/digest e questa cosa è molto pericolosa, \
se hash(A)=hash(B) e A≠B allora A e B sono una collisione. Nella hash function si ha una collisione dopo  $2^{n/2}$ o  $\sqrt{n}$  quindi se si usasse una SHA256 l'aggressore dovrebbe provare 340282366920938463463374607431768211456 quindi lo SHA256 è resistente alle collisioni


  all'interno della funzione i blocchi vengono processati sempre il doppio della lunghezza del digest 


Tutti i vari tipi di SHA sono stati pubblicati dal NIST \
![](img/Screenshot%202024-07-17%20145534.png)


### links 

- https://en.wikipedia.org/wiki/SHA-2#Pseudocode

- https://stackoverflow.com/questions/7321694/sha-256-implementation-in-python

- https://medium.com/@domspaulo/python-implementation-of-sha-256-from-scratch-924f660c5d57

- https://brilliant.org/wiki/secure-hashing-algorithms/

- https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf

per immagini componenti clicca [qui](img.md)
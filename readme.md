# Secure Hash Algorithms aka SHA

Secure Hash Algorithms aka SHA
The **SHA** functions are a family of cryptographic hash functions primarily used in the field of **cryptography** to validate data integrity and security. They are also employed in **cryptocurrency protocols**, like the Bitcoin blockchain, for generating wallet private keys. They are used for **passwords** as well, so that the server stores only the hash of the password: this way, if an attacker were to steal the database content, they couldn't retrieve the original password.
SHA is also used in the **handshake** process of TLS/SSL cryptographic protocols to share keys among participants.
This algorithm is thus very widely used and important today.

![](https://www.simplilearn.com/ice9/free_resources_article_thumb/hashing1.PNG)


## What is a hash function?
A hash function is a function that behaves like a **one-way function**, meaning that while it is easy to obtain the output from the function, it is difficult to obtain the input from the output without knowing additional information.
The hash function alters the input text, rendering it meaningless to human eyes; this output is called a digest (the output is usually in hexadecimal form).
Three other characteristics of hash functions are:

  1. Acting as a deterministic algorithm, meaning that unless the input text changes, the digest will always remain the same.
  2. Non-Linearity, meaning that even if just one character of the input is changed, the digest must change completely.\
  ![](img/Screenshot%202024-07-17%20151940.png)

  3. The SHA function digest must always have a fixed length, depending on which SHA is used.
  4. Collision resistance is a very important characteristic because there is a potential attack based on a mathematical paradox known as the birthday paradox [here](https://it.wikipedia.org/wiki/Paradosso_del_compleanno).\
  This is the formula for the birthday paradox: 
 ![](img/Screenshot%202024-07-11%20155229.png) 
where 1 would be the first person, so they would have a probability of 365/365, and the block on the right calculates the probability that no one has the same birthday, using combinatorial calculation. If this piece is hard to understand, imagine it like this:\
 ![](img/Screenshot%202024-07-11%20161235.png) \
In this case, the operation isn't lengthy, but if we wanted to do it with a larger group, it would be.
So, this birthday paradox is used to indicate that hash functions should be resistant to collisions, meaning there shouldn't be any efficient algorithm capable of finding collisions. Collisions occur when two different inputs yield the same output/digest, which is very dangerous.
If hash(A) = hash(B) and A ≠ B, then A and B are a collision. In a hash function, a collision occurs after $2^{n/2}$ or $\sqrt{n}$. So, if SHA256 is used, the attacker would need to try 340282366920938463463374607431768211456 times, thus SHA256 is collision-resistant.


Inside the function, blocks are always processed at twice the length of the digest.

The SHA256 function has a message length limit of **2<sup>64</sup> - 1**. This is because, during the padding process, 64 bits are added at the end, part of which indicates the message length, thus limiting the message to **2<sup>64</sup> - 1**. If the message were longer than 2<sup>64</sup> - 1, more than 64 bits would be added, resulting in incorrect padding.

All the various types of SHA have been published by NIST. \
![](img/Screenshot%202024-07-17%20145534.png)


### links 

- https://en.wikipedia.org/wiki/SHA-2#Pseudocode

- https://stackoverflow.com/questions/7321694/sha-256-implementation-in-python

- https://medium.com/@domspaulo/python-implementation-of-sha-256-from-scratch-924f660c5d57

- https://brilliant.org/wiki/secure-hashing-algorithms/

- https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf

For component images, click  [here](img.md)
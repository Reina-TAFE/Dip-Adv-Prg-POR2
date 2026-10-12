# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> All of these functions are hashing functions as they all can take an arbitrarily sized input, and map in onto a fixed sized output. 

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> ### SSH:
> Advantages:
> - Simple
> - High determinism since all inputs return the same output
> - Very efficient since only 1 step is performed
> 
> Disadvantages:
> - Poor uniformity as all inputs will return the same output
> - No collision resistance
> - Zero sensitivity to changes in input
> - No security
> 
> ### sum_of_ascii_values
> Advantages:
> - Efficient to run since the number of steps is equal to the length of the input
> 
> Disadvantages:
> - Poor collision resistance since many letter combinations will produce the same output
> - Low sensitivity to changes in input since changing 1 letter can only shift the output value by a maximum of 25
> - Low determinism since ascii values are case-sensitive, so capitalisation of the input can affect the output
> - Poor uniformity and collision resistance since common letter combinations can cause outputs to cluster around certain ranges of values, especially since the order/arrangement of the letter doesn't affect the output.
> - Zero security as outputs are easily reversible and predictable since it relies on simple linear addition.
> 
> 
> ### Pearson Hash
> Advantages:
> - Highly efficient, especially on 8-bit processors due to the use of a 256-byte permutation table
> - Good uniformity if permutation table is truly random
> - Strictly deterministic given the same permutation table and input
> - Good collision resistance for natural (accidental) collisions when dealing with psuedo-random data  
> - Highly sensitive to changes in input due to the use of iterative XOR and permutation table operations
> 
> Disadvantages:
> - uniformity relies on the randomness of the 256-byte permutation table. 
> - Poor cyptographic security since it provides no protections or resistance against malicious collision generation
> - Limited maximum table size (max size of 256)
> 
> ### Built-in Hash
> Advantages:
> - Designed to be highly efficient for 64-bit systems
> - Highly uniform for String, Byte, and Datetime inputs
> 
> Disadvantages:
> - Uniformity and input sensitivity highly dependent of the data type of the input 
> - Integer inputs provide zero uniformity, as they hash to themselves
> - Not cryptographically secure
> - Only deterministic within a single execution session, outputs will change next time program is run
> - No collision resistance
> 
> ### SHA-2 Hash
> Advantages:
> - Extremely high cryptographic security, collision resistance, and input sensitivity
> - Roughly uniform output distribution
> - Moderately efficient, while remaining cryptographically secure
> - Strictly deterministic across all systems in instances
> 
> Disadvantages:
> - Slower than other non-cryptographically secure alternatives
> 

3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> Determinism - Determinism is the most important aspect of a hashing algorithm since if the same input doesn't produce a consistent output, then it would be impossible to retrieve the correct item from the hash table.
> Efficiency - Efficiency is one of the main benefits that hashmaps provide over other data structures such as linked lists or BSTs. If a hashing algorithm is inefficient, then it loses the main benefit it holds over alternative data structures
> Uniformity - Good uniformity ensures keys are distributed evenly across the available slots. If uniformity is poor, it can cause keys to cluster or collide which negatively impacts efficiency

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> Since the requirements of this task do not require cryptographic security, I would pick the built=in python hash() function
> as it provides high efficiency and uniformity when using string inputs such as player's uids. Since the hashmap is not being
> stored between executions, determinism only needs to be consistent within a single execution session.

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.
```python
import random
random.seed(42) #1

pearson_table = list(range(256)) #2
random.shuffle(pearson_table) #3

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0 #4
    for char in key: #5
        hash_ = pearson_table[hash_ ^ ord(char)] #6
    return hash_ % size #7
```
> #1 - The first line imports python's 'random' library, which provides methods for generating psuedo-random numbers.
> <br>
> #2 - The second line sets to seed of the instance of the random library to a known value to ensure determinism remains consistent
> between executions.
> <br>
> #3 - This line generates a list of all values from 0-255 in order.
> <br>
> #4 - This line uses the random library to shuffle the list into a psuedo-random order based on the seed. This creates
> a consistent permutation table of randomly arranged 256 byte values, which determines the uniformity of the hashmap/
> <br>
> #5 - This line iterates through each character in the key in order, ensuring all characters in the key contribute to the final hash_ value
> This helps to ensure the key-length and character order contribute to the input-sensitivity of the algorithm.
> <br>
> #6 - This line uses a binary XOR operation to calculate the position of the permutation table to set the hash_ value to next. 
> This provides good uniformity and input-sensitivity by allowing the previous characters' hashes to greatly affect the hash of the subsequent characters.
> This process is extremely efficient as it requires very little computation, especially on 8-bit processors due to their 256-byte nature
> <br>
> #7 - This line modulos the final calculated hash value by the table size to map the key to a position within the table,
> 
> 

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> Your answer here

## Reflection

1. What was the most challenging aspect of this task?

> Your answer here

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> Your answer here

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
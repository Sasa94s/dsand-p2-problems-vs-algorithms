### Program Design Summary
#### Trie - Insert
Looping over characters of word linearly.
- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
#### Trie - Find
Looping over characters of prefix linearly.
- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
#### TrieNode - Insert
To avoid recreating TrieNode of the same reference, A `not in` keyword is used (Noting that in Python has time complexity `O(n)`)
*where `n` is the number of keys in the `child` dictionary.
- Time Complexity: `O(n)`.
- Space Complexity: `O(n)`
#### TrieNode - Suffixes
Looping over keys of `child` dictionary, then calling the same function recursively.
- Time Complexity: `O(m^n)`
- Space Complexity: `O(m^n)`

*where `m` is number of keys and `n` is the number of recursive calls.
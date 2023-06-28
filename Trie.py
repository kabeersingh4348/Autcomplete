class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._get_words(node, prefix)

    def _get_words(self, node, prefix):
        results = []
        if node.is_end_of_word:
            results.append(prefix)
        for char in node.children:
            results.extend(self._get_words(node.children[char], prefix + char))
        return results

trie = Trie()
words = ["apple", "app", "application", "banana", "bike"]       #Dictionary of words which should exist beforehand.

# Insert words into the trie
for word in words:
    trie.insert(word)

# Autocomplete with a prefix
prefix = "app"
autocomplete_results = trie.search(prefix)
print(autocomplete_results)

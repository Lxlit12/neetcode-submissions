class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['.'] = '.'

    def search(self, word: str) -> bool:
        def dfs(d,i):
            if i == len(word):
                return '.' in d
            if word[i] == '.':
                for key in d:
                    if key != '.' and dfs(d[key],i+1):
                        return True
                return False
            if word[i] not in d:
                return False
            return dfs(d[word[i]],i+1)
        return dfs(self.trie,0)

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()


    def suffixes(self):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        suffixes = []

        def find_suffix(Node, output_str):
            if Node.is_word:
                suffixes.append(output_str)
            for char in Node.children:
                temp = output_str + char
                find_suffix(Node.children[char], temp)

        find_suffix(self, "")
        return suffixes


class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]

        return current_node




# # Testing it all out
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.


trie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    trie.insert(word)

# In[4]:



def auto_complete(prefix):
    if prefix  is None:
        return
    if prefix != '':
        prefixNode = trie.find(prefix)
        if prefixNode: #if  prefix node is not None
            print(prefixNode.suffixes())
        else:
            print("prefix:" + prefix + " not found")
    else:
        print('')



auto_complete('')  # ''
auto_complete(None)  # simply return doing nothing
auto_complete('                             ')  # prefix:                 not found
auto_complete('123')  # prefix: 123 not found
auto_complete('an')  # ['t', 'thology', 'tagonist', 'tonym']
auto_complete('ant')  # ['', 'hology', 'agonist', 'onym']
auto_complete('anto')  # ['onym']
auto_complete('trig')  # ['ger', 'onometry']
auto_complete('fun')  # ['', 'ction']






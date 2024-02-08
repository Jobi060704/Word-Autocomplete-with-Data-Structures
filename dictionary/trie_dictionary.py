from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter            # letter stored at this node
        self.frequency = frequency      # frequency of the word if this letter is the end of a word
        self.is_last = is_last          # True if this letter is the end of a word
        self.children: dict[str, TrieNode] = {}     # a hashtable containing children nodes, key = letter, value = child node


class TrieDictionary(BaseDictionary):

    def __init__(self):
        # making root node
        self.root = TrieNode()
        pass

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # for each WordFrequency in words_frequencies list, we add them to the trie
        for i in words_frequencies:
            self.add_word_frequency(i)


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # start from root node
        search_node = self.root
        # for each character in word, check if it is in node's children
        for char in word:
            if char not in search_node.children:
                # if not, retunt o or NOT FOUND
                return 0
            search_node = search_node.children[char]

        # if the end node is not a word we return 0 or NOT FOUND
        if(search_node.is_last == False):
            return 0
        else:
            # if found, we return the frequency of the word
            return search_node.frequency


    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # base return is False or FAILURE
        ret = False

        # check if word in wordfrequency already exists in the trie
        if(self.search(word_frequency.word) == 0):
            # if not, we start to add
            ret = True
            
            # we dig into the last node available for word addition
            current = self.root
            for char in word_frequency.word:
                if char not in current.children:
                    # if no more children nodes are present for the given word, we vreate new child nodes
                    current.children[char] = TrieNode(char)

                current = current.children[char]

            # set the word frequency
            current.frequency = word_frequency.frequency
            current.is_last = True

        return ret

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # base return if False or FAILURE
        ret = False

        if(self.search(word) != 0):
            # if word in trie we delete it
            ret = True
            
            # dig to the needed word node
            current = self.root
            for char in word:
                current = current.children[char]

            # set it to NOT be a word by changing is_last value
            current.is_last = False

        return ret



    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        # start with root node
        search_node = self.root

        # dig into the needed node end
        for char in word:
            if char not in search_node.children:
                # if node not found, we return an empty array
                return []

            search_node = search_node.children[char]

        # dfs to get each child node that forms a word (is_last is equal to True)
        def DFS(node, word_part):
            found_words = []

            # if node forms a word, we add it to the found_words array
            if node.is_last:
                found_words.append(WordFrequency(word_part, node.frequency))

            # get each sub-node in node children
            for char in node.children.keys():
                found_words.extend(DFS(node.children[char], word_part + char))

            return found_words

        # get all words from prefic word from DFS 
        contain_array = DFS(search_node, word)

        # sort the array
        sorted_array = sorted(contain_array, reverse=True, key=lambda wf: wf.frequency)

        # get 3 items with biggest Frequency
        best_array = sorted_array[:3]

        return best_array

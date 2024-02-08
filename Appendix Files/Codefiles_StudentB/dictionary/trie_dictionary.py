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
        # TO BE IMPLEMENTED
        # making root node
        self.root = TrieNode()

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED

        # for each wf in words_frequencies list, we add them to the trie
        for wf in words_frequencies:
            self.add_word_frequency(wf)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        # convert the word to lowercase for case-insensitive search
        word = word.lower()
        # start from root node
        cur = self.root

        # traverse the Trie character by character to search for the word
        for i in range(len(word)):
            letter = word[i]
            next_lst = cur.children

            # reach the last character of the word
            if i == len(word) - 1:
                # reach last one
                # print(letter + "last")
                
                if next_lst.get(letter) is not None:
                    cur = next_lst[letter]
                    # print(cur.letter + "found " + str(cur.is_last))
                    # if found, we return the frequency of the word if it's the end of a word
                    if cur.is_last:
                        return cur.frequency
                # return 0 if the word is not found
                return 0
            else:
                if next_lst.get(letter) is not None:
                    cur = next_lst[letter]
                else:
                    # return 0 if a character is not found in the Trie
                    return 0
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        # TO BE IMPLEMENTED
        # convert the word to lowercase for case-insensitive matching
        cur = self.root
        word = word_frequency.word.lower()
        cur = self.root
        for i in range(len(word)):
            letter = word[i]
            next_lst = cur.children

            if i == len(word) - 1:
                # reach the last character of the word
                
                if next_lst.get(letter) is not None:
                    cur = next_lst[letter]
                    if cur.is_last:
                        # word is already in the dictionary, return False
                        return False
                    cur.is_last = True
                    cur.frequency = word_frequency.frequency
                else:

                    # create a new node for the last character of the word
                    node = TrieNode(letter, word_frequency.frequency)
                    node.is_last = True
                    node.frequency = word_frequency.frequency
                    next_lst[letter] = node

                 # successfully added the word and frequency
                return True
            else:
                if next_lst.get(letter) is not None:
                    cur = next_lst[letter]
                else:

                    # create a new node for the character
                    node = TrieNode(letter, 0)
                    next_lst[letter] = node
                    cur = node
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        start_cut_idx = 0  # record the start of unique suffix
        cut_list = [self.root]  # record the nodes as path
        cur = self.root
        word = word.lower()
        for i in range(len(word)):
            letter = word[i]
            # check if current letter does not exist in tree.
            if cur.children.get(letter) is None:
                return False
            cur = cur.children.get(letter)
            cut_list.append(cur)

            # if the word reaches the end, cut or just change the flag
            if i == len(word) - 1:
                if not cur.is_last:
                    return False

                cur.is_last = False
                next_lst = cur.children
                # if count >= 1, cur node is shared by other words.
                if len(next_lst) >= 1:
                    return True
                else:
                    break

            # check if other path exists
            path_count = 0
            next_lst = cur.children
            for key in next_lst:
                path_count = path_count + 1
                if next_lst[key].is_last:
                    path_count = 2
            # if count > 1 or the flag is True, cur node is shared by other words.
            if path_count > 1:
                start_cut_idx = i + 1

        # start cutting
        cur = cut_list[start_cut_idx + 1]
        prev = cut_list[start_cut_idx]

        idx = ord(cur.letter) - ord('a')
        del prev.children[cur.letter]
        return True

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        result = []
        copy = []
        prefix = ''
        self.dfs_helper(self.root, copy, prefix)

        copy.sort(key=lambda x: x.frequency, reverse=True)
        for data_pair in copy:
            if data_pair.word.startswith(word):
                result.append(data_pair)
                if len(result) == 3:
                    return result
        return result

    def dfs_helper(self, cur, copy: [WordFrequency], prefix: str):
        if cur is None:
            return
        next_lst = cur.children
        for key in next_lst:
            if next_lst[key].is_last:
                copy.append(WordFrequency((prefix + next_lst[key].letter), next_lst[key].frequency))
            self.dfs_helper(next_lst[key], copy, (prefix + next_lst[key].letter))

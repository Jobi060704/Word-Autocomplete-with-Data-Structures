from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        # create the head node of the linked list
        self.m_head = None

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # if the list is empty, stop the build function
        if len(words_frequencies) == 0:
            return
        
        # set head node to the first item in list
        self.m_head = ListNode(words_frequencies[0])
        cur = self.m_head

        # add the items from the list to the linkedlist from second till last
        for i in range(1, len(words_frequencies)):
            node = ListNode(words_frequencies[i])
            cur.next = node
            cur = cur.next

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # set start node to the head
        cur = self.m_head

        # transverse all nodes to find the word
        while cur is not None:
            if cur.word_frequency.word == word:
                # if found, return the words frequency
                return cur.word_frequency.frequency
            cur = cur.next
        
        # if not found, return 0
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # set start node to the head
        cur = self.m_head
        prev = None

        # transverse until the node is not None
        while cur is not None:
            if cur.word_frequency.word == word_frequency.word:
            # if word in linkedlist, return False or ALREADY IN LINKEDLIST
                return False
            prev = cur
            cur = cur.next
        
        # add the new node in the end
        node = ListNode(word_frequency)
        # set the last nodes next parameter to the new node
        prev.next = node
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # set node to head
        cur = self.m_head
        prev = None
        # transverse until the node is not None
        while cur is not None:
            # if found, proceed in to nest operations
            if cur.word_frequency.word == word:
                if prev is not None:
                    # if prev node is not None,  we set the last nodes next, to current nodes next (skip the current node in linkedlist)
                    prev.next = cur.next
                else:
                    # if prev is None, we set the head to the next node (head node was to be deleted)
                    self.m_head = cur.next
                return True
            prev = cur
            cur = cur.next
        return False

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        # sub-arrays for each step in the function
        contain_array = []
        sorted_array = []
        best_array = []

        # set search node to head
        search_node = self.m_head
        # transverse until the end
        while (search_node != None):
            if (search_node.word_frequency.word.startswith(word)):
                # if node has prefic of word, add to contain array
                contain_array.append(search_node.word_frequency)
            search_node = search_node.next

        # sort all items in array
        sorted_array = sorted(contain_array, reverse=True, key=lambda wf: wf.frequency)

        # get 3 items with biggest Frequency
        best_array = sorted_array[:3]

        return best_array

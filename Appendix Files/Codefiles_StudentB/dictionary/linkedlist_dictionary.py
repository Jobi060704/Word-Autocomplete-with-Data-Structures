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
        # TO BE IMPLEMENTED
        # create the head node of the linked list
        self.m_head = None

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        # if the list is empty, stop the build function
        if len(words_frequencies) == 0:
            return
        self.m_head = ListNode(words_frequencies[0])
        # set head node to the first item in list
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
        # TO BE IMPLEMENTED
        # set start node to the head
        cur = self.m_head

        # transverse all nodes to find the word
        while cur is not None:
            if cur.word_frequency.word == word:
                # if found, return the words frequency
                return cur.word_frequency.frequency
            cur = cur.next

        # otherwise, return 0
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        # TO BE IMPLEMENTED
        # set start node to the head
        cur = self.m_head
        # point to the previous node,now is none
        prev = None

        # transverse until the node is not None
        while cur is not None:

            # if word in linkedlist, return False or ALREADY IN LINKEDLIST
            if cur.word_frequency.word == word_frequency.word:
                return False
            # record the current node
            prev = cur
            # move to next
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
        # TO BE IMPLEMENTED

        # set node to head
        cur = self.m_head
        # No node need be record now
        prev = None

        # transverse until the end
        while cur is not None:
            # if found, proceed into next operations
            if cur.word_frequency.word == word:

                # if prev node is not None,  we set the last nodes next, to current nodes next (skip the current node in linkedlist)
                if prev is not None:
                    prev.next = cur.next

                # if prev is None, we set the head to the next node (head node was to be deleted)
                else:
                    self.m_head = cur.next
                return True
            # record the current node
            prev = cur
            # move to next
            cur = cur.next
        return False

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        # TO BE IMPLEMENTED
        result = []
        # copy list for manipulate
        copy = []
        # set search node to head
        cur = self.m_head
        # transverse until the end
        while cur is not None:
            # add word_freque to the copy list
            copy.append(cur.word_frequency)
            # next node
            cur = cur.next
        # sort all items in array
        copy.sort(key=lambda x: x.frequency, reverse=True)

        # transverse copy to match prefix
        for data_pair in copy:
            if data_pair.word.startswith(word):
                # add in result
                result.append(data_pair)

                # get 3 items with biggest Frequency
                if len(result) == 3:
                    return result
        return result

from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ArrayDictionary(BaseDictionary):
    # constructor
    def __init__(self):
        # TO BE IMPLEMENTED
        # property
        self.data = []
        pass

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        # for loop to traverse the list
        for wf in words_frequencies:
            # add the wf into self.data
            self.data.append(wf)

        # sort the list by word
        self.data.sort(key=lambda x: x.word)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        # traverse the self.data
        for data_pair in self.data:
            if data_pair.word == word:
                # if found the word then return its frequency
                return data_pair.frequency
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        # traverse the self.data
        for i in range(len(self.data)):
            # word is already in the dictionary
            if self.data[i].word == word_frequency.word:
                return False
            # find the right location to insert
            if self.data[i].word > word_frequency.word:
                self.data.insert(i, word_frequency)
                return True

        # all element are less than the new one, hence append to the last position
        self.data.append(word_frequency)
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # find the position of 'word' in the list, if exists, will be at idx-1
        # TO BE IMPLEMENTED
        for i in range(len(self.data)):
            if self.data[i].word == word:
                # delete the i index of self.data
                del self.data[i]
                return True
        return False

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        result = []
        copy = self.data
        # copy the list to a new list and sort by the frequency Max-min
        copy.sort(key=lambda x: x.frequency, reverse=True)
        # Traverse the sorted copy
        for data_pair in copy:
            # if word start with prefix_word then append to result
            if data_pair.word.startswith(prefix_word):
                result.append(data_pair)

                # length 3 at most
                if len(result) == 3:
                    return result
        return result

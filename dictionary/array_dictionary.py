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

    def __init__(self):
        # creating an empty array to perate on
        self.main_array = []
        pass


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # for each WordFrequency in words_frequencies list, we append them to the array
        for i in words_frequencies:
            self.main_array.append(i)


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # base return is 0 or NOT FOUND
        ret = 0

        # for each item in array, we check if the word is present
        for i in self.main_array:
            if(i.word == word):
                # if present, we return the frequency of the word
                ret = i.frequency
                break
    
        return ret

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # base return is True or SUCCESS
        ret = True

        # search if the word exists in the array
        for i in self.main_array:
            if(i.word == word_frequency.word):
                # if found, return False or ALREADY IN DICTIONARY
                ret = False        

        if(ret):
            # if not found, we add the word_frequency to the array
            self.main_array.append(word_frequency)

        return ret

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        ret = False

        # if word in array is found, we proceed with deletion
        if(self.search(word) != 0):
            ret = True
            # check items for which is the desired one
            for i in self.main_array:
                if(i.word == word):
                    remove_this = i
                    break
            # removing the desired item
            self.main_array.remove(remove_this)

        return ret


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        # sub-arrays for each step in the function
        contain_array = []
        sorted_array = []
        best_array = []

        # if any items start with the prefix, add to the contain list 
        for i in self.main_array:
                if(i.word.startswith(prefix_word)):
                    contain_array.append(i)

        # sort all items in array
        sorted_array = sorted(contain_array, reverse=True, key=lambda wf: wf.frequency)

        # get 3 items with biggest Frequency
        best_array = sorted_array[:3]

        return best_array

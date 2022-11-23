from functions import load_words


class BasicWord:
    """
    The class is used for polling, the arguments of the class are set during initialization.
    "word" - contains the original word,
    "subwords" - contains a list of possible words made up of the letters of the original word.
    Methods of the class:
    check_word - checks the suitability of the word,
    count_subword - returns the number of words that can be composed.
    """

    def __init__(self):
        """
        The function is executed when initializing an instance of the class and sets the value
        of the arguments of the instance of the class.
        """
        word_dict = load_words()
        self.word = word_dict['word']
        self.subwords = word_dict['subwords']


    def __repr__(self):
        """
        The run function sets a string representation of an instance of a class in an easy-to-read format.
        """
        return f'I am a word {self.word} from the letters of which it is necessary to select anograms'


    def check_word(self, user_word):
        """
        The class method accepts a word and returns True if the word is in the list of correct answers, otherwise False.
        """
        if len(user_word) < 3:
            print('слишком короткое слово')
            return False

        elif not user_word in self.subwords:
            print('неверно')
            return False

        return True


    def count_subword(self):
        """
        The class method does not accept any arguments and returns the number of derived words from the letters
        of the original word as an integer.
        """
        return len(self.subwords)

class Player:
    """
    The class represents the player, the arguments of the class are set during initialization.
    "name" - contains the user's name,
    "users_word" - contains a list of words guessed by the user.
    Methods of the class:
    check_word - checks the suitability of the word,
    count_subword - returns the number of words that the user named,
    add_word - adds the word to the list of the argument "users_word"
    """
    def __init__(self, name):
        """
        The function is executed when initializing an instance of the class and sets the value
        of the arguments of the instance of the class.
        """
        self.name = name
        self.users_word = []


    def __repr__(self):
        """
         The run function sets a string representation of an instance of a class in an easy-to-read format.
        """
        return f"I'm a gambler {self.name }, which will compose words from the given letters"


    def count_subword(self):
        """
        The method returns the number of words correctly named by the user as an integer.
        """
        return len(self.users_word)


    def add_word(self,subword):
        """
        The class method takes a word as an argument and adds it to the class argument list.
        """
        self.users_word.append(subword)


    def check_word(self, sub_word):
        """
        The class method accepts a word and returns True if the word is not in the class argument list,
        otherwise the value is False.
        """
        if sub_word in self.users_word:
            print('уже использовано')
            return False
        return True
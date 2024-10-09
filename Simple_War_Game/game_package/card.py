# my_package/card.py

# define Card class
# self.value - is an instance variable of the Card class,
# --  It represents the value of the specific card object being created.
# values - is a parameter passed into the class constructor.
# -- It’s a dictionary that provides a mapping of card ranks to their numerical values.
#
# These two variables live in different scopes:
# -- self.value is an attribute of the instance (the object).
# -- values is a local variable in the scope of the __init__ method,
#    or it could be passed into the class from the outside.
#  When you do self.value = values[rank], you are saying:
# -- "Set this card's value attribute to the corresponding
#     value from the values dictionary, based on the card's rank."


class Card:

    def __init__(self, suit, rank, values):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit
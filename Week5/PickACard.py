import random

SUIT = ("c", "d", "h", "s")
VALUE = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

def pickSuit():
    """Gets a card Suit"""
    mysuit = SUIT[random.randrange(len(SUIT))]
    return mysuit

def pickValue():
    """Gets a card Value"""
    myvalue = VALUE[random.randrange(len(VALUE))]
    return myvalue

if __name__ == "__main__":
    print("This is a library file and is not intended as a 'main' program!")
    exit()


            

    

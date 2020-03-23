"""
Main:
    A simple program that allows testing of nose2
"""

def printWords(words):
    """
    Takes a set of words and prints them individually.

    Parameters
    ----------
    words : List of strings to be printed.

    """
    for word in words:
        print(word)
        
    return words
        
def main():
    """
    Main function.

    """
    words = ("Hello", "World!")
    printWords(words)
    

if __name__ == "__main__":
    main()

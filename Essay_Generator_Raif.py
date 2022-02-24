'''
This program allows users to generate random essays using words in the given url.
Users can choose how many paragraphs should the essay have as well as the amount
of words each paragraph should have.

Author: Raif Rizwan Karkal
Student Number: 20261498
Date: 9th Nov 2021
'''

# imports for usage in program
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import string
import random

# decleration of global variable for usage within program
longestWordLength = 0


def readWebPage(url):
    """
    This function uses the url parameter to access the website and read through the
    contents of the website. The function is based on try and except to make sure
    the website is loaded correctly and the program reads thorough it with no errors.
    If an error occurs, user is notified with an empty list returned. If program reads
    through the website correctly, words in the website are placed in a list and returned.

    Parameters: url
    Return: empty_list, list_of_words
    """

    # Try and except. In the try, the program insures the url opens and the words in the website are placed as a list.
    try:
        response = urllib.request.urlopen(url)
        # content of the website (words) are assigned to the variable data
        data = response.read().decode('utf-8')
        # List of words variable words all the words in the website as a list
        list_of_words = data.split()
        # list of word returned for further usage
        return list_of_words

    # The except is used to inform user if any error occurs.
    except:
        # if error occurs, user informed website did not open or words not placed in a list
        print("Website did not open or words not placed in list - error")
        # empty list is created if error occurs
        empty_list = []
        # empty list returned
        return empty_list


def removePunctuation (word_list):
    """
    This function takes the parameter - word list which is a list of words from a website.
    It reads through the list of words and removes any punctuations in the list.

    Parameters: word_list
    Return: None
    """

    # assigning empty list to variable punctuation_list
    punctuation_list = []

    # for loop is used to convert the string of punctuation to a list. Punctuation variable is assigned to each punctuation in a string
    for punctuation in string.punctuation:
        # punctuation list is appended with the variable punctuation which represents each punctuation in a string.
        punctuation_list.append(punctuation)

    # for loop in which the variable num assigned to each number from 0 to the length of the list
    for num in range(0, len(word_list)):
        # if statement to check if the last character of each word in the word list, is in the punctuation list.
        if word_list[num][-1] in punctuation_list:
            # if true, the word is strip of the last character (punctuation) and assigned to variable new word
            New_word = word_list[num].rstrip(word_list[num][-1])
            # The old word in the list is replaced by the new word that doesn't have the punctuation
            word_list[num] = New_word


def convertToDictionary(list_of_words):
    """
    This function takes the parameter - list_of_words which is a list of words without
    the punctuation. It uses the content in the list and produces a dictionary with a key
    and value. The value is a list of word that all begin with the same letter and have the same
    size while the key is a string consisting of the first letter of the word found and the length
    of the word. The dictionary created is returned.

    Parameters: list_of_words
    Return: dictionary_of_words
    """

    # global variable that was initial defined, is used in this function
    global longestWordLength

    # empty dictionary assigned to disctionary_of_words
    dictionary_of_words = {}

    # for loop used were the variable word assigned to each word in the list of words.
    for word in list_of_words:
        # to make dictionary key, first make sure each word is lower cased
        word_lower = word.lower()
        # the first letter of the word assigned to variable first_letter
        first_letter = word_lower[0]
        # length of word converted to str and assigned to length
        length = str(len(word_lower))
        # dictionary key created by combining the first letter and the length of the word.
        key = first_letter + length

        # if the key created is not one of the keys that exist in the dictionary than the statement executes
        if key not in dictionary_of_words.keys():
            # new word list created
            new_word_list = []
            # new word list appended with the word used to created the key, lower case of word taken
            new_word_list.append(word_lower)
            # the new list is assigned to the new key that is created in the dictionary
            dictionary_of_words[key] = new_word_list

        # elif statement - if key created exist in the dictionary - this part of program executes
        elif key in dictionary_of_words.keys():
            # If the lower case of word that was used to create the key, doesn't exist in the list within the the specified dictionary key, program continues
            if word_lower not in dictionary_of_words[key]:
                # if key exist and word does not exist in list, the specified dictionary key is appended with the word.
                dictionary_of_words[key].append(word_lower)

    # the longest word in the list is found and converted into its length (number) which is than assigned to a variable
    longestWordLength = len(max (list_of_words, key = len))

    # returning the dictionary of words
    return dictionary_of_words


def makeParagraph (dictionary_of_words, number_of_words):
    """
    This function uses the paramemter dictionary_of_words to create paragraphs for
    the user. The words in the paragraph are taken from the dictionary randomly, while the word count
    of each paragraph is determined using the number_of_words parameter. The paragraph
    generated is returned.
    Parameters: dictionary_of_words, number of words
    Return: A dictionary
    """

    # Using longest word length global variable in this function
    global longestWordLength

    # defining an empty string called paragraph
    paragraph = ""

    # for loop used to limit the amount of word used per paragraph.
    for counter in range (0, number_of_words):
        # A random number selected from 1 to longest word length which is 14.
       num = random.randint(1,longestWordLength)
        # A random letter selected from the alphabet
       letter = random.choice(string.ascii_letters.lower())
        # a random key is generated by combinig the letter with a number
       random_key = letter + str(num)

        # While loop in which is random key that was generated earlier is not a key in the dictionary, loop begins.
       while random_key not in dictionary_of_words.keys():
           # A random number selected from 1 to longest word length which is 14.
           num = random.randint(1,longestWordLength)
           # A random letter selected from the alphabet
           letter = random.choice(string.ascii_letters.lower())
           # a random key is generated by combinig the letter with a number
           random_key = letter + str(num)

        # if statement - if the random key generated is a key in the dictionary, program continues
       if random_key in dictionary_of_words.keys():
           # The random key translates to a list of words within the dictionary. A random word is taken from the list of words and assigned to word.
           word = random.choice(dictionary_of_words[random_key])
           # The words generated are added to the paragraph as the loop continues. Spaces are also added.
           paragraph  = paragraph + word + " "

    # This code is used to remove unnecessary indents in the paragraph output and add a full stop after every paragraph.
    paragraph = paragraph[0:-1] + "."

    # paragraph is returned
    return paragraph


def createEssay (dictionary_of_words):
    """
    This function asks the user the amount of paragraph they would like in there essay.
    It also ask the amount of words each paragraph should have. With this information,
    the makeParagraph function is called and given the parameter dictionary or words and
    the word count of each paragraph. The returned paragraph from the makeParagraph function
    is added to the variable essay. Once the essay is generated, the essay is returned.

    Parameters: dictionary_of_words
    Return: essay
    """

    # count variable defined and assigned number 1
    count = 1

    # essay variable defined and assigned empty string
    essay = ""

    # User asked the amount of paragraph user wants in there essay. Answer assigned to variable paragraph amount
    paragraph_amount = int(input ("How many paragraph's would you like to generate for your essay? "))

    # While loop in which the loop continues until the count variable is greater than the paragraph amount
    while count <= paragraph_amount:
        # User asked how many words they would require for the first paragraph and so on. User asked continously until loop stops
        word_count_for_paragraph = int(input("How many words should be in paragraph " + str(count)+": "))
        # make paragraph function called. function given dictionary of words and word count as parameter. The return value is assigned to essay variable
        essay += makeParagraph(dictionary_of_words, word_count_for_paragraph)
        # adding new line to essay variable. This is for output design
        essay += "\n"
        # adding new line to essay variable. This is for output design
        essay += "\n"
        # adding 1 to the count as the loop finishes in order for the while loop to stop after paragraph amount is passed.
        count += 1

    # essay created is returned
    return essay


def writeToFile(text):
    """
    This function takes the parameter text which is the essay created by the createEssay
    function and writes the text into a file called - essay.txt. Try and except is used
    to make sure the file is opened properly and the text is written into the file. If

    Parameters: text
    Return: None
    """

    # Try and except statement. The try statement makes sure the file opens up and the essay is written into the file
    try:
        #Opening essay.txt file in writing mode
        essay = open("essay.txt", "w")
        # writing the text (essay) into the file
        essay.write(text)
        #closing file
        essay.close()
        #letting user know the above code excuted sucessfully
        print ("File opened properly and essay is written into file")

    except:
        # if an error occurs the file, user informed
        print ("File error occured")


def main ():
    """
    The main function controls the program flow. This is where execution will start. In the main function,
    the URL of the website is stored in the variable URL. Furthermore, different functions are called
    from the main function.

    Parameters: None
    Return: None
    """
    # Url defined for use in list_of_words function
    url = "https://research.cs.queensu.ca/home/cords2/cs.txt"
    # read web page function called with url as parameter. Return value assigned to variable list of words
    list_of_words = readWebPage(url)
    # remove punctuation function called with list of words as parameter
    removePunctuation(list_of_words)
    # convert to dictionary function called with list of word as parameter. Return value assigned to variable dictionary of words
    dictionary_of_words = convertToDictionary(list_of_words)
    # create essay function called with dictionary of words as parameter. Return value assigned to variable essay.
    essay = createEssay(dictionary_of_words)
    #write to file function called with essay as parameter
    writeToFile(essay)


# Calling main function in order to execute program
main()

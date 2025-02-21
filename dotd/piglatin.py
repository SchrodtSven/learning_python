def piglatinize_me(given_word: str):
    ay = "ay"
    way = "way"
    consonant = (
        "B",
        "C",
        "D",
        "F",
        "G",
        "H",
        "J",
        "K",
        "L",
        "M",
        "N",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "Y",
        "V",
        "X",
        "Z",
    )
    vowel = ("A", "E", "I", "O", "U")
    first = given_word[0]
    first = str(first)
    first = first.upper()
    if first in consonant:
        print(first, "is a consonant")
        length_of_word = len(given_word)
        remove_first = given_word[1:length_of_word]
        pig_latin = remove_first + first + ay
        print("The word in Pig Latin is:", pig_latin)
    elif first in vowel:
        print(first, "is a vowel")
        pig_latin = given_word + way
        print("The word in Pig Latin is:", pig_latin)
    else:
        print("I dont know what", first, "is")



piglatinize_me(given_word = input("Enter a word to translate to Pig Latin: "))
# getting first letter and making sure its a string and setting it to uppercase

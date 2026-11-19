
# Brandon Jun // COMSC 078 // Sequences

VOWELS = "aeiouy"

def word_to_pig_latin(word):

    if word[0] in VOWELS:
        return word + "way"

    i = 0
    while i < len(word) and word[i] not in VOWELS:
        i += 1
    return word[i:] + word[:i] + "ay"

def sentence_to_pig_latin(string):
    result = []
    for word in string.split():
        if word != "":
            result.append(word_to_pig_latin(word))
    return result

def main():

    while True:
        input_str = input("Enter a word or phrase (or press ENTER to quit): ").lower()
        if input_str == "" : break
        piglatin_str = sentence_to_pig_latin(input_str)
        for i in range(0, len(piglatin_str)):
            print(piglatin_str[i], end = " ")
        print()

main()
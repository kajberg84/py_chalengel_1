nato_alfabet_svenska = {
    "A": "Adam",
    "B": "Bertil",
    "C": "Caesar",
    "D": "David",
    "E": "Erik",
    "F": "Fredrik",
    "G": "Gustav",
    "H": "Helge",
    "I": "Ivar",
    "J": "Johan",
    "K": "Kalle",
    "L": "Ludvig",
    "M": "Martin",
    "N": "Niklas",
    "O": "Olof",
    "P": "Petter",
    "Q": "Qvintus",
    "R": "Rudolf",
    "S": "Sigurd",
    "T": "Tore",
    "U": "Urban",
    "V": "Viktor",
    "W": "Wilhelm",
    "X": "Xerxes",
    "Y": "Yngve",
    "Z": "Zäta",
    "Å": "Åke",
    "Ä": "Ärlig",
    "Ö": "Östen"
}

# Get an input from user and convert it to uppercase
word = input("Enter a word: ").upper()

translated_words = []

# Get value from key
for letter in word:
    #  Check that it is a char
    if letter.isalpha():
        # Get the Value from the key and add to the list.
        translated_words.append(nato_alfabet_svenska.get(letter))
    else:
        print("You should only throw in words. No digits or other shit, but hey Im kind this time and only print this and will ignore your stupidity :D")

# Print out
print(translated_words)

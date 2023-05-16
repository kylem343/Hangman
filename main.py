import random


def get_word(filename):
    with open(filename) as f:
        lines = f.readlines()
        size = len(lines)
        ran = random.randint(0, size - 1)
        return lines[ran]


def go_through_word(let, w, s):
    new_word = ''
    for x in range(0, len(w)):
        if let == w[x]:
            new_word += let
        else:
            new_word += s[x]
    return new_word


word = get_word("words.txt").strip()
# print(word)
solve = ''
for i in word:
    solve += '_'
# print(solve)

tries = 0
used = ""
while tries != 6 and "_" in solve:
    print("\nTries left: " + str(6 - tries))
    print("Used letters: " + used)
    print(solve)

    letter = input("Enter a letter: ")
    while letter in solve or letter.isalpha() is False or len(letter) != 1:
        letter = input("Invalid input. Please enter a single letter ")

    used += letter + " "
    if letter not in word:
        print("Not in the word")
        tries += 1
    solve = go_through_word(letter, word, solve)

if tries == 6:
    print("You Failed, the word was " + word)
else:
    print("You Win!")

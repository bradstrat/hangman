word = "elephant"

lines = []
for i in word:
    lines.append('_')

counter = 0

while True:
    letter = input('\nGuess your letter :')
    if letter in word:
        for i in range(0, len(word)):
            if word[i] == letter:
                lines[i] = letter
    else:  # letter is not in the word
        counter += 1
    # print the word with inserted letters
    for i in lines:
        print(i, end=" ")

    # check letters remained in the list

    cnt = "".join(lines).count('_')

    if cnt == 0 or counter == 6:
        break
# end of while loop

if counter >= 6:
    print("\n\n\n You looser..............Think properly")
else:
    print("\n\n\n Yes!!!!!!!!!!! You WON this match")

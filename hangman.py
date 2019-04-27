def display_has_underscores(list):
    return True

def update_word_display(word,l_guess,display):
    for x in range(len(word)):
        if l_guess == word[x]:
            display[x] = l_guess
    return display


word = ["r","o","c","k","e","t"]
display = ["_","_","_","_","_","_"]
while display_has_underscores(display):
    l_guess = input("Enter a single letter ")
    display = update_word_display(word,l_guess,display)
    print(display)

#if l_guess in word:

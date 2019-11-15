def challenge_2(hidden_text):
    #the answer to this challenge is search for some alphanumeric char in the middle of the hidden string 
    # in the source code of the website

    word = ''
    for line in hidden_text:
        for char in line:
            word += (char if char.isalpha() else '')

    print(word)


if __name__ == '__main__':
    challenge_2(open('./resources/challenge_2.txt', 'r'))

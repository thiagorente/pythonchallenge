def calc_char(charactere):
    #check if char is a letter, if yes advance two letters if it's not y or z
    #if y or z return to a and b respectively
    new_char = charactere

    if(charactere.isalpha()):
        if(charactere == 'y' or charactere == 'z'):
            new_char = chr(ord(charactere) - 24)
        else:
            new_char = chr(ord(charactere) + 2)
    
    return new_char

def challenge_1(text_to_convert):
    #the answer to this challenge is get the text from the website and decode it by 
    #changing the letter for the second letter after that
    new_string = ''

    for line in text_to_convert:
        for char in line:
            #check if the char is a letter
            new_string = new_string + calc_char(char)
        
    print(new_string + '\n')

def new_challenge_1(text_to_convert):
    dict = {"a" : "c", "b": "d", "c" : "e", "d": "f", "e" : "g", "f" : "h", "g" : "i", "h" : "j", "i" : "k",
            "j": "l", "k" : "m", "l" : "n", "m" : "o", "n" : "p", "o" : "q", "p" : "r", "q" : "s", "r" : "t", 
            "s" : "u", "t" : "v", "u" : "w", "v" : "x", "w" : "y", "x" : "z", "y" : "a", "z" : "b"}
    
    new_text = ''

    for line in text_to_convert:
        mktrans = (line.maketrans(dict))

        new_text = new_text + line.translate(mktrans)
    
    print(new_text + '\n')


if __name__ == '__main__':
    challenge_1('map')
    challenge_1(open('./resources/challenge_1.txt', 'r'))
    new_challenge_1('map')
    new_challenge_1(open('./resources/challenge_1.txt', 'r'))
def challenge_3(text_to_search):
        #my answer to this challenge is to make a loop in the text and check if the 3 letters on right of the char
        #and the 3 letters on the left is upper, if yes make a string with this letters surrounded by uppers
        #need to see if the fourth letter in the right and in the left is lower or if it is the begin/end of line
        #example of regex  '[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'

        answer = ''

        for line in text_to_search:
            #just look for lines with 7 or more letters
            if(len(line) > 7):
                for ind in range(3, len(line)-3):
                    answer += (line[ind] if line[ind].islower() and
                                            (line[ind-4].islower() or line[ind-4] == '\n') and
                                            line[ind-3].isupper() and 
                                            line[ind-2].isupper() and
                                            line[ind-1].isupper() and
                                            line[ind+1].isupper() and 
                                            line[ind+2].isupper() and
                                            line[ind+3].isupper() and
                                            (line[ind+4].islower() or line[ind+4] == '\n')  else '')

        print(answer)


if __name__ == '__main__':
    challenge_3(open('./resources/challenge_3.txt', 'r'))

#lib to get URL content
import requests

def challenge_4(nothing_value):
    #in this challenge we need to make about 400 requests to the pythonchallenge link and change the nothing parameter
    #after a lot of refresh in page, there was a line 'Yes. Divide by two and continue'

    page_code = nothing_value

    while page_code != '':
        link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + page_code
        url_content = requests.get(link)
        print(str(url_content.text))
        
        old_page_code = page_code

        if(str(url_content.text) == 'Yes. Divide by two and keep going.'):
            page_code = str(int(old_page_code) / 2)
        else:
            for word in str(url_content.text).split(' '):
                page_code = word if word.isnumeric() else page_code

        if(page_code == old_page_code):
            page_code = ''


if __name__ == '__main__':
    challenge_4('12345') #first link

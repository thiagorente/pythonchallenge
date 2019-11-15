import requests

def challenge_4():
    #in this challenge we need to make about 400 requests to the pythonchallenge link and change the nothing parameter

    link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
data = requests.request("GET", link)
url = data.url
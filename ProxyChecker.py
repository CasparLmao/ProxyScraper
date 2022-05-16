import os
from time import sleep
import requests
import random
import string
import pyfiglet
from colorama import Fore
import webbrowser

webbrowser.open("https://pastebin.com/hXhpK1DD")

os.system("cls")

text = pyfiglet.figlet_format("CASPARS PROXY SCRAPER" , font = "big")
print(text)

info = '''
WELCOME TO: CASPARS PROXY SCRAPER
Youtube channel : https://www.youtube.com/channel/UCBN0J7TlGr3Hb3wS_mJELzQ
'''

print(Fore.LIGHTRED_EX+info)
print()
ready = input (f'{Fore.YELLOW} This Program Will autoscrape (HTTP,SOCKS4,SOCKS5) proxies into seperate files (Hit "ENTER" to continue)')

url = "https://api.openproxylist.xyz/http.txt"
r = requests.get(url)
results = r.text
with open ("http.txt", "w") as file:
    file.write(results)
    
url = "https://api.openproxylist.xyz/socks4.txt"
r = requests.get(url)
results = r.text
with open ("socks4.txt", "w") as file:
    file.write(results)
    
url = "https://api.openproxylist.xyz/socks5.txt"
r = requests.get(url)
results = r.text
with open ("socks5.txt", "w") as file:
    file.write(results)
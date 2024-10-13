import requests, random
from user_agent import generate_user_agent
Random = random.randint(100000, 999999)
q = '\033[1;30m'
w = '\033[1;31m'
e = '\033[1;32m'
r = '\033[1;33m'
t = '\033[1;34m'
y = '\033[1;35m'
u = '\033[1;36m'
i = '\033[1;37m'
user = input(r+'• InstaGram UserName : ')
print ('_'*40)
print ('_'*35)
print ('_'*30)
print ('_'*25)
print ('_'*20)
link = input(r+'• Post Link : ')
print ('_'*15)
print ('_'*13)
print ('_'*11)
print ('_'*9)
print ('_'*7)
res = requests.post('https://api.likesjet.com/freeboost/7', jso>
print(res.json()['message'])
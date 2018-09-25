import numpy as np
import pandas as pd
import random

trans_number = range(10)

line = []
len_line = len(line)
#while len_row <= trans_number:

#n = range(trans_number)
#print n

for i in trans_number:
    trans =  str(i) + "th"
    line.append(trans)

print line
print random.choice(line)

randomIndex = random.randrange(0,len(line))
print line[randomIndex]


data1 = [{'name': 'Mark'} , {'name':'Eric'},{'name':'Jennifer'}]
df = pd.DataFrame(data1)
print df



a_0 = {}
a_0['color'] = 'green'
a_0['points'] = 5
print a_0

colors = ["a","b","c","d","e","f","g","h","i","j"]
points = range(5)
a = []
for i in trans_number:
    i = {}
    i['color'] = random.choice(colors)
    i['points'] = random.choice(points)
    print i
    a.append(i)
print pd.DataFrame(a)

#dict_list = list(a.values())
# need 25 transactions


id_list = ["a","b","c","d","e","f","g","h","i","j"]
buyer_list = ["Brown","Robinson","Thompson","Wright","Walker","White","Davies","Edwards","Hughes","Green","Hall","Lewis","esther_01","Collins","Bell",
                "Shaw","Murphy","Miller","evans","Harris","Clarke","Patel","Jackson","Wood","Johnson","Turner","Martin","Cooper","Hill","Ward","jones",
              "Morris","Moore","Clark","Lee"]
phone_list = ['01072518121','01067498121','01034588121']
domain_list = ['@kimnkims.com','@ipacktour.com']

email_list = []
for buyer in buyer_list:
    email_ads = buyer + domain_list[0]
    email_list.append(email_ads)
print(email_list)

total_amount = 101.0
nomal_rule = 4.0
real_trans =  float(total_amount / nomal_rule) #25.25
total_trans = int(round(real_trans + 0.5)) #26
print(total_trans)
perfect_trans = round(real_trans - 0.5) #25
remainder = real_trans - perfect_trans #0.25
print(remainder)
print(perfect_trans)

qunt_list = []
i = 0
while i < perfect_trans:
    qunt_list.append(nomal_rule)
    i += 1

qunt_list.append(remainder*nomal_rule)
print(qunt_list)
print sum(qunt_list)

buy_data = []


for h in range(total_trans):
    x = {}
    x['buyer'] = buyer_list[h]
    x['email'] = email_list[h]
    x['phone_nub'] = random.choice(phone_list)
    x['how many '] = qunt_list[h]

    print x
    buy_data.append(x)
print pd.DataFrame(buy_data)

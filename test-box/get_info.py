import numpy as np
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

myreal_accounts = ["Brown","Robinson","Thompson","Wright","Walker","White","Davies","Edwards","Hughes","Green","Hall","Lewis","esther_01","Collins",
                    "Bell","Shaw","Murphy","Miller","evans","Harris","Clarke","Patel","Jackson","Wood","Johnson","Turner","Martin","Cooper","Hill",
                    "Ward","jones","Morris","Moore","Clark","Lee"]
url = ['@poon','@kimnkims.com']

def accounts():
    quantity = input("tell me how many you need?")
    print(quantity)

    current_quantity = 0
    while current_quantity <= quantity:
        print(current_quantity)
        current_quantity += 1


###company & condition
def question():
    companies = ['myreal' , 'waug']
    items_region = ['hongkong' , 'singapore']
    transaction_mode = ['normal', 'except']

    ch_company = input("choose the company code ; 1 = myreal , 2 = waug")
    ch_item_region = input("choose region of citems ; 1 = hongkong , 2 = singapore")
    ch_trans_mode = input("choose trans mode ; 1 = normal , 2 = except")

    ch_company = companies[int(ch_company)-1]
    ch_item_region = items_region[int(ch_item_region)-1]
    ch_trans_mode = transaction_mode[int(ch_trans_mode)-1]


#####
def number_purchase():
    total_amount = input("tell me how many tickets do you have to purchase?")
    print total_amount

    amount_rule = 0
    if ch_company == companies[0]:
        amount_rule = 4.0
    elif ch_company == companies[1]:
        amount_rule = 10.0

    print amount_rule

    if  ch_trans_mode ==  transaction_mode[0]:
        True
    elif ch_trans_mode ==  transaction_mode[1]:
        amount_rule = 1.0

    print amount_rule

    deal_amount =  float(total_amount / amount_rule)
    print deal_amount

    #
    trans_numb = round(deal_amount + 0.5)
    print trans_numb

#myreal = 4times *except : 1
#waug = 10times *except : 1


if __name__ == "__main__":
    #accounts()
    #company_condition()
    number_purchase()
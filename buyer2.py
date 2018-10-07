#-*- coding: utf-8 -*-

import myreal as mr
#import functions as fc
import codes as cd

#구매전 정보 받는 함수

def question():
    global quantity
    global company
    global product
    global prc_date
    quantity = input("how many tickets do you want to buy? :")
    company = input("which company do you want buy from?  \n"
                    "myreal = 11 \n"
                    "waug = 12\n"
                    "enter ::::: ")
    product = input("what product do you want buy? \n"
                    "hkdiseny = 0  \n uss = 1 \n"
                    ":")
    prc_date = input("reservation date :")

def cal(amount , rule):
    total_amount = float(amount)
    nomal_rule = float(rule)
    real_trans =  float(total_amount / nomal_rule) #25.25
    total_trans = int(round(real_trans + 0.5)) #26
    global perfect_trans
    perfect_trans = round(real_trans - 0.5) #25
    global remainder
    remainder = real_trans - perfect_trans #0.25


if __name__ == "__main__":
    question()
    print(quantity, company, product, prc_date)

    if company == cd.company_code[0]['nb_code']:
        rules = cd.company_code[0]['buy_rule']
    elif company == cd.company_code[1]['nb_code']:
        rules = cd.company_code[1]['buy_rule']


    if company == cd.produc_code[0]['nb_code']:
        #uss url 가지고오기
        prod_url = ""
    elif company == cd.produc_code[1]['nb_code']:
        #홍디 ur 가지고오기
        prod_url = ""


    cal(quantity , rules)
    print(perfect_trans, remainder)





    #구매시행
    if company == cd.company_code[0]['nb_code']:
        #마리구매시행
    elif company == cd.company_code[1]['nb_code']:
        #와그 구매실행

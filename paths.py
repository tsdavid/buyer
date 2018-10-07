#myreal-x-1 paths

#function1
mr_login_pth = [
"//*/input[@name='user[email]']",
"//*/input[@name='user[password]']",
"/html/body/main/div/div/div[3]/form/div/div[4]/button"
]

#function2
mr_logout_pth = [
"/html/body/div[3]/header/nav/div[1]/div[3]/ul/li[4]/a/img",
"/html/body/div[3]/header/nav/div[1]/div[3]/div/ul/li[5]/div"
]

#function3
mr_res_date_pth = [
"//*[@id='calendarBtn']",
#str(rsv_date),

]


#function4
mr_res_qunt_pth = [
"//*[@id='optionBtn']/div[3]",
"//*[@id='optionBtn']/div[4]/div/div/div[2]/div/div/div/span[4]/button",
"//*[@id='checkPriceBtn']/button",
"/html/body/main/section/div[2]/div[1]/div[2]/div[3]/div/div[2]/form/div[2]/div/div[2]/button"
]

#function5
mr_order_pth=[
"/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[2]/div[2]/input",
"/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[3]/div[2]/input",
"/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[4]/div[2]/input",
"//*[@id='input-icc']",
"/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[5]/div[2]/select/option[2]",
"/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[6]/div[2]/input",
"/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/input",
"/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/select",
"/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/select/option[5]",
"/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[2]/div[3]/div/select",
"/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[2]/div[3]/div/select/option[4]",
"//*[@id='type-wcard']",
"//*[@id='checkbox_terms_traveler']",
"//*[@id='reservation-btn']"
]

#function6
mr_ticket_pth=[
"/html/body/div[3]/header/nav/div[1]/div[3]/ul/li[4]/a/img",
"/html/body/div[3]/header/nav/div[1]/div[3]/div/ul/li[2]/div[2]",
"/html/body/main/div/div[4]/div[2]/div[2]/div/a"
]

#function7
mr_clk_ticket_pth = [
"//*[@id='vouchersBtn']",
"/html/body/main/div/div[4]/div[3]/div/div[1]/div[3]/div[1]/a",
"/html/body/main/div/div[4]/div[3]/div/div[1]/div[3]/div[2]/a",
"/html/body/main/div/div[4]/div[3]/div/div[1]/div[3]/div[3]/a",
"/html/body/main/div/div[4]/div[3]/div/div[1]/div[3]/div[4]/a",
"/html/body/main/div/div[4]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]",

]

print mr_login_pth[0]
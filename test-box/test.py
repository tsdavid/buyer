total_amount = 101.0
nomal_rule = 4.0
real_trans =  float(total_amount / nomal_rule) #25.25
print(real_trans)
total_trans = int(round(real_trans + 0.5)) #26
print(total_trans)
perfect_trans = round(real_trans - 0.5) #25
print(perfect_trans)
remainder = real_trans - perfect_trans #0.25
print(remainder)
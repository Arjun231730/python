# Farmer Problem
# Mahesh is a farmer and owns 80 acres of land. His land is equally divided into 5 segments. He grows
# tomatoes in the 1st segment, potatoes in the 2nd segment, cabbage in the 3rd segment, sunflower in
# the 4th segment and sugarcane in the 5th segment.
# He is converting his land from chemical-driven farming to chemical-free farming. Mahesh starts with
# the conversion of vegetables into chemical-free produce. He spends the first 6 months doing the same.
# He then converts the sunflower land bank into chemical-free farming. This takes him another 4
# months. Finally, he converts sugarcane into chemical-free farming over the next 4 months.
# He gets a yield of the following for tomatoes. 30% of his tomato land gives him 10 tonne yield per acre.
# The remaining 70% of his tomato land gives him 12 tonnes yield per acre. The selling price of tomato
# is Rs. 7 per Kg.
# The yield of potatoes is 10 tonnes per acre. He sells each kg at Rs. 20.
# The yield of cabbage is 14 tonnes per acre. He sells each kg at Rs. 24.
# The yield of sunflowers is 0.7 tonnes per acre. He sells each kg at Rs. 200.
# The yield of sugarcane is 45 tonnes per acre. He sells each tonne at Rs. 4,000.
# All the crops are sowed at the same time. Mahesh gets the above yield at the above-mentioned rate
# in one crop cycle across his entire land of 80 acres.
# What is
# a. The overall sales achieved by Mahesh from the 80 acres of land.
# b. Sales realisation from chemical-free farming at the end of 11 months?

total_land=int(input("enter the total land in acre\n"))
segment=int(input("enter the total segment land is divided\n"))
segment=total_land/segment
total_yeild_by_tomato=(30/100)*segment*10000 + (70/100)*segment*12000
total_income_from_tomato=total_yeild_by_tomato*7
total_yeild_and_income_by_potato=segment*10000*20
total_yeild_and_income_by_cabbage=segment*14000*24
total_yeild_and_income_by_sunflower=700*segment*200
total_yeild_and_income_by_sugarcane=45*segment*4000
total_sales=total_income_from_tomato+total_yeild_and_income_by_potato+total_yeild_and_income_by_cabbage+total_yeild_and_income_by_sunflower+total_yeild_and_income_by_sugarcane
sale_for_11months=total_income_from_tomato+total_yeild_and_income_by_potato+total_yeild_and_income_by_cabbage+total_yeild_and_income_by_sunflower
print(total_land)
print(segment)
print(f"overall income from tomato: {total_income_from_tomato}")
print(f"overall income from potato: {total_yeild_and_income_by_potato}")
print(f"overall income from cabbage: {total_yeild_and_income_by_cabbage}")
print(f"overall income from sunflower: {total_yeild_and_income_by_sunflower}")
print(f"overall income from sugarcane: {total_yeild_and_income_by_sugarcane}")
print(f"overall sales achieved by mashesh from 80 scres land is: {total_sales}")
print(f"Sales realisation from chemical-free farming at the end of 11 months is: {sale_for_11months}")



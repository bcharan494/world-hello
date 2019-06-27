#! /usr/bin/python
"""
   purpose: assignment

"""
#charan

#selling price
tooth_paste_selling_price = 13
sandals_selling_price = 99
hair_oil_selling_price = 45

#quantity
quantity_of_tooth_paste = 1 
quantity_of_sandals = 1 
quantity_of_hair_oil = 1

#cost of each item
cost_of_tooth_paste = tooth_paste_selling_price * quantity_of_tooth_paste
cost_of_sandals = sandals_selling_price * quantity_of_sandals
cost_of_hair_oil = hair_oil_selling_price * quantity_of_hair_oil

#total cost 
total_cost = cost_of_tooth_paste + cost_of_sandals +cost_of_hair_oil
print("total cost =", total_cost)

#discount
total_discount= (23/100) * total_cost
print("total dsicount=",total_discount)

#new price after discount

New_price_after_discount = total_cost - total_discount
print("new price after discount=" , New_price_after_discount)

#gst of 12.5%
total_gst = (12.5/100) * New_price_after_discount
print("total gst=",total_gst)

#fianl price
final_price= New_price_after_discount + total_gst
print("final price=",final_price)






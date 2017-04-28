# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 17:27:03 2017

@author: tp293
"""

#constants
semi_annual_raise = .07
total_cost = 1000000.00
portion_down_payment = 0.25
downpay = total_cost * portion_down_payment
r = 0.04
months = 0



#user input
annual_salary = float(input("Enter your starting annual salary: "))
reset_salary = annual_salary



#changing variables
current_savings = 0
high = 10000
low = 0
portion_saved = int((high+low)/2)

                
                
while(abs(current_savings - downpay)  > 100 and portion_saved != low and portion_saved != high):         
    current_savings = 0
    annual_salary = reset_salary
    
    for i in range(36):
        current_savings += current_savings * r / 12 + annual_salary / 12 * portion_saved/10000
        if ( i + 1 ) % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
        
    if( current_savings < downpay):
        low = portion_saved
    else:
        high = portion_saved
        
    portion_saved = (high+low)/2
    months += 1

if (abs(current_savings - downpay)  > 100 and portion_saved != low and portion_saved != high):
    print("Best savings rate:",int(portion_saved) / 10000)
    print(months)
else:
    print("no good")
# Pounds to Kilograms Converter
# 2/11/2019
# CTI-110 P2HW2  - Meal Tip Calculator
# Da'Juan Avant

# total amount of purchased food
price= float(input('Enter the total cost'))

# tip for 15% 18% and 20%
tip1= price * .15
tip2= price * .18
tip3= price * .20

# display total of tips needed
print("tips for 15% $", format(tip1,",.2f"))
print("tips for 18% $", format(tip2,",.2f"))
print("tips for 20% $", format(tip3,",.2f"))
                               


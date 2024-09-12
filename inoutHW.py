import math
# familySize = 4
# pizzaSlices = 8
# slicesOrdered = int(input('Enter Number of Slices You Wish to Eat: '))
# totalSlices = slicesOrdered * familySize
# wholePizzas = math.ceil(totalSlices/pizzaSlices)
# leftover = wholePizzas*pizzaSlices - totalSlices

# if slicesOrdered == -1:
#     print('Please enter a valid number')
# else:
#     print('We need to order', wholePizzas, 'pizzas')
#     print('The number of leftover slices is', leftover)







# Solution using lists and loops #

familyOrder = []
familySize = int(input('Enter Family Size: '))
pizzaSlices = 8
totalSlices = 0

for i in range(familySize):
    slicesOrdered = int(input('Enter Number of Slices You Wish to Eat: '))
    familyOrder.append(slicesOrdered)
    totalSlices += slicesOrdered

    

wholePizzas = math.ceil(totalSlices/pizzaSlices)
leftover = wholePizzas*pizzaSlices - totalSlices
print('We need to order', wholePizzas, 'pizzas')
print('The number of leftover slices is', leftover)


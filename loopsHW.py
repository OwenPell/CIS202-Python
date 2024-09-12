muffins = 10
cupcakes = 10

while muffins > -1 and cupcakes > -1:
    order = input('Would you like to buy a cupcake or a muffin: ')
    if order == '0':
        print('Shop closed, come back tomorrow!')
        print(f'Remaining muffins: {muffins} | Remaining cupcakes: {cupcakes}')
        break
    elif order == 'Muffin' or order == 'muffin':
        if muffins == 0 and cupcakes != 0:
            print('Sorry, muffins are currently out of stock')
            print(f'Try a cupcake instead! We still have {cupcakes} cupcakes left')
        elif muffins == 0 and cupcakes == 0:
            print('Sorry, we are out of muffins and cupcakes for the day. Come back tomorrow!')
            break
        else:
            muffins = muffins - 1
            print(f'Muffin ordered')
    elif order == 'Cupcake' or order == 'cupcake':
        if cupcakes == 0 and muffins != 0:
            print('Sorry, cupcakes are currently out of stock')
            print(f'Try a muffin instead! We still have {muffins} muffins left')
        elif cupcakes == 0 and muffins == 0:
            print('Sorry, we are out of muffins and cupcakes for the day. Come back tomorrow!')
            break
        else:
            cupcakes = cupcakes - 1
            print(f'Cupcake ordered')
    else:
        print('Please enter valid response!')



water = int( input ('water '))
load = int (input('load '))
clothes = int (input ('clothes '))

def how_much_water(water, load, clothes):
    powi = (clothes-load)
    power = pow(1.1, powi)
    
    if (clothes > 2*load):
        amount_water='Too much clothes'
    elif (clothes < load):
        amount_water='Not enough clothes'
    else :
        amount_water=round((water*power),2)
    return (amount_water)

print (how_much_water(water,load,clothes))
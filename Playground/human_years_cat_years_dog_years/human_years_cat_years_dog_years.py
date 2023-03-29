
# def human_years_cat_years_dog_years(human_years):
#     human_years= input(int())
#     if human_years <=1:
#         cat_years= 15
#     elif human_years == 2:
#         cat_years= 15
#     else
#         cat_years=(human_years-2)*4+(15+9)

#     return [0,0,0] */

human_years = input('inserisci gli anni umani : ')

def human_years_cat_years_dog_years(human_years):

    if (int(human_years)) == 1:
        cat_years= 15
        dog_years=cat_years
    elif (int(human_years)) == 2:
        cat_years= 24
        dog_years=cat_years
    else :
        cat_years=(int(human_years)-2)*4+(15+9)
        dog_years=(int(human_years)-2)*5+(15+9)
    return [int(human_years),cat_years,dog_years]

print (human_years_cat_years_dog_years(human_years))

#print (human_years_cat_years_dog_years)
#%%
################################################################
#################own solution################################
import itertools
def secret_code(pin):
    possible_numbers = {'1': [1,2,4], '2':[2,1,3,5], '3':[3,2,6], '4':[4,1,5,7], '5':[5,2,4,6,8], '6':[6,3,5,9],
                     '7': [7,4,8], '8': [8,5,7,9,0], '9':[9,6,8], '0':[0,8]}
    list_of_possible_pins = []
    for i in str(pin):
        for j in possible_numbers.keys():
            if str(i) == j:
                to_append = list(map(str, possible_numbers[j]))
                list_of_possible_pins.append(to_append)
    list_of_possible_pins = itertools.product(*list_of_possible_pins) 
    result = [''.join(i) for i in list(list_of_possible_pins)]

    return result

#################################################################
######best-practice solution#####################################
from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
get_pins('12')
#%%
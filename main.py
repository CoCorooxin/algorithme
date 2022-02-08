from typing import List

"""
position_Init, position_Fin and position_Tmp are three list of integers
"""

def deplace(position_Init, position_Fin):
    todo = position_Init.pop(-1)
    if len(position_Fin) == 0 or todo < position_Fin[-1]:
        position_Fin.append(todo)
        return position_Init, position_Fin
    else:
        raise Exception(f"{position_Init}, {position_Fin}")



position_tmp = []
"""n is a integer, pos_1 and pos_2 are two lists"""
def positionTmp(n, position_1,position_2):
    position_tmp = []
    for i in range(n, 0, -1):
        if i in position_1 or i in position_2:
            continue
        else:
            position_tmp.append(i)
    return position_tmp


def deplaceTour(n, position_1, position_2):
    position_tmp = positionTmp(n, position_1, position_2)
    if n== 3:
        deplace(position_1,position_2)
        deplace(position_1, position_tmp)
        deplace(position_2, position_tmp)
        deplace(position_1, position_2)
        deplace(position_tmp, position_1)
        deplace(position_tmp, position_2)
        deplace(position_1, position_2)
        return position_2
    elif n>3:
        deplaceTour((n-1),position_1, position_tmp)
        deplace(position_1, position_2)
        deplaceTour((n-1),position_tmp, position_2)
        return f"the value on the last tower is {position_2}"

print(deplaceTour(6, [6,5,4,3,2,1], []))


"""
pour un tour de taille "n" on a
les étapes à réaliser
f(3) = 7
f(n) = f(n)*2 +1
çàd:
si on simplifie la fonct deplaceTour(n, position_1, position_2) à d(n, pos_1, pos_2)
on a:
d(4) = d(3,pos_1, pos_tmp) -> deplace(pos_1,pos_2) -> d(3,pos_tmp, pos_2)
d(5) = d(4,pos_1, pos_tmp) -> deplace(pos_1,pos_2) -> d(4,pos_tmp, pos_2)
...
d(n) = d((n-1),pos_1, pos_tmp) -> deplace(pos_1,pos_2) -> d((n-1),pos_tmp, pos_2)
"""
# Xin Chen 22105822

## TD3 Algo

###### I. D'après les informations données dans l'instruction, on peut faire une analyse sur les procéssu récursive de la fonction deplaceTour: 

$$
deplaceTour(n,pos_1, pos_2)=
\begin{cases}
n==3  & deplaceTour(3);\\ 
n>3 &  deplaceTour(n-1,pos_1,pos\_tmp) \to deplace(pos_1,pos_2) \to deplaceTour(n-1,pos\_tmp,pos_2)) ;
\end{cases}
\\
$$



Le code en python est donnée ainsi:

```Python
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
    position_tmp = positionTmp(n, position_1, position_2)  """initialise la 3eme tour"""
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
        deplaceTour((n-1),position_1, position_tmp)  """f(n-1) fois de deplace()"""
        deplace(position_1, position_2)              """1 fois"""
        deplaceTour((n-1),position_tmp, position_2)  """f(n-1) fois de deplace()"""
        return f"the value on the last tower is {position_2}"

print(deplaceTour(6, [6,5,4,3,2,1], []))
"""the value on the last tower is [6, 5, 4, 3, 2, 1]"""

"""
si on simplifie la fonct deplaceTour(n, position_1, position_2) à d(n, pos_1, pos_2)
on a:
d(4) = d(3,pos_1, pos_tmp) -> deplace(pos_1,pos_2) -> d(3,pos_tmp, pos_2)
d(5) = d(4,pos_1, pos_tmp) -> deplace(pos_1,pos_2) -> d(4,pos_tmp, pos_2)
...
d(n) = d((n-1),pos_1, pos_tmp) -> deplace(pos_1,pos_2) -> d((n-1),pos_tmp, pos_2)
"""
```

##### *II. La complexité de temps*

*on suppose que la complexité de la fonct deplace() est 1 &sans prenant en compte la complexité de la fonct positionTmp()   :* 

Pour un tour de taille "n" on définit une f(n) qui est la fonct pour calculer tous les processus de deplace() à réaliser
$$
f(3) =  2 \times 3 +1 = 7 , f(4) = 2 \times 7 + 1 = 15 ...  f(n) =  2\times f(n-1)  +1
$$

On peut en déduire que la complexité de temps T(n) est approximativement: 
$$
\mathrm{T(n)} = \sum_{i=3}^{n} f(i)
$$
Et si on ignore l'opération d'addition à la fin("+1")  Ce qui donne un O(n) = 
$$
{3 \times 2^n} \in \Theta(2^n)
$$

$$

$$


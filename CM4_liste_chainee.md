# la récursivité

### les structures de données récursives 

### listes chainées (à ne pas confondre avec les listes en python, pcq cette structure n'est pas indexée; on a uniquement l'accès à la premier élément de la liste chainée)

c'est comme une chaine composé des mallons; 

Si on a l'adresse du premier élément d'une liste chainée, on a un table de deux champs

| val(la val actuelle) | suivre (l'adresse de la val suivante) - un pointeur |
| -------------------- | :-------------------------------------------------: |
| book b = 48 octet    |                       book c                        |

Le concept de l'adresse - valeur

![image-20220208110448537](C:\Users\Chaumi\AppData\Roaming\Typora\typora-user-images\image-20220208110448537.png)



Structure de donnée dynamique 

deux attributs ou champs val est le champs de la structure où on stock un donnée 

Pour se donner une liste chainée , il suffit de se donner l'adresse du premier élément

### ça s'appel un système référentiel

### la définition : dans la plupart des langages la programmation du type "maillon" est récursive : 

### type : maillon =  

### structure { val : entier (ou autre)  suiv : maillon * (un pointeur vers un maillon ) \}

type liste  = maillon étoile 



l'exemple : une structure dynamique

```java
I.
    écrire un algo qui ajout un élément X à la tête d'une list chainée
ajouter un élément dans la liste - change la taille d'une liste
"origin first element in the list" : 
| 48| suir(2eme elem)|
"after":
| 22| suir(48) |
    
pseudo code:
ALGO InsereEnTete(L:liste d'entiers  x: entier) -> liste{
     P: maillon; 
     p = new(maillon);
     p.val = 22;
     p.suir = L;
     L = p;
}


II.
   écrire un programme qui affiche toutes les valeurs contenue des éléments d'une liste chainée 
                  
ALGO  AFFICHE (L: liste)-> liste{
    addresse_maillon_actuel: maillon*; // maillon_actuel est un addresse à un maillon actuel; maillon* signifie l'adresse du maillon;
    addresse_maillon_actuel = L;
    While(addresse_maillon_actuel != null){  
  // le dernier élément dans la liste a un adresse suir nulle
        print(addresse_maillon_actuel.val);
        addresse_maillon_actuel = addresse_maillon_actuel.suir;
    }
}                        
     
III.
   écrire un programme qui ajoute à la fin d'une liste un nouvel élément   
                  la même principe que la précédente
ALGO 
                  
                  
IV.
  écrire un programme qui supprime élément en tête

ALGO SUPPRIME(L:liste)-> liste{
    // il faut faire l'affectation et après supprimer le premier élément pour ne pas gaspiller la mémoire bon practique 
    p : maillon* 
    p = L;
    if (L.isEmpty){
         L = L.suir;
        free(p); 
    }
      
    return L;
}                  
                  
Remarque: 
    si p est un pointeur contenant l'adresse d'un objet X est "y" ; on peut l'accéder par p.y  pcq le champ y de l'objet pointé par p qui est X dans l'adresse 
                 
avant de changer ou ajouter element dans le Liste il faut liberer la mémoire dont occupe les elements qui est déjà dans le maillon      
                  
                  
V.
écrire un programme qui étant donné une liste L rétrouve la taile (la maillon)
                  
ALGO TAILLE_iterative(L:liste){
    counter: int; 
    adress_maillon : maillon;
    adress_maillon = L;
    while(adress_maillon != null){
        counter = counter+;
        adress_maillon = adress_maillon.suir;
    }
    return counter
}                 
                  
ALGO TAILLE_recursive(L:liste){
    if(L == null){
        return vide;
    }
    else{
        return (1+TAILLE_recursive(L.suir));
    }
}
                  
                  
```






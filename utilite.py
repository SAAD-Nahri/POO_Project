def input_non_vide(text):
    while True:
        x = input(text)
        if x:
            return x
        else:
            print('ce champ ne peut etre null, retapez')

def input_plus(text,i,*args):
    if args:
        x = input(text+f",la nouvele valeur et taper none si tu ne veut pas changer {args[0][i]} :")
        if x == '':
            return args[0][i]
        else:
            return x
    else:
        x = input_non_vide(text)
        return x


def afficher_list(L):
    for i in range(len(L)):
        print(i + 1, " : ", L[i], "\n")

def input_in_range(L):
    while True:
        i = int(input("Selon votre choix taper un nombre entre 1 et " + str(len(L)) + " -->  "))
        if (i > 0 and i <= len(L)):
            return i
        else:
            print('out of range, retapez')
def input_in_list(L):
    if len(L)==1:
        return L[0]
    else:
        afficher_list(L)
        x = input_in_range(L)
        return L[x-1]
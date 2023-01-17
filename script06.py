def pair(nombre):
    """cette fonction prend un nombre et definit sa parite"""
    if nombre%2==0:
        print("le nombre est pair")
    else:
        print("le nombre est impair")

pair(5)
print(pair.__doc__)
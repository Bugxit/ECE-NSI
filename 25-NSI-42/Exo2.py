def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a = "" 
    while a: 
        bin_a = str(a%2) + bin_a 
        a = a//2 
    return bin_a

print(binaire(0))
print(binaire(77))
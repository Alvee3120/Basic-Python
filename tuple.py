# () --> Tuple  --> Immutabel (cant be changed after assigning)
# {} --> Dictionary
# [] --> List  --> Mutable (can be change)

color = ('green','red', 'blue', 'yellow' )

print(color[0])

print(color[-1]) # yellow

print( color[1:]) # ('red', 'blue', 'yellow')

color[0] = 'black' # Not possible
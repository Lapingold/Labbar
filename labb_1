import math

print(''' 
   __ _ __ ___   ___    _   ___    _____ ___ _____ ___    _   _ __ ___  __   ___   _   _  __
 ,'_//// // o.) / _/  ,' \ / o |  /_  _// _//_  _// o | .' \ /// // _/ /  \ / o |,' \ / |/ /
/ /_/ U // o \ / _/  / o |/  ,'    / / / _/  / / /  ,' / o // ` // _/ / o |/  ,'/ o |/ || / 
|__/\_,'/___,'/___/  |_,'/_/`_\   /_/ /___/ /_/ /_/`_\/_n_//_n_//___//__,'/_/`_\|_,'/_/|_/ 
''')
print("Do you want to calculate the volume of a Cube or Tetrahedron? ")
choice = (input("Choose 1: Cube, or 2: Tetrahedron "))
if int(choice) == 1:
    side = float(input("Enter the length of one side of the cube (cm): "))
    cube = (side ** 3)
    print(f'The cube is {cube} in cm3')

if int(choice) == 2:
    side = float(input("Enter the length of one side of the tetrahedron (cm): "))
    sqrt = math.sqrt(2)
    tetrah = ((sqrt/12)*side**3)            
    round_off = round(tetrah, 4)            # Rounds off with 4 decimals
    print(f"The tetrahedron's volume is {round_off} cm3")

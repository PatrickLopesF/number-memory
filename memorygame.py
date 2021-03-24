import random
from os import system, name 
from time import sleep
list = []
round = 1


GAME_DIF = input("Choose your difficulty!\na)Easy\nb)Medium\nc)Hard\nd)Impossible ")

if GAME_DIF == "a":
    n = 2.5
elif GAME_DIF == "b":
    n = 1.75
elif GAME_DIF == "c":
    n = 1
elif GAME_DIF == "d":
    n = 0.5
else:
    print("Invalid input.")

def clear():
    if name == 'nt':
        _ = system('cls')

list.append(random.randint(1, 9))
x = ''.join(str(e) for e in list)
print(str(x))

y = input("Number: ")
x = ''.join(str(e) for e in list)
while x == y:
    del list[:]    
    for i in range(0, round + 1):                  
        list.append(random.randint(1, 9))
    x = ''.join(str(e) for e in list)
    print(x)
    sleep(n)
    clear()
    y = input("Number: ")
    clear()
    round += 1

if x != y:
    print("You lost!")
    sleep(2.5)

exit()
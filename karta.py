import sys
karta = [["#", "#", "#", "#", "#", "#"],["#", "P"," "," "," ", "#"], ["#", " "," "," "," ", "#"],["#", " "," "," "," ", "#"] ,["#", " "," "," "," ", "#"] ,["#","#","#","#","#","#"]]

class player:
    x=1
    y=1

def print_map():
    global karta
    for i in range(len(karta)):
        print(" ".join(karta[i]))

def check_collision(karta, move, player):
    if karta[player.y+move[0]][player.x+move[1]] == "G":
        battling()


def move(karta, riktning):
    global player
    move = [0,0]
    if riktning == "w":
        move = [-1,0]
    if riktning == "a":
        move = [0,-1]
    if riktning == "s":
        move = [1,0]
    if riktning == "d":
        move = [0,1]
    check_collision(karta, move, player)
    if not karta[player.y+move[0]][player.x+move[1]] == "#":
        karta[player.y+move[0]][player.x+move[1]] = "P"
        karta[player.y][player.x] = " "
        player.y += move[0]
        player.x += move[1]
    return(karta)

def death():
    print("Tyvärr verkar du ha dött, bättre lycka nästa gång 'v'")
    exit()

death()
while True:
    riktning = input("input: ")
    karta = move(karta, riktning)
    check_collision()
    print_map()


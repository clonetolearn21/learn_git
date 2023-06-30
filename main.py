from player import Player

def display_player(player):
    print("Info abour this player:")    
    print(player.name)
    print(player.age)
    print(player.nation)
    print(player.club)
    print(player.salary)
    print(player.position)

if __name__ == "__main__":
    player1 = Player(
        name="Bukayo Saka",
        age=23,
        nation="England",
        club="Arsenal",
        salary=100000,
        position="LF"  
    )
    
    display_player(player=player1)
    player1.salary = 200000

    display_player(player=player1)









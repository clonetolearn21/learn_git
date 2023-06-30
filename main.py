from player import Player

def display_player(player):
    print("Info abour this player:")    
    print(player.name)
    print(player.age)
    print(player.nation)
    print(player.club)

if __name__ == "__main__":
    player1 = Player(
        name="Bukayo Saka",
        age=23,
        nation="England",
        club="Arsenal"  
    )
    
    display_player(player=player1)








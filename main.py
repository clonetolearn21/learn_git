from player import Player


if __name__ == "__main__":
    player1 = Player(
        name="Bukayo Saka",
        age=23,
        nation="England",
        club="Arsenal",
        salary=100000,
        position="LF"  
    )
    print("Before up his salary:")
    print(player1)

    player1.salary = 200000
    
    print("After up his salary:")
    print(player1)
    

    print("This line is just to make me understand how git merge")
    print(f"Is {player1.name} rich: {Player.is_player_rich(player1.salary)}")







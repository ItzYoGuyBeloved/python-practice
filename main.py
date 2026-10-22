player_name = input("Enter player name: ").strip()
player_club = input("Enter club: ").strip()
player_position = input("Enter position: ").strip()
player_age = input("Enter age: ").strip()

if player_name == "":
    print("Error: Player name cannot be empty.")
elif player_club == "":
    print("Error: Club cannot be empty.")
elif player_position == "":
    print("Error: Position cannot be empty.")
elif not player_age.isdigit():
    print("Error: Age must be a whole number.")
else:
    print()
    print("Player Information")
    print(f"Player: {player_name}")
    print(f"Club: {player_club}")
    print(f"Position: {player_position}")
    print(f"Age: {player_age}")

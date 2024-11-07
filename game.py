import random

class Player:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        self.class_ = None  
        self.inventory = []
        self.health = 100

class Enemy:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.health = random.randint(10, 20) * difficulty

def get_class():
    print("Choose a class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        return "Warrior"
    elif choice == "2":
        return "Mage"
    elif choice == "3":
        return "Rogue"
    else:
        return "Invalid choice"

def get_stats():
    print("Choose a set of stats:")
    print("1. Strength 15, Agility 5, Magic 5")
    print("2. Strength 10, Agility 10, Magic 5")
    print("3. Strength 5, Agility 5, Magic 10")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        return {"Strength": 15, "Agility": 5, "Magic": 5}
    elif choice == "2":
        return {"Strength": 10, "Agility": 10, "Magic": 5}
    elif choice == "3":
        return {"Strength": 5, "Agility": 5, "Magic": 10}
    else:
        return {"Strength": 0, "Agility": 0, "Magic": 0}  

def create_player():
    name = input("Enter your name: ")
    class_ = get_class()
    player_stats = get_stats()

    enemy_difficulty = random.randint(1, 3)
    
    # Create a new Enemy with the chosen difficulty
    return Player(name, player_stats), Enemy(enemy_difficulty)

def fight(player, enemy):
    print(f"\n{player.name} encounters an enemy!")
    
    while player.health > 0 and enemy.health > 0:
        print(f"{player.name}'s health: {player.health}, Enemy's health: {enemy.health}")
        
        action = input("What would you like to do? (Attack, Use Magic) ")
        
        if action == "Attack":
            damage = random.randint(5, 10)
            enemy.health -= damage
            print(f"{player.name} attacks for {damage} damage!")
        elif action == "Use Magic":
            magic_damage = player.stats["Magic"] * 2
            enemy.health -= magic_damage
            print(f"{player.name} uses magic and deals {magic_damage} damage to the enemy!")
        else:
            print("Invalid choice. Please try again.")
            
        if enemy.health <= 0:
            break
            
    if player.health > 0:
        print(f"{player.name} wins the fight!")
    else:
        print("The enemy defeats you.")

def main():
    player, enemy = create_player()
    
    while True:
        fight(player, enemy)
        play_again = input("Would you like to play again? (Yes/No) ")
        
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    main()
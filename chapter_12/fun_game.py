import random


# Class to represent a creature
class Creature:

  def __init__(self, name, hitpoints, attack, level=1):
    self.name = name
    self.hitpoints = hitpoints
    self.attack = attack
    self.level = level

  def __str__(self):
    return f"{self.name} (HP: {self.hitpoints}, Attack: {self.attack}, Level: {self.level})"

  def to_dict(self):
    """Converts the Creature instance into a dictionary."""
    return {
        'name': self.name,
        'hitpoints': self.hitpoints,
        'attack': self.attack,
        'level': self.level
    }


# Function to display game rules
def display_rules():
  """Displays the game rules."""
  print(
      "Welcome to Pokemon!\nHere you can capture and battle against a great variety of Pokemon!\nDefeating other Pokemon allows your own Pokemon to level up! "
  )


# Function to simulate a creature capture
def capture_creature():
  """Simulates capturing a new Pokémon."""
  pokemons = [{
      'name': 'Blissey',
      'hitpoints': 255,
      'attack': 10
  }, {
      'name': 'Chansey',
      'hitpoints': 250,
      'attack': 5
  }, {
      'name': 'Wobbuffet',
      'hitpoints': 190,
      'attack': 33
  }, {
      'name': 'Wailord',
      'hitpoints': 170,
      'attack': 90
  }, {
      'name': 'Alomomola',
      'hitpoints': 165,
      'attack': 75
  }, {
      'name': 'Snorlax',
      'hitpoints': 160,
      'attack': 110
  }, {
      'name': 'Drifblim',
      'hitpoints': 150,
      'attack': 80
  }, {
      'name': 'GiratinaAltered',
      'hitpoints': 150,
      'attack': 100
  }, {
      'name': 'GiratinaOrigin',
      'hitpoints': 150,
      'attack': 120
  }, {
      'name': 'Slaking',
      'hitpoints': 150,
      'attack': 160
  }, {
      'name': 'Hariyama',
      'hitpoints': 144,
      'attack': 120
  }, {
      'name': 'Wigglytuff',
      'hitpoints': 140,
      'attack': 70
  }, {
      'name': 'Munchlax',
      'hitpoints': 135,
      'attack': 85
  }, {
      'name': 'Lapras',
      'hitpoints': 130,
      'attack': 85
  }, {
      'name': 'Vaporeon',
      'hitpoints': 130,
      'attack': 65
  }, {
      'name': 'Wailmer',
      'hitpoints': 130,
      'attack': 70
  }, {
      'name': 'Xerneas',
      'hitpoints': 126,
      'attack': 131
  }, {
      'name': 'Yveltal',
      'hitpoints': 126,
      'attack': 131
  }, {
      'name': 'Kyurem',
      'hitpoints': 125,
      'attack': 130
  }, {
      'name': 'KyuremBlack',
      'hitpoints': 125,
      'attack': 170
  }, {
      'name': 'KyuremWhite',
      'hitpoints': 125,
      'attack': 120
  }, {
      'name': 'Lanturn',
      'hitpoints': 125,
      'attack': 58
  }, {
      'name': 'Aurorus',
      'hitpoints': 123,
      'attack': 77
  }, {
      'name': 'Gogoat',
      'hitpoints': 123,
      'attack': 100
  }, {
      'name': 'Arceus',
      'hitpoints': 120,
      'attack': 120
  }, {
      'name': 'Cresselia',
      'hitpoints': 120,
      'attack': 70
  }, {
      'name': 'Throh',
      'hitpoints': 120,
      'attack': 100
  }, {
      'name': 'Musharna',
      'hitpoints': 116,
      'attack': 55
  }, {
      'name': 'Entei',
      'hitpoints': 115,
      'attack': 115
  }, {
      'name': 'Jigglypuff',
      'hitpoints': 115,
      'attack': 45
  }]
  pokemon = random.choice(pokemons)
  creature = Creature(pokemon['name'], pokemon['hitpoints'], pokemon['attack'])
  print(f"You have captured a {creature}!")
  return creature


# Battle function
def battle(creature1, creature2):
  """Simulates a battle between two Pokémon."""
  print(f"Battle Start: {creature1} vs {creature2}")
  while creature1.hitpoints > 0 and creature2.hitpoints > 0:
    creature1.hitpoints -= creature2.attack
    creature2.hitpoints -= creature1.attack
  winner = creature1 if creature1.hitpoints > 0 else creature2
  winner.level += 1  # Level up the winner
  print(f"{winner.name} wins and levels up to Level {winner.level}!")


# Save game state
def save_game(game_state):
  try:
    with open('game_save.txt', 'w') as file:
      for player in ['player1', 'player2']:
        file.write(f"{player}\n")
        for creature in game_state[player]:
          file.write(
              f"{creature.name},{creature.hitpoints},{creature.attack},{creature.level}\n"
          )
        file.write("\n")
    print("Game saved successfully.")
  except Exception as e:
    print(f"An error occurred while saving the game: {e}")


# Load game state
def load_game():
    try:
        with open('game_save.txt', 'r') as file:
            lines = file.readlines()
            game_state = {'player1': [], 'player2': []}
            current_player = None
            for line in lines:
                line = line.strip()
                if line in ['player1', 'player2']:
                    current_player = line
                elif line:
                    creature_data = line.split(',')
                    creature = {
                        'name': creature_data[0], 'hitpoints': creature_data[1],
                        'attack': creature_data[2], 'level': creature_data[3]
                    }
                    game_state[current_player].append(creature)
                else:
                    current_player = None
            game_state['current_player'] = 1
            return game_state
    except Exception as e:
        print(f"An error occurred while loading the game: {e}")
        return None


# Function to choose a creature from the player's collection
def choose_creature(player_creatures):
  """Lets the player choose a creature from their collection."""
  print("Choose a creature:")
  for i, creature in enumerate(player_creatures, 1):
    print(f"{i}. {creature}")
  choice = int(input("Enter your choice: ")) - 1
  return player_creatures[choice]


# Battle function
def battle(creature1, creature2):
  """Simulates a battle between two creatures."""
  # Simple battle mechanics
  while creature1.hitpoints > 0 and creature2.hitpoints > 0:
    creature1.hitpoints -= creature2.level
    creature2.hitpoints -= creature1.level
  winner = creature1 if creature1.hitpoints > 0 else creature2
  winner.level += 1  # Level up the winner
  print(f"{winner.name} wins and levels up to Level {winner.level}!")


# Main game loop
def main():
  # Initialize game state with default values
  game_state = {'player1': [], 'player2': [], 'current_player': 1}

  # Attempt to load saved game state
  loaded_game = load_game()
  if loaded_game:
    # Check if the loaded game state has the necessary keys
    if all(key in loaded_game
           for key in ['player1', 'player2', 'current_player']):
      for key in loaded_game.keys():
        if key in ['player1', 'player2']:
          pokelist = []
          for poke in loaded_game[key]:
            creature = Creature(poke['name'], int(poke['hitpoints']),
                              int(poke['attack']), int(poke['level']))
            pokelist.append(creature)
          loaded_game[key] = pokelist
      game_state = loaded_game
      print("Successfully load game.")
    else:
      print("Saved game is corrupted or incomplete. Starting a new game.")

  while True:
    current_player = game_state['current_player']
    player_creatures = game_state[f'player{current_player}']

    print(f"\nPlayer {current_player}'s turn")
    print("1. Display Rules")
    print("2. Capture a Creature")
    print("3. Battle")
    print("4. Save Game")
    print("5. End Turn")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
      display_rules()
    elif choice == '2':
      creature = capture_creature()
      player_creatures.append(creature)
    elif choice == '3':
      if len(player_creatures) == 0:
        print("You don't have any creatures to battle with!")
        continue

      # Choose a creature for battle
      your_creature = choose_creature(player_creatures)

      # Randomly select an opponent creature
      opponent_player = 'player2' if current_player == 1 else 'player1'
      opponent_creatures = game_state[opponent_player]
      if len(opponent_creatures) == 0:
        print(
            f"Player {opponent_player[-1]} doesn't have any creatures to battle against!"
        )
        continue

      opponent_creature = random.choice(opponent_creatures)
      print(f"Your creature: {your_creature}")
      print(f"Opponent's creature: {opponent_creature}")

      # Conduct the battle
      battle(your_creature, opponent_creature)

      # Remove defeated creatures and update the game state
      player_creatures = [c for c in player_creatures if c.hitpoints > 0]
      opponent_creatures = [c for c in opponent_creatures if c.hitpoints > 0]
      game_state[f'player{current_player}'] = player_creatures
      game_state[opponent_player] = opponent_creatures
    elif choice == '4':
      save_game(game_state)
    elif choice == '5':
      game_state['current_player'] = 2 if current_player == 1 else 1
    elif choice == '6':
      print("Thanks for playing!")
      break
    else:
      print("Invalid choice. Please try again.")


# Run the game
if __name__ == "__main__":
  main()


# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Hangman game using Python strings, loops, conditionals, and user input. This assignment helps you practice game logic and control flow while managing game state.

## 📝 Tasks

### 🛠️ Game Setup

#### Description
Create a list of secret words and randomly choose one for each game round.

#### Requirements
Completed program should:
- Use a predefined list of words in the code.
- Select a random word for the player to guess.
- Initialize a display version of the word using blanks (`_`) for each hidden letter.

### 🛠️ Guess Handling

#### Description
Allow the player to guess letters and update the game display accordingly.

#### Requirements
Completed program should:
- Accept letter guesses from the player.
- Reveal matched letters in their correct positions.
- Keep a list of letters already guessed and ignore repeated guesses.
- Show the current word progress in `_ _ _` format after each guess.

### 🛠️ Win/Lose Logic

#### Description
Track incorrect guesses and end the game when the player wins or runs out of attempts.

#### Requirements
Completed program should:
- Track the number of incorrect guesses remaining.
- End the game with a win message when the player guesses the entire word.
- End the game with a lose message when the player uses all attempts.
- Display the correct word when the game ends.

## 💡 Skills Practiced
- String manipulation
- Loops and conditionals
- User input handling
- Basic game state management

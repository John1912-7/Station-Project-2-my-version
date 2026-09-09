🎯 Guess the Number

A simple Python guessing game where the computer chooses a random number from 1 to 1000, and the player tries to guess it.

The game has three difficulty levels, limited attempts, and a temperature system that tells the player how close their guess is to the secret number.

🎮 How the Game Works

When the game starts, the computer randomly chooses a number between 1 and 1000.

The player first chooses a difficulty:

Difficulty	Attempts
Easy	20
Normal	14
Hard	7

The player then enters guesses until they:

Guess the secret number and win 🎉
Use all their attempts and lose

After every incorrect guess, the game gives two pieces of information:

Temperature — how close the guess is.
Higher / Lower — which direction the player should go.
🌡️ Temperature System

The temperature depends on the difference between the player's guess and the secret number.

Difference	Hint	Meaning
1–10	🔥 Sahara	Extremely close
11–25	🔥 Very Hot	Very close
26–50	🌡️ Hot	Close
51–100	☀️ Warm	Getting closer
101–200	🌤️ Cool	Somewhat far
201–350	❄️ Cold	Far away
351–500	🥶 Very Cold	Very far away
501+	🧊 Antarctica	Extremely far away
⬆️ Higher / Lower

The game also tells the player which direction to search.

For example, if the secret number is 505 and the player guesses 500:

Sahara 🔥 (Higher)


This means the player is very close, but needs to guess a higher number.

If the player guesses 510:

Sahara 🔥 (Lower)


This means the player is very close, but needs to guess a lower number.

The player is never shown the secret number until they lose.

🏆 Winning

If the player guesses the secret number correctly, the game displays:

You win 🎉!!!


The game then stops immediately.

💀 Losing

If the player uses all of their attempts without finding the secret number, the game displays:

You lose. Right number was - [secret number]


This reveals the correct number after the game ends.

🛠️ Technologies Used

The project is written entirely in Python.

It uses:

random — generates the secret number.
while — allows the player to make multiple guesses and validates the difficulty.
if / elif / else — controls the game logic and temperature hints.
input() — gets the player's choices and guesses.
print() — displays messages to the player.
abs() — calculates the positive difference between the guess and secret number.
Custom function get_attempts() — determines the number of attempts based on the selected difficulty.
📋 Example
Choose difficulty: Easy - type 1, Normal - type 2, Hard - type 3: 1

Your current attempts = 20
Input number: 500
Warm ☀️ (Higher)

Your current attempts = 19
Input number: 600
Hot 🌡️ (Lower)

Your current attempts = 18
Input number: 550
Very hot 🔥 (Lower)

...

You win 🎉!!!

🎯 Goal of the Project

The goal of this project is to practice fundamental Python concepts such as:

Variables
Random numbers
Functions
Loops
Conditions
User input
Basic game logic

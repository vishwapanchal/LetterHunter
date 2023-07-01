## Letter Hunter

Letter Hunter is a Python command-line game where players have to guess a randomly chosen word by entering individual letters. Put your letter-guessing skills to the test and see how many words you can uncover!

## Features
- Random word generation: Each game session features a unique word, ensuring a fresh experience every time.
- Interactive gameplay: Players can guess letters and see their progress in revealing the hidden word.

## Requirements
- Python 3.x
- random_word library
- colorama library
## Install the required libraries:
pip install random_word colorama

## Installation
1. Clone the repository:
git clone https://github.com/vishwapanchal/LetterHunter.git

2. Run the game script:
python letter_hunter.py

## How to Play
1. The game will generate a random word, represented by a series of dashes. This represents the hidden word that the player needs to guess.

2. Enter a letter and press Enter. If the letter is correct and exists in the word, it will be revealed in the corresponding positions. If the letter is incorrect, you will receive a message indicating so.

3. Continue guessing letters until you either reveal the entire word or run out of attempts. The number of attempts is not limited, so keep trying until you guess the word correctly.

4. After the game ends, you will be prompted to play again. Choose 'Y' to start a new game or 'N' to exit the game.

## Acknowledgements
This project utilizes the following libraries:

- Random-Word: For generating random words.
- Colorama: For adding colored text to the command-line interface.
Special thanks to the developers of these libraries for their contributions.

## Contributing
Contributions to Letter Hunter are welcome! If you have any suggestions, bug reports, or feature requests, please feel free to open an issue or submit a pull request.

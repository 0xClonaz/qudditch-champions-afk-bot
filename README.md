# Harry Potter: Quidditch Champions Bot

A Python bot for automating actions in the game "Harry Potter: Quidditch Champions."

You won't get banned (atleast now. I'll delete the bot if it changes). DO NOT USE it in online games, only use it in Offline carreer or exhibition games at your own risks.
If something is wrong or you found a bug leave a comment I will fix it. :)
If you have any ideas leave a comment.
I'm making a bot for The Qudditch Worldcup mode so it'll do the challenges.
## Features

- Detects and interacts with game elements using image recognition.
- Handles game actions such as pressing buttons and updating game stats.

## Installation

1. **Clone the Repository & How to use it**:
   ```bash
   git clone https://github.com/0xClonaz/qudditch-champions-afk-bot.git
   cd hp-quidditch-bot
   
OR download it from github

2. If python is not installed download and install the latest version: https://www.python.org/downloads/ 
then 
```pip install -r requirements.txt```

2. **Download tesseract .exe file and install it in 'C:\Program Files\Tesseract-OCR\tesseract.exe'
Download link for tesseract.exe:
https://github.com/UB-Mannheim/tesseract/wiki

3. Set every variable to your prefs: 
 -```pytesseract.pytesseract.tesseract_cmd = 'tesseract.exe's path'```
 -At the '```#SET Next item button here'``` comment change your Next item (when you get an item check the Next item button's coordinates with MPos for example: https://github.com/Bluegrams/MPos?tab=readme-ov-file) default is: 1470, 750
 -At '```#SET Continue button here'``` change it to the Continue's button coords. (It is after Next item button)
 -You can set 
        ```games_played += 1``` - Leave it 1 if it's your first game with the afk bot. 
        ```experience_points += 100``` - The XP you get after each game. It should be 50, but there is a double XP weekend atm so you can set it to 100
    These two is just for displaying stats in the terminal. It doesn't affect the game.

5. Open the game and click on Play -> Exhibition and start a Casual difficulty game with any team and any maps. In casual difficulty you don't have to play the bots will win every games for you.

6. Run the code. 'python main.py' in the console/terminal.

If you liked this project and want future updates you can buy a coffee for me here:
[![Buy me a butterbeer](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/0xThomasFlow)


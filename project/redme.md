# CONNECT INLINE 4
#### Video Demo:  <URL HERE>
#### Description: For my final project I created a match inline 4 game using python's pygame module.

## Requirements
- Python 3.x
- Pygame library
- board2.pn
- red.png
- yellow.png

## How to use
To start the game, run inline4.py. Command prompt will open with further instructions. 

## Goal of the game
Player one plays as a yellow color, while player two plays as red. Both players are human.  
Goal of the game is to match 4 pieces of your color in same row, column or diagonal in any direction.  
Players take turns picking columns in which to set their chip. Chips always fall to the lowest posible position.

## Explanation of the code
Game was first created to be playable completly in console without graphics. Console would first clear, then print out board with current state.  
To store current game state, list is used. Lists elements are lists that act as rows, and inside each list elements are empty strings that represent empty positions on the board.
Later, I decided to add graphics to the game to make it look better. List as a way to store gamestate stayed.  
To keep track player turns, I count the rounds played. Even/Odd round determine who is on the move.  
After every move, game checks if win condition is met. If its met, main game loop break, winner is determined by current round number and win message is displayed. After that program ends.
  
Here its important to note that check_win() function can be optimized so it doesnt check whole board everytime but instead it checks only around last played chip.  
This inefficiency is not noticable to end user so its is not a problem.


## Thought process and challenges of writing this game  
This game is my first contact with pygame module. With whole game logic writen, it was surprisingly easy to swap from console to pygame window.  
Biggest challange for me was correct placement of chips on screen so they match grid good enough while also to match gamestate list.  
For this I assume there must be a more elegant way of doing it. Because multiplying x and y coordinates of a chip by iteration integer gave me headaches while alligning it.  
  
Win condition was straight forward to program, untill in last minute i noticed that while checking in negative direction, -1 index goeas to last position in list and  
doing so it make a row/column a closed loop. This was fixed by adding a condition that checks if indexes are positive.  
  
I had great fun writing this code and it feels really rewarding to be able to play with my family the game I made from scratch. Can only imagine how awesome would be to  
invent and implend a new game. 

## Contribution
Feel free to download, edit, use or contribute to this project. Only purpose of this was to learn skills, and test abilities. It will remain forever so, for everyone. 

## Special thanks
Thanks to everyone who made CS50P possible. Special thanks to Proffesor David J. Malan for hosting such well put together lectures.




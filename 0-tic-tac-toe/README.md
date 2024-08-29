### README: Tic-Tac-Toe Game Implementation

#### Project Overview:

The **Tic-Tac-Toe** game is a simple, two-player game played on a 3x3 grid. Players take turns marking a square on the grid with their respective symbols: "X" or "O." The first player to get three of their symbols in a row (vertically, horizontally, or diagonally) wins the game. If all nine squares are filled without a winner, the game ends in a draw.

#### Features:

- **Two-player mode**: Players take turns playing on the same device.
- **Basic UI**: Command-line interface or basic graphical UI (to be decided).
- **Game Flow Management**: Automatically detects when a player wins or when the game is a draw.
- **Replay Option**: Players can restart the game after a match ends.

#### Project Structure:

- **README.md**: Provides information about the project, installation, and usage instructions.
- **main.py** (or `tic_tac_toe.py`): The main Python file containing the game logic.
- **utils.py**: (Optional) A helper module that may contain utility functions like checking for a win or validating inputs.
- **test_tic_tac_toe.py**: (Optional) Unit tests for the core game logic.

#### Technologies:

- **Language**: Python
- **Libraries**: None (built with standard Python libraries)

#### Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tic_tac_toe.git
   cd tic_tac_toe
   ```

2. Run the game:
   ```bash
   python main.py
   ```

---

### Pseudocode:

1. **Initialize the Game Board**:
   - Create a 3x3 grid to represent the board.
   - Set all positions on the board to empty (e.g., `None` or `" "`).

2. **Display the Board**:
   - Create a function to print the current state of the board to the screen.

3. **Player Turn Logic**:
   - Start with Player 1 (X).
   - Alternate between Player 1 and Player 2 (O) after each valid move.
   - Prompt the player to choose a grid position (1-9).
   - Check if the chosen position is valid (not already taken).

4. **Check for Win/Draw**:
   - After each move, check if the current player has won by checking all rows, columns, and diagonals.
   - If a win is detected, announce the winner and end the game.
   - If the board is full and no winner, announce a draw.

5. **Restart or End the Game**:
   - Ask the players if they want to play again.
   - If yes, reset the board and restart the game.
   - If no, exit the game.

---

### Flowchart:

```plaintext
+-------------------------------+
|          Initialize Board     |
+---------------+---------------+
                |
                v
+---------------+---------------+
|        Display Initial Board  |
+---------------+---------------+
                |
                v
+---------------+---------------+
|  Player Turn Logic (Player 1) |
+---------------+---------------+
                |
                v
+---------------+---------------+
|       Check Valid Move?       |
+---------------+---------------+
        | Yes             | No
        v                 |
+---------------+         |
| Place Symbol  |---------+
+---------------+
        |
        v
+---------------+---------------+
|   Check Win/Draw Condition?   |
+---------------+---------------+
    | Win       | Draw         | No
    v           v              v
+---------+ +---------+    +---------------+
| Announce| | Announce|    |  Alternate    |
| Winner  | |  Draw   |    |    Player     |
+---------+ +---------+    +---------------+
                |              |
                v              v
+-------------------------------+
|    Restart or End Game?       |
+-------------------------------+
        | Yes             | No
        v                 |
+---------------+         |
| Reset Board   |---------+
+---------------+
```

---

### Next Steps:

1. **Write the code for each step**: Start by writing the basic code to initialize and display the board.
2. **Develop player turn logic**: Implement the code for player input and symbol placement.
3. **Implement win/draw logic**: Write functions to check for win/draw conditions after each move.
4. **Test and Refine**: Ensure the game works correctly, handling edge cases like invalid inputs or ties.
5. **Optional Enhancements**: Consider adding a basic graphical UI or more advanced features like AI for single-player mode.


1. Define the class board and display
2. Initialize the class
3. header function
4. Refresh function ( clear the screen, print header , show board)

5. While loop (refresh the screen)
6. Get X input
7. update the board ( board.update_cell())
8. Refresh the screen again and copy that as the same thing for O 

9. Define is_winner to determine the winner(true or false)


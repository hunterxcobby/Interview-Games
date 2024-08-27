
### Breakdown of Logic:

- **User Input**: We prompt the user to select between Rock, Paper, and Scissors by entering `0`, `1`, or `2`.
- **Validation**: We validate the user's input to ensure it's a valid choice. If the user enters anything other than `0`, `1`, or `2`, we print a message that they've lost by entering an invalid number.
- **Computer's Choice**: The computer randomly picks its move using `random.randint(0, 2)`, which will give either `0` (Rock), `1` (Paper), or `2` (Scissors).
- **Game Outcome**:
  - We check the different conditions to decide who wins. This involves comparing the user's choice with the computer's choice and determining the winner based on the rules of Rock-Paper-Scissors.
  - If both choices are the same, it's a tie.
  - We explicitly handle some special cases (e.g., Rock vs. Scissors) and then use the relative size of the choices to handle the remaining cases.
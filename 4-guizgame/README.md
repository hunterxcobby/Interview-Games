### Explanation of Key Sections:

1. **Question Bank and Options**:  
   - The `question_bank` list contains dictionaries. Each dictionary holds a question (`text`) and the correct answer (`answer`).
   - The `options` list contains all the multiple-choice options for each question.

2. **check_answer Function**:  
   - This function checks whether the user's guess is correct. It takes the user's input (`guess`) and the correct answer from the question bank (`answer`), returning `True` if correct, and `False` if incorrect.

3. **Main Loop**:  
   - The `for` loop iterates over the questions in the `question_bank`. For each question, it displays the question and its options, takes the user's guess, and checks if it’s correct using the `check_answer()` function.
   - Based on whether the user's answer is correct or not, the script updates the score and informs the user.

4. **Score Calculation**:  
   - After all questions are answered, the final score is calculated as a percentage and displayed to the user.

---

### How to Use This for Visualization:

- **Before running the code**, you can walk through each section of the code and try to mentally visualize what happens at each step (e.g., displaying the question, getting the answer, checking the correctness).
- **When practicing**, comment out certain sections of the code (e.g., the answer-checking logic) and try rewriting them from scratch.
- **Test modifications**: Try tweaking the quiz logic slightly. For example, add more questions, or make the code handle more advanced features like handling invalid inputs. This will further solidify your understanding.

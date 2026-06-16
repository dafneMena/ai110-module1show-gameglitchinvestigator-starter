# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.

1. **Select a Difficulty Level**
   - Determines the range of numbers and attempt limit:
     - **Easy**: 1-20 range, 6 attempts
     - **Normal**: 1-100 range, 8 attempts
     - **Hard**: 1-50 range, 5 attempts

2. **Guess the Secret Number**
   - The game generates a random secret number at the start of each round
   - Player enters numerical guesses

3. **Receive Feedback**
   - 📈 **"Go HIGHER!"** - Guess is too low
   - 📉 **"Go LOWER!"** - Guess is too high
   - 🎉 **"Correct!"** - Player wins

4. **Earn Points**
   - Winning quickly = higher score (up to 100 points)
   - Incorrect guesses add/subtract points based on attempt parity
   - Minimum score: 10 points per win

5. **Game Over**
   - **Win**: Guess the number before attempts run out
   - **Lose**: Exhaust all attempts without guessing correctly

Key Features

- Difficulty-based gameplay with different ranges and attempt limits
- Score tracking system
- Guess history logging
- Developer debug mode to view game state
- Dynamic difficulty switching with secret number regeneration

- [X] Detail which bugs you found.

1. **Never ending game** - 
  The first time I ran this project, the game never ended. For example, I attempted to guess the number until I reached a maximum of 8 attempts. After reaching those attempts, I tried to click 'New Game,' but the game would not reset. My previous guess would still be in the text box, and the message "Game over. Start a new game to try again." would not disappear. Also, impossible to restart the game after winning. Previous submission does not erase, new attempts do not update. 

2. **Incorrect number of attempts** - 
  The number of attempts begin at 1 not 0. This means the user has one less attempt to guess. 

3. **Incorrect hint** - 
  The hints were inaccurate. The game would tell me to guess lower when the secret number was actually higher and vice versa

4. **Secret number is not always within range of difficulty** - The number range of each diffculty varies. The issue is the secret number sometimes exceeds the range of the hard and easy level.


- [X] Explain what fixes you applied.

1. Wrong Attempt Counting
- **Problem**: Attempts started at 1, reducing the actual number of guesses allowed
- **Solution**: Initialize attempts at 0 so players get the full attempt limit
- **Code**: Changed `st.session_state.attempts = 1` to `= 0`

2. Reversed Hint Logic

- **Problem**: The "Higher/Lower" hint messages were backwards
  - When guess was **too high**, message said "Go HIGHER!" ❌
  - When guess was **too low**, message said "Go LOWER!" ❌
  - Made the game unwinnable since hints were deliberately misleading

- **Solution**: Corrected the comparison logic in `check_guess()` function
  - When `guess > secret` → "Go LOWER!" ✅
  - When `guess < secret` → "Go HIGHER!" ✅

- **Code Fix**: 
  ```python
  if guess > secret:
      return "Too High", "📉 Go LOWER!"
  else:
      return "Too Low", "📈 Go HIGHER!"

3. Difficulty Range Mismatch
- **Problem**: Secret number wasn't regenerated when switching difficulties, could fall outside new range
- **Solution**: Added check to regenerate secret if it falls outside the new difficulty's range
- **Code**: Added validation `if not (low <= st.session_state.secret <= high):` when difficulty changes

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects difficulty of Easy
2. User enters a guess of 15 & hits "Submit Guess"
3. The hint returns "Go HIGHER" 
4. User enters a guess of 20 -> hint returns "Go LOWER"
5. The number of attempts is modified correctly 
6. Game ends after the correct guess or the max attempts has been reached

**Screenshot**: 

<img width="665" height="855" alt="image" src="https://github.com/user-attachments/assets/7bb0bdb7-cbe8-492d-b524-a107a824651e" />


## 🧪 Test Results

```
collected 19 items                                                                                                                                                               
tests/test_game_logic.py::test_winning_guess PASSED                                                                                                                        [  5%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                                                                                       [ 10%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                                                                                        [ 15%]
tests/test_game_logic.py::test_guess_too_high_with_string_secret PASSED                                                                                                    [ 21%]
tests/test_game_logic.py::test_guess_too_low_with_string_secret PASSED                                                                                                     [ 26%]
tests/test_game_logic.py::test_winning_guess_with_string_secret PASSED                                                                                                     [ 31%]
tests/test_game_logic.py::TestSecretRangeValidation::test_easy_difficulty_range PASSED                                                                                     [ 36%]
tests/test_game_logic.py::TestSecretRangeValidation::test_normal_difficulty_range PASSED                                                                                   [ 42%]
tests/test_game_logic.py::TestSecretRangeValidation::test_hard_difficulty_range PASSED                                                                                     [ 47%]
tests/test_game_logic.py::TestSecretRangeValidation::test_invalid_difficulty_defaults_to_normal PASSED                                                                     [ 52%]
tests/test_game_logic.py::TestSecretRangeValidation::test_secret_outside_hard_range PASSED                                                                                 [ 57%]
tests/test_game_logic.py::TestSecretRangeValidation::test_secret_at_hard_upper_boundary PASSED                                                                             [ 63%]
tests/test_game_logic.py::TestSecretRangeValidation::test_secret_at_hard_lower_boundary PASSED                                                                             [ 68%]
tests/test_game_logic.py::TestSecretRangeValidation::test_secret_switching_normal_to_hard_valid PASSED                                                                     [ 73%]
tests/test_game_logic.py::TestSecretRangeValidation::test_secret_switching_normal_to_hard_invalid PASSED                                                                   [ 78%]
tests/test_game_logic.py::TestSecretRangeValidation::test_secret_switching_hard_to_easy_invalid PASSED                                                                     [ 84%]
tests/test_game_logic.py::TestSecretRangeValidation::test_secret_switching_easy_to_hard_valid PASSED                                                                       [ 89%]
tests/test_game_logic.py::TestSecretRangeValidation::test_secret_at_easy_upper_boundary_invalid_in_hard PASSED                                                             [ 94%]
tests/test_game_logic.py::TestSecretRangeValidation::test_secret_outside_easy_range_from_normal PASSED                                                                     [100%]

============================================================================== 19 passed in 0.04s ===============================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

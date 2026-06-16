# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game appeared to be functioning correctly. I could easily change the difficulty level, enter a guess, hit submit, and receive hints telling me to guess lower or higher. However, after playing the game a few times, I noticed the game was running incorrectly. Continue reading to learn about the bugs I discovered.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

1. **Never ending game** - 
  The first time I ran this project, the game never ended. For example, I attempted to guess the number until I reached a maximum of 8 attempts. After reaching those attempts, I tried to click 'New Game,' but the game would not reset. My previous guess would still be in the text box, and the message "Game over. Start a new game to try again." would not disappear

  Also, impossible to restart the game after winning. Previous submission does not erase, new attempts do not update. 

2. **Incorrect number of attempts** - 
  The number of attempts begin at 1 not 0. This means the user has one less attempt to guess. 

3. **Incorrect hint** - 
  The hints were inaccurate. The game would tell me to guess lower when the secret number was actually higher and vice versa

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|----------------------|
| N/A | "Attempts left: 8 ", on normal difficulty | "Attempts left: 7 ", on normal difficulty | None |
| guess of 60 | "Go LOWER!", hint shown | "Go HIGHER!", hint shown | None |
| "New Game" btn click | New game starts, hint messages disappear, previous guess is cleared | Nothing, can't end game. Previous guess is still entered. Hint messages don't disappear. Can't submit guess | None |
| guess of 12 | "Go HIGHER!", hint shown | "Go LOWER!", hint shown | None |


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

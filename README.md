

## **Project Title:**

**Rock, Paper, Scissors Game using Python Tkinter**--

## **1. Introduction**

This project is a simple **Rock, Paper, Scissors** game created using **Python's Tkinter GUI** library. The game allows the user to choose between Rock, Paper, or Scissors, while the computer makes a random choice. The program determines the winner based on classic game rules and displays the outcome and score dynamically.

This application demonstrates key programming concepts such as event-driven programming, GUI design, and basic game logic in Python.

## **2. Main Objectives**

1. To build a user-interactive Rock, Paper, Scissors game using Python’s `tkinter` GUI module.
2. To understand event-driven programming through button interactions.
3. To implement decision-making using `if-elif-else` logic based on user and computer choices.
4. To create a visual interface for displaying game results and score tracking.
5. To help beginners understand how logic and GUI elements work together in Python.

## **3. Software & Tools Used**

* **Programming Language**: Python 3.x
* **Library**: tkinter (built-in GUI library in Python), random
* **IDE**: PyCharm / VS Code / IDLE
* **Platform**: Desktop (Windows recommended)
* **Input Devices**: Keyboard and Mouse

## **4. System Design**

* **Main Window**: Configured using `Tk()`, with title and size.
* **Labels**: Used to display headings, scores, and results.
* **StringVar**: Stores and dynamically updates text labels.
* **Buttons**: For Rock, Paper, Scissors options and a Reset Game button.
* **Functions**:

  * `play()`: Handles game logic and score updates.
  * `reset()`: Resets scores and display text to start a new game.
* **Layout Management**: Achieved using `.pack()` and `.grid()` methods.

## **5. Functionalities Implemented**

* Allows user to select Rock, Paper, or Scissors using buttons.
* Computer makes a random choice.
* Displays the result of each round (Win/Lose/Tie).
* Tracks and updates user and computer scores.
* Provides a Reset button to restart the game.

## **6. Workflow**

1. User starts the application.
2. The window displays the game title and instructions.
3. User clicks one of the buttons: Rock, Paper, or Scissors.
4. The computer randomly selects a move.
5. The result and updated scores are shown.
6. User can click **Reset Game** to restart at any time.

## **7. Sample Input/Output**

| **Action**          | **Expected Result**                             |                     |
| ------------------- | ----------------------------------------------- | ------------------- |
| Clicks "Rock"       | Displays: You chose Rock, Computer chose Paper… |                     |
| Computer wins       | Score updates: Computer +1                      |                     |
| Clicks "Reset Game" | Score reset to 0                                | 0 and message reset |
| Clicks "Scissors"   | Displays: You Win! if computer chose Paper      |                     |
## **8. Advantages**

* Simple and engaging game logic.
* Beginner-friendly GUI using only built-in libraries.
* Interactive and visual game flow.
* Good foundation for learning Python functions and GUI.
* Easy to extend or customize.
## **9. Limitations**

* No animations or sound effects.
* Only supports single-player mode against computer.
* No game history or leaderboard feature.
* GUI styling is basic.
## **10. Future Enhancements**
* Add icons/images instead of plain text buttons.
* Add sound effects or animations.
* Introduce score saving or high score tracking.
* Include multiple rounds and round selection.
* Improve UI with better styling or dark/light mode toggle.
## **11. Conclusion**
The Rock, Paper, Scissors game using Python's `tkinter` is a fun and educational project that introduces basic GUI programming, event handling, and conditional logic. This project serves as a stepping stone for more complex game development and GUI applications. It is ideal for Python beginners who want to practice building interactive desktop applications.

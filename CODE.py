from tkinter import *
import random

# Create main window
root = Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.configure(bg="#ffffff")

# Scores
user_score = 0
comp_score = 0

# Choices list
choices = ["Rock", "Paper", "Scissors"]

# Heading
Label(root, text="Rock Paper Scissors Game", font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=10)

# Score labels
score_text = StringVar()
score_text.set("Your Score: 0 | Computer Score: 0")
score_label = Label(root, textvariable=score_text, font=("Arial", 12), bg="#ffffff")
score_label.pack(pady=5)

# Result label
result_text = StringVar()
result_text.set("Choose Rock, Paper or Scissors to start")
result_label = Label(root, textvariable=result_text, font=("Arial", 12), fg="blue", bg="#ffffff")
result_label.pack(pady=20)

# Game logic
def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(choices)

    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        user_score += 1
        result = "You Win!"
    else:
        comp_score += 1
        result = "Computer Wins!"

    result_text.set(f"You chose: {user_choice}\nComputer chose: {comp_choice}\n{result}")
    score_text.set(f"Your Score: {user_score} | Computer Score: {comp_score}")

# Reset function
def reset():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    score_text.set("Your Score: 0 | Computer Score: 0")
    result_text.set("Choose Rock, Paper or Scissors to start")

# Button Frame
button_frame = Frame(root, bg="#ffffff")
button_frame.pack(pady=10)

# Rock button
rock_btn = Button(button_frame, text="Rock", width=10, font=("Arial", 12), command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

# Paper button
paper_btn = Button(button_frame, text="Paper", width=10, font=("Arial", 12), command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

# Scissors button
scissors_btn = Button(button_frame, text="Scissors", width=10, font=("Arial", 12), command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Reset button
reset_btn = Button(root, text="Reset Game", font=("Arial", 12), bg="red", fg="white", command=reset)
reset_btn.pack(pady=20)

# Start main event loop
root.mainloop()

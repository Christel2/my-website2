import tkinter as tk
from tkinter import messagebox
import random

class MathGameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Math Rescue")
        self.geometry("800x600")
        self.configure(background="#669966")  # Set background color
        self.create_home_page()

    def create_home_page(self):
        # Math Rescue logo
        self.logo_image = tk.PhotoImage(file="math_rescue_logo.png")
        self.background_label = tk.Label(self, image=self.logo_image, bg="#669966")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=0.5)

        # Full name input
        self.full_name_label = tk.Label(self, text="Enter your full name:", font=("Arial", 16), bg="#669966")
        self.full_name_label.place(relx=0.5, rely=0.6, anchor="center")
        self.full_name_entry = tk.Entry(self, font=("Arial", 14))
        self.full_name_entry.place(relx=0.5, rely=0.65, anchor="center")

        # Age input
        self.age_label = tk.Label(self, text="Enter your age:", font=("Arial", 16), bg="#669966")
        self.age_label.place(relx=0.5, rely=0.7, anchor="center")
        self.age_entry = tk.Entry(self, font=("Arial", 14))
        self.age_entry.place(relx=0.5, rely=0.75, anchor="center")

        # Continue button
        self.continue_btn = tk.Button(self, text="Continue", font=("Arial", 16), command=self.proceed_to_whos_here, bg="#FFA07A")
        self.continue_btn.place(relx=0.5, rely=0.85, anchor="center")

    def proceed_to_whos_here(self):
        name = self.full_name_entry.get()
        age = self.age_entry.get()
        if name.strip() and age.strip():
            self.destroy()
            whos_here_page = WhosHerePage(name, age)
            whos_here_page.mainloop()
        else:
            messagebox.showwarning("Incomplete Information", "Please enter your full name and age.")

class WhosHerePage(tk.Tk):
    def __init__(self, name, age):
        super().__init__()
        self.title("Math Rescue - Who's Here")
        self.geometry("400x300")
        self.configure(background="#669966")  # Set background color
        self.name = name
        self.age = age
        self.create_widgets()

    def create_widgets(self):
        # Greeting
        welcome_text = tk.Label(self, text=f"Hi {self.name}! Welcome to Math Rescue!", font=("Arial", 20), bg="#669966", fg="darkblue")
        welcome_text.pack(pady=20)

        # Tiger image
        self.tiger_image = tk.PhotoImage(file="max_the_math_tiger.png")
        tiger_label = tk.Label(self, image=self.tiger_image, bg="#669966")
        tiger_label.pack(pady=20)

        # "Who's Here?" text
        who_text = tk.Label(self, text="Who's Here?", font=("Arial", 18), bg="#669966")
        who_text.pack(pady=10)

        # Buttons
        btn_kid = tk.Button(self, text="Kid", font=("Arial", 16), command=self.start_game_kid, bg="#FF6961", bd=4, relief=tk.GROOVE)
        btn_kid.pack(pady=5)

        btn_parent = tk.Button(self, text="Parent", font=("Arial", 16), command=self.show_parent_page, bg="#77DD77", bd=4, relief=tk.GROOVE)
        btn_parent.pack(pady=5)

        btn_both = tk.Button(self, text="Both", font=("Arial", 16), command=self.show_parent_page, bg="#ADD8E6", bd=4, relief=tk.GROOVE)
        btn_both.pack(pady=5)

    def start_game_kid(self):
        self.destroy()  # Close the home page window
        game = MathGame()
        game.mainloop()

    def show_parent_page(self):
        self.destroy()  # Close the home page window
        parent_page = ParentPage()
        parent_page.mainloop()

class ParentPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Parent Page")
        self.geometry("400x300")
        self.configure(background="#669966")  # Set background color
        self.create_widgets()

    def create_widgets(self):
        # Back button
        btn_back = tk.Button(self, text="Back to Menu", font=("Arial", 14), command=self.back_to_menu, bg="#FFA07A", bd=4, relief=tk.GROOVE)
        btn_back.pack()

    def back_to_menu(self):
        self.destroy()  # Close the parent page window
        app = MathGameApp()
        app.mainloop()

class MathGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Math Game")
        self.geometry("400x300")
        self.configure(background="#669966")  # Set background color
        self.create_widgets()
        self.score = 0
        self.generate_question()
        self.hint_count = 0

    def create_widgets(self):
        # Question label
        self.lbl_question = tk.Label(self, text="", font=("Arial", 20), bg="#669966")
        self.lbl_question.pack(pady=10)

        # Entry field for answer
        self.entry_answer = tk.Entry(self, font=("Arial", 16))
        self.entry_answer.pack(pady=5)

        # Submit button
        self.btn_submit = tk.Button(self, text="Submit", font=("Arial", 14), command=self.check_answer, bg="#FFA07A", bd=4, relief=tk.GROOVE)
        self.btn_submit.pack(pady=5)

        # Score label
        self.lbl_score = tk.Label(self, text="Score: 0", font=("Arial", 14, "bold"), bg="#669966")
        self.lbl_score.pack()

        # Feedback label for incorrect answers
        self.lbl_feedback = tk.Label(self, text="", font=("Arial", 14, "italic"), fg="red", bg="#669966")
        self.lbl_feedback.pack()

        # Hint button
        self.btn_hint = tk.Button(self, text="Hint", font=("Arial", 14), command=self.show_hint, bg="#FFA07A", bd=4, relief=tk.GROOVE)
        self.btn_hint.pack()

        # Back button
        self.btn_back = tk.Button(self, text="Back to Menu", font=("Arial", 14), command=self.back_to_menu, bg="#FFA07A", bd=4, relief=tk.GROOVE)
        self.btn_back.pack()

    def generate_question(self):
        # Generate a simple addition question for now
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.correct_answer = self.num1 + self.num2
        self.question_text = f"What is {self.num1} + {self.num2}?"
        self.lbl_question.config(text=self.question_text)

    def check_answer(self):
        user_answer = self.entry_answer.get()
        try:
            user_answer = int(user_answer)
            if user_answer == self.correct_answer:
                self.score += 1
                self.lbl_score.config(text=f"Score: {self.score}")
                self.lbl_feedback.config(text="Well done!", fg="green")  # Provide feedback for correct answer
                self.generate_question()
                self.entry_answer.delete(0, tk.END)  # Clear entry field
            else:
                if self.hint_count < 2:
                    self.show_hint()
                else:
                    self.lbl_feedback.config(text="Try again.", fg="red")  # Provide feedback for incorrect answer
        except ValueError:
            self.lbl_feedback.config(text="Please enter a number.", fg="red")  # Handle non-numeric input

    def show_hint(self):
        hints = [
            "Try counting up from the first number.",
            "Think about how you can split the problem into smaller parts.",
            "Remember to carry over if necessary."
        ]
        messagebox.showinfo("Hint", hints[self.hint_count])
        self.hint_count += 1

    def back_to_menu(self):
        self.destroy()  # Close the game window
        app = MathGameApp()
        app.mainloop()

def main():
    app = MathGameApp()
    app.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox

class MoodTrackerApp:
    def __init__(self, master):
        self.master = master
        master.title("Graphical Mood Tracker")

        self.days_to_track = 14
        self.mood_scores = []
        self.days_tracked = 0

        self.create_widgets()

    def create_widgets(self):
        self.label_title = tk.Label(self.master, text="What's your mood today?", font=("Arial", 24))
        self.label_title.pack(pady=20)

        self.label_days_left = tk.Label(self.master, text=f"Days left: {self.days_to_track}", font=("Arial", 16))
        self.label_days_left.pack(pady=10)

        self.frame_buttons = tk.Frame(self.master)
        self.frame_buttons.pack(pady=10)

        self.buttons = {
            "☺️": 10,
            "🥴": 5,
            "😅": 4,
            "😪": 5,
            "😭": 1,
            "🥲": 2
        }

        for emoji, score in self.buttons.items():
            button = tk.Button(self.frame_buttons, text=emoji, font=("Arial", 36), command=lambda e=emoji, s=score: self.record_mood(s))
            button.pack(side=tk.LEFT, padx=5, pady=5)

    def record_mood(self, score):
        self.mood_scores.append(score)
        self.days_tracked += 1
        self.days_to_track -= 1
        self.label_days_left.config(text=f"Days left: {self.days_to_track}")

        if self.days_tracked >= 14:
            self.show_results()

    def show_results(self):
        self.frame_buttons.pack_forget()
        self.label_title.pack_forget()
        self.label_days_left.pack_forget()

        if self.mood_scores:
            average_mood_score = sum(self.mood_scores) / len(self.mood_scores)
            
            happiness_level = ""
            if average_mood_score >= 8:
                happiness_level = "Very Happy! 😊"
            elif average_mood_score >= 5:
                happiness_level = "Good! 👍"
            elif average_mood_score >= 3:
                happiness_level = "Okay. 🙂"
            else:
                happiness_level = "Needs Improvement. 😞"

            messagebox.showinfo("Happiness Meter", f"Your average mood score is: {average_mood_score:.2f}\nYour estimated happiness level is: {happiness_level}")

        self.master.destroy()

root = tk.Tk()
app = MoodTrackerApp(root)
root.mainloop()

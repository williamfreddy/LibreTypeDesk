import tkinter as tk
import random
import time

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Libre Type")

        # Dark Mode Styles
        self.root.configure(bg="#111111")

        # Navbar
        self.navbar = tk.Frame(root, bg="#111111")
        self.navbar.pack(fill="x")

        self.navbar_logo = tk.Label(self.navbar, text="Libre Type", font=("Helvetica", 20), bg="#111111", fg="#FFFFFF")
        self.navbar_logo.pack(side="left", padx=20, pady=10)

        self.navbar_buttons = tk.Frame(self.navbar, bg="#111111")
        self.navbar_buttons.pack(side="right", padx=20)

        buttons = ["Learn", "Practice", "Compete"]
        for button_text in buttons:
            button = tk.Button(self.navbar_buttons, text=button_text, font=("Helvetica", 12), bg="#FFFFFF", fg="#190617")
            button.pack(side="left", padx=10)

        # Input Text Box
        self.input_box = tk.Entry(root, bg="#111111", fg="#FFFFFF", font=("Helvetica", 14), bd=0)
        self.input_box.pack(pady=(100, 10), padx=20, fill="x")
        self.input_box.bind('<KeyRelease>', self.check_typing_speed)

        # Display WPM
        self.wpm_display = tk.Label(root, text="WPM: 0", bg="#111111", fg="#FFFFFF", font=("Consolas", 16))
        self.wpm_display.pack(pady=(0, 10))

        # Paragraph Content
        self.paragraphs = [
            "Above all, don't lie to yourself. The man who lies to himself and listens to his own lie comes to a point that he cannot distinguish the truth within him, or around him, and so loses all respect for himself and for others. And having no respect he ceases to love.",
            "Pain and suffering are always inevitable for a large intelligence and a deep heart. The really great men must, I think, have great sadness on earth.",
            "To go wrong in one's own way is better than to go right in someone else's",
            "We sometimes encounter people, even perfect strangers, who begin to interest us at first sight, somehow suddenly, all at once, before a word has been spoken.",
            "People speak sometimes about the 'bestial' cruelty of man, but that is terribly unjust and offensive to beasts, no animal could ever be so cruel as a man, so artfully, so artistically cruel."
        ]

        self.paragraph_index = random.randint(0, len(self.paragraphs) - 1)
        self.current_paragraph = self.paragraphs[self.paragraph_index]

        self.paragraph_label = tk.Label(root, text=self.current_paragraph, bg="#111111", fg="#FFFFFF", font=("Helvetica", 16), wraplength=600, justify="center")
        self.paragraph_label.pack()

        self.start_time = None
        self.words_typed = 0
        self.last_typed_word_index = -1

    def check_typing_speed(self, event):
        typed_text = self.input_box.get()
        if self.current_paragraph.startswith(typed_text):
            if not self.start_time:
                self.start_time = time.time()

            elapsed_time = time.time() - self.start_time
            words = typed_text.split()
            typed_words = len(words)
            wpm = int((typed_words / elapsed_time) * 60)
            self.wpm_display.config(text=f"WPM: {wpm}")

            if wpm < 30:
                self.wpm_display.config(fg="red")
            elif wpm < 60:
                self.wpm_display.config(fg="orange")
            else:
                self.wpm_display.config(fg="#FFFFFF")

            # Check for incorrectly typed words and highlight them
            typed_word_index = typed_text.count(' ')
            if typed_word_index > self.last_typed_word_index:
                paragraph_words = self.current_paragraph.split()
                actual_word = paragraph_words[typed_word_index]
                if typed_text.endswith(' '):
                    actual_word += ' '
                if words[-1] != actual_word:
                    paragraph_words[typed_word_index] = f'<span style="color: red;">{actual_word}</span>'
                    self.current_paragraph = ' '.join(paragraph_words)
                    self.paragraph_label.config(text=self.current_paragraph)

                self.last_typed_word_index = typed_word_index

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
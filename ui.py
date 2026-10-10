from tkinter import Tk, Button, Label
from calculation import calculate

class Ui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")
        self.window.configure(height=130, width=105, bg="cyan")

        self.num0 = Button(text="0", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=lambda: self.update_Text("0"))
        self.num0.grid(column=0, row=5, pady=5, padx=5)

        self.num1 = Button(text="1", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command= lambda: self.update_Text("1"))
        self.num1.grid(column=0, row=4, pady=5, padx=5)

        self.num2 = Button(text="2", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=lambda: self.update_Text("2"))
        self.num2.grid(column=1, row=4, pady=5, padx=5)

        self.num3 = Button(text="3", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=lambda: self.update_Text("3"))
        self.num3.grid(column=2, row=4, pady=5, padx=5)

        self.num4 = Button(text="4", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=lambda: self.update_Text("4"))
        self.num4.grid(column=0, row=3, pady=5, padx=5)

        self.num5 = Button(text="5", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=lambda: self.update_Text("5"))
        self.num5.grid(column=1, row=3, pady=5, padx=5)

        self.num6 = Button(text="6", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=lambda: self.update_Text("6"))
        self.num6.grid(column=2, row=3, pady=5, padx=5)

        self.num7 = Button(text="7", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=lambda: self.update_Text("7"))
        self.num7.grid(column=0, row=2, pady=5, padx=5)

        self.num8 = Button(text="8", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=lambda: self.update_Text("8"))
        self.num8.grid(column=1, row=2, pady=5, padx=5)

        self.num9 = Button(text="9", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=lambda: self.update_Text("9"))
        self.num9.grid(column=2, row=2, pady=5, padx=5)

        self.dot = Button(text=".", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=lambda: self.update_Text("."))
        self.dot.grid(column=1, row=5, pady=5, padx=5)

        self.delete = Button(text="<-", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=self.delete_char)
        self.delete.grid(column=2, row=5, pady=5, padx=5)

        self.equal = Button(text="=", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=self.calculate_result)
        self.equal.grid(column=3, row=5, pady=5, padx=5)

        self.add = Button(text="+", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=lambda: self.update_Text("+"))
        self.add.grid(column=3, row=4, pady=5, padx=5)

        self.subtract = Button(text="-", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=lambda: self.update_Text("-"))
        self.subtract.grid(column=3, row=3, pady=5, padx=5)

        self.multiply = Button(text="*", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=lambda: self.update_Text("*"))
        self.multiply.grid(column=3, row=2, pady=5, padx=5)

        self.divide = Button(text="/", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=lambda: self.update_Text("/"))
        self.divide.grid(column=3, row=1, pady=5, padx=5)

        self.clear = Button(text="AC", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=self.clear_text)
        self.clear.grid(column=0, row=1, pady=5, padx=5)

        self.left_brac = Button(text="(", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=lambda: self.update_Text("("))
        self.left_brac.grid(column=1, row=1, pady=5, padx=5)

        self.right_brac = Button(text=")", height=2, width=2, highlightthickness=0, borderwidth=0, border=0,
                           command=lambda: self.update_Text(")"))
        self.right_brac.grid(column=2, row=1, pady=5, padx=5)

        self.label = Label(text="", border=0, borderwidth=1, highlightthickness=0, bg="yellow", height=2, width=25,
                           fg="black", anchor="e")
        self.label.grid(column=0, row=0, columnspan=4, padx=5, pady=10)

        self.window.mainloop()

    def update_Text(self, text):
        self.label.configure(text=f"{self.label["text"]}{text}")

    def delete_char(self):
        self.label.configure(text=f"{self.label["text"][:len(self.label["text"])-1]}")

    def calculate_result(self):
        self.label.configure(text=str(calculate(self.label["text"])))

    def clear_text(self):
        self.label.configure(text="")
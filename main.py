from tkinter import Tk, Label, Entry, StringVar, IntVar, Radiobutton, Button


class TipCalculator:
    def calculate(self):
        pre_tip = float(self.meal_cost.get())
        percentage = self.tip_percent.get() / 100
        tip_amount_entry = pre_tip * percentage
        self.tip.set(tip_amount_entry)

        final_bill = pre_tip + tip_amount_entry
        self.total_cost.set(final_bill)

    def clear(self):
        self.meal_cost.set("")
        self.tip.set("")
        self.total_cost.set("")

    def __init__(self):
        window = Tk()
        window.title("Tip Calculator App")
        window.configure(background="#cdd4d3")
        window.geometry("375x250")
        window.resizable(width=False, height=False)

        # Create the variables, type of each Var.
        self.meal_cost = StringVar()
        self.tip_percent = IntVar()
        self.tip = StringVar()
        self.total_cost = StringVar()

        # Create a labels and the entries
        bill_amount = Label(window, text="Bill Amount", bg="#000000", fg="white", width=9)
        bill_amount.grid(column=1, row=0, padx=40, pady=15)
        bill_amount_entry = Entry(window, textvariable=self.meal_cost, width=14)
        bill_amount_entry.grid(column=2, row=0)

        tip_amount = Label(window, text="Tip Amount", bg="#b17e54", fg="white", width=9)
        tip_amount.grid(column=1, row=3, padx=15)
        tip_amount_entry = Entry(window, textvariable=self.tip, width=14)
        tip_amount_entry.grid(column=2, row=3)

        bill_total = Label(window, text="Bill Total", bg="#2c2c66", fg="white", width=9)
        bill_total.grid(column=1, row=5, padx=15)
        bill_total_entry = Entry(window, textvariable=self.total_cost, width=14)
        bill_total_entry.grid(column=2, row=5)

        tip_percents = Label(window, text="Tip Percentages", bg="#800080", fg="white")
        tip_percents.grid(column=0, row=0, padx=15, pady=15)

        # Create a radiobutton
        five_percent_tip = Radiobutton(window, text=" 5% ", variable=self.tip_percent, value=5)
        five_percent_tip.grid(column=0, row=1)
        ten_percent_tip = Radiobutton(window, text="10%", variable=self.tip_percent, value=10)
        ten_percent_tip.grid(column=0, row=2)
        fifteen_percent_tip = Radiobutton(window, text="15%", variable=self.tip_percent, value=15)
        fifteen_percent_tip.grid(column=0, row=3)
        twenty_percent_tip = Radiobutton(window, text="20%", variable=self.tip_percent, value=20)
        twenty_percent_tip.grid(column=0, row=4)
        twenty_five_percent_tip = Radiobutton(window, text="25%", variable=self.tip_percent, value=25)
        twenty_five_percent_tip.grid(column=0, row=5)
        thirty_percent_tip = Radiobutton(window, text="30%", variable=self.tip_percent, value=30)
        thirty_percent_tip.grid(column=0, row=6)

        # Calculate button
        calculate_btn = Button(window, text="Calculate", bg="#58554a", fg="white", width=10, command=self.calculate)
        calculate_btn.grid(column=1, row=7, padx=15)

        # Clear button
        clear_btn = Button(window, text="Clear", bg="#a52a2a", fg="white", width=10, command=self.clear)
        clear_btn.grid(column=2, row=7)

        window.mainloop()


TipCalculator()

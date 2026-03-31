import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title = ("Calculator")
        self.root.geometry("470x275")
        self.root.configure(bg="#5D5C5C")

        self.expression = ""
        self.displayVar = tk.StringVar(value="")

        self.bodyBg = "#1E1E1E"
        self.btnBg1 = "#525151"
        self.btnBg2 = "#6D6D6D"
        self.btnBg3 = "#9A9A9A"
        self.btnGreen = "#579948"
        self.displayBg = "#676767"

        self.textCol = "#FFFFFF"
        self.appFontNormal = font.Font(family="Comfortaa", size=24, weight="normal")
        self.appFontBold = font.Font(family="Comfortaa", size=24, weight="bold")

        self._creteWidgets()
        # self._creatKeybinds()

    #this function creates frames
    def _creteWidgets(self):
        #displayFrame
        displyFrame = tk.Frame(self.root, bg = self.displayBg, pady=20)
        displyFrame.pack(expand=True, fill="both")

        self.label = tk.Label(displyFrame, textvariable=self.displayVar, anchor="se", bg=self.displayBg, 
                              fg=self.textCol, font=("Comfortaa", 32), padx=20, pady=40, wraplength=300)
        self.label.pack(expand=True, fill="both", padx=15, pady=10)
        
        #topBtnFrames
        top_btns_frame = tk.Frame(self.root, bg=self.bodyBg, padx=10)
        top_btns_frame.pack(fill="x")

        tk.Button(top_btns_frame, text="Tips&Tricks", bg=self.btnGreen, fg=self.textCol, font=self.appFontNormal, borderwidth=0).pack(side="left", expand=True, fill="x", padx=5)
        tk.Button(top_btns_frame, text="Settings", bg=self.btnGreen, fg=self.textCol, font=self.appFontNormal, borderwidth=0).pack(side="left", expand=True, fill="x", padx=5)

        #mainBodyBtnFrames
        btnFrame = tk.Frame(self.root, bg=self.bodyBg, padx=10,pady=10)
        btnFrame.pack(fill="both")

        btns = [('DEL', 0, 0, self.btnBg1),('AC', 0, 1, self.btnBg1),('%', 0, 2, self.btnBg1),('Sin', 0, 3, self.btnBg1), ('Cos', 0, 4, self.btnBg1),
                ('+', 1, 0, self.btnBg2),('-', 1, 1, self.btnBg2),('x', 1, 2, self.btnBg2),('/', 1, 3, self.btnBg2), ('Tg', 1, 4, self.btnBg1),
                ('7', 2, 0, self.btnBg3),('8', 2, 1, self.btnBg3),('9', 2, 2, self.btnBg3),('x!', 2, 3, self.btnBg2), ('|x|', 2, 4, self.btnBg1),
                ('4', 3, 0, self.btnBg3),('5', 3, 1, self.btnBg3),('6', 3, 2, self.btnBg3),('√x', 3, 3, self.btnBg2), ('Shift', 3, 4, self.btnBg1),
                ('1', 4, 0, self.btnBg3),('2', 4, 1, self.btnBg3),('3', 4, 2, self.btnBg3),('xⁿ', 4, 3, self.btnBg2),
                ('+/-', 5, 0, self.btnBg3), ('0', 5, 1, self.btnBg3), (',', 5, 2, self.btnBg3)]
        #mainBodyBtn Grid initialization
        for (text, r, c, color) in btns:
                btn = tk.Button(btnFrame, text=text, bg=color, fg=self.textCol,font=self.appFontNormal, borderwidth=0, command=lambda t=text: self.on_click(t))
                btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
        
        #mainBodyBtn Enter design and initialization
        enter_top = tk.Button(btnFrame, text="", bg=self.btnGreen, fg=self.textCol,font=self.appFontNormal, borderwidth=0, highlightthickness=0,command=lambda: self.on_click("Enter"))
        enter_top.grid(row=4, column=3, columnspan=2, padx=5, pady=(5, 0), sticky="nsew")
        enter_bottom = tk.Button(btnFrame, text="Enter", bg=self.btnGreen, fg=self.textCol,font=self.appFontNormal, borderwidth=0, highlightthickness=0,command=lambda: self.on_click("Enter"))
        enter_bottom.grid(row=5, column=3, columnspan=2, padx=5, pady=(0, 5), sticky="nsew")

        for i in range(5): 
            btnFrame.columnconfigure(i, weight=1)
        for i in range(6): 
            btnFrame.rowconfigure(i, weight=1)

    #this function makes setup for keybinds
    def _setup_keybinds(self):
        for i in range(10): self.root.bind(str(i), lambda e, val=i: self.on_click(str(val)))
        self.root.bind("+", lambda e: self.on_click("+"))
        self.root.bind("-", lambda e: self.on_click("-"))
        self.root.bind("*", lambda e: self.on_click("*"))
        self.root.bind("/", lambda e: self.on_click("/"))
        self.root.bind(",", lambda e: self.on_click(","))
        self.root.bind(".", lambda e: self.on_click(","))
        self.root.bind("<Return>", lambda e: self.on_click("Enter"))
        self.root.bind("<BackSpace>", lambda e: self.on_click("DEL"))
        self.root.bind("<Escape>", lambda e: self.on_click("AC"))

    def on_click(self, char):
        if char == "AC": self.expression = ""
        else: self.expression += str(char)
        self.displayVar.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
"""
@file calc.py
@author Marek Rzeszoto (xrzeszm00)
@brief Design of the calculator
@details This is a python frontend of our calculator.
@version 0.4
@date 2026-04-03

@section LICENSE
This software is licensed under the GNU GPL v3 license.
"""

import customtkinter as ctk
import tkinter as tk
import math_lib as ml

ctk.set_appearance_mode("dark")


class Calculator:
    def __init__(self, root):
        """
        @brief Initializes the calculator application
        @details Sets dimensions, styles, frames, and widget components
        @param root The root CustomTkinter window 
        """

        # Dimensions
        self.idx = 0
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x700")
        self.root.configure(bg="#1E1E1E")

        # Default values
        self.expression = ""
        self.displayVar = tk.StringVar(value="")
        self.shiftActive = False
        self.history = []

        # Color palette
        self.bodyBg = "#1E1E1E"
        self.displayBg = "#444444"
        self.btnBg1 = "#525151"
        self.btnBg2 = "#6D6D6D"
        self.btnBg3 = "#9A9A9A"
        self.btnGreen = "#579948"
        self.hoverBtnBg1 = "#636262"
        self.hoverBtnBg2 = "#808080"
        self.hoverBtnBg3 = "#B0B0B0"
        self.hoverBtnGreen = "#6AB858"
        self.textCol = "#FFFFFF"

        # Setup pages
        self.mainFrame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.menuFrame = ctk.CTkFrame(self.root, fg_color=self.bodyBg)
        self.historyFrame = ctk.CTkFrame(self.root, fg_color=self.bodyBg)
        self.controlsFrame =ctk.CTkFrame(self.root, fg_color=self.bodyBg)
        self.tipsFrame =ctk.CTkFrame(self.root, fg_color=self.bodyBg)

        self.createCalculatorWidgets()
        self.createMenuWidgets()
        self.createControlsWidgets()
        self.createTipsWidgets()
        self.createHistoryWidgets()

        self.mainFrame.pack(expand=True, fill="both")

        self.setupKeybinds()

    def showMenu(self):
        """
        @brief Switches UI to the menu page
        """
        self.mainFrame.pack_forget()
        self.historyFrame.pack_forget()
        self.tipsFrame.pack_forget()
        self.controlsFrame.pack_forget()
        self.menuFrame.pack(expand=True, fill="both")

    def showCalculator(self):
        """ 
        @brief Switches UI to the calculator page
        """
        self.menuFrame.pack_forget()
        self.historyFrame.pack_forget()
        self.mainFrame.pack(expand=True, fill="both")

    def showControls(self):
        """
        @brief Switches UI to the controls page
        """
        self.menuFrame.pack_forget()
        self.historyFrame.pack_forget()
        self.controlsFrame.pack(expand=True, fill="both")

    def showTips(self):
        """
        @brief Switches UI to the tips&tricks page
        """
        self.menuFrame.pack_forget()
        self.historyFrame.pack_forget()
        self.tipsFrame.pack(expand=True, fill="both")

    def showQuit(self):
        """
        @brief Closes the application
        """
        self.root.destroy()

    def showHistory(self):
        """
        @brief Updates the history dispaly and switches UI to the history page
        """
        self.mainFrame.pack_forget()
        self.menuFrame.pack_forget()
        self.updateHistoryDisplay()
        self.historyFrame.pack(expand=True, fill="both")

    def createMenuWidgets(self):
        """
        @brief Creates buttons and title for the menu page.
        """
        title = ctk.CTkLabel(self.menuFrame, text="Menu",text_color=self.textCol, font=("Comfortaa", 50, "bold"))
        title.pack(pady=40)

        btnContinue = ctk.CTkButton(self.menuFrame, text="Continue", fg_color=self.btnGreen,height=50,corner_radius=25, hover_color=self.hoverBtnGreen, font=("Comfortaa", 24),command=self.showCalculator)
        btnContinue.pack(pady=10, padx=50, fill="x")

        btnControls = ctk.CTkButton(self.menuFrame, text="Controls", fg_color="transparent",border_width=2, border_color=self.btnGreen, height=50,corner_radius=25, hover_color=self.btnGreen, font=("Comfortaa", 24),command=self.showControls)
        btnControls.pack(pady=10, padx=50, fill="x")

        btnTips = ctk.CTkButton(self.menuFrame, text="Tips&Tricks", fg_color="transparent",border_width=2, border_color=self.btnGreen, height=50,corner_radius=25, hover_color=self.btnGreen, font=("Comfortaa", 24),command=self.showTips)
        btnTips.pack(pady=10, padx=50, fill="x")

        btnQuit = ctk.CTkButton(self.menuFrame, text="Quit", fg_color="transparent", border_width=2, border_color=self.btnGreen,height=50,corner_radius=25,  hover_color=self.btnGreen,font=("Comfortaa", 24),command=self.showQuit)
        btnQuit.pack(pady=10, padx=50, fill="x")

    def createControlsWidgets(self):
        """
        @brief Shows the controls page with legend of keybinds
        @bug Auto gestures scroll
        """
        title = ctk.CTkLabel(self.controlsFrame, text="Controls", font=("Comfortaa", 50, "bold"), text_color=self.textCol)
        title.pack(pady=40)
    
        self.controlsScrollContainer = ctk.CTkScrollableFrame(self.controlsFrame, fg_color=self.bodyBg, label_text="")
        self.controlsScrollContainer.pack(expand=True, fill="both", padx=20, pady=10)
        self.controlsScrollContainer.bind("<Down>", lambda e: self.controlsScrollContainer._parent_canvas.yview_scroll(-1, "units"))
        self.controlsScrollContainer.bind("<Up>", lambda e: self.controlsScrollContainer._parent_canvas.yview_scroll(1, "units"))
        self.controlsScrollContainer.bind("<MouseWheel>", lambda e: self.controlsScrollContainer._parent_canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

        controlsData = [
            ("Ac", "Clear all", "ESC"),
            ("Del", "Delete last", "Backspace"),
            ("Shift", "Secondary functions", "Shift"),
            ("=", "Calculate", "Enter"),
            ("%", "Modulo", "M"),
            ("Sin", "Sine", "S"),
            ("Cos", "Cosine", "C"),
            ("Tg", "Tangent", "T"),
            ("Asin", "Arc sine", "Shift + S"),
            ("Acos", "Arc cosine", "Shift + C"),
            ("Atg", "Arc tangent", "Shift + T"),
            ("+", "Addition", "+"),
            ("-", "Subtraction", "-"),
            ("x", "Multiplication", "*"),
            ("/", "Division", "/"),
            ("x!", "Factorial", "!"),
            ("xⁿ", "Power of n", "W"),
            ("√x", "Square root", "Q"),
            ("π", "Constant Pi", "P"),
            (",", "Decimal point", "."),
            ("+/-", "Negative/Positive", ";")
        ]
        for btnText, keybind, descText in controlsData:
            row = ctk.CTkFrame(self.controlsScrollContainer, fg_color="transparent")
            row.pack(fill="x", pady=5)

            item = ctk.CTkButton(row, text=btnText, width=70, height=40, corner_radius=15,fg_color=self.btnGreen, text_color=self.textCol,font=("Comfortaa", 16, "bold"))
            item.pack(side="left")

            item = ctk.CTkLabel(row, text=descText, text_color=self.textCol,font=("Comfortaa", 16))
            item.pack(side="left", padx=15)

            keybind = ctk.CTkLabel(row, text=keybind,  text_color=self.btnGreen,font=("Comfortaa", 16))
            keybind.pack(side="right", padx=10)

        btnBack = ctk.CTkButton(self.controlsFrame, text="Back", fg_color="transparent",border_width=2,border_color=self.btnGreen,height=50,corner_radius=25, hover_color=self.hoverBtnGreen, font=("Comfortaa", 24),command=self.showMenu)
        btnBack.pack(pady=30, padx=50, fill="x")

    def createTipsWidgets(self):
        """
        @brief Shows the tips&tricks page with some guides
        @bug Auto gestures scroll
        """
        title = ctk.CTkLabel(self.tipsFrame, text="Tips&Tricks", font=("Comfortaa", 50, "bold"))
        title.pack(pady=40)
        
        self.tipsScrollContainer = ctk.CTkScrollableFrame(self.tipsFrame, fg_color=self.bodyBg, label_text="")
        self.tipsScrollContainer.pack(expand=True, fill="both", padx=20, pady=10)
        self.tipsScrollContainer.bind("<Down>", lambda e: self.tipsScrollContainer._parent_canvas.yview_scroll(-1, "units"))
        self.tipsScrollContainer.bind("<Up>", lambda e: self.tipsScrollContainer._parent_canvas.yview_scroll(1, "units"))
        self.tipsScrollContainer.bind("<MouseWheel>", lambda e: self.tipsScrollContainer._parent_canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        
        tips = [
            ("💡 Shifting", "Hold SHIFT to access inverse functions like Asin, Acos, or Atg. The button labels will update automatically."),
            ("💡 Unary Ops", "Trigonometry and negation (+/-) are instant. Just enter a number and press the function key for an immediate result."),
            ("💡 Binary Ops", "For basic math (+, -, x, /) or powers (xⁿ), enter the full expression and press the ENTER/EQUAL button."),
            ("💡 Shortcuts", "Use your keyboard for speed! 'S' for Sin, 'Q' for Square Root, or 'W' for Powers. ESC clears everything.")
        ]
        for tipTitle, tipText in tips:
            card = ctk.CTkFrame(self.tipsScrollContainer, fg_color=self.btnGreen, corner_radius=15)
            card.pack(fill="x", pady=10, padx=5)
            
            ctk.CTkLabel(card, text=tipTitle, font=("Comfortaa", 18, "bold"),  text_color="white", anchor="w").pack(fill="x", padx=15, pady=(10, 0))
            ctk.CTkLabel(card, text=tipText, font=("Comfortaa", 13),text_color="white", wraplength=300, justify="left").pack(fill="x", padx=15, pady=(5, 10))

        btnBack = ctk.CTkButton(self.tipsFrame, text="Back", fg_color="transparent",border_width=2,border_color=self.btnGreen,height=50,corner_radius=25, hover_color=self.hoverBtnGreen, font=("Comfortaa", 24),command=self.showMenu)
        btnBack.pack(pady=30, padx=50, fill="x")

    def updateHistoryDisplay(self):
        """
        @brief Clears and reloads history records into the UI historyScrollContainer
        """
        for widget in self.historyScrollContainer.winfo_children():
            widget.destroy()

        self.loadHistoryFromFile()

        if not self.history:
            ctk.CTkLabel(self.historyScrollContainer, text="No history yet...", font=("Comfortaa", 14), text_color=self.btnBg3).pack(pady=20)
        
        for item in reversed(self.history):
            card = ctk.CTkFrame(self.historyScrollContainer, fg_color=self.displayBg, corner_radius=10)
            card.pack(fill="x", pady=5, padx=5)
            
            ctk.CTkLabel(card, text=item, font=("Comfortaa", 16), text_color=self.textCol, padx=10, pady=10).pack(side="left")

    def createHistoryWidgets(self):
        """
        @brief Creates the history page
        @bug Auto gestures scroll
        """
        title = ctk.CTkLabel(self.historyFrame, text="History", font=("Comfortaa", 50, "bold"))
        title.pack(pady=40)
        
        self.historyScrollContainer = ctk.CTkScrollableFrame(self.historyFrame, fg_color=self.bodyBg, label_text="")
        self.historyScrollContainer.pack(expand=True, fill="both", padx=20, pady=10)
        self.historyScrollContainer.bind("<MouseWheel>", lambda e: self.historyScrollContainer._parent_canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        self.historyScrollContainer.bind("<Down>", lambda e: self.historyScrollContainer._parent_canvas.yview_scroll(-1, "units"))
        self.historyScrollContainer.bind("<Up>", lambda e: self.historyScrollContainer._parent_canvas.yview_scroll(1, "units"))
        
        btnBack = ctk.CTkButton(self.historyFrame, text="Back", fg_color="transparent",border_width=2,border_color=self.btnGreen,height=50,corner_radius=25, hover_color=self.hoverBtnGreen, font=("Comfortaa", 24),command=self.showCalculator)
        btnBack.pack(pady=30, padx=50, fill="x")

    def saveToHistoryFile(self, entry):
        """
        @brief Appends a calculation record to the history.txt file
        @param entry String with the expression and result
        """
        try:
            with open("history.txt", "a", encoding="utf-8") as f:
                f.write(f"{entry}\n")
        except Exception as e:
            print(f"Error saving history: {e}")

    def loadHistoryFromFile(self):
        """
        @brief Reads all records from history.txt into the local history list
        """
        try:
            with open("history.txt", "r", encoding="utf-8") as f:
                self.history = [line.strip() for line in f.readlines() if line.strip()]
        except FileNotFoundError:
            self.history = [] 

    def createCalculatorWidgets(self):
        """
        @brief Creates all UI widgets of calculator
        @details Defines the display, top buttons, and the main calculator buttons
        """
        # Display
        self.label = ctk.CTkLabel(self.mainFrame, textvariable=self.displayVar, fg_color=self.displayBg, text_color=self.textCol, corner_radius=20, font=("Comfortaa", 40),anchor="se", padx=20, pady=20, height=180)        
        self.label.pack(expand=True, fill="both", padx=15, pady=15)

        # Helper btns
        topFrame = ctk.CTkFrame(self.mainFrame, fg_color="transparent")
        topFrame.pack(fill="x", padx=10, pady=5)

        ctk.CTkButton(topFrame, text="History", command=self.showHistory,fg_color=self.btnGreen, text_color=self.textCol, hover_color=self.hoverBtnGreen, corner_radius=10, font=("Comfortaa", 16)).pack(side="left", expand=True, fill="x", padx=5)
        ctk.CTkButton(topFrame, text="Menu", command=self.showMenu, fg_color=self.btnGreen, text_color=self.textCol, hover_color=self.hoverBtnGreen, corner_radius=10, font=("Comfortaa", 16)).pack(side="left", expand=True, fill="x", padx=5)

        # Main btns grid definition
        btnFrame = ctk.CTkFrame(self.mainFrame, fg_color="transparent")
        btnFrame.pack(fill="both", expand=True, padx=10, pady=5)
        btns = [
            ('Del', 0, 0, self.btnBg1,self.hoverBtnBg1, 'Del'), ('Ac', 0, 1, self.btnBg1,self.hoverBtnBg1,'Ac'), ('%', 0, 2, self.btnBg1,self.hoverBtnBg1,'%'), ('Sin', 0, 3, self.btnBg1,self.hoverBtnBg1,'Sin'), ('Cos', 0, 4, self.btnBg1,self.hoverBtnBg1,'Cos'),
            ('+', 1, 0, self.btnBg2,self.hoverBtnBg2, '+'), ('-', 1, 1, self.btnBg2,self.hoverBtnBg2,'-'), ('x', 1, 2, self.btnBg2,self.hoverBtnBg2,'x'), ('/', 1, 3, self.btnBg2,self.hoverBtnBg2,'/'), ('Tg', 1, 4, self.btnBg1,self.hoverBtnBg1,'Tg'),
            ('7', 2, 0, self.btnBg3,self.hoverBtnBg3,'7'), ('8', 2, 1, self.btnBg3,self.hoverBtnBg3,'8'), ('9', 2, 2, self.btnBg3,self.hoverBtnBg3,'9'), ('x!', 2, 3, self.btnBg2,self.hoverBtnBg2,'!'), ('|x|', 2, 4, self.btnBg1,self.hoverBtnBg1,'Abs('),
            ('4', 3, 0, self.btnBg3,self.hoverBtnBg3,'4'), ('5', 3, 1, self.btnBg3,self.hoverBtnBg3,'5'), ('6', 3, 2, self.btnBg3,self.hoverBtnBg3,'6'), ('√x', 3, 3, self.btnBg2,self.hoverBtnBg2,'√'), ('π', 3, 4, self.btnBg1,self.hoverBtnBg1, 'π'),
            ('1', 4, 0, self.btnBg3,self.hoverBtnBg3,'1'), ('2', 4, 1, self.btnBg3,self.hoverBtnBg3,'2'), ('3', 4, 2, self.btnBg3,self.hoverBtnBg3,'3'), ('xⁿ', 4, 3, self.btnBg2,self.hoverBtnBg2, 'ⁿ'),
            ('+/-', 5, 0, self.btnBg3,self.hoverBtnBg3,'+/-'), ('0', 5, 1, self.btnBg3,self.hoverBtnBg3,'0'), (',', 5, 2, self.btnBg3,self.hoverBtnBg3,','), ('Shift', 5, 3, self.btnBg2,self.hoverBtnBg2,'Shift'),
        ]

        # Button dimensions
        btnWidth, btnHight = 60, 60

        # Shifted buttons
        self.shiftedBtns = {}

        # Basic buttons layout 
        for (text, r, c, color, hover, value) in btns:
            btn = ctk.CTkButton(btnFrame, text=text, fg_color=color, text_color=self.textCol,font=("Comfortaa", 18), corner_radius=12, width=btnWidth, height=btnHight,hover_color=hover, command=lambda t=value: self.onClick(t))
            btn.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

            if text in ("Sin", "Cos", "Tg", "Shift"):
                self.shiftedBtns[text] = btn

        # Equal button spans two rows
        enterBtn = ctk.CTkButton(btnFrame, text="=", fg_color=self.btnGreen, text_color=self.textCol, font=("Comfortaa", 20, "bold"), corner_radius=12, width=btnWidth, hover_color=self.hoverBtnGreen, command=lambda: self.onClick("Enter"))
        enterBtn.grid(row=4, column=4, rowspan=2, padx=4, pady=4, sticky="nsew")

        for i in range(5): 
            btnFrame.columnconfigure(i, weight=1, uniform="col")
        for i in range(6): 
            btnFrame.rowconfigure(i, weight=1, uniform="row")

    def setupKeybinds(self):
        """
        @brief Binds keyboard keys to calculator functions
        @details Maps keystrokes, numpad keys, and other operators to the onClick method
        """
        # Nums
        for i in range(10): 
            self.root.bind(str(i), lambda e, val=i: self.onClick(str(val)))
            self.root.bind(f"<KP_{i}>", lambda e, val=i: self.onClick(str(val)))

        # Basic Operations
        self.root.bind("+", lambda e: self.onClick("+"))
        self.root.bind("<KP_Add>", lambda e: self.onClick("+"))
        self.root.bind("-", lambda e: self.onClick("-"))
        self.root.bind("<KP_Subtract>", lambda e: self.onClick("-"))
        self.root.bind("*", lambda e: self.onClick("x"))
        self.root.bind("<KP_Multiply>", lambda e: self.onClick("x"))
        self.root.bind("/", lambda e: self.onClick("/"))
        self.root.bind("<KP_Divide>", lambda e: self.onClick("/"))

        # Other operations
        self.root.bind(";", lambda e: self.onClick("+/-"))
        self.root.bind("!", lambda e: self.onClick("!"))
        # Lower case
        self.root.bind("w", lambda e: self.onClick("ⁿ"))
        self.root.bind("q", lambda e: self.onClick("√"))
        self.root.bind("a", lambda e: self.onClick("Abs("))
        self.root.bind("m", lambda e: self.onClick("%"))
        self.root.bind("s", lambda e: self.onClick("Sin"))
        self.root.bind("c", lambda e: self.onClick("Cos"))
        self.root.bind("t", lambda e: self.onClick("Tg"))
        self.root.bind("p", lambda e: self.onClick("π"))
        # Upper case
        self.root.bind("W", lambda e: self.onClick("ⁿ"))
        self.root.bind("Q", lambda e: self.onClick("√"))
        self.root.bind("A", lambda e: self.onClick("Abs("))
        self.root.bind("M", lambda e: self.onClick("%"))
        self.root.bind("S", lambda e: self.onClick("Sin"))
        self.root.bind("C", lambda e: self.onClick("Cos"))
        self.root.bind("T", lambda e: self.onClick("Tg"))
        self.root.bind("P", lambda e: self.onClick("π"))

        # Delimiters, Delete and Result
        self.root.bind(".", lambda e: self.onClick(","))
        self.root.bind(",", lambda e: self.onClick(","))
        self.root.bind("<Return>", lambda e: self.onClick("Enter"))
        self.root.bind("<KP_Enter>", lambda e: self.onClick("Enter"))
        self.root.bind("<BackSpace>", lambda e: self.onClick("Del"))
        self.root.bind("<Escape>", lambda e: self.onClick("Ac"))

        # Shift handling
        self.root.bind("<KeyPress-Shift_L>", self.shiftOn)
        self.root.bind("<KeyRelease-Shift_L>", self.shiftOff)
        self.root.bind("<KeyPress-Shift_R>", self.shiftOn)
        self.root.bind("<KeyRelease-Shift_R>", self.shiftOff)

    def shiftOn(self, event=None):
        """
        @brief Activates Shift mode and updates sin,cos,tg button labels to asin,acos,atg
        """
        self.shiftActive = True
        if "Shift" in self.shiftedBtns:
            self.shiftedBtns["Shift"].configure(fg_color=self.hoverBtnBg2)
        self.shiftedBtns["Sin"].configure(text="Asin")
        self.shiftedBtns["Cos"].configure(text="Acos")
        self.shiftedBtns["Tg"].configure(text="Atg")

    def shiftOff(self, event=None):
        """
        @brief Deactivates Shift mode and restores labels from asin,acos,atg button back to sin,cos,tg
        """
        self.shiftActive = False
        if "Shift" in self.shiftedBtns:
            self.shiftedBtns["Shift"].configure(fg_color=self.btnBg2)
        self.shiftedBtns["Sin"].configure(text="Sin")
        self.shiftedBtns["Cos"].configure(text="Cos")
        self.shiftedBtns["Tg"].configure(text="Tg")


    def onClick(self, char):
        """
        @brief Handles button click and keypress events
        @details Manages the expression string, performs calculations using math_lib (ml), and updates the display
        @param char The character or command string from the pressed button or key
        """
        if char == "Ac": 
            self.expression = ""
        elif char == "Del": 
            self.expression = self.expression[:-1]
        elif char == "Shift":
            if self.shiftActive:
                self.shiftOff()
            else:
                self.shiftOn()
            return
        elif char == "Enter":
            try:
                # comma replacing
                exprHistory = self.expression
                expr = self.expression.replace(',', '.')
                
                # Binary operations - lazy
                result = None
                if "+" in expr:
                    a, b = expr.split("+")
                    result = ml.add(float(a),float(b))
                elif "-" in expr:
                    parts = expr.split("-")
                    if len(parts) == 2:
                        result = ml.sub(float(parts[0]), float(parts[1]))
                elif "x" in expr:
                    a, b = expr.split("x")
                    result = ml.mul(float(a), float(b))
                elif "/" in expr:
                    a, b = expr.split("/")
                    result = ml.div(float(a), float(b))
                elif "ⁿ" in expr: 
                    a, b = expr.split("ⁿ")
                    result = ml.pow(float(a), int(b))
                elif "%" in expr:
                    a, b = expr.split("%")
                    result = ml.percent(float(a), float(b))
                
                # Unar operations - lazy
                elif "√" in expr:
                    a = float(expr[1:].strip())
                    result = ml.sqrt(a)
                elif "!" in expr:
                    a = float(expr[:1].strip())
                    result = ml.factorial(int(a))
                elif "Abs(" in expr:
                    a = float(expr[4:].strip())
                    result = ml.abs(a)


                if result is not None:
                    if isinstance(result, float):
                        result = round(result, 5)

                    self.expression = str(result).replace('.', ',')
                    # Saving to history.txt
                    history_entry = f"{exprHistory} = {self.expression}"
                    self.saveToHistoryFile(history_entry)

            except Exception as e:
                print(f"Error: {e}") 
                self.expression = (f"Error: {e}")


        # Other operations - instant
        elif char in ("Sin", "Cos", "Tg", "+/-"):
            try:
                if not self.expression:
                    return
                
                val = float(self.expression.replace(',', '.'))
                instantResult = None

                if char == "Sin":
                    if self.shiftActive:
                        instantResult = ml.arcsin(val)  
                    else:
                        instantResult = ml.sin(val)
                
                elif char == "Cos":
                    if self.shiftActive:
                        instantResult = ml.arccos(val) 
                    else:
                        instantResult = ml.cos(val)
                
                elif char == "Tg":
                    if self.shiftActive:
                        instantResult = ml.arctg(val)
                    else:
                        instantResult = ml.tg(val)
                
                elif char == "+/-":
                    instantResult = ml.negate(val)

                elif char == "Shift":
                    if self.shiftActive:
                        self.shiftOff()
                    else:
                        self.shiftOn() 
                    return  
                
                if instantResult is not None:
                    self.expression = str(round(instantResult, 2)).replace('.', ',')
            except Exception as e:
                print(f"Error: {e}")
                self.expression = "Error"
        
        elif char == "π":
            self.expression += str(round(ml.pi, 2)).replace('.', ',')
            
        elif char == "xⁿ":
            self.expression += "ⁿ"
            
        else:
            self.expression += str(char)
        
        self.displayVar.set(self.expression)

if __name__ == "__main__":
    root = ctk.CTk()
    app = Calculator(root)
    root.mainloop()
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
import os

# Disply limitaition
DISPLAY_MAX_CHARS = 18
# Display adaptive font
DISPLAY_FONT_LARGE = 40
DISPLAY_FONT_SMALL = 20
#Heading and texts
HEADINGS = 50
BIGGER_TEXT = 18
SMALLER_TEXT = 14
#Buttons
CALC_BTNS = 16
UI_BTNS = 24

# Theme set
ctk.set_appearance_mode("dark")

def checkIntOrFloat(value: float):
    """
    @brief Checks whether a float should be shown as int
    @details If the float has no .00 decimal part, it gets converted to int so the display doesn't show useless zeros
    @param value The number to check
    @return int if value is a whole number, otherwise the original float
    """
    if isinstance(value, float) and value.is_integer():
        #type conversion from float with *.00 ending to int 
        return int(value)
    return value

def parse(string: str):
    """
    @brief Turns a display string into a number
    @details Swaps comma for dot then tries to return an int when possible, float otherwise
    @param string The string to parse
    @return int or float depending on the value
    """
    stringDot = string.replace(',', '.')
    try:
        floatNum = float(stringDot)
        if floatNum.is_integer():
            return int(floatNum)
        else:
            return floatNum
    except ValueError:
        raise ValueError(f"Invalid number: {string!r}")

class Calculator:
    def __init__(self, root):
        """
        @brief Initializes the calculator application
        @details Sets dimensions, styles, frames, and widget components
        @param root The root CustomTkinter window 
        """
        # Dimensions
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x700")
        self.root.configure(bg="#1E1E1E")

        # Default values
        self.expression = ""
        self.displayVariable = tk.StringVar(value="")
        self.shiftActive = False
        self.history = []

        # Single expression showing variables
        self.waitingVariable = tk.StringVar(value="")
        self.waitingOpereation = None
        self.waitingValue = None

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

        #history reset per session
        self.resetHistoryFile()
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
        title = ctk.CTkLabel(self.menuFrame, text="Menu",text_color=self.textCol, font=("Comfortaa", HEADINGS, "bold"))
        title.pack(pady=40)

        btnContinue = ctk.CTkButton(self.menuFrame, text="Continue", fg_color=self.btnGreen,height=50,corner_radius=25, hover_color=self.hoverBtnGreen, font=("Comfortaa", UI_BTNS),command=self.showCalculator)
        btnContinue.pack(pady=10, padx=50, fill="x")

        btnControls = ctk.CTkButton(self.menuFrame, text="Controls", fg_color="transparent",border_width=2, border_color=self.btnGreen, height=50,corner_radius=25, hover_color=self.btnGreen, font=("Comfortaa", UI_BTNS),command=self.showControls)
        btnControls.pack(pady=10, padx=50, fill="x")

        btnTips = ctk.CTkButton(self.menuFrame, text="Tips&Tricks", fg_color="transparent",border_width=2, border_color=self.btnGreen, height=50,corner_radius=25, hover_color=self.btnGreen, font=("Comfortaa", UI_BTNS),command=self.showTips)
        btnTips.pack(pady=10, padx=50, fill="x")

        btnQuit = ctk.CTkButton(self.menuFrame, text="Quit", fg_color="transparent", border_width=2, border_color=self.btnGreen,height=50,corner_radius=25,  hover_color=self.btnGreen,font=("Comfortaa", UI_BTNS),command=self.showQuit)
        btnQuit.pack(pady=10, padx=50, fill="x")

    def createControlsWidgets(self):
        """
        @brief Shows the controls page with legend of keybinds
        @bug Auto gestures scroll
        """
        title = ctk.CTkLabel(self.controlsFrame, text="Controls", font=("Comfortaa", HEADINGS, "bold"), text_color=self.textCol)
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
            ("%", "Percentile", "M"),
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

            item = ctk.CTkButton(row, text=btnText, width=70, height=40, corner_radius=15,fg_color=self.btnGreen, text_color=self.textCol,font=("Comfortaa", CALC_BTNS, "bold"))
            item.pack(side="left")

            item = ctk.CTkLabel(row, text=descText, text_color=self.textCol,font=("Comfortaa", CALC_BTNS))
            item.pack(side="left", padx=15)

            keybind = ctk.CTkLabel(row, text=keybind,  text_color=self.btnGreen,font=("Comfortaa", CALC_BTNS))
            keybind.pack(side="right", padx=10)

        btnBack = ctk.CTkButton(self.controlsFrame, text="Back", fg_color="transparent",border_width=2,border_color=self.btnGreen,height=50,corner_radius=25, hover_color=self.hoverBtnGreen, font=("Comfortaa", UI_BTNS),command=self.showMenu)
        btnBack.pack(pady=30, padx=50, fill="x")

    def createTipsWidgets(self):
        """
        @brief Shows the tips&tricks page with some guides
        @bug Auto gestures scroll
        """
        title = ctk.CTkLabel(self.tipsFrame, text="Tips&Tricks", font=("Comfortaa", HEADINGS, "bold"))
        title.pack(pady=40)
        
        self.tipsContainer = ctk.CTkFrame(self.tipsFrame, fg_color=self.bodyBg)
        self.tipsContainer.pack(expand=True, fill="both", padx=20, pady=10)

        tips = [
            ("💡 Shifting", "Hold SHIFT to access inverse functions like Asin, Acos, or Atg. The button labels will update automatically."),
            ("💡 Unary Ops", "Trigonometry and negation (+/-) are instant. Just enter a number and press the function key for an immediate result."),
            ("💡 Binary Ops", "For basic math (+, -, x, /) or powers (xⁿ), enter the full expression and press the ENTER/EQUAL button."),
        ]
        for tipTitle, tipText in tips:
            card = ctk.CTkFrame(self.tipsContainer, fg_color=self.btnGreen, corner_radius=15)
            card.pack(fill="x", pady=10, padx=5)
            
            ctk.CTkLabel(card, text=tipTitle, font=("Comfortaa", BIGGER_TEXT, "bold"),  text_color="white", anchor="w").pack(fill="x", padx=15, pady=(10, 0))
            ctk.CTkLabel(card, text=tipText, font=("Comfortaa", SMALLER_TEXT),text_color="white", wraplength=300, justify="left").pack(fill="x", padx=15, pady=(5, 10))

        btnBack = ctk.CTkButton(self.tipsFrame, text="Back", fg_color="transparent",border_width=2,border_color=self.btnGreen,height=50,corner_radius=25, hover_color=self.hoverBtnGreen, font=("Comfortaa", UI_BTNS),command=self.showMenu)
        btnBack.pack(pady=30, padx=50, fill="x")

    def resetHistoryFile(self):
        """
        @brief Overwrits the history file per session
        """
        home = os.path.expanduser("~")
        self.historyPath = os.path.join(home, "calc_history.txt")
        try:
            open(self.historyPath, "w", encoding="utf-8").close()
        except Exception as e:
            print(f"Error: unable to reset the history file: {e}")
            self.historyPath = None

    def loadHistoryFromFile(self):
        """
        @brief Reads history entries from file into self.history
        @details Skips blank lines, strips whitespace from each entry
        """
        if not self.historyPath:
            self.history = []
            return

        try:
            with open(self.historyPath, "r", encoding="utf-8") as historyFile:
                new_history = []

                for line in historyFile:
                    cleaned_line = line.strip()
                    
                    if cleaned_line:
                        new_history.append(cleaned_line)
                
                self.history = new_history

        except FileNotFoundError:
            self.history = []

    def updateHistoryDisplay(self):
        """
        @brief Clears and reloads history records into the UI historyScrollContainer
        """
        for widget in self.historyScrollContainer.winfo_children():
            widget.destroy()

        self.loadHistoryFromFile()

        if not self.history:
            ctk.CTkLabel(self.historyScrollContainer, text="No history yet...", font=("Comfortaa", SMALLER_TEXT), text_color=self.btnBg3).pack(pady=20)
        
        # Most recent shown first
        for item in reversed(self.history):
            card = ctk.CTkFrame(self.historyScrollContainer, fg_color=self.displayBg, corner_radius=10)
            card.pack(fill="x", pady=5, padx=5)
            
            ctk.CTkLabel(card, text=item, font=("Comfortaa", BIGGER_TEXT), text_color=self.textCol, padx=10, pady=10).pack(side="left")

    def createHistoryWidgets(self):
        """
        @brief Creates the history page
        @bug Auto gestures scroll
        """
        title = ctk.CTkLabel(self.historyFrame, text="History", font=("Comfortaa", HEADINGS, "bold"))
        title.pack(pady=40)
        
        self.historyScrollContainer = ctk.CTkScrollableFrame(self.historyFrame, fg_color=self.bodyBg, label_text="")
        self.historyScrollContainer.pack(expand=True, fill="both", padx=20, pady=10)
        self.historyScrollContainer.bind("<MouseWheel>", lambda e: self.historyScrollContainer._parent_canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        self.historyScrollContainer.bind("<Down>", lambda e: self.historyScrollContainer._parent_canvas.yview_scroll(-1, "units"))
        self.historyScrollContainer.bind("<Up>", lambda e: self.historyScrollContainer._parent_canvas.yview_scroll(1, "units"))
        
        btnBack = ctk.CTkButton(self.historyFrame, text="Back", fg_color="transparent",border_width=2,border_color=self.btnGreen,height=50,corner_radius=25, hover_color=self.hoverBtnGreen, font=("Comfortaa", UI_BTNS),command=self.showCalculator)
        btnBack.pack(pady=30, padx=50, fill="x")

    def saveToHistoryFile(self, entry):
        """
        @brief Appends a calculation record to the history.txt file
        @param entry Formatted string like "3 + 5 = 8"
        """
        if not self.historyPath:
            return
        try:
            with open(self.historyPath, "a", encoding="utf-8") as historyFile:
                historyFile.write(f"{entry}\n")
        except Exception as e:
            print(f"Error: unable to save history: {e}")

    def createCalculatorWidgets(self):
        """
        @brief Creates all UI widgets of calculator
        @details Defines the display, top buttons, and the main calculator buttons
        """
        #komentare
        self.waitingLabel = ctk.CTkLabel(self.mainFrame, textvariable=self.waitingVariable,fg_color="transparent", text_color=self.btnBg3,font=("Comfortaa", CALC_BTNS), anchor="se", padx=20, height=24)
        self.waitingLabel.pack(fill="x", padx=15, pady=(15, 0))

        self.mainDisplayLabel = ctk.CTkLabel(self.mainFrame, textvariable=self.displayVariable,fg_color=self.displayBg, text_color=self.textCol,corner_radius=20, font=("Comfortaa", DISPLAY_FONT_LARGE),anchor="se", padx=20, pady=20, height=156,wraplength=320)
        self.mainDisplayLabel.pack(expand=True, fill="both", padx=10, pady=(5, 15))

        # Helper btns
        topFrame = ctk.CTkFrame(self.mainFrame, fg_color="transparent")
        topFrame.pack(fill="x", padx=10, pady=5)

        ctk.CTkButton(topFrame, text="History", command=self.showHistory,fg_color=self.btnGreen, text_color=self.textCol, hover_color=self.hoverBtnGreen, corner_radius=10, font=("Comfortaa", CALC_BTNS)).pack(side="left", expand=True, fill="x", padx=5)
        ctk.CTkButton(topFrame, text="Menu", command=self.showMenu, fg_color=self.btnGreen, text_color=self.textCol, hover_color=self.hoverBtnGreen, corner_radius=10, font=("Comfortaa", CALC_BTNS)).pack(side="left", expand=True, fill="x", padx=5)

        # Main btns grid definition
        btnFrame = ctk.CTkFrame(self.mainFrame, fg_color="transparent")
        btnFrame.pack(fill="both", expand=True, padx=10, pady=5)
        btns = [
            #first row 
            ('Del', 0, 0, self.btnBg1,self.hoverBtnBg1, 'Del'),
            ('Ac', 0, 1, self.btnBg1,self.hoverBtnBg1,'Ac'), 
            ('%', 0, 2, self.btnBg1,self.hoverBtnBg1,'%'), 
            ('Sin', 0, 3, self.btnBg1,self.hoverBtnBg1,'Sin'), 
            ('Cos', 0, 4, self.btnBg1,self.hoverBtnBg1,'Cos'),

            #second row
            ('+', 1, 0, self.btnBg2,self.hoverBtnBg2, '+'), 
            ('-', 1, 1, self.btnBg2,self.hoverBtnBg2,'-'), 
            ('x', 1, 2, self.btnBg2,self.hoverBtnBg2,'x'), 
            ('/', 1, 3, self.btnBg2,self.hoverBtnBg2,'/'), 
            ('Tg', 1, 4, self.btnBg1,self.hoverBtnBg1,'Tg'),

            #third row
            ('7', 2, 0, self.btnBg3,self.hoverBtnBg3,'7'), 
            ('8', 2, 1, self.btnBg3,self.hoverBtnBg3,'8'), 
            ('9', 2, 2, self.btnBg3,self.hoverBtnBg3,'9'), 
            ('x!', 2, 3, self.btnBg2,self.hoverBtnBg2,'!'), 
            ('|x|', 2, 4, self.btnBg1,self.hoverBtnBg1,'Abs('),

            #fourth row
            ('4', 3, 0, self.btnBg3,self.hoverBtnBg3,'4'), 
            ('5', 3, 1, self.btnBg3,self.hoverBtnBg3,'5'), 
            ('6', 3, 2, self.btnBg3,self.hoverBtnBg3,'6'), 
            ('√x', 3, 3, self.btnBg2,self.hoverBtnBg2,'√'), 
            ('π', 3, 4, self.btnBg1,self.hoverBtnBg1, 'π'),

            #fifth row
            ('1', 4, 0, self.btnBg3,self.hoverBtnBg3,'1'), 
            ('2', 4, 1, self.btnBg3,self.hoverBtnBg3,'2'), 
            ('3', 4, 2, self.btnBg3,self.hoverBtnBg3,'3'), 
            ('xⁿ', 4, 3, self.btnBg2,self.hoverBtnBg2, 'ⁿ'),

            #sixth row
            ('+/-', 5, 0, self.btnBg3,self.hoverBtnBg3,'+/-'), 
            ('0', 5, 1, self.btnBg3,self.hoverBtnBg3,'0'), 
            (',', 5, 2, self.btnBg3,self.hoverBtnBg3,','), 
            ('Shift', 5, 3, self.btnBg2,self.hoverBtnBg2,'Shift'),
        ]

        # Button dimensions
        btnWidth = 60
        btnHeight = 60

        # Shifted buttons
        self.shiftedBtns = {}

        # Basic buttons layout 
        for (text, r, c, color, hover, value) in btns:
            btn = ctk.CTkButton(btnFrame, text=text, fg_color=color, text_color=self.textCol,font=("Comfortaa", BIGGER_TEXT), corner_radius=12, width=btnWidth, height=btnHeight,hover_color=hover, command=lambda t=value: self.onClick(t))
            btn.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

            if text in ("Sin", "Cos", "Tg", "Shift"):
                self.shiftedBtns[text] = btn

        # Equal button spans two rows
        enterBtn = ctk.CTkButton(btnFrame, text="=", fg_color=self.btnGreen, text_color=self.textCol, font=("Comfortaa", BIGGER_TEXT, "bold"), corner_radius=12, width=btnWidth, hover_color=self.hoverBtnGreen, command=lambda: self.onClick("Enter"))
        enterBtn.grid(row=4, column=4, rowspan=2, padx=4, pady=4, sticky="nsew")

        for i in range(5): 
            btnFrame.columnconfigure(i, weight=1, uniform="col")
        for i in range(6): 
            btnFrame.rowconfigure(i, weight=1, uniform="row")

    def updateDisplay(self, text: str):
        """
        @brief Pushes text to the display and shrinks the font if needed
        @details Errors always use the small font; long numbers also switch to small
        @param text The string to show on the display
        """
        if text.startswith("Error:"):
            # Already formatted short error
            self.mainDisplayLabel.configure(font=("Comfortaa", DISPLAY_FONT_SMALL))
        elif len(text) > DISPLAY_MAX_CHARS:
            self.mainDisplayLabel.configure(font=("Comfortaa", DISPLAY_FONT_SMALL))
        else:
            self.mainDisplayLabel.configure(font=("Comfortaa", DISPLAY_FONT_LARGE))
        self.displayVariable.set(text)
 
    def updatePending(self):
        """
        @brief Refreshes the small label above the display with the pending operation
        @details Shows something like "12 +" while the user types the second number. Clears itself when there is nothing waiting
        """
        if self.waitingValue is not None and self.waitingOpereation is not None:
            self.waitingVariable.set(f"{self.waitingValue} {self.waitingOpereation}")
        else:
            self.waitingVariable.set("")


    def setupKeybinds(self):
        """
        @brief Binds keyboard keys to calculator functions
        @details Maps keystrokes, numpad keys, other operators and Shift press/release to the onClick method
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

    def processingOperations(self,char):
        """
        @brief Changes waiting varaibles values
        @details Changes the waiting variables according to char from user
        @param char The character or string from user
        """
        if self.expression:
            self.waitingValue = self.expression
            self.waitingOpereation  = char
            self.expression = ""
            self.updatePending()
            self.updateDisplay("")
        elif self.waitingValue is not None:
            self.waitingOpereation = char
            self.updatePending()
        return
    
    def showError(self, msg: str):
        """
        @brief Display a short error, reset state
        @details Displays a short form of error output and resets the states
        @param msg The error message that will be displayed
        """
        self.expression = msg
        self.waitingOpereation  = None
        self.waitingValue = None
        self.updatePending()
        self.updateDisplay(msg)

    #komentare
    def onClick(self, char):
        """
        @brief Handles button click and keypress events
        @details Manages the expression string, performs calculations using math_lib (ml), and updates the display
        @param char The character or string from user
        """
        if char == "Ac": 
            self.expression = ""
            self.waitingOpereation  = None
            self.waitingValue = None
            self.updatePending()
            self.updateDisplay("")
            return

        if char == "Del": 
            self.expression = self.expression[:-1]
            self.updateDisplay(self.expression)
            return

        if char == "Shift":
            if self.shiftActive:
                self.shiftOff()
            else:
                self.shiftOn()
            return
        
        if char in ("+", "-", "x", "/", "ⁿ", "%"):                         
            self.processingOperations(char)
            return

        if char == "Enter":
            try:
                if self.waitingOpereation is None:                          
                    return

                a = parse(self.waitingValue or "0")                         
                b = parse(self.expression or "0")
                op = self.waitingOpereation
                exprHistory = f"{self.waitingValue} {op} {self.expression}"

                result = None
                if op == "+":
                    result = ml.add(a, b)
                elif op == "-":
                    result = ml.sub(a, b)
                elif op == "x":
                    result = ml.mul(a, b)
                elif op == "/":
                    result = ml.div(a, b)
                elif op == "ⁿ":
                    result = ml.pow(a, int(b))
                elif op == "%":
                    result = ml.percent(a, b)

                if result is not None:
                    result = checkIntOrFloat(result)                        
                    if isinstance(result, float):
                        result = round(result, 5)
                    self.expression = str(result).replace('.', ',')
                    self.waitingOpereation = None                           
                    self.waitingValue = None
                    self.updatePending()
                    self.updateDisplay(self.expression)
                    self.saveToHistoryFile(f"{exprHistory} = {self.expression}")

            except ZeroDivisionError:
                self.showError("Error: Diviation by zero")                               
            except Exception as e:
                self.showError(f"Error: {str(e)[:12]}")
            return

        if char in ("Sin", "Cos", "Tg", "+/-", "!", "√", "Abs("):         
            try:
                if not self.expression:
                    return

                val = parse(self.expression)
                exprHistory = self.expression
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
                elif char == "!":
                    instantResult = ml.factorial(int(val))
                elif char == "√":
                    instantResult = ml.sqrt(val)
                elif char == "Abs(":
                    instantResult = ml.abs(val)

                if instantResult is not None:
                    instantResult = checkIntOrFloat(instantResult)
                    if isinstance(instantResult, float):
                        instantResult = round(instantResult, 5)
                    self.expression = str(instantResult).replace('.', ',')
                    self.updateDisplay(self.expression)
                    self.saveToHistoryFile(f"{char}({exprHistory}) = {self.expression}")

            except ZeroDivisionError:
                self.showError("Error: Diviation by zero")
            except Exception as e:
                self.showError(f"Error: {str(e)[:12]}")
            return

        if char == "π":
            self.expression += str(round(ml.pi, 5)).replace('.', ',')
            self.updateDisplay(self.expression)
            return

        self.expression += str(char)
        self.updateDisplay(self.expression)

if __name__ == "__main__":
    root = ctk.CTk()
    app = Calculator(root)
    root.mainloop()
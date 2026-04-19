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
        @brief Initializes the calculator application.
        @details Sets up the main window, styling variables, and initializes the UI components.
        @param root The root Tkinter/CustomTkinter window object.
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

        # Setup 
        self._createWidgets()
        self._setup_keybinds()

    def _createWidgets(self):
        """
        @brief Creates and packs all UI widgets.
        @details Defines the display area, top navigation buttons, and the main grid of calculator buttons.
        """
        # Display
        self.label = ctk.CTkLabel(self.root, textvariable=self.displayVar, fg_color=self.displayBg, text_color=self.textCol, corner_radius=20, font=("Comfortaa", 40),anchor="se", padx=20, pady=20, height=180)
        self.label.pack(expand=True, fill="both", padx=15, pady=15)

        # Helper btns
        topFrame = ctk.CTkFrame(self.root, fg_color="transparent")
        topFrame.pack(fill="x", padx=10, pady=5)
        ctk.CTkButton(topFrame, text="Tips&Tricks", fg_color=self.btnGreen, text_color=self.textCol, hover_color=self.hoverBtnGreen, corner_radius=10, font=("Comfortaa", 14)).pack(side="left", expand=True, fill="x", padx=5)
        ctk.CTkButton(topFrame, text="Settings", fg_color=self.btnGreen, text_color=self.textCol, hover_color=self.hoverBtnGreen, corner_radius=10, font=("Comfortaa", 14)).pack(side="left", expand=True, fill="x", padx=5)

        # Main btns grid definition
        btnFrame = ctk.CTkFrame(self.root, fg_color="transparent")
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

        # Basic buttons layout 
        for (text, r, c, color, hover, value) in btns:
            btn = ctk.CTkButton(btnFrame, text=text, fg_color=color, text_color=self.textCol,font=("Comfortaa", 18), corner_radius=12, width=btnWidth, height=btnHight,hover_color=hover, command=lambda t=value: self.on_click(t))
            btn.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

        # Equal button spans two rows
        enterBtn = ctk.CTkButton(btnFrame, text="=", fg_color=self.btnGreen, text_color=self.textCol, font=("Comfortaa", 20, "bold"), corner_radius=12, width=btnWidth, hover_color=self.hoverBtnGreen, command=lambda: self.on_click("Enter"))
        enterBtn.grid(row=4, column=4, rowspan=2, padx=4, pady=4, sticky="nsew")

        for i in range(5): 
            btnFrame.columnconfigure(i, weight=1, uniform="col")
        for i in range(6): 
            btnFrame.rowconfigure(i, weight=1, uniform="row")

    def _setup_keybinds(self):
        """
        @brief Binds physical keyboard keys to calculator functions.
        @details Maps numbers, Numpad keys, and basic mathematical operators to the on_click method.
        """
        # Nums
        for i in range(10): 
            self.root.bind(str(i), lambda e, val=i: self.on_click(str(val)))
            self.root.bind(f"<KP_{i}>", lambda e, val=i: self.on_click(str(val)))

        # Basic Operations
        self.root.bind("+", lambda e: self.on_click("+"))
        self.root.bind("<KP_Add>", lambda e: self.on_click("+"))
        self.root.bind("-", lambda e: self.on_click("-"))
        self.root.bind("<KP_Subtract>", lambda e: self.on_click("-"))
        self.root.bind("*", lambda e: self.on_click("x"))
        self.root.bind("<KP_Multiply>", lambda e: self.on_click("x"))
        self.root.bind("/", lambda e: self.on_click("/"))
        self.root.bind("<KP_Divide>", lambda e: self.on_click("/"))

        # Other operations
        self.root.bind("!", lambda e: self.on_click("!"))
        self.root.bind("w", lambda e: self.on_click("ⁿ"))
        self.root.bind("q", lambda e: self.on_click("√"))
        self.root.bind("a", lambda e: self.on_click("Abs("))
        self.root.bind("m", lambda e: self.on_click("%"))
        self.root.bind("s", lambda e: self.on_click("Sin"))
        self.root.bind("c", lambda e: self.on_click("Cos"))
        self.root.bind("t", lambda e: self.on_click("Tg"))
        self.root.bind("p", lambda e: self.on_click("π"))
        self.root.bind(";", lambda e: self.on_click("+/-"))

        # Delimiters, Delete and Result
        self.root.bind(".", lambda e: self.on_click(","))
        self.root.bind(",", lambda e: self.on_click(","))
        self.root.bind("<Return>", lambda e: self.on_click("Enter"))
        self.root.bind("<KP_Enter>", lambda e: self.on_click("Enter"))
        self.root.bind("<BackSpace>", lambda e: self.on_click("Del"))
        self.root.bind("<Escape>", lambda e: self.on_click("Ac"))

    def on_click(self, char):
        """
        @brief Handles button click and keypress events.
        @details Manages the expression string, performs calculations using math_lib (ml), and updates the display. Handles errors gracefully.
        @param char The character or command string from the pressed button or key.
        """
        # handling input
        if char == "Ac": 
            self.expression = ""
        elif char == "Del": 
            self.expression = self.expression[:-1]
        elif char == "Enter":
            try:
                # comma replacing
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
            except Exception as e:
                print(f"Error: {e}") 
                self.expression = (f"Error: {e}")


        # Other operations - instant
        elif char in ("Sin", "Cos", "Tg", "+/-"):
            try:
                val = float(self.expression.replace(',', '.'))
                if char == "Sin":
                    instantResult = ml.sin(val)
                    instantResult = round(instantResult,2)
                elif char == "Cos":
                    instantResult = ml.cos(val)
                    instantResult = round(instantResult,2)
                elif char == "Tg":
                    instantResult = ml.tg(val)
                    instantResult = round(instantResult,2)
                elif char == "+/-":
                    instantResult = ml.negate(val)
                
                self.expression = str(instantResult).replace('.', ',')
            except:
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
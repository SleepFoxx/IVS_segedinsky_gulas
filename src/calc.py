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
            ('DEL', 0, 0, self.btnBg1,self.hoverBtnBg1), ('AC', 0, 1, self.btnBg1,self.hoverBtnBg1), ('%', 0, 2, self.btnBg1,self.hoverBtnBg1), ('Sin', 0, 3, self.btnBg1,self.hoverBtnBg1), ('Cos', 0, 4, self.btnBg1,self.hoverBtnBg1),
            ('+', 1, 0, self.btnBg2,self.hoverBtnBg2), ('-', 1, 1, self.btnBg2,self.hoverBtnBg2), ('x', 1, 2, self.btnBg2,self.hoverBtnBg2), ('/', 1, 3, self.btnBg2,self.hoverBtnBg2), ('Tg', 1, 4, self.btnBg1,self.hoverBtnBg1),
            ('7', 2, 0, self.btnBg3,self.hoverBtnBg3), ('8', 2, 1, self.btnBg3,self.hoverBtnBg3), ('9', 2, 2, self.btnBg3,self.hoverBtnBg3), ('x!', 2, 3, self.btnBg2,self.hoverBtnBg2), ('|x|', 2, 4, self.btnBg1,self.hoverBtnBg1),
            ('4', 3, 0, self.btnBg3,self.hoverBtnBg3), ('5', 3, 1, self.btnBg3,self.hoverBtnBg3), ('6', 3, 2, self.btnBg3,self.hoverBtnBg3), ('√x', 3, 3, self.btnBg2,self.hoverBtnBg2), ('π', 3, 4, self.btnBg1,self.hoverBtnBg1),
            ('1', 4, 0, self.btnBg3,self.hoverBtnBg3), ('2', 4, 1, self.btnBg3,self.hoverBtnBg3), ('3', 4, 2, self.btnBg3,self.hoverBtnBg3), ('xⁿ', 4, 3, self.btnBg2,self.hoverBtnBg2),
            ('+/-', 5, 0, self.btnBg3,self.hoverBtnBg3), ('0', 5, 1, self.btnBg3,self.hoverBtnBg3), (',', 5, 2, self.btnBg3,self.hoverBtnBg3), ('Shift', 5, 3, self.btnBg2,self.hoverBtnBg2),
        ]
        
        # Button dimensions
        btnWidth, btnHight = 60, 60

        # Basic buttons layout 
        for (text, r, c, color, hover) in btns:
            btn = ctk.CTkButton(btnFrame, text=text, fg_color=color, text_color=self.textCol,font=("Comfortaa", 18), corner_radius=12, width=btnWidth, height=btnHight,hover_color=hover, command=lambda t=text: self.on_click(t))
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

        # Extra operations
        # self.root.bind("/", lambda e: self.on_click("/"))
        # self.root.bind("!", lambda e: self.on_click("!"))

        # Delimiters and Result
        self.root.bind(".", lambda e: self.on_click(","))
        self.root.bind(",", lambda e: self.on_click(","))
        self.root.bind("<Return>", lambda e: self.on_click("Enter"))
        self.root.bind("<KP_Enter>", lambda e: self.on_click("Enter"))
        self.root.bind("<BackSpace>", lambda e: self.on_click("DEL"))
        self.root.bind("<Escape>", lambda e: self.on_click("AC"))

    def on_click(self, char):
        """
        @brief Handles button click and keypress events.
        @details Manages the expression string, performs calculations using math_lib (ml), and updates the display. Handles errors gracefully.
        @param char The character or command string from the pressed button or key.
        """
        # handling input
        if char == "AC": 
            self.expression = ""
        elif char == "DEL": 
            self.expression = self.expression[:-1]
        elif char == "Enter":
            try:
                # comma replacing
                expr = self.expression.replace(',', '.')
                
                # Binary operations
                result = None
                if "+" in expr:
                    a, b = expr.split("+")
                    result = ml.add(a, b)
                elif "-" in expr:
                    parts = expr.split("-")
                    if len(parts) == 2:
                        result = ml.sub(parts[0], parts[1])
                elif "x" in expr:
                    a, b = expr.split("x")
                    result = ml.mul(a, b)
                elif "/" in expr:
                    a, b = expr.split("/")
                    result = ml.div(a, b)
                elif "xⁿ" in expr: 
                    a, b = expr.split("ⁿ")
                    result = ml.pow(float(a), int(b))
                elif "%" in expr:
                    a, b = expr.split("%")
                    result = ml.percent(a, b)

                if result is not None:
                    if isinstance(result, float):
                        result = round(result, 5)
                    self.expression = str(result).replace('.', ',')
            except Exception as e:
                self.label = ctk.CTkLabel(self.root, textvariable=self.displayVar, fg_color=self.displayBg, text_color=self.textCol, corner_radius=20, font=("Comfortaa", 10),anchor="se", padx=20, pady=20, height=180)
                print(f"Error: {e}") 
                self.expression = (f"Error: {e}")


        # Other operations
        elif char in ("Sin", "Cos", "Tg", "x!", "|x|", "√x", "+/-"):
            try:
                val = float(self.expression.replace(',', '.'))
                if char == "Sin":
                    res = ml.sin(val)
                elif char == "Cos":
                    res = ml.cos(val)
                elif char == "Tg":
                    res = ml.tg(val)
                elif char == "!":
                    res = ml.factorial(int(val))
                elif "|x|":
                    res = ml.abs(val)
                elif "√x":
                    res = ml.sqrt(val)
                elif "+/-":
                    res = ml.negate(val)
                
                self.expression = str(res).replace('.', ',')
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
import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark")

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x700")
        self.root.configure(bg="#1E1E1E")

        self.expression = ""
        self.displayVar = tk.StringVar(value="")

        self.bodyBg = "#1E1E1E"
        self.btnBg1 = "#525151"
        self.btnBg2 = "#6D6D6D"
        self.btnBg3 = "#9A9A9A"
        self.btnGreen = "#579948"
        self.displayBg = "#444444"
        self.textCol = "#FFFFFF"

        self._createWidgets()
        self._setup_keybinds()

    def _createWidgets(self):
        # Display
        self.label = ctk.CTkLabel(self.root, textvariable=self.displayVar,fg_color=self.displayBg, text_color=self.textCol,corner_radius=20, font=("Comfortaa", 40),anchor="se", padx=20, pady=20, height=180)
        self.label.pack(expand=True, fill="both", padx=15, pady=20)

        # Helper btns
        top_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        top_frame.pack(fill="x", padx=10)
        ctk.CTkButton(top_frame, text="Tips&Tricks", fg_color=self.btnGreen, text_color=self.textCol, hover_color="#467a3a", corner_radius=10, font=("Comfortaa", 14)).pack(side="left", expand=True, fill="x", padx=5)
        ctk.CTkButton(top_frame, text="Settings", fg_color=self.btnGreen, text_color=self.textCol, hover_color="#467a3a", corner_radius=10, font=("Comfortaa", 14)).pack(side="left", expand=True, fill="x", padx=5)

        # Main btns 
        btnFrame = ctk.CTkFrame(self.root, fg_color="transparent")
        btnFrame.pack(fill="both", expand=True, padx=10, pady=10)
        btns = [
            ('DEL', 0, 0, self.btnBg1), ('AC', 0, 1, self.btnBg1), ('%', 0, 2, self.btnBg1), ('Sin', 0, 3, self.btnBg1), ('Cos', 0, 4, self.btnBg1),
            ('+', 1, 0, self.btnBg2), ('-', 1, 1, self.btnBg2), ('x', 1, 2, self.btnBg2), ('/', 1, 3, self.btnBg2), ('Tg', 1, 4, self.btnBg1),
            ('7', 2, 0, self.btnBg3), ('8', 2, 1, self.btnBg3), ('9', 2, 2, self.btnBg3), ('x!', 2, 3, self.btnBg2), ('|x|', 2, 4, self.btnBg1),
            ('4', 3, 0, self.btnBg3), ('5', 3, 1, self.btnBg3), ('6', 3, 2, self.btnBg3), ('√x', 3, 3, self.btnBg2), ('Log', 3, 4, self.btnBg1),
            ('1', 4, 0, self.btnBg3), ('2', 4, 1, self.btnBg3), ('3', 4, 2, self.btnBg3), ('xⁿ', 4, 3, self.btnBg2),
            ('+/-', 5, 0, self.btnBg3), ('0', 5, 1, self.btnBg3), (',', 5, 2, self.btnBg3), ('Shift', 5, 3, self.btnBg2),
        ]

        # Static size of grid unit
        BTN_W = 60
        BTN_H = 60

        for (text, r, c, color) in btns:
            btn = ctk.CTkButton(btnFrame, text=text, fg_color=color, text_color=self.textCol,font=("Comfortaa", 18), corner_radius=12,width=BTN_W, height=BTN_H,hover_color="#333333", command=lambda t=text: self.on_click(t))
            btn.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

        # Enter btn
        enter_btn = ctk.CTkButton(btnFrame, text="=", fg_color=self.btnGreen, text_color=self.textCol,font=("Comfortaa", 20, "bold"), corner_radius=12,width=BTN_W, hover_color="#467a3a",command=lambda: self.on_click("Enter"))
        enter_btn.grid(row=4, column=4, rowspan=2, padx=4, pady=4, sticky="nsew")

        # Scaling 
        for i in range(5):
            btnFrame.columnconfigure(i, weight=1, uniform="col")
        for i in range(6):
            btnFrame.rowconfigure(i, weight=1, uniform="row")

    def _setup_keybinds(self):
        # Nums
        for i in range(10): 
            self.root.bind(str(i), lambda e, val=i: self.on_click(str(val)))
            self.root.bind(f"<KP_{i}>", lambda e, val=i: self.on_click(str(val)))

        # Math
        self.root.bind("+", lambda e: self.on_click("+"))
        self.root.bind("<KP_Add>", lambda e: self.on_click("+"))
        
        self.root.bind("-", lambda e: self.on_click("-"))
        self.root.bind("<KP_Subtract>", lambda e: self.on_click("-"))
        
        self.root.bind("*", lambda e: self.on_click("x"))
        self.root.bind("<KP_Multiply>", lambda e: self.on_click("x"))
        
        self.root.bind("/", lambda e: self.on_click("/"))
        self.root.bind("<KP_Divide>", lambda e: self.on_click("/"))

        # Comma
        self.root.bind(".", lambda e: self.on_click(","))
        self.root.bind(",", lambda e: self.on_click(","))
        self.root.bind("<KP_Separator>", lambda e: self.on_click(","))
        self.root.bind("<KP_Decimal>", lambda e: self.on_click(","))

        # Enter/Equal
        self.root.bind("<Return>", lambda e: self.on_click("Enter"))
        self.root.bind("<KP_Enter>", lambda e: self.on_click("Enter"))

        # Remove
        self.root.bind("<BackSpace>", lambda e: self.on_click("DEL"))
        self.root.bind("<Escape>", lambda e: self.on_click("AC"))
        self.root.bind("<Delete>", lambda e: self.on_click("AC"))

    def on_click(self, char):
        if char == "AC": 
            self.expression = ""
        elif char == "DEL": 
            self.expression = self.expression[:-1]
        elif char == "Enter":
            try:
                temp_expr = self.expression.replace('x', '*').replace(',', '.')
                result = eval(temp_expr)
                if result == int(result):
                    self.expression = str(int(result))
                else:
                    self.expression = str(round(result, 4)).replace('.', ',')
            except Exception:
                self.expression = "Error"
        else:
            self.expression += str(char)
        
        self.displayVar.set(self.expression)

if __name__ == "__main__":
    root = ctk.CTk()
    app = Calculator(root)
    root.mainloop()
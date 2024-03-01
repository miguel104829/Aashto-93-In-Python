import tkinter as tk
from src.flexible_pavement_gui import PavimentoApp

if __name__ == "__main__":
    root = tk.Tk()
    app = PavimentoApp(root)
    root.mainloop()
import tkinter as tk
from src.gui import CalisteniaSimulacionApp

def main():
    root = tk.Tk()
    app = CalisteniaSimulacionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

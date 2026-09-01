import tkinter as tk
import random

def create_popup():
    root = tk.Tk()
    root.title("⚠️ SYSTEM CRISIS ⚠️")
    
    # Randomly position it on her screen
    x = random.randint(100, 800)
    y = random.randint(100, 600)
    root.geometry(f"300x100+{x}+{y}")
    
    label = tk.Label(root, text="Error: Your outfit today is too distracting.", padx=10, pady=10)
    label.pack()
    
    # When she closes the window, it triggers two more
    def on_close():
        root.destroy()
        create_popup()
        create_popup()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

# Start the outbreak
create_popup()

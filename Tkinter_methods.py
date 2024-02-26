from tkinter import messagebox

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

def Valida_input(testo):
    if testo.isdigit() or testo == "":
        return True
    else:
        messagebox.showerror("Error", "Si prega di inserire esclusivamente valori numerici")
        return False
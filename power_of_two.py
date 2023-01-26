from tkinter import E


def recursive(n): 
    if n == 0:
        return 1
    else:
        
        power = recursive(n -1)
        return power * 2
    
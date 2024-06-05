import tkinter as tk

button_list = [["c", "/", "*", "-"],
               ["7", "8", "9", "+"],
               ["4", "5", "6"],
               ["1", "2", "3", "enter"],
               ["0", "."]
               ]

buttons = []
check = 0


def button_command(t, in_put, out_put):
    global check
    print(f"Button {t} pressed, check = {check}")
    
    if t == "c":
        in_put.config(text="")
        out_put.config(text="")
        check = 1
    elif t == "enter":
        try:
            temp = eval(in_put.cget("text"))
            out_put.config(text=temp)
            check = 0
        except:
            print(f"Button {t} pressed")
            

            
    elif ord(t[0]) < 48:
        if check == 0:
            temp = str(out_put.cget("text")) + t
            in_put.config(text=temp)
            check = 1
        else:
            temp = in_put.cget("text") + t
            in_put.config(text=temp)
    else:
        if check == 0:
            in_put.config(text="")
            check = 1
            
        temp = in_put.cget("text") + t
        in_put.config(text=temp)

def createButton(input_list, in_put, out_put, root):
    for i, row in enumerate(input_list):
        for j, val in enumerate(row):
            button = tk.Button(root, text = val, width=10, height=2,
                               bg="white",
                               command = lambda
                               t = val : button_command(t, in_put, out_put))
            button.grid(row = i + 2, column = j, padx = 5, pady = 5)
            buttons.append(button)
    for button in buttons:
        print(f"{button['text']}")
        if button["text"] == "+" or button["text"] == "enter":
            print("yes")
            button.grid(rowspan=2)
            button.config( height=6)
            
def changeFont(in_put):
    global check
    if check == 0:
        in_put.config(foreground="gray")
    else:
        in_put.config(foreground="black")
        
    in_put.after(100, changeFont, in_put)

if __name__ == "__main__":
    font_size = 18
    
    win = tk.Tk()
    win.title("計算機")
    win.geometry("400x600")
    win.resizable(False, False)
    
    out_put = tk.Label(win)
    out_put.config(width=50, height=5, font=("Arial", font_size), 
                   anchor="w",wraplength=400,
                   text="")
    out_put.grid(row = 0, column = 0, columnspan=50)

    in_put = tk.Label(win)
    in_put.config(width=50, height=5, font=("Arial", font_size), 
                  anchor="w",wraplength=400,
                  text="")
    in_put.grid(row = 1, column = 0, columnspan=50)
    
    createButton(button_list, in_put, out_put, win)
    
    changeFont(in_put)
    
    win.mainloop()

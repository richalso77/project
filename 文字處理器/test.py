import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from tkinterdnd2 import TkinterDnD, DND_FILES
import difflib

FILE_ENCODING = "utf-8"
FILE_PATH_LEFT = ""
FILE_PATH_RIGHT = ""

# f"{j+1}.0", f"{j+1}.end"





def compare_texts2(a, b):
    tempA = a.split(' ')
    tempB = b.split(' ')
    tempA = [x for x in tempA if x.strip() != ""]
    tempB = [x for x in tempB if x.strip() != ""]
    print("ff")
    print(tempA)
    print(tempB)
    i = 0
    finished = 0
    tempACheck = [-1] * len(tempA)
    tempBCheck = [-1] * len(tempB)
    ansLeft = []
    ansRight = []
    while (i < len(tempA)):
        for j in range(finished, len(tempB)):
            if tempA[i] == tempB[j]:
                print("==")
                finished = j
                tempACheck[i] = 1
                tempBCheck[j] = 1
                break
        i += 1
    i = 0
    j = 0
    print("tempACheck")
    print(tempACheck)
    print("tempBCheck")
    print(tempBCheck)
    while i < (len(a)):
        if a[i] == ' ':
            i += 1
            continue
        if tempACheck[j] == -1:
            print("if tempACheck[j] == -1:")
            ansLeft.append([i, i + len(tempA[j])])
            
        print(f"i={i}")
        i += len(tempA[j])
        j += 1

    i = 0
    j = 0
    while i < (len(b)):
        if b[i] == ' ':
            i += 1
            continue
        if tempBCheck[j] == -1:
            print("if tempBCheck[j] == -1:right")
            ansRight.append([i, i + len(tempB[j])])

        print(f"i={i}")
        i += len(tempB[j])
        j += 1
    return [ansLeft, ansRight]
    


def compare_texts1(a, b):
    if (a in b) or (b in a):
        return 1
    tempA = a.split(' ')
    tempB = b.split(' ')
    ans = 0
    i = 0
    finished = 0

    while (i < len(tempA)):
        for j in range(finished, len(tempB)):
            if tempA[i] == tempB[j]:
                finished = j
                ans += 1
                break
        i += 1
    return (ans) / (len(tempA) + len(tempB))

def compare_texts():
    lt = text_left.get(1.0, tk.END).split('\n')
    rt = text_right.get(1.0, tk.END).split('\n')
    lt = [x for x in lt if x.strip() != ""]
    rt = [x for x in rt if x.strip() != ""]
    comList0 = [-1] * len(lt)
    comList1 = [[] for _ in range(len(lt))]
    comList2 = [-1] * len(rt)

    finished = -1
    for i in range(len(lt)):
        for j in range(len(rt)):
            if lt[i] == rt[j]:
                if (j <= finished):
                    continue
                comList0[i] = j
                finished = j
                break
    for i in range(len(lt)):
        for j in range(len(rt)):
            if compare_texts1(lt[i], rt[j]) > 0.2:
                comList1[i].append(j)
    check = -1
    for i in range(len(lt)):
        if comList0[i] != -1:
            check = comList0[i]
        else:
            comList1[i] = [x for x in comList1[i] if x > check]

    check = 1000000
    for i in range(len(lt) - 1, -1, -1):
        if comList0[i] != -1:
            check = comList0[i]
        else:
            comList1[i] = [x for x in comList1[i] if x < check]
    check = -1
    for i in range(len(lt)):
        if comList0[i] != -1:
            check = comList0[i]
        else:
            comList1[i] = [x for x in comList1[i] if x > check]
            try:
                comList0[i] = comList1[i][0]
                check = comList1[i][0]
            except:
                continue
    print(comList0)
    for i in range(len(comList0)):
        if comList0[i] != -1:
            print(compare_texts2(lt[i], rt[comList0[i]]))
    color_menu_left = [-1] * len(lt)
    color_menu_right = [-1] * len(rt)
    for i in range(len(comList0)):
        if comList0[i] != -1:
            tmpa, tmpb = compare_texts2(lt[i], rt[comList0[i]])
            color_menu_left[i] = []
            color_menu_right[comList0[i]] = []
            for x in tmpa:
                color_menu_left[i].append([f"{i+1}.{x[0]} {i+1}.{x[1]}"])
            for x in tmpb:
                color_menu_right[comList0[i]].append([f"{comList0[i]+1}.{x[0]} {comList0[i]+1}.{x[1]}"])#123
    
    print("123123132")
    print(color_menu_left)

    text_left.tag_remove("diff", "1.0", tk.END)
    text_right.tag_remove("diff", "1.0", tk.END)

    for i in range(len(color_menu_left)):
        if color_menu_left[i] == -1:
            text_left.tag_add("diff", f"{i+1}.0", f"{i+1}.end")
            text_left.tag_configure("diff", foreground="purple")
        elif color_menu_left[i] == []:
            continue
        else:
            for x in color_menu_left[i]:
                string_from_list = x[0]
                index_of_space = string_from_list.find(' ')
                text_left.tag_add("diff", string_from_list[:index_of_space], string_from_list[index_of_space + 1:])
                text_left.tag_configure("diff", foreground="purple")

    for i in range(len(color_menu_right)):
        if color_menu_right[i] == -1:
            text_right.tag_add("diff", f"{i+1}.0", f"{i+1}.end")
            text_right.tag_configure("diff", foreground="red")
        elif color_menu_right[i] == []:
            continue
        else:
            for x in color_menu_right[i]:
                string_from_list = x[0]
                index_of_space = string_from_list.find(' ')
                text_right.tag_add("diff", string_from_list[:index_of_space], string_from_list[index_of_space + 1:])
                text_right.tag_configure("diff", foreground="red")




def renew_label(text_widget, file_path):
    if text_widget == text_left:
        global FILE_PATH_LEFT
        FILE_PATH_LEFT = file_path
        label_left.config(text=FILE_PATH_LEFT)
    else:
        global FILE_PATH_RIGHT
        FILE_PATH_RIGHT = file_path
        label_right.config(text=FILE_PATH_RIGHT)

def open_file(text_widget, file_path):
    try:
        if file_path == "":
            text_widget.delete(1.0, tk.END)
        else:
            with open(file_path, "r", encoding=FILE_ENCODING) as file:
                content = file.read()
                text_widget.delete(1.0, tk.END)
                text_widget.insert(tk.END, content)
        renew_label(text_widget, file_path)
    except Exception as e:
        messagebox.showerror("打開文件", f"無法打開文件:\n{e}")

def save_file(text_widget, file_path):
    if file_path == "":
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ])
        renew_label(text_widget, file_path)
    try:
        content = text_widget.get(1.0, tk.END)
        with open(file_path, "w", encoding=FILE_ENCODING) as file:
            file.write(content)
        messagebox.showinfo("保存文件", f"文件已成功保存到:\n{file_path}")
    except Exception as e:
        messagebox.showerror("保存文件", f"無法保存文件:\n{e}")

def handle_drop(event):
    file_path = event.data.strip('{}')
    open_file(event.widget, file_path)

def make_menu(root):
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # menu0
    menu_left_file = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="處理左側檔案", menu=menu_left_file)

    command0 = [
        ("開新檔案", lambda: open_file(text_left, "")),
        ("開啟舊檔", lambda: open_file(
            text_left,
            filedialog.askopenfilename(filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ])
        )),
        ("儲存檔案", lambda: save_file(text_left, FILE_PATH_LEFT)),
        ("另存新檔", lambda: save_file(text_left, ""))
    ]
    for a, b in command0:
        menu_left_file.add_command(label=a, command=b)

    # menu1
    menu_right_file = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="處理右側檔案", menu=menu_right_file)

    command1 = [
        ("開新檔案", lambda: open_file(text_right, "")),
        ("開啟舊檔", lambda: open_file(
            text_right,
            filedialog.askopenfilename(filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ])
        )),
        ("儲存檔案", lambda: save_file(text_right, FILE_PATH_RIGHT)),
        ("另存新檔", lambda: save_file(text_right, ""))
    ]
    for a, b in command1:
        menu_right_file.add_command(label=a, command=b)

    # menu2
    menu_function_file = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="功能", menu=menu_function_file)

    command2 = [
        ("比較文本", compare_texts),
        
    ]
    for a, b in command2:
        menu_function_file.add_command(label=a, command=b)

if __name__ == "__main__":

    win = TkinterDnD.Tk()
    win.title("文字處理器_許吉銓_n09172102")
    win.geometry("1024x768")
    win.minsize(width=800, height=200)

    top_frame = tk.Frame(win)
    top_frame.pack(side="top", fill="x")
    
    label_left = tk.Label(top_frame, text=FILE_PATH_LEFT, anchor="w", padx=5)
    label_left.pack(side="left")
    
    label_right = tk.Label(top_frame, text=FILE_PATH_RIGHT, anchor="w", padx=5)
    label_right.pack(side="right")

    text_left = tk.Text(win, wrap="word", undo=True, maxundo=-1)
    text_left.pack(side="left", expand=1, fill="both", padx=10, pady=10)
    text_right = tk.Text(win, wrap="word", undo=True, maxundo=-1)
    text_right.pack(side="right", expand=1, fill="both", padx=10, pady=10)

    text_left.drop_target_register(DND_FILES)
    text_left.dnd_bind("<<Drop>>", handle_drop)
    text_right.drop_target_register(DND_FILES)
    text_right.dnd_bind('<<Drop>>', handle_drop)

    win.bind('<Control-Shift-z>', lambda event: text_left.edit_redo())
    
    make_menu(win)

    win.mainloop()

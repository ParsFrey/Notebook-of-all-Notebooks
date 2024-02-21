import datetime
import os
#ask teacher about try and except, and also about lines.append(line), why we use both save and return, and how to make the edit fun better
date_time = datetime.datetime.now()
def edit(title):
    lines = []
    filename2 = f"note_{title}.txt"
    if os.path.exists(filename2):
        with open(filename2, "r") as file:
            note = file.read()
        print("Current Note:")
        print(note)
        new_note = input("\nafter pressing the 'Enter button' for one time , Type the new content for the note: ")
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        x = '\n'.join(lines)
        print("\n\n ", x, "\n")
        save(title, x)
        return title, x , new_note
    else:
        print("File not found.")

def delete(title):
    filename1 = f"note_{title}.txt"
    if os.path.exists(filename1):
        os.remove(filename1)
    else:
        print("File not found.")

def save(title, note):
    filename = f"note_{title}.txt"
    with open(filename, "w") as file:
        file.write(note)
        file.write(f"\n\n{date_time}\n")

def add():
    lines = []
    title = input("Type a Title: ")
    print("\n    ", title)
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    x = '\n'.join(lines)
    print("\n\n ", x, "\n")
    
    print("date:  ", date_time, "\n")
    save(title, x) 
    return title, x, date_time

notebook = []

while True:
    task = input("""a : add note
d : delete note
e : edit note
n : nothing.
                 
    What do you need? """)
    
    if task == 'a':
        note = add()
        notebook.append(note)
    elif task == 'd':
        title = input("Enter the title of the note you want to delete: ")
        delete(title)
    elif task == 'e':
        title = input("Enter the title of the note you want to edit: ")
        edit(title)
    elif task == 'n':
        break

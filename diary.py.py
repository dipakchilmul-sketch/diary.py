from datetime import datetime

def load_notes():
    notes = []
    try:
        with open("diary.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line != "":
                    notes.append(line)
    except FileNotFoundError:
        pass
    return notes

def add_notes():
    date = input("Date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return
    
    text = input("Text: ").strip()

    if text == "":
        print("Note text cannot be empty.")
        return

    with open("diary.txt", "a") as f:
        f.write(date + "|" + text + "\n")
    
    print("Note saved.")

def view_notes():
    notes = load_notes()

    if len(notes) == 0:
        print("No notes found. Your diary is empty.")
    else:
        number = 1
        for note in notes:
            parts = note.split("|", 1)
            print(number, "|", parts[0], "|", parts[1])
            number = number + 1

def search_notes():
    keyword = input("keyword: ").strip().lower()
    notes = load_notes()

    found = []
    number = 1
    for note in notes:
        parts = note.split("|", 1)
        if parts[1].lower().find(keyword) != -1:
            found.append(str(number) + "|" + parts[0] + "|" + parts[1])
        number = number + 1
    if len(found) == 0:
        print("No matching notes found.")
    else:
        print("Found", len(found), "notes:")
        for item in found:
            print(item)

def delete_notes():
    notes = load_notes()

    try:
        number = int(input("Note number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if number < 1 or number > len(notes):
        print("Note number", number, "not found.")
    else:
        notes.pop(number - 1)

        with open("diary.txt", "w") as f:
            for note in notes:
                f.write(note + "\n")
        
        print("Notes", number, "deleted. Notes left:", len(notes))
    
while True:
    print("\n--- Digital Diary ---")
    print("1. Add")
    print("2. View all")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_notes()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        search_notes()
    elif choice == "4":
        delete_notes()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

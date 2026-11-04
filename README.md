## What it does

- **Add** a note with a date (YYYY-MM-DD) and text
- **View all** notes, numbered from 1
- **Search** notes by a keyword (capital and small letters are treated the same)
- **Delete** a note by its number

All notes are saved in a text file called `diary.txt`, so they are still there after the program is closed.

## How to run

1. Install Python 3.
2. Download `diary.py` into a folder.
3. Open a terminal in that folder and run:

```
python diary.py
```

The file `diary.txt` is created automatically when you add your first note.

## Example

```
--- Digital Diary ---
1. Add
2. View all
3. Search
4. Delete
5. Exit
Enter your choice: 2
1 | 2026-10-10 | Started Python project
2 | 2026-10-11 | Python exam on Monday
```

## How notes are stored

Each note is one line in `diary.txt`, with the date and the text separated by a `|` sign:

```
2026-10-10|Started Python project
```

## Input checks

- Empty note text: "Note text cannot be empty."
- Wrong date format: "Invalid date. Use YYYY-MM-DD."
- Note number that does not exist: "Note number 9 not found."
- Letters instead of a number when deleting: "Please enter a valid note number."
- Missing `diary.txt`: the diary is treated as empty.

## Concepts used

Strings, files, functions, lists, and try/except.

## Files in this repository

- `diary.py`: the program
- `report.pdf`: the project report with test cases and screenshots

## Author

[Dipak Chilmul], BCA, [REF No.- RU-26-02287]

*Mentored by:* [Mr. Satyaprakash Sethy](https://github.com/SATYAPRAKASHSETHY)

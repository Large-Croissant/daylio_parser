import csv
import pathlib
import os
import time

this_folder = pathlib.Path(__file__).parent
output_folder = this_folder / "output" / time.strftime("%m-%d-%y %Hh%Mm%Ss")
os.mkdir(output_folder)

entries = []  # (date, time, mood, activities, note_title, note)

with open(this_folder / "export.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        activities = row["activities"].split(" | ")
        # entries.append((row["full_date"], row["time"], row["mood"], activities, row["note_title"], row["note"]))
        entries.append({"date": row["full_date"], "time": row["time"], "mood": row["mood"], "activities": (activities), "note_title": row["note_title"], "note": row["note"]})

entries.reverse()

for entry in entries:
    filepath = output_folder / f"{entry['date']}.txt"
    add_space = False
    if os.path.exists(filepath):
        add_space = True
    with open(filepath, "a", encoding="utf-8") as file:
        if add_space:
            file.write("\n\n")
        file.write(f"{entry['time']}\n")
        file.write(f"Mood: {entry['mood']}\n")
        file.write(f"Tags: {', '.join(entry['activities'])}\n")
        file.write(f"Title: {entry['note_title']}\n")
        file.write(entry["note"])

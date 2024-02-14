import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window.
    frm_main = Frame(root)
    frm_main.master.title("Rectangle Area Calculator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function to add widgets.
    populate_main_window(frm_main)

    # Start the tkinter event loop.
    root.mainloop()


def populate_main_window(frm_main):
    """Populate the main window with labels, entry boxes, and buttons."""
    # Create labels and entry boxes for width and height.
    lbl_width = Label(frm_main, text="Width:")
    ent_width = IntEntry(frm_main, width=4)
    lbl_height = Label(frm_main, text="Height:")
    ent_height = IntEntry(frm_main, width=4)

    # Create label to display the area.
    lbl_area = Label(frm_main, text="Area:")

    # Create Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout widgets in a grid.
    lbl_width.grid(row=0, column=0, padx=3, pady=3)
    ent_width.grid(row=0, column=1, padx=3, pady=3)
    lbl_height.grid(row=1, column=0, padx=3, pady=3)
    ent_height.grid(row=1, column=1, padx=3, pady=3)
    lbl_area.grid(row=2, column=0, padx=3, pady=3)
    btn_clear.grid(row=3, column=0, columnspan=2, padx=3, pady=3, sticky="w")

    # Function to calculate area.
    def calculate_area(event):
        try:
            width = ent_width.get()
            height = ent_height.get()
            area = width * height
            lbl_area.config(text=f"Area: {area}")
        except ValueError:
            lbl_area.config(text="Invalid input")

    # Function to clear entries.
    def clear_entries():
        ent_width.clear()
        ent_height.clear()
        lbl_area.config(text="Area:")

    # Bind events and commands.
    ent_width.bind("<KeyRelease>", calculate_area)
    ent_height.bind("<KeyRelease>", calculate_area)
    btn_clear.config(command=clear_entries)

    # Focus on width entry.
    ent_width.focus()


if __name__ == "__main__":
    main()
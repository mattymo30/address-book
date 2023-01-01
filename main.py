from tkinter import *
from dataclasses import dataclass
from tkinter import messagebox as mb


main_screen = Tk()
main_screen.title("Address Book")
width = 400
height = 500
screen_width = main_screen.winfo_screenwidth()  # Width of the screen
screen_height = main_screen.winfo_screenheight()  # Height of the screen
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
main_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))


@dataclass
class Address:
    name: str
    phone: str
    address: str
    notes: str


def change_to_menu():
    main_screen.title("Address Book")
    add_frame.forget()
    update_frame.forget()
    delete_frame.forget()
    display_frame.forget()
    main_menu.pack(fill='both', expand=1)


def change_to_add():
    main_screen.title("Add New Contact")
    main_menu.forget()
    update_frame.forget()
    delete_frame.forget()
    display_frame.forget()
    add_frame.pack(fill='both', expand=1)


def change_to_update():
    main_screen.title("Update Contact")
    main_menu.forget()
    add_frame.forget()
    delete_frame.forget()
    display_frame.forget()
    update_frame.pack(fill='both', expand=1)


def change_to_delete():
    main_screen.title("Delete Contact")
    main_menu.forget()
    add_frame.forget()
    update_frame.forget()
    display_frame.forget()
    delete_frame.pack(fill='both', expand=1)


def change_to_display():
    main_screen.title("All Contacts")
    main_menu.forget()
    add_frame.forget()
    update_frame.forget()
    delete_frame.forget()
    display_frame.pack(fill='both', expand=1)


def confirm_exit():
    answer = mb.askyesno(title="Confirm Exit",
                         message="Are you sure you want to exit?")
    if answer:
        main_screen.destroy()


def add_entry():
    name_to_add = name.get()
    number_to_add = number.get()
    address_to_add = address.get()
    notes_to_add = notes.get()
    if name_to_add != "" and number_to_add != "" and address_to_add != "":
        if notes_to_add == "":
            notes_to_add = "N/A"
        line_str = (name_to_add + "\t" + number_to_add + "\t" + address_to_add
                    + "\t" + notes_to_add)
        file = open("addresses.txt", "a")
        file.write(line_str)
        file.write("\n")
        file.close()
        name.delete(0, END)
        number.delete(0, END)
        address.delete(0, END)
        notes.delete(0, END)
        mb.showinfo(title="Success", message="Entry Successful")
    else:
        error_message = ""
        if name_to_add == "":
            error_message += "Name Cannot Be Blank\n"
        if number_to_add == "":
            error_message += "Phone Number Cannot Be Blank\n"
        if address_to_add == "":
            error_message += "Address Cannot Be Blank\n"
        mb.showerror(title="Unsuccessful", message=error_message)


def update_entry():
    update_name = name_to_update.get()
    change_name = new_name.get()
    change_phone = new_number.get()
    change_address = new_address.get()
    change_notes = new_note.get()
    file = open("addresses.txt")
    for line in file:
        line_list = line.split("\t")
        if line_list[0] == update_name:
            pass
    mb.showerror(title="Unsuccessful", message="Name Does Not Exist "
                                               "In Database")
    file.close()


main_menu = Frame(main_screen)
add_frame = Frame(main_screen)
update_frame = Frame(main_screen)
delete_frame = Frame(main_screen)
display_frame = Frame(main_screen)


Label(main_menu, text="Address Book", font=25).pack()
Label(main_menu, text='').pack()
Button(main_menu, text="Add New Entry", height="2", width="30",
       command=change_to_add).pack()
Label(main_menu, text='').pack()
Button(main_menu, text="Update Entry", height="2", width="30",
       command=change_to_update).pack()
Label(main_menu, text='').pack()
Button(main_menu, text="Delete Entry", height="2", width="30",
       command=change_to_delete).pack()
Label(main_menu, text='').pack()
Button(main_menu, text="Display Entries", height="2", width="30",
       command=change_to_display).pack()
Label(main_menu, text='').pack()
Button(main_menu, text="Exit", height="2", width="30",
       command=confirm_exit).pack()


Label(add_frame, text="Add New Entry", font=25).pack()
Label(add_frame, text="").pack()
Label(add_frame, text="Name:").pack()
name = Entry(add_frame)
name.pack()
Label(add_frame, text="").pack()
Label(add_frame, text="Phone Number:").pack()
number = Entry(add_frame)
number.pack()
Label(add_frame, text="").pack()
Label(add_frame, text="Address:").pack()
address = Entry(add_frame)
address.pack()
Label(add_frame, text="").pack()
Label(add_frame, text="Notes:").pack()
notes = Entry(add_frame)
notes.pack()
Label(add_frame, text="").pack()
Button(add_frame, text="Submit", height="2", width="30",
       command=add_entry).pack()
Button(add_frame, text="Main Menu", height="2", width="30",
       command=change_to_menu).pack()


Label(update_frame, text="Update Entry", font=25).pack()
Label(update_frame, text="").pack()
Label(update_frame, text="Name To Be Updated:").pack()
name_to_update = Entry(update_frame)
name_to_update.pack()
Label(update_frame, text="").pack()
Label(update_frame, text="Updated Name:").pack()
new_name = Entry(update_frame)
new_name.pack()
Label(update_frame, text="").pack()
Label(update_frame, text="New Number: ").pack()
new_number = Entry(update_frame)
new_number.pack()
Label(update_frame, text="").pack()
Label(update_frame, text="New Address: ").pack()
new_address = Entry(update_frame)
new_address.pack()
Label(update_frame, text="").pack()
Label(update_frame, text="New Notes: ").pack()
new_note = Entry(update_frame)
new_note.pack()
Label(update_frame, text="").pack()
Button(update_frame, text="Update", height="2", width="30").pack()
Button(update_frame, text="Main Menu", height="2", width="30",
       command=change_to_menu).pack()


Label(delete_frame, text="Delete Entry", font=25).pack()
Label(delete_frame, text="").pack()
Label(delete_frame, text="Contact Name to be Deleted:").pack()
Label(delete_frame, text="").pack()
delete_name = Entry(delete_frame)
delete_name.pack()
Label(delete_frame, text="").pack()
Button(delete_frame, text="Delete", height="2", width="30").pack()
Button(delete_frame, text="Main Menu", height="2", width="30",
       command=change_to_menu).pack()


Label(display_frame, text="Address Book", font=25).pack()
Button(display_frame, text="Show", height="2", width="30").pack()
Button(display_frame, text="Main Menu", height="2", width="30",
       command=change_to_menu).pack()


main_menu.pack(fill='both', expand=1)
main_screen.mainloop()

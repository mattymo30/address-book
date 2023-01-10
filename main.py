from tkinter import *
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
    file = open("addresses.txt", "r")
    data = file.readlines()
    file.close()
    counter = 0
    for line in data:
        line_list = line.split("\t")
        if line_list[0] == update_name:
            if change_name != "":
                line_list[0] = change_name
            if change_phone != "":
                line_list[1] = change_phone
            if change_address != "":
                line_list[2] = change_address
            if change_notes != "":
                line_list[3] = change_notes
            data[counter] = (line_list[0] + "\t" + line_list[1] + "\t" +
                             line_list[2] + "\t" + line_list[3] + "\n")
            file = open("addresses.txt", "w")
            file.writelines(data)
            name_to_update.delete(0, END)
            new_name.delete(0, END)
            new_number.delete(0, END)
            new_address.delete(0, END)
            new_note.delete(0, END)
            mb.showinfo(title="Success", message="Update Successful")
            file.close()
            return
        counter += 1
    mb.showerror(title="Unsuccessful", message="Name Does Not Exist "
                                               "In Database")
    file.close()


def delete_entry():
    name_to_delete = delete_name.get()
    file = open("addresses.txt", "r")
    data = file.readlines()
    file.close()
    counter = 0
    for line in data:
        line_list = line.split("\t")
        if line_list[0] == name_to_delete:
            answer = mb.askyesno(title="Confirm Deletion",
                                 message="Are you sure you want to delete"
                                         " this entry?")
            if answer:
                data[counter] = ""
                file = open("addresses.txt", "w")
                file.writelines(data)
                delete_name.delete(0, END)
                mb.showinfo(title="Success", message="Deletion Successful")
                file.close()
                return
            else:
                file.close()
                return
        counter += 1
    mb.showerror(title="Unsuccessful", message="Name Does Not Exist "
                                               "In Database")
    file.close()


def get_data():
    results = []
    with open("addresses.txt", "r") as fp:
        for i in fp.readlines():
            line = i.split('\t')
            line[3].strip('\n')
            results.append((line[0], line[1], line[2], line[3]))
    return results


def display(counter=0):
    results = get_data()
    if len(results) == 0:
        mb.showerror(title="Empty Data", message="No Entries In The Address"
                                                 " Book")
    else:
        name_display.config(text=results[counter][0])
        number_display.config(text=results[counter][1])
        address_display.config(text=results[counter][2])
        notes_display.config(text=results[counter][3])
        if counter == 0:
            show.forget()
            next_button.pack()
            back_button.pack()


def next_element():
    page_counter.set(page_counter.get() + 1)
    counter = page_counter.get()
    if len(get_data()) <= counter:
        mb.showerror(title="End of Data", message="You have reached the"
                                                  " end of the "
                                                  "address book.")
        page_counter.set(page_counter.get() - 1)
        return
    display(counter)


def back():
    page_counter.set(page_counter.get() - 1)
    counter = page_counter.get()
    if counter < 0:
        mb.showerror(title="Beginning of Data", message="You have reached the"
                                                        " beginning of the "
                                                        "address book.")
        page_counter.set(page_counter.get() + 1)
        return
    display(counter)


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
Button(update_frame, text="Update", height="2", width="30",
       command=update_entry).pack()
Button(update_frame, text="Main Menu", height="2", width="30",
       command=change_to_menu).pack()

Label(delete_frame, text="Delete Entry", font=25).pack()
Label(delete_frame, text="").pack()
Label(delete_frame, text="Contact Name to be Deleted:").pack()
Label(delete_frame, text="").pack()
delete_name = Entry(delete_frame)
delete_name.pack()
Label(delete_frame, text="").pack()
Button(delete_frame, text="Delete", height="2", width="30",
       command=delete_entry).pack()
Button(delete_frame, text="Main Menu", height="2", width="30",
       command=change_to_menu).pack()

page_counter = IntVar(value=0)
Label(display_frame, text="Address Book", font=25).pack()
page_number = Label()
Label(display_frame, text="Name:").pack()
name_display = Label(display_frame, text="")
name_display.pack()
Label(display_frame, text="").pack()
Label(display_frame, text="Phone Number:").pack()
number_display = Label(display_frame, text="")
number_display.pack()
Label(display_frame, text="").pack()
Label(display_frame, text="Address:").pack()
address_display = Label(display_frame, text="")
address_display.pack()
Label(display_frame, text="").pack()
Label(display_frame, text="Notes:").pack()
notes_display = Label(display_frame, text="")
notes_display.pack()
Label(display_frame, text="").pack()
show = Button(display_frame, text="Show", height="2", width="30",
              command=lambda: display())
show.pack()
next_button = Button(display_frame, text="Next", height="2", width="30",
                     command=lambda: next_element())
back_button = Button(display_frame, text="Back", height="2", width="30",
                     command=lambda: back())
Button(display_frame, text="Main Menu", height="2", width="30",
       command=change_to_menu).pack()

main_menu.pack(fill='both', expand=1)
main_screen.mainloop()

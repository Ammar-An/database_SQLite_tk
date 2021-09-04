# made by Ammar An
from tkinter import *
import sqlite3

window = Tk()
window.title("DataBase OpProject")
window.geometry("360x500")

# Create a database or connect to one 
conn = sqlite3.connect('address_book.db')

# Create cursor 
c = conn.cursor()

# Create table 
'''
c.execute("""CREATE TABLE addresses(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")
'''

# Create Edit Function to Update A Record
def update():
    # Create a database or connect to one 
    conn = sqlite3.connect('address_book.db')
    # Create cursor 
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode 

        WHERE oid = :oid""",
        {
        'first': f_name_editor.get(),
        'last': l_name_editor.get(),
        'address': address_editor.get(),
        'city': city_editor.get(),
        'state': state_editor.get(),
        'zipcode': zipcode_editor.get(),
        'oid': record_id
        })


    delete_box.delete(0, END)

    # Commit Changes 
    conn.commit()
    # Close Connection 
    conn.close()
    '''
    # Clear The Text Boxes 
    f_name_editor.delete(0, END)
    l_name_editor.delete(0, END)
    address_editor.delete(0, END)
    city_editor.delete(0, END)
    state_editor.delete(0, END)
    zipcode_editor.delete(0, END)
    '''                                 # السطر يلي تحت هاد بيغني عن حذف محتويات الإنتري من النافذة الجديدة (لأن بدو يلغيا) فمافي داعي لهدول 
    editor.destroy()


def edit():
    global editor
    editor = Tk()
    editor.title("Update A Record")
    editor.geometry("345x172")

    # Create a database or connect to one 
    conn = sqlite3.connect('address_book.db')
    # Create cursor 
    c = conn.cursor()

    record_id = delete_box.get()
    # Query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()                      # we can put fetchone() or fetchmany(50) 

    # Create Global Variabless for text box names 
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Create Text Boxes
    f_name_editor = Entry(editor, width=30)        # نستطيع أن نترك الأسماء دون تغيير 
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # Create Text Box Labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    # Loop thru Results 
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create a Save Button To Save edited record 
    edit_btn = Button(editor, text="Save Record", command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=130)




# Create Function to Delete A Record
def delete():
    # Create a database or connect to one 
    conn = sqlite3.connect('address_book.db')
    # Create cursor 
    c = conn.cursor()

    # Delete a record 
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    delete_box.delete(0, END)

    # Commit Changes 
    conn.commit()
    # Close Connection 
    conn.close()

#    delete_box.delete(0, END)           # هاي من عندي 



# Create Submit Function For database 
def Submit():
    # Create a database or connect to one 
    conn = sqlite3.connect('address_book.db')
    # Create cursor 
    c = conn.cursor()

    # Insert Into Table 
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            })


    # Commit Changes 
    conn.commit()
    # Close Connection 
    conn.close()


    # Clear The Text Boxes 
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Create Query Function 
def query():
    # Create a database or connect to one 
    conn = sqlite3.connect('address_book.db')
    # Create cursor 
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()                        # we can put fetchone() or fetchmany(50) ...
    # print(records)

    # Loop through Results 
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1])+ "\t\t" + "ip: " + str(record[6]) + "\n"

    query_label = Label(window, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit Changes 
    conn.commit()
    # Close Connection 
    conn.close()

# Create Text Boxes
f_name = Entry(window, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(window, width=30)
l_name.grid(row=1, column=1)
address = Entry(window, width=30)
address.grid(row=2, column=1)
city = Entry(window, width=30)
city.grid(row=3, column=1)
state = Entry(window, width=30)
state.grid(row=4, column=1)
zipcode = Entry(window, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(window, width=30)
delete_box.grid(row=9, column=1, pady=5)


# Create Text Box Labels
f_name_label = Label(window, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(window, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(window, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(window, text="City")
city_label.grid(row=3, column=0)
state_label = Label(window, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(window, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(window, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button 
Submit_btn = Button(window, text="Add Record To Database", command=Submit)
Submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)         # and we can put ipady 

# Create a Query Button 
query_btn = Button(window, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=129)

# Create a Select Button 
delete_btn = Button(window, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=130)


# Create an Update Button 
edit_btn = Button(window, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)



# Commit Changes 
conn.commit()

# Close Connection 
conn.close()

window.mainloop()

# python Update_a_record_from_database_App_Part2.py

from tkinter import *

def login():
    root = Tk()
    root.geometry('450x350')
    root.title("Logging Page")

    label_0 = Label(root, text="USER LOGIN", width=10, font=("Bold", 20), background="Yellow", foreground="Black")
    label_0.place(x=125, y=30)

    label_1 = Label(root, text="Username/Email:", width=25, font=("Italic", 11))
    label_1.place(x=-20, y=130)

    entry_1 = Entry(root)
    entry_1.place(x=160, y=130)

    label_2 = Label(root, text="Password:", width=27, font=("bold", 11))
    label_2.place(x=-50, y=165)

    entry_2 = Entry(root, show='*')
    entry_2.place(x=160, y=170)


    Button(root, text='Login Now', width=20, bg='blue', fg='white', bd=4, command=root.destroy).place(x=30, y=260)
    Button(root, text='New User', width=20, bg='blue', fg='white', bd=4, command=register).place(x=230, y=260)

    root.mainloop()


# registration new user 2
from tkinter import *


def register():
    root = Tk()
    root.geometry('500x400')
    root.title("Register")

    label_0 = Label(root, text="User Registration ", width=15, font=("bold", 20), bg="yellow")
    label_0.place(x=100, y=23)

    label_1 = Label(root, text="Name", width=20, font=("bold", 11))
    label_1.place(x=34, y=130)

    entry_1 = Entry(root)
    entry_1.place(x=240, y=130)

    label_3 = Label(root, text="Gender", width=20, font=("bold", 11))
    label_3.place(x=35, y=230)
    var = IntVar()
    Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
    Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)

    label_4 = Label(root, text="Mobile Number", font=("bold", 11), width=20)
    label_4.place(x=60, y=275)

    entry_x = Entry(root)
    entry_x.place(x=240, y=280)

    label_2 = Label(root, text="Email ID ", width=20, font=("bold", 11))
    label_2.place(x=42, y=180)

    entry_2 = Entry(root)
    entry_2.place(x=240, y=180)

    Button(root, text='Submit', width=20, bg='blue', fg='yellow', command=root.destroy).place(x=180, y=350)

    root.mainloop()


# Available Roots From 3
from tkinter import *


def booking():
    root = Tk()
    root.geometry('500x500')
    root.title("Booking request")

    label_0 = Label(root, text="Booking Request", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)

    label_1 = Label(root, text="Mobile", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)

    entry_1 = Entry(root)
    entry_1.place(x=240, y=130)

    label_2 = Label(root, text="Select Date", width=20, font=("bold", 11))
    label_2.place(x=80, y=180)
    list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
             '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    a = StringVar()
    droplist_1 = OptionMenu(root, a, *list1)
    a.set('DATE')
    droplist_1.config(width=3)
    droplist_1.place(x=250, y=180)


    list2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    b = StringVar()
    dropdown = OptionMenu(root, b, *list2)
    dropdown.config(width=5)
    b.set('MONTH')
    dropdown.place(x=315, y=180)

    list3 = ['2019', '2020', '2021', '2022', '2023', '2024', '2025']
    c = StringVar()
    droplist_2 = OptionMenu(root, c, *list3)
    droplist_2.config(width=3)
    c.set('YEAR')
    droplist_2.place(x=400, y=180)

    label_3 = Label(root, text=" From ", width=20, font=("bold", 10))
    label_3.place(x=70, y=230)
    list4 = ['Block(1-8)', 'Block(8-14)', 'Block(16-24)', 'Block(25-53)', 'Boys Hostel', 'Girl Hostel']
    d = StringVar()

    droplist_3 = OptionMenu(root, d, *list4)
    droplist_3.config(width=15)
    d.set('Departure')
    droplist_3.place(x=235, y=230)

    label_4 = Label(root, text="Fare", width=20, font=("bold", 10))
    label_4.place(x=70, y=280)
    list5 = ['RS.1000', 'RS.2000', 'RS.3000', 'RS.4000', 'RS.5000+']
    e = StringVar()
    e.set('select rupees')

    droplist_4 = OptionMenu(root, e, *list5)
    droplist_4.config(width=15)
    droplist_4.place(x=240, y=280)

    label_5 = Label(root, text=" To ", width=20, font=("bold", 10))
    label_5.place(x=70, y=230)
    f = StringVar()
    f.set('arrival')

    droplist_5 = OptionMenu(root, f, 'Block(1-8)', 'Block(8-14)', 'Block(16-24)', 'Block(25-53)', 'Boys Hostel', 'Girl Hostel')
    droplist_5.config(width=15)
    droplist_5.place(x=235, y=230)

    root.mainloop()


from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('500x400')
root.title("Cab Booking Site")

image1 = Image.open("C://Users//aakra//Downloads//Picture1.png")
resize_img = image1.resize((250, 150))
test = ImageTk.PhotoImage(resize_img)

label1 = Label(image=test, anchor='center')
label1.image = test
label1.pack()

label_0 = Label(root, text="Cab Booking", width=20, font=("bold", 20), background="Yellow")
label_0.place(x=100, y=180)

Button(root, text='Login', width=20, bg='blue', fg='white', border=5, command=login).place(x=20, y=350)
Button(root, text='New User', width=20, bg='cyan', fg='red', border=5, command=register).place(x=180, y=350)
Button(root, text='Available routes', width=20, bg='green', fg='black', border=5, command=booking).place(x=340, y=350)

root.mainloop()

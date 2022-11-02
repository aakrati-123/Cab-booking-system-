def login():
    root = Tk()
    root.geometry('500x500')
    root.title("Loging Page")

    label_0 = Label(root, text="User Loging",width=20,font=("bold", 20))
    label_0.place(x=100,y=53)


    label_1 = Label(root, text="User Name",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)

    entry_1 = Entry(root)
    entry_1.place(x=240,y=130)

    label_2 = Label(root, text="Password",width=20,font=("bold", 10))
    label_2.place(x=68,y=180)

    entry_2 = Entry(root)
    entry_2.place(x=240,y=180)

    Button(root, text='Login Now',width=20,bg='blue',fg='grey').place(x=180,y=280)
    Button(root, text='New User',width=20,bg='blue',fg='grey').place(x=180,y=330)

    root.mainloop()
#registration new user 2
from tkinter import *

def register():
    root = Tk()
    root.geometry('500x500')
    root.title("Register")

    label_0 = Label(root, text="Cab Registration ",width=20,font=("bold", 20))
    label_0.place(x=100,y=53)


    label_1 = Label(root, text="Name",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)

    entry_1 = Entry(root)
    entry_1.place(x=240,y=130)

    label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
    label_3.place(x=70,y=230)
    var = IntVar()
    Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
    Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

    label_4 = Label(root, text="mobile number",font=("bold", 10),width=20)
    label_4.place(x=70,y=280)

    entry_x= Entry(root)
    entry_x.place(x=240,y=280)

    label_2 = Label(root, text="Email id ", width=20, font=("bold", 10))
    label_2.place(x=68, y=180)

    entry_2 = Entry(root)
    entry_2.place(x=240, y=180)

    Button(root, text='Submit',width=20,bg='blue',fg='grey').place(x=180,y=380)

    root.mainloop()


#Available Roots From 3
from tkinter import *
def booking():

    root = Tk()
    root.geometry('500x500')
    root.title("Booking request")

    label_0 = Label(root, text="Booking Request",width=20,font=("bold", 20))
    label_0.place(x=90,y=53)


    label_1 = Label(root, text="Mobile",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)

    entry_1 = Entry(root)
    entry_1.place(x=240,y=130)

    label_2 = Label(root, text="Select Date",width=20,font=("bold", 10))
    label_2.place(x=68,y=180)
    listx = ['1','2','3','4','5','6','7','8''9','10','11','12','13','14','15','16''17','18','19','20','21','22','23','24','25','26','27','28','29','30'];
    c=StringVar()
    droplist=OptionMenu(root,c, *listx)
    droplist.config(width=3)
    c.set('DATE')
    droplist.place(x=260,y=180)

    listy = ['1','2','3','4','5','6','7','8''9','10','11','12'];
    c=StringVar()
    droplist=OptionMenu(root,c, *listy)
    droplist.config(width=7)
    c.set('MONTH')
    droplist.place(x=330,y=180)

    listz = ['2019','2020','2021','2022','2023','2024','2025'];
    c=StringVar()
    droplist=OptionMenu(root,c, *listz)
    droplist.config(width=3)
    c.set('YEAR')
    droplist.place(x=400,y=180)



    label_3 =  Label(root, text=" From ",width=20,font=("bold", 10))
    label_3.place(x=70,y=230)
    list1 = ['Block(1-8)','Block(8-14)','Block(16-24)','Block(25-53)','Boys Hostel','Girl Hostel'];
    c=StringVar()
    droplist=OptionMenu(root,c, *list1)
    droplist.config(width=15)
    c.set('Departure')
    droplist.place(x=235,y=230)


    label_4 = Label(root, text="Fare", width=20, font=("bold", 10))
    label_4.place(x=70, y=280)
    list3 = ['RS.1000', 'RS.2000', 'RS.3000', 'RS.4000', 'RS.5000+'];
    c = StringVar()
    droplist = OptionMenu(root, c, *list3)
    droplist.config(width=15)
    c.set('select rupees')
    droplist.place(x=240, y=280)

    label_5 = Label(root, text=" To ", width=20, font=("bold", 10))
    label_5.place(x=70, y=230)
    list2 = ['Block(1-8)', 'Block(8-14)', 'Block(16-24)', 'Block(25-53)', 'Boys Hostel', 'Girl Hostel'];
    c = StringVar()
    droplist = OptionMenu(root, c, *list2)
    droplist.config(width=15)
    c.set('arrival')
    droplist.place(x=235, y=230)

    root.mainloop()
from tkinter import *

root = Tk()
root.geometry('500x200')
root.title("Cab Booking Site")

label_0 = Label(root, text="CabMS",width=20,font=("bold", 20))
label_0.place(x=100,y=53)

Button(root, text='Login',width=20,bg='blue',fg='white',command=login).place(x=20,y=100)
Button(root, text='New User',width=20,bg='blue',fg='white',command = register).place(x=180,y=100)
Button(root, text='Available routers',width=20,bg='blue',fg='white',command=booking).place(x=340,y=100)

root.mainloop()

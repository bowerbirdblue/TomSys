# universal serial 🅱️us
"""
Levi Pender
12/11/2023
This project was a bit weird. Most of my issues revolved around either not having appropriate permissions
to use Python/etc or general Tkinter weirdness (which there is *a lot of*. seriously.) However, even though
there are some things that don't quite work the way I want, and some things I want to add or remove,
I'm pretty proud of myself and happy with it. It was fun and challenging in a good way, and I appreciate
that a lot.
"""
import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk
from tkinter import messagebox
import tkcalendar as tkc
import babel as bb
import datetime as dt
font1 = 'Menlo'
# creating the' application window
def open_app_win():
    """
    creates app window (app_win), names + sets size
    creates list variables for name/age/pronouns etc, globalizes them and assigns them
    creates frames for different stages of window, widgets that go in the frames, destroys when necessary
    serves as main program window
    """
    # creating app_win
    app_win = tk.Tk()
    app_win.title("TomSys")
    # window size
    app_win.geometry("1200x830")
    # pre-setting profile vars
    global username_prolist, password_prolist, firstnamelist, lastnamelist, ageyearlist, agemonthlist, usrpronounlist
    firstnamelist = []
    lastnamelist = []
    ageyearlist = []
    agemonthlist = []
    usrpronounlist = []
    username_prolist = []
    password_prolist = []
    # profile setting widgets
    frame1 = tk.Frame(app_win)
    frame1.place(x=0,y=0,height=830, width=1200)
    frame1["relief"]="groove"  
    def login_entry():
        '''
        this is where the labels and entries for all profile info are
        '''
        global fname_entry, lname_entry, yrage_entry, mnage_entry, current_var, current_value, prncombo, prnother
        # flavor text (title etc)
        tk.Label(frame1, text="TomSys SetProfile",font=(font1,25)).place(relx=0.5,rely=0, anchor="n")
        tk.Label(frame1, text="Welcome. Please complete your profile.",font=(font1,18)).place(relx=.5, rely=.05, anchor="n")
        # first name entry
        tk.Label(frame1, text="First Name:", font=(font1,15)).place(relx=.3, rely=.16, anchor="w")
        fname_entry = tk.Entry(frame1)
        fname_entry.place(relx=.3,rely=.19,anchor="w")
        # last name entry
        tk.Label(frame1, text="Last Name:", font=(font1,15)).place(relx=.3,rely=.23,anchor="w")
        lname_entry = tk.Entry(frame1)
        lname_entry.place(relx=.3,rely=.26,anchor="w")
        # age (years) entry
        tk.Label(frame1, text="Age (Years):", font=(font1,15)).place(relx=.7,rely=.16,anchor="e")
        yrage_entry = tk.Entry(frame1)
        yrage_entry.place(relx=.7,rely=.19,anchor="e")
        # age (months) entry
        tk.Label(frame1, text="Age (Addl. Months):",font=(font1,15)).place(relx=.7,rely=.23,anchor="e")
        mnage_entry = tk.Entry(frame1)
        mnage_entry.place(relx=.7,rely=.26,anchor="e")
        # pronouns entry
        tk.Label(frame1, text="Pronouns:", font=(font1, 15)).place(relx=.5, rely=.46,anchor="center")
        current_var = tk.StringVar()
        current_value = current_var.get()
        prncombo = ttk.Combobox(frame1, state="readonly", textvariable=current_var)
        prncombo['values'] = ("He/Him/His", "She/Her/Hers", "They/Them/Theirs", "Other")
        prncombo.place(relx=.5, rely=.50,anchor="center")
        # pronoun entry if other
        tk.Label(frame1, text="If 'Other', please specify here.", font=(font1, 12)).place(relx=.5,rely=.56,anchor='center')
        prnother = tk.Entry(frame1)
        prnother.place(relx=.5,rely=.6, anchor='center')
    login_entry()
    def view_sched():
        frame3 = tk.Frame(app_win)
        frame3.place(x=0,y=0,height=830,width=1200)
        def timeset():
            global calclock
            def time_update():
                """
                updates the time in label calclock
                """
                global calclock
                d = dt.datetime.now()
                current_dname = d.strftime('%A')
                current_date = d.strftime('%b %d %Y')
                current_time = d.strftime('%I:%M %p')
                current_min = d.strftime('%M')
                calclock.config(text=f"Today is {current_dname}, {current_date}, and it is {current_time}.")
                frame3.after(1000,time_update)
            #global d, current_dname, current_date, current_time, current_min
            calclock = tk.Label(frame3, font=(font1, 20))
            calclock.place(relx=.5,rely=0,anchor="n")
            time_update()
        timeset()
        tk.Button(frame3, text="Go Back", font=(font1, 15), command=app_win_phase2).place(relx=0.05,rely=.9,anchor="w")
    def view_profile():
            """
            upon button press, creates + configures frame3, places labels on it displaying stored profile
            info, creates "back" button which sends user back to app_win_phase2
            """
            frame3 = tk.Frame(app_win)
            frame3.place(x=0,y=0,height=830,width=1200)
            # displays profile info
            tk.Label(frame3, text="Your Profile Info:",font=(font1, 20)).place(relx=0.1,rely=0,anchor="n")
            tk.Label(frame3, text=f"First Name: {firstname}",font=(font1, 17)).place(relx=0.05,rely=0.075,anchor="w")
            tk.Label(frame3, text=f"Last Name: {lastname}",font=(font1, 17)).place(relx=0.05,rely=0.105,anchor="w")
            tk.Label(frame3, text=f"Age: {ageyear}y {agemonth}m", font=(font1,17)).place(relx=0.05,rely=.15,anchor="w")
            tk.Label(frame3, text=f"Pronouns: {usrpronoun}", font=(font1,17)).place(relx=0.05,rely=.195,anchor="w")
            tk.Label(frame3, text=f"Username: {username.pop(0)}", font=(font1,17)).place(relx=0.35,rely=.075,anchor="w")
            tk.Button(frame3, text="Go Back", font=(font1, 15), command=app_win_phase2).place(relx=0.05,rely=.9,anchor="w")
    def app_win_phase2():
        """
            creates + configures 'phase 2' frame for app_win, adds labels
            """
        frame2 = tk.Frame(app_win)
        frame2.place(x=0,y=0,height=830, width=1200)
        tk.Label(frame2, text="TomSys Home",font=(font1,25)).place(relx=0.5,rely=0, anchor="n")
        tk.Button(frame2, text="View Profile", font=(font1,15),command=view_profile).place(relx=0.25,rely=0.25,anchor="center",width=225)     
        tk.Button(frame2, text="View Today's Schedule", font=(font1,15), command=view_sched).place(relx=0.75,rely=0.25,anchor="center",width=225)
    def submit_profile():
        """
            contains + runs assignage function, creates + displays messagebox, destroys frame 
            (profile submit screen) and runs app_win_phase2 upon pressing of submit button
            """
        def assignage(a,b):
            """
            adds profile entry variables to list variables, pops list values to display variables
            """
            # actually assigning profile vars (list and then display value)
            global username_pro, password_pro, firstname, lastname, ageyear, agemonth, usrpronoun
            firstnamelist.append(fname_entry.get())
            firstname = firstnamelist.pop(0)
            lastnamelist.append(lname_entry.get())
            lastname = lastnamelist.pop(0)
            ageyearlist.append(yrage_entry.get())
            ageyear = ageyearlist.pop(0)
            agemonthlist.append(mnage_entry.get())
            agemonth = agemonthlist.pop(0)
            usrpronounlist.append(current_var.get())
            if "Other" in usrpronounlist:
                usrpronounlist.remove("Other")
                usrpronounlist.append(prnother.get())
            else:
                pass
            usrpronoun = usrpronounlist.pop(0)
        assignage("a", "b")
        # vv what happens when profile submit button is pressed vv
        messagebox.showinfo("Profile Confirm", f"First Name: {firstname}\tLast Name: {lastname}\nAge: {ageyear} years {agemonth} months\nPronouns: {usrpronoun}")
        frame1.destroy()
        app_win_phase2() 
        return
    # submit command button
    tk.Button(frame1, text="Submit",font=(font1, 15), command=submit_profile).place(relx=.5,rely=.7,anchor="center")
    # event loop for the app win   
    app_win.mainloop()
# creating a function to destroy root
def destroy1():
    """
    destroys root window (login window)
    """
    root.destroy()
username = []
password = []
# vv what happens when submit button is pressed vv
def submit_login():
    """
    takes in two strings (setusername and setpassword), checks if they are both alphanumeric, continues 
    to success + confirmation messageboxes then app_win if true and does not continue if false.
    if false, failure messagebox is displayed 
    """
    # storage for invalid characters
    global inv_char_p, inv_char_u
    inv_char_p = ""
    inv_char_u = ""
    # initial storage of username/password values
    setusername = username_entry.get()
    setpassword = password_entry.get()
    def authenticate(ulog, plog):
        """
        checks if setusername and setpassword are alnum, adds them to username and password, destroys 
        root and opens app_win if true
        if false, adds invalid characters to inv_char_u and inv_char_p and shows in messagebox
        """
        global inv_char_p, inv_char_u
        inv_char_p = ""
        inv_char_u = ""
        # stores stored username/password values if alnum
        if setusername.isalnum() and setpassword.isalnum():
            username.insert(0, setusername)
            password.append(setpassword)
            messagebox.showinfo("Confirm Credentials", f"Username: {setusername}\nPassword: {setpassword}")
            messagebox.showinfo("Login Successful.", "Welcome to the System of the Starship Tomia.")
            # destroy login window
            destroy1()
            open_app_win()
        else:
            # if username/password values are not alnum, iterates through initial stored values and takes + stores non-alnum characters, then displays
            for smth in setusername:
                if smth.isalnum():
                    pass
                else:
                    inv_char_u += smth
            for smth in setpassword:
                if smth.isalnum():
                    pass
                else:
                    inv_char_p += smth
            messagebox.showerror("Error - Invalid Username or Password", f"Invalid Characters (Usr): {inv_char_u}" + f"\nInvalid Characters (Pwd): {inv_char_p}")
            login_win()
    authenticate(username, password)    
    return setusername, setpassword             
# creating "root" (aka login window)
# creates login window (root), frame
root = tk.Tk()
root.title("TomSys Login")
frame = ttk.Frame(root)
frame.grid(row=5,column=0)
frame['relief'] = 'flat'
def login_win():
    """
    creates labels and entries and submit button, which calls submit_login when pressed
    """
    # globalizes login_win variables
    global username_entry, password_entry, root, frame
    # creating the login (+submit/cancel buttons), getting values
    # username/password labels and entries
    tk.Label(root, text="Please set your username and password and login to continue.", font=(font1)).grid(row=0,column=0,padx=10,pady=5)
    tk.Label(root, text="Username:", font=(font1)).grid(row=1, column=0, padx=1, pady=5)
    username_entry = tk.Entry(root)
    username_entry.grid(row=2, column=0, padx=1, pady=5)
    tk.Label(root, text="Password:", font=(font1)).grid(row=3, column=0, padx=1, pady=5)
    password_entry = tk.Entry(root, show = "*")
    password_entry.grid(row=4, column=0, padx=1, pady=5)
    # cancel/submit buttons for login screen
    tk.Button(frame, text="Cancel", font=(font1), command=destroy1).grid(row=5, column=0, padx=2, pady=10)
    tk.Button(frame, text="Submit", font=(font1), command=submit_login).grid(row=5, column=1, padx=2, pady=10)
    root.mainloop()
login_win()
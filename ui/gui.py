# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from tkinter import messagebox
import time


LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Colla 0.1.0')
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, ManualPage, WaypointPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 30))

        ## build frame
        self.grid(sticky='nwse')
        for column in range(2):
            self.columnconfigure(column, weight=1)
        self.rowconfigure(2, weight=1)

        ## text labels
        tk.Label(self, text=u"Colla", 
                font=("Helvetica", 32)).grid(in_=self,
                        column=0, row=2, columnspan=3, sticky="ew")

        manualbutton = ttk.Button(self, text = 'Manual' , style='my.TButton' ,command=lambda: controller.show_frame(ManualPage) )
        followbutton = ttk.Button(self, text = 'Follow Me', style='my.TButton' ,command=lambda: controller.show_frame(FollowPage))
        waypointbutton = ttk.Button(self, text = 'Waypoint', style='my.TButton' ,command=lambda: controller.show_frame(WaypointPage))
        returnbutton = ttk.Button(self, text = 'Return to Luanch', style='my.TButton', command=gotohome)
        manualbutton.grid(row = 3, column = 0, padx = 10, pady = 10)
        followbutton.grid(row = 3, column = 1, padx = 10, pady = 10)
        waypointbutton.grid(row = 4, column = 0, padx = 10, pady = 10)
        returnbutton.grid(row = 4, column = 1, padx = 10, pady = 10)
def gotohome():
    
    result = messagebox.askyesno("", "Go to Home")
    if result == True:
        print("Go to home")
    else:
        pass


class ManualPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 30))

        ## build frame
        self.grid(sticky='nwse')
        for column in range(2):
            self.columnconfigure(column, weight=1)
        self.rowconfigure(2, weight=1)

        
        homebutton = ttk.Button(self, text = 'Home' , style='my.TButton',command=lambda: controller.show_frame(StartPage) )
        homebutton.grid(row = 0, column = 0, padx = 10, pady = 10)

        ## text labels
        tk.Label(self, text=u"Manual", anchor='center',
                font=("Helvetica", 32)).grid(in_=self,
                        column=1, row=0,  sticky="ew")

        forwardbutton = ttk.Button(self, text = 'Forward' , style='my.TButton',command=forward )
        backbutton = ttk.Button(self, text = 'Back', style='my.TButton',command=back )
        rightbutton = ttk.Button(self, text = 'Right', style='my.TButton',command=right )
        leftbutton = ttk.Button(self, text = 'Left', style='my.TButton',command=left )
        forwardbutton.grid(row = 3, column = 1, padx = 10, pady = 10)
        backbutton.grid(row = 5, column = 1, padx = 10, pady = 10)
        rightbutton.grid(row = 4, column = 2, padx = 10, pady = 10)
        leftbutton.grid(row = 4, column = 0, padx = 10, pady = 10)
    
def forward():
    print("forward")    
def back():
    print("back")    
def right():
    print("right")    
def left():
    print("left")

class FollowPage(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 30))


class WaypointPage(tk.Frame):

    count = 0;
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 30))

        ## build frame
        self.grid(sticky='nwse')
        for column in range(2):
            self.columnconfigure(column, weight=1)
        self.rowconfigure(2, weight=1)

        
        homebutton = ttk.Button(self, text = 'Home' , style='my.TButton',command=lambda: controller.show_frame(StartPage) )
        homebutton.grid(row = 0, column = 0, padx = 10, pady = 10)

        ## text labels
        tk.Label(self, text=u"Waypoint", anchor='center',
                font=("Helvetica", 32)).grid(in_=self,
                        column=1, row=0,  sticky="ew")

        w1button = ttk.Button(self, text = 'W1' , style='my.TButton')
        w2button = ttk.Button(self, text = 'w2' , style='my.TButton')
        w3button = ttk.Button(self, text = 'w3' , style='my.TButton')
        w4button = ttk.Button(self, text = 'w4' , style='my.TButton')
        w5button = ttk.Button(self, text = 'w5' , style='my.TButton')
        w6button = ttk.Button(self, text = 'w6' , style='my.TButton')
        w1button.grid(row = 3, column = 0, padx = 10, pady = 10)
        w2button.grid(row = 3, column = 1, padx = 10, pady = 10)
        w3button.grid(row = 3, column = 2, padx = 10, pady = 10)
        w4button.grid(row = 4, column = 0, padx = 10, pady = 10)
        w5button.grid(row = 4, column = 1, padx = 10, pady = 10)
        w6button.grid(row = 4, column = 2, padx = 10, pady = 10)
        
        w1button.bind('<ButtonPress-1>',pressdown)
        w1button.bind('<ButtonRelease-1>', lambda event: pressup(event, id='1'))
        w2button.bind('<ButtonPress-1>',pressdown)
        w2button.bind('<ButtonRelease-1>', lambda event: pressup(event, id='2'))
        w3button.bind('<ButtonPress-1>',pressdown)
        w3button.bind('<ButtonRelease-1>', lambda event: pressup(event, id='3'))
        w4button.bind('<ButtonPress-1>',pressdown)
        w4button.bind('<ButtonRelease-1>',pressup)
        w5button.bind('<ButtonPress-1>',pressdown)
        w5button.bind('<ButtonRelease-1>',pressup)
        w6button.bind('<ButtonPress-1>',pressdown)
        w6button.bind('<ButtonRelease-1>',pressup)
timer_a = 0
def pressdown(event):
    global timer_a
    timer_a = time.time()
    print(timer_a)
def pressup(event, id):
    global timer_a
    timer_b = time.time()
    count = timer_b - timer_a
    if timer_b - timer_a > 1:
        result = messagebox.askyesno("", "Save current Position")
        if result == True:
            print("Save current Position" + id)
        else:
            pass
    else:
        result = messagebox.askyesno("", "Go to Waypoint")
        if result == True:
            print("Go to Waypoint" + id)
        else:
            pass

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()
        


app = SeaofBTCapp()
app.mainloop()
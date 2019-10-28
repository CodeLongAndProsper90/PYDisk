from tkinter import *
from playsound import playsound as play
import blockioh as io
def get_settings(filename):
    from ast import literal_eval
    with open(filename,'r') as inf:
        settings = literal_eval(inf.read())
    return settings
dev = ''
path = ''
"""
class alert():
    def __init__(self, title, message, ecode,x,y):
        if ecode == '0': 
            play('i.wav')
        elif ecode == '1': 
            play('E.wav')
        elif ecode == '2': 
            play('ue.wav')
        elif ecode == '3': 
            play('Hal.wav')
        
        top = Toplevel()
        top.title(title)
        top.minsize(x,y)
        msg = Message(top, text=message)
        msg.pack()

        button = Button(top, text="Dismiss", command=top.destroy)
        button.pack()
        from time import sleep
        
        top.mainloop()
"""
class mount():

 
    dev = StringVar()
    path = StringVar()
    class mount:

        def m(self):
            global dev, path
            device = io.device(dev.get(), path.get())
            error = device.mount()
            if error == 2: main.stat.set_color('yellow') ; main.stat.set_text('Permission denied. Run as root')
            if error == 1: main.stat.set_color('red') ; main.stat.set_text('Mountpoint or device not found')
            elif error ==3: main.stat.set_color('red'); main.stat.set_text('WARNING: I/O ERROR')
        def __init__(self, master):
            self.mount_button = Button(master,text="Mount", width=10, height=5, command=self.m)
            self.mount_button.grid(row=0,column=0, padx=2)

    class umount:

        def u(self):
            device = io.device(dev, path)
            device.umount()
        def __init__(self, master):
            self.umount_button = Button(master, text = "Unmount",width=10, height=5, command=self.u)
            self.umount_button.grid(row=0, column=1, padx=2)
    
    class m_text:
        def __init__(self, master):
            global path
            self.info = Label(master, textvariable=self.Output)
            self.info.grid(row=1, column=0, pady=2, sticky='W')
            self.text = Entry(master, textvariable=path)
            self.text.grid(row=2, column=0, pady=2, sticky='W')
        def get_input(self, *args):
            global path
            path = self.Input.get()
            print(path)
        def set_output(self, master,string):
            self.Output.set(string)
            master.update()

    class d_text:
        def __init__(self, master):
            global dev
            self.Output = StringVar()
            self.info = Label(master, textvariable=self.Output)
            self.info.grid(row=3, column=0, pady=2, sticky='W')
            self.text = Entry(master, textvariable=dev)
            self.text.grid(row=4, column=0, pady=2, sticky='W')
        def get_input(self, *args):
            global dev
            dev = self.Input.get()
            print(dev)
        def set_output(self, master,string):
            print('set_output called')
            self.Output.set(string)
            master.update()

            
    class new_user():
        def __init__(self):


            def Set():
                sett = {'name' : name.get(),
                        'root' : root.get(),
                        'hal' : True
                        }
                se = open('.mountrc', 'w')
                se.write(str(sett))
                se.close()
                top.destroy()
            # Define the popup window
            top = Toplevel()
            # Make the variables we will use to store the users name and root disk
            name = StringVar()
            root = StringVar()

            top.title("Config")
            # Define GUI elements and make thim visible
            msg1 = Message(top, text='What is your first name?')
            msg1.pack()
            in1 = Entry(top, textvariable=name)
            in1.pack()
            msg2 = Message(top, text='What is the root disk?')
            msg2.pack()
            in2 = Entry(top, textvariable=root)
            in2.pack()
            done = Button(top, text='Start', command=Set)
            done.pack()
            # Start the window running
            top.mainloop()
            
    class status():
        def __init__(self, master, text, col):
            color = StringVar()
            tex = StringVar()
            color.set(col)
            tex.set(text)
            msg = Label(master, textvariable=tex, fg=(color.get()), width=20, height=2)
            msg.grid(row=5, column=0, pady=2)
        def set_color(self, col):
            self.color.set(color)
            master.refresh()
        def set_text(self, text):
            self.tex.set(text)
            master.update()
    def __init__(self, master):
        master.title("PYMount")
        try:
            se = get_settings('.mountrc')
        except:
            self.new_user()
        m = self.mount(master)
        u = self.umount(master)
        filename = self.m_text(master)
        filename.text.bind('<Return>', filename.get_input) 
        filename.set_output(master, 'Enter your mountpoint')
        dev = self.d_text(master)
        dev.text.bind('<Return>', dev.get_input)
        dev.set_output(master, "Enter your drive location [/dev/sd*]")
class disk():
    def __init__(self, master):
        pass
    class write():
        def __init__(self, master):
            but = Button(master, text='Write', command=write)
            but.grid(row=0, column=0, padx=2, pady=2,  width=10, height=5)
        def write():
            pass 
print("We are go with no exceptions")
cmd = input('Start PYDisk or PYWrite?')
win = Tk()
if cmd=='PYDisk':
    app = mount(win)
elif cmd == 'PYWrite':
    app = disk(main)
else:
    print('Invalid')
    exit()
win.mainloop()

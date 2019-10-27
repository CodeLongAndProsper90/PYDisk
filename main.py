from tkinter import *
from playsound import playsound as play
import blockioh as io
def get_settings(filename):
    from ast import literal_eval
    with open(filename,'r') as inf:
        settings = literal_eval(inf.read())
    return settings
device = io.device('', '')
class main():

 
    devic = ''
    path = ''
    class mount:

        def m(self):
            class permissionError(Exception):
                pass
            class notFoundError(Exception):
                pass
            class unknownError(Exception):
                pass
            class done(Exception):
                pass

            global device
            try:
                device.mount()
            except permissionError:
                alt = self.alert('Oooops', 'PYMount does not have permission to access block devices. Please rerun as sudo.', 2)
            except notFoundError:
                alt = self.alert('Oooops','The file or directory you specifed does not exist.',1)
            except unknownError:
                alt = self.alert('Oooops', 'You have encountered an unknown I/O error. Check the file mountlog.txt for more info',2)
            except done:
                alt = self.alert('Woohoo!', 'Device mounted',0)
        def __init__(self, master):
            self.mount_button = Button(master,text="Mount", width=10, height=5, command=self.m)
            self.mount_button.grid(row=0,column=0, padx=2)

    class umount:

        def u(self):
            global device
            device.umount()
        def __init__(self, master):
            self.umount_button = Button(master, text = "Unmount",width=10, height=5, command=self.u)
            self.umount_button.grid(row=0, column=1, padx=2)
    
    class m_text:
        def __init__(self, master):
            self.Input =StringVar()
            self.Output = StringVar()
            self.info = Label(master, textvariable=self.Output)
            self.info.grid(row=1, column=0, pady=2, sticky='W')
            self.text = Entry(master, textvariable=self.Input)
            self.text.grid(row=2, column=0, pady=2, sticky='W')
        def get_input(self, *args):
            self.path = self.Input.get()
            print(self.path)
        def set_output(self, master,string):
            self.Output.set(string)
            master.update()

    class d_text:
        def __init__(self, master):
            self.Input = StringVar()
            self.Output = StringVar()
            self.info = Label(master, textvariable=self.Output)
            self.info.grid(row=3, column=0, pady=2, sticky='W')
            self.text = Entry(master, textvariable=self.Input)
            self.text.grid(row=4, column=0, pady=2, sticky='W')
        def get_input(self, *args):
            self.devic = self.Input.get()
            print(self.devic)
        def set_output(self, master,string):
            print('set_output called')
            self.Output.set(string)
            master.update()
    class alert():
        def __init__(self, title, message, ecode):

            top = Toplevel()
            top.title(title)

            msg = Message(top, text=message)
            msg.pack()

            button = Button(top, text="Dismiss", command=top.destroy)
            button.pack()
            if ecode ==2:
                play('ue.wav')
            elif ecode == 1:
                play('e.wav')
            elif ecode == 0:
                play('i.wav')
            top.mainloop()
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
print("We are go with no exceptions")
win = Tk()
print('win formed')
app = main(win)
win.mainloop()

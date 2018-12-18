## Python standard library
import tkinter as tk # Referring to TkInter as tk 
from tkinter import messagebox # importing optional tkinter moduals
from tkinter import ttk
import time

## Importing other peoples code

from client import sendmessage

class clsApplication():
    """Main Class. Windows are called from here. Referred to as 'objApp' throughout the program"""
    def __init__(self, window):
        """ Initializes all classes as objects of objApp """
        
        self.window = window
        self.window.title("Campus guide")
        self.window.minsize(300,800)
        
        self.objPage = clsPage(self.window)
        self.objHome = clsHome(self)
        self.objChat = clsChat(self)
        self.objHelp = clsHelp(self)

        
        # Calls the home page
        self.objHome.View()


class clsPage():
    """ Controls the layout and clearing of all pages """
    def __init__(self, window):
        """ Startup setup for the page layout """
        self.window = window
        self.pnlPage = None
        self.Refresh()

        
        
    def Refresh(self):
        """ Destroys the current content and creates the layout of frames """
        
        if self.pnlPage is not None: # If pnlPage is currently  being displayed then destroy it
            self.pnlPage.destroy()
            
        
        self.pnlPage = tk.Frame(self.window)
        self.pnlPage.grid(row = 0, column = 0)
        
        self.pnlHead = tk.Frame(self.pnlPage)#                              Creates layout
        self.pnlHead.grid(row = 0, column = 0, columnspan = 3, padx = 10)
        
        self.pnlLeft = tk.Frame(self.pnlPage, padx = 10)
        self.pnlLeft.grid(row = 1, column = 0, sticky = "n")
        self.pnlMiddle = tk.Frame(self.pnlPage)
        self.pnlMiddle.grid(row = 1, column = 1)
        self.pnlRight = tk.Frame(self.pnlPage)
        self.pnlRight.grid(row = 1, column = 2)
        self.pnlFoot = tk.Frame(self.pnlPage)
        self.pnlFoot.grid(row = 2, column = 0, columnspan = 3, sticky = "w")


class clsHome():
    """ Main home page """
    def __init__(self, objApp):
        self.objApp = objApp
    def View(self, Panel=None):
        """ Shows the home page """
        if Panel is None:# If pnlPage is currently  being displayed then destroy it
            self.objApp.objPage.Refresh()
            Panel = self.objApp.objPage.pnlMiddle
        self.Panel = Panel

        self.pnlHome = tk.Frame(self.Panel)  #  Creates the Frame, Labels and Buttons on the home page
        self.pnlHome.grid(sticky = "nsew")
        
        tk.Label(self.pnlHome, text = "Welcome to your Campus Guide:").grid(sticky = "nsew")

        tk.Button(self.pnlHome, text = "Start", command = self.homeStart).grid(sticky = "ew")

        tk.Label(self.pnlHome, text = "Need help?").grid(sticky = "ew")

        tk.Button(self.pnlHome, text = "Help!", command = self.homeHelp).grid(sticky = "ew")

    def homeStart(self): # Fuction called when the Start button is clicked
        self.objApp.objChat.View()

    def homeHelp(self): # Fuction called when the Help button is clicked
        self.objApp.objHelp.View()

class clsHelp():
# Main home page
    def __init__(self, objApp):
        self.objApp = objApp
    def View(self, Panel=None): # Shows the home page
        if Panel is None:# If pnlPage is currently  being displayed then destroy it
            self.objApp.objPage.Refresh()
            Panel = self.objApp.objPage.pnlMiddle
        self.Panel = Panel

        tk.Button(self.Panel, text = "<- Back", command = self.Return).grid(sticky = "w") # Button to return to the Home menu
        self.pnlMain = tk.Frame(self.Panel)

        self.pnlHelp = tk.Frame(self.Panel)  #  Creates the Frame, Labels and Buttons on the home page
        self.pnlHelp.grid(sticky = "nsew")

        tk.Label(self.pnlHelp, text="Help").grid(sticky = "nsew")

        with open("README.md") as f:
            tk.Label(self.pnlHelp, text=(f.read())).grid(sticky="nw")

    def Return(self): # Returns to the home
        self.objApp.objPage.Refresh()
        self.objApp.objHome.View()
        


class clsChat():
    """ The main windows of the chat bot, used for chatting with the bot """
    def __init__(self, objApp):
        self.objApp = objApp
    def View(self, Panel=None):
        
        if Panel is None:# If pnlPage is currently  being displayed then destroy it
            self.objApp.objPage.Refresh()
            Panel = self.objApp.objPage.pnlMiddle
        self.Panel = Panel
        
        lblHeading = tk.Label(self.Panel, text = "Chat!", font = "bold") # Creates headings
        lblHeading.grid(column = 0, sticky = "ew")

        tk.Button(self.Panel, text = "<- Back", command = self.Return).grid(sticky = "w") # Button to return to the Home menu
        self.pnlMain = tk.Frame(self.Panel)
        self.pnlMain.grid()
        #                                                   Creates the frames nessesary for the scrolling frame
        self.pnlHeadings = tk.Frame(self.pnlMain)
        self.pnlHeadings.grid(row = 0)
        
        self.pnlContent = tk.Frame(self.pnlMain)
        self.pnlContent.grid(row = 1)
        self.objApp.window.update()
        
        self.pnlMaster = tk.Frame(self.pnlContent) # Creates Frame
                

        self.pnlMaster.pack(side = tk.LEFT, fill = tk.BOTH, expand = True, padx = 10, pady = 10) # Packed on to pnlContent

        ########################################################################################################################
        ### Adapted from https://stackoverflow.com/questions/7727804/python-and-tkinter-using-scrollbars-on-a-canvas ###########
        ########################################################################################################################
        
        self.canvas = tk.Canvas(self.pnlMaster, width = 500) # Creates a canvas so that it can be scrolled
        self.canvas.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)

        self.scroll = tk.Scrollbar(self.pnlMaster, orient = "vertical", command = self.canvas.yview, bg = "yellow") # Creates a scrollbar for the frame

        self.canvas.config(yscrollcommand = self.scroll.set) # Sets the yscrollcommand to be the scrollbar
        
        self.scroll.pack(side = tk.RIGHT, fill = tk.Y)

        
        
        self.pnlChatContent = tk.Frame(self.canvas, width = 800) # Frame for the content to be placed on the canvas

        self.canvas_frame = self.canvas.create_window((0,0), window=self.pnlChatContent, anchor = tk.NW)
        

        self.pnlChatContent.bind("<Configure>", self.OnFrameConfigure) # When the Scrollbar is moved run onFrameConfigure
        self.canvas.bind("<Configure>", self.FrameWidth) # When the canvas width changes run FrameWidth
        ## FrameWidth() and OnFrameConfigure() are also part of this adapted code
        ########################################################################################################################
        ## END of adapted code ################################################################################################# 
        ########################################################################################################################
                
        self.objApp.window.minsize(800,800)
        self.objApp.window.update()
        
        #tk.Label(self.pnlChatContent, text = "Test").grid()

##        self.pnlLeftFrame = tk.Frame(self.pnlChatContent,bg="Black").grid(row = 0, column = 0)
##        self.pnlRightFrame = tk.Frame(self.pnlChatContent,bg="Grey").grid(row = 1, column = 0)

        #tk.Label(self.pnlChatContent, text = "Test").grid()



        
        self.SubmitTextBox = tk.Text(self.pnlMain, height=10, width=45)
        self.SubmitTextBox.grid(row = 2, column=0)

        self.btnTextSubmit = tk.Button(self.pnlMain, text="Submit", height=10, width=5, command=lambda: self.btnSend())
        self.btnTextSubmit.grid(row = 2,column=1, padx=0, sticky="w")


        self.objApp.window.update()

        
        #tk.Button(self.pnlMain, text="Test", command=self.Test).grid()
        tk.Label(self.pnlChatContent, text = "Welcome to campus guide ", justify=tk.LEFT, wraplength=200, anchor="nw", width=30).grid(column = 0, sticky = "ew", pady=1)
        
    def FrameWidth(self, event): # Called when the canvas size is changed
        #### Part of the adapted code
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width = canvas_width)

    def OnFrameConfigure(self, event): # Called when the scrollbar is moved
        #### Part of the adapted code
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

##    def Test(self):
##        tk.Label(self.pnlChatContent, text = "TestLeft ", justify=tk.LEFT, wraplength=100, anchor="nw", width=30).grid(column = 0, sticky = "nw", pady=5)
##        tk.Label(self.pnlChatContent, text = "TestRight ", justify=tk.LEFT, wraplength=100, anchor="nw", width=30).grid(column = 1, sticky = "nw", pady=5)
##        self.Scrollwin()
##        self.objApp.window.update()
        
    def Scrollwin(self):
        """ Automatically scrolls the chat bot frame to the bottom """
        self.objApp.window.update()
        self.canvas.yview_moveto(10000)

        
    def Return(self):
        """ Returns the user to the Home screen """
        self.objApp.objPage.Refresh()
        self.objApp.objHome.View()

    def btnSend(self):
        """ Takes the current text from the textbox and servers it to the server as a string and displays the return message"""
        if self.SubmitTextBox.get("1.0","end-1c") == "":
            return
        tk.Label(self.pnlChatContent, text = self.SubmitTextBox.get("1.0","end-1c"), justify=tk.LEFT, wraplength=200, anchor="nw", width=200).grid(column = 1, sticky = "nw", pady=5)
        #messagebox.showinfo(None,self.SubmitTextBox.get("1.0","end-1c"))

        self.returnmsg = sendmessage(self.SubmitTextBox.get("1.0","end-1c"))

        tk.Label(self.pnlChatContent, text = self.returnmsg, justify=tk.LEFT, wraplength=200, anchor="nw", width=30).grid(column = 0, sticky = "nw", pady=5)
        
        while self.SubmitTextBox.get("1.0","end-1c") != "": # Loops through the textbox untill the textbox is empty
            self.SubmitTextBox.delete(1.0)
            self.objApp.window.update()
        self.Scrollwin()
        




window = tk.Tk() # Creates the Main window
window.columnconfigure(0, weight=1) # Makes all coulmns at least 1 wide
window.resizable(False, False) # Make the window unresizable
window.option_add("*Font",("TkDefaultFont", 12)) # Changes the font
objApp = clsApplication(window) # Creates an instance of clsApplication
window.mainloop() # Runs inbuilt MainLoop which checks for update to the window

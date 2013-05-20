#!/usr/bin/env python

"""
Example of the very basic, minimal farmework for a wxPython application

This shows how to do a text box and a dialog box
"""

import wx
import os

#---------------------------------------------------------------------------

# This is how you pre-establish a file filter so that the dialog
# only shows the extension(s) you want it to.
wildcard = "Python source (*.py)|*.py|"     \
           "Compiled Python (*.pyc)|*.pyc|" \
           "SPAM files (*.spam)|*.spam|"    \
           "Egg file (*.egg)|*.egg|"        \
           "All files (*.*)|*.*"

#---------------------------------------------------------------------------


class AppLogic(object):
    """
    A class to hold the application Application Logic.

    You generally don't want the real logic of the app mixed
    in with the GUI

    In a real app, this would be a substantial collection of 
    modules, classes, etc...
    """
    def file_open(self, filename="default_name"):
        """This method opens a file"""
        print "Open a file: "
        print "I'd be opening file: %s now"%filename

    def file_close(self):
        """This method closes a file"""
        print "Close a file: "
        print "I'd be closing a file now"

class ButtonPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)

        ## add just a single button:
        self.theButton = wx.Button(self, label="Push Me")
        self.theButton.Bind(wx.EVT_BUTTON, self.onButton)
                                   
    def onButton(self, evt=None):
        print "You pushed the button!"

class TestFrame(wx.Frame):
    def __init__(self, app_logic, *args, **kwargs):
        kwargs.setdefault('title', "Simple test App")
        wx.Frame.__init__(self, *args, **kwargs)

        self.app_logic = app_logic

        # put the Panel on the frame
        self.buttonPanel = ButtonPanel(self)

        # Build up the menu bar:
        menuBar = wx.MenuBar()
        
        fileMenu = wx.Menu()
        openMenuItem = fileMenu.Append(wx.ID_ANY, "&Open", "Open a file" )
        self.Bind(wx.EVT_MENU, self.onOpen, openMenuItem)

        closeMenuItem = fileMenu.Append(wx.ID_ANY, "&Close", "Close a file" )
        self.Bind(wx.EVT_MENU, self.onClose, closeMenuItem)

        exitMenuItem = fileMenu.Append(wx.ID_EXIT, "Exit", "Exit the application")
        self.Bind(wx.EVT_MENU, self.onExit, exitMenuItem)
        menuBar.Append(fileMenu, "&File")
        
        helpMenu = wx.Menu()
        helpMenuItem = helpMenu.Append(wx.ID_HELP, "Help", "Get help")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)
        

    def onOpen(self, evt=None):
        """This method opens an existing file"""
        print "Open a file: "
        # Create the dialog. In this case the current directory is forced as the starting
        # directory for the dialog, and no default file name is forced. This can easilly
        # be changed in your program. This is an 'open' dialog, and allows multitple
        # file selections as well.
        #
        # Finally, if the directory is changed in the process of getting files, this
        # dialog is set up to change the current working directory to the path chosen.
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(), 
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.CHANGE_DIR
            )

        # Show the dialog and retrieve the user response. If it is the OK response, 
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            path = dlg.GetPath()
            print "I'd be opening file in onOpen ", path
            self.app_logic.file_open( path )
        else :
            print "The file dialog was canceled before anything was selected"
            



        # Destroy the dialog. Don't do this until you are done with it!
        # BAD things can happen otherwise!
        dlg.Destroy()



    def onClose(self, evt=None):
        print "close menu selected"
        self.app_logic.file_close()

    def onExit(self, evt=None):
        print "Exit the program here"
        print "The event passed to onExit is type ", type(evt),
        self.Close()


class TestApp(wx.App):
    def OnInit(self):
        """
        App initilization goes here -- not much to do, in this case
        """
        app_logic = AppLogic()
        f = TestFrame(app_logic, parent=None)
        f.Show()

        return True

if __name__ == "__main__":
    app = TestApp(False)
    app.MainLoop()


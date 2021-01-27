from src.FrontEndApp import MainApp
import logging
from tkinter import Tk

def main():
    #The logs of this application is stored under the src folder in myapp.log
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    #The following code calls the MainApp which builts the UI and also calls the backend logic
    root = Tk()
    root.geometry("600x400")
    app = MainApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
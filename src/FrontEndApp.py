import tkinter as tk
from tkinter import messagebox, Button, Canvas
from tkinter import Frame, BOTH
from src.ConfigParserUtility import ConfigUtility
from src.Deck import Deck
import logging
import os

class MainApp(Frame):
    def __init__(self, master=None):
        logging.info('Init the UI frame')
        Frame.__init__(self, master)                 
        self.master = master
        configUtil = ConfigUtility()
        self.configs = configUtil.ConfigSectionMap('Default Values')
        self.init_window()
        
    def createImages(self):
        logging.info('Creating the images Dictionary')
        dir_path = os.getcwd()
        image_dir = os.path.join(dir_path, self.configs['img_dir'])
        self.image_dict = {}
        for card in self.deck1._cards:
            # all images have filenames that match the card_list names + extension .gif
            filename = card.value+".gif"
            self.image_dict[card] = tk.PhotoImage(file=os.path.join(image_dir, filename))

    def quit(self):
        logging.info('Quitting the app')
        self.deck1._cards.clear()
        self.deck2._cards.clear()
        self.image_dict.clear()
        self.master.destroy()
    
    def dealACard(self):
        try:
            logging.info('Dealing a card from Deck to Dealt')
            self.deck1.deal(self.deck2)
            self.canvas1.delete("all")
            self.fillDeckCanvas()
            self.canvas2.delete("all")
            self.fillDealtCanvas()
        except:
            logging.info('All the cards are dealt, need user input to proceed')
            self.deck1._cards.clear()
            self.deck2._cards.clear()
            self.MsgBox = tk.messagebox.askquestion('No more Cards to Deal',' Want to Reset',icon = 'warning')
            if self.MsgBox == 'yes':
                self.init_window()
            
        
    def fillDeckCanvas(self):
        logging.info('Refreshing Cards in Deck')
        self.canvas1.create_text(
            self.configs['canvastext_x'],
            self.configs['canvastext_y'],
            fill= self.configs['color'],
            font= self.configs['fontname']+' '+self.configs['fontsize']+' '+self.configs['fonttype'],
            text="Deck")
        self.x = int(self.configs['canvasimg_x'])
        self.y = int(self.configs['canvasimg_y'])
        for card in self.deck1._cards:
            self.canvas1.create_image(self.x, self.y, image=self.image_dict[card], anchor='nw')
            self.x += int(self.configs['x_threshold'])
        self.canvas1.place(x=self.configs['canvas_1_x'], y=self.configs['canvas_1_y'])
        
    def fillDealtCanvas(self):
        logging.info('Refreshing Cards in Dealt')
        self.canvas2.create_text(
            self.configs['canvastext_x'],
            self.configs['canvastext_y'],
            fill= self.configs['color'],
            font= self.configs['fontname']+' '+self.configs['fontsize']+' '+self.configs['fonttype'], 
            text="Dealt")
        self.x = int(self.configs['canvasimg_x'])
        self.y = int(self.configs['canvasimg_y'])
        for card in self.deck2._cards:
            self.canvas2.create_image(self.x, self.y, image=self.image_dict[card], anchor='nw')
            self.x += int(self.configs['x_threshold'])
        self.canvas2.place(x=self.configs['canvas_2_x'], y=self.configs['canvas_2_y'])
        
    #Creation of init_window
    def init_window(self):  
        logging.info('Initializing the UI')
        self.master.title("Deck of Cards")
        self.pack(fill=BOTH, expand=1)
        
        self.deck1 = Deck(fill=True)
        self.createImages()
        self.canvas1 = Canvas(width=self.configs['canvaswidth'], height=self.configs['canvasheight'])
        self.fillDeckCanvas()
        
        self.canvas2 = Canvas(width=self.configs['canvaswidth'], height=self.configs['canvasheight'])
        self.canvas2.create_text(
            self.configs['canvastext_x'],
            self.configs['canvastext_y'],
            fill= self.configs['color'],
            font= self.configs['fontname']+' '+self.configs['fontsize']+' '+self.configs['fonttype'], 
            text="Dealt")
        self.deck2 = Deck(fill=False)
        self.canvas2.place(x=self.configs['canvas_2_x'], y=self.configs['canvas_2_y'])
       
        # creating a button instance
        self.dealButton = Button(self, text="Deal", command=self.dealACard)
        self.dealButton.place(x=self.configs['button_1_x'], y=self.configs['button_1_y'])
        
        # creating a button instance
        self.quitButton = Button(self, text="Quit", command=self.quit)
        self.quitButton.place(x=self.configs['button_2_x'], y=self.configs['button_2_y'])

MainApp.__doc__ = "This class initializes the UI, places two Canvas elements(one for the deck and other for the dealt cards), " \
                  "two buttons (one to deal a card from the deck of cards to the dealt list and the other is to quit the play)" \
                  "The configurations of the UI are loaded from the config.ini file." \
                  "The card images are built using the tkinter library and the images are in the cards folder (all are in gif format)" \
                  "The class has dealACard method which has the logic of popping a card from the deck of cards and filling it in the dealt " \
                  "cards deck." \
                  "After all the cards have been dealt, the user has two options, either to reset the game or quit the game" \
                  "This class has a quit method which clears all the deck and destroys the UI frame"
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

class Main_Window:
    #Stores all decorations for widgets - makes it easier to change later
    decorations = {
        "Buttons":{
                
        "Background Color":"#C70000",
        "Text Color": "#000000",
        "Border Color": "#000000",
        "Border Size": 3,
        "Hover Color": "#A50909",
        "Font": "Kabel Heavy"},

        "Creator Label":{

        "Text Color": "#333333",
        "Background Color": "transparent",
        "Font Size": 10}
    }

    def __init__(self, window):
        super().__init__()

        #Initialize Window and Hide Window
        self.window = window
        window.withdraw()

        #Checks if other windows are open
        self.howto_win = None

        #Changes the Window's icon after a short delay
        window.after(200, lambda: window.iconbitmap("images/Cash-icon.ico"))

        window.title("Monopoly Cash Tracker")
        window.minsize(700, 500)
        window.configure(fg_color="#cde6d0")
    
        #Initalizes the raw image for the background and the background img
        self.background_raw = Image.open("images/Monoploy-bg.png").convert('RGB')
        self.background_raw.thumbnail((1920, 1080))


        #Creates background image using PhotoImage
        self.bg_photo = ImageTk.PhotoImage(self.background_raw)
       
        #Raw Logo Image, That's resized and set with PhotoImage
        logo_raw = Image.open("images/Monoploy-logo.png").convert('RGBA')
        logo_raw = logo_raw.resize((500, 500), Image.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(logo_raw)

        #Background canvas: places the image and sits behind everything
        self.canvas = tk.Canvas(window, highlightthickness=0, bd=0, bg="#cde6d0")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        tk.Misc.lower(self.canvas)



        #Creates logo and background with canvas
        self.bg_item = self.canvas.create_image(0, 0, image=self.bg_photo, anchor='center')
        self.logo_item = self.canvas.create_image(0, 0, image=self.logo_photo, anchor="center", state="hidden")

        #Help Button - Tells the user about the application
        self.help_btn = ctk.CTkButton(self.canvas,
            text="How To Use?",
            command=self.open_help,

            border_color=self.decorations["Buttons"]["Border Color"],
            border_width=self.decorations["Buttons"]["Border Size"],

            font= (self.decorations["Buttons"]["Font"], 14),
            fg_color= self.decorations["Buttons"]["Background Color"],
            
            hover=True,
            hover_color=self.decorations["Buttons"]["Hover Color"])

        self.help_win = self.canvas.create_window(0, 0, window=self.help_btn, anchor="nw")
    
    
        #New Game button for players to start a new game and assign Players
        self.new_game_btn = ctk.CTkButton(self.canvas,
            text="Create New Game",

            #Border Properties
            border_color=self.decorations["Buttons"]["Border Color"],
            border_width=3,

            #Size Properties
            width=200,
            height=50,

            #Font Properties
            font=("Kabel Heavy",20,"bold"),
            fg_color=self.decorations["Buttons"]["Background Color"],

            #Hover Properties
            hover=True,
            hover_color=self.decorations["Buttons"]["Hover Color"],
            )


        #Load Button for players to load a saved game. 
        self.load_game_btn = ctk.CTkButton(self.canvas,
            text="Load Game",

            #Border Properties
            border_color=self.decorations["Buttons"]["Border Color"],
            border_width=3,

            #Size Properties
            width=200,
            height=50,

            #Font Properties
            font=("Kabel Heavy",20,"bold"),
            fg_color=self.decorations["Buttons"]["Background Color"],

            #Hover Properties
            hover=True,
            hover_color=self.decorations["Buttons"]["Hover Color"],
            )

         #Adds buttons to canvas 
        self.new_game_win = self.canvas.create_window(0, 0, window=self.new_game_btn, anchor="center")
        self.load_game_win = self.canvas.create_window(0, 0, window=self.load_game_btn, anchor="center")
        
        self.creator_label = ctk.CTkLabel(
            window,

            #Text Properties
            text="Creator - Addison Murphy",
            text_color=self.decorations["Creator Label"]["Text Color"],

            #Font Properties
            fg_color=self.decorations["Creator Label"]["Background Color"],
            font=("", self.decorations["Creator Label"]["Font Size"], "bold"),

            #Padding (Inner)
            padx=10,

            #Size Properties
            width=0,
            height=0)

        self.creator_label.place(relx=0, rely=1, anchor='sw', x=10, y=-5)


        self.canvas.bind("<Configure>", self.on_resize)
        #Loads widgets and unhides window 
        self.finish_setup()

    def open_help(self):
        if self.howto_win is not None and self.howto_win.winfo_exists():
            return 

        self.window.withdraw()
        self.howto_win = HowToWindow(self.window)

    def on_resize(self, event):
        self.place_items(event.width, event.height)

    #Places the widgets on the canvas with the center widgets having the same x value
    def place_items(self, width, height):
        cx, cy = width // 2, height // 2
        self.canvas.coords(self.bg_item, cx, cy)
        self.canvas.coords(self.logo_item, cx, 250)
        self.canvas.coords(self.help_win, 20, 20)          # stays top-left
        self.canvas.coords(self.new_game_win, cx, 540)
        self.canvas.coords(self.load_game_win, cx, 640)
        
    def finish_setup(self):
        # Maximize while still hidden, then let tkinter lay everything out
        self.window.state("zoomed")
        self.window.update()

        w, h = self.window.winfo_width(), self.window.winfo_height()

        #Logo into its grid cell
        self.place_items(w, h)
        self.canvas.itemconfigure(self.logo_item, state='normal')
        
        #Small pause, then show everything at once
        self.window.deiconify()

class HowToWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.state("zoomed")
        self.update()
       
        self.after(100, self.bring_to_front)

        self.title("How To Use")
        self.minsize(700, 500)
        self.configure(fg_color="#cde6d0")

        self.background_raw = Image.open("images/Monoploy-bg.png").convert('RGB')
        self.background_raw.thumbnail((1920, 1080))
        self.bg_photo = ImageTk.PhotoImage(self.background_raw)

        self.canvas = tk.Canvas(self, highlightthickness=0, bd=0, bg="#cde6d0")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        tk.Misc.lower(self.canvas)

        self.bg_item = self.canvas.create_image(0, 0, image=self.bg_photo, anchor="center")

        self.canvas.bind("<Configure>", self.on_resize)

    def bring_to_front(self):
        self.lift()
        self.attributes("-topmost", True)
        self.after(600, lambda: self.attributes("-topmost", False))
        self.focus()

    def on_resize(self, event):
        self.place_item(event.width, event.height)
    
    def place_item(self, width, height):
        cx, cy = width // 2, height // 2
        self.canvas.coords(self.bg_item, cx, cy)

      
        
        
        
   
if __name__ == '__main__':
    root = ctk.CTk()
    w = Main_Window(root)
    root.mainloop()



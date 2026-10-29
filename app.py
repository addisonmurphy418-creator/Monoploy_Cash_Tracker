import os
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

#Stores all decorations for widgets - makes it easier to change later
decorations = {
    "Buttons":{
            
    "Background Color":"#C70000",
    "Text Color": "#FFFFFF",
    "Border Color": "#000000",
    "Border Size": 3,
    "Hover Color": "#A50909",
    "Font": "Kabel Heavy"},

    "Creator Label":{

    "Text Color": "#333333",
    "Background Color": "#cde6d0",
    "Font Size": 10},

    "Frames":{
        "Background Color": "#FFFFFF",
        "Border Color": "#000000",
        "Border Size": 3,
        "Corner Radius": 5,
    },

    "Header":{
        "Text Color": "#000000",
        "Font": "Kabel Heavy",
    }

}


class App(ctk.CTk):
    def __init__(self): 
        super().__init__()
        self.title("Monopoly Cash Tracker")
        self.geometry("1000x700")
        self.minsize(1000,500)

        self.after(200, lambda: self.iconbitmap("images/Cash-icon.ico"))

        self.bg_photo = self.load_background()

        #Every screen is stacked in the same spot
        container = tk.Frame(self, bg="#cde6d0")
        container.pack(fill="both", expand=True)

        self.pages = {}
        for Page in (MenuPage, HowToPage, CreatePlayers):
            self.pages[Page] = Page(container, decorations, self)

        self.show_page(MenuPage)
        self.after(10, lambda: self.state("zoomed"))

    def load_background(self):
        img = Image.open("images/Monoploy-bg.png").convert('RGB')
        img.thumbnail((1920, 1080))
        return ImageTk.PhotoImage(img)
    
    def show_page(self, page_class):
        for p in self.pages.values():
            p.place_forget()
        page = self.pages[page_class]
        page.place(x=0, y=0, relwidth=1, relheight=1)
        page.tkraise()
        self.after_idle(lambda: self.refresh_page(page))

    def refresh_page(self, page):
        page.update_idletasks()
        w, h = page.canvas.winfo_width(), page.winfo_height()
        if w < 200 or h < 200:
            return
        page.place_items(w, h)


class MenuPage(ctk.CTkFrame):
    def __init__(self, parent, decorations, controller):
        super().__init__(parent)
        self.controller = controller
        self.decorations = decorations

        #Grabs background image from main App class
        self.bg_photo = controller.bg_photo
       
        #Raw Logo Image, That's resized and set with PhotoImage
        logo_raw = Image.open("images/Monoploy-logo.png").convert('RGBA')
        logo_raw = logo_raw.resize((500, 500), Image.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(logo_raw)

        #Background canvas: places the image and sits behind everything
        self.canvas = tk.Canvas(self, highlightthickness=0, bd=0, bg="#cde6d0")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        #Creates logo and background with canvas
        self.bg_item = self.canvas.create_image(0, 0, image=self.bg_photo, anchor='center')
        self.logo_item = self.canvas.create_image(0, 0, image=self.logo_photo, anchor="center")

        #Help Button - Tells the user about the application
        self.help_btn = ctk.CTkButton(self.canvas,
            text="How To Use?",
            text_color=decorations["Buttons"]["Text Color"],
            command=lambda: controller.show_page(HowToPage),

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
            command=lambda: controller.show_page(CreatePlayers),
            text_color=decorations["Buttons"]["Text Color"],

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
            text_color=decorations["Buttons"]["Text Color"],

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
            self,

            #Text Properties
            text="Creator - Addison Murphy",
            text_color=decorations["Creator Label"]["Text Color"],

            #Font Properties
            fg_color=decorations["Creator Label"]["Background Color"],
            font=("", decorations["Creator Label"]["Font Size"], "bold"),

            #Padding (Inner)
            padx=10,

            #Size Properties
            width=0,
            height=0)

        self.creator_label.place(relx=0, rely=1, anchor='sw', x=10, y=-5)

        self.canvas.bind("<Configure>", self.on_resize)
     
    def on_resize(self, event):
        if event.width < 200 or event.height < 200:
            return
        if not self.winfo_viewable():
            return
        self.place_items(event.width, event.height)

    #Places the widgets on the canvas with the center widgets having the same x value
    def place_items(self, width, height):
        cx, cy = width // 2, height // 2
        self.canvas.coords(self.bg_item, cx, cy)
        self.canvas.coords(self.logo_item, cx, 250)
        self.canvas.coords(self.help_win, 20, 20)          # stays top-left
        self.canvas.coords(self.new_game_win, cx, 540)
        self.canvas.coords(self.load_game_win, cx, 640)
        
#Creates subclass for scroll frame in How to Page, Makes only scroll below the header
class FixedScrollableFrame(ctk.CTkScrollableFrame):
    def _mouse_wheel_all(self, event):
       canvas = self._parent_canvas
       bbox = canvas.bbox("all")

       if bbox and (bbox[3] - bbox[1]) <= canvas.winfo_height():
           canvas.yview_moveto(0)
           return
       super()._mouse_wheel_all(event)
       


class HowToPage(ctk.CTkFrame):
    def __init__(self, parent, decorations, controller):
        super().__init__(parent)
        self.controller = controller
        self.decorations = decorations

        #Grabs background image from App clas
        self.bg_photo = controller.bg_photo
        
        #Creates the canvas for the background and other widgets
        self.canvas = tk.Canvas(self, highlightthickness=0, bd=0, bg="#cde6d0")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)


        #Creates the back button
        self.back_btn = ctk.CTkButton(self.canvas,
        text="← Back",
        command=lambda: controller.show_page(MenuPage),

        border_width=decorations["Buttons"]["Border Size"],
        border_color=decorations["Buttons"]["Border Color"],

        hover=True,
        hover_color=decorations["Buttons"]["Hover Color"],
        
        fg_color=decorations["Buttons"]["Background Color"],

        #Font Properties 
        font=(decorations["Buttons"]["Font"], 14, "bold"),
        text_color=decorations["Buttons"]["Text Color"],
        )

        #Adds the Back Button to the canvas
        self.back_win = self.canvas.create_window(0, 0, window=self.back_btn, anchor="nw")

        self.howto_frame = FixedScrollableFrame(
            self,
            orientation="vertical",

            #Background Color 
            fg_color= decorations["Frames"]["Background Color"],

            #Size Properties
            width=650,
            #height=600,

            #Border Properties
            border_color = decorations["Frames"]["Border Color"],
            border_width= decorations["Frames"]["Border Size"],
            corner_radius= decorations["Frames"]["Corner Radius"]
            )

        #Places the frame on the window
        self.howto_frame.place(relx=0.5, rely=0.5, relheight=0.85, relwidth=0.45, anchor="center")
        self.howto_frame.lift()

        #Creates How to Heading
        self.header = ctk.CTkLabel(self.howto_frame,
            text="How to Use Monoploy Cash Tracker",


            text_color=decorations["Header"]["Text Color"],
            font=(decorations["Header"]["Font"], 24, "bold")
            )
        

        #Places the header on to the scroll frame
        self.header.pack(pady=(20, 10))

        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "HowTo.txt")
        with open(path, "r", encoding="utf-8") as f:
            self.howto_text = f.read()


        self.content = ctk.CTkLabel(self.howto_frame,
            text=self.howto_text,
            text_color=decorations["Header"]["Text Color"],
            wraplength=500,
            justify="left",
            anchor="center"
            )
        self.content.pack(pady=20, padx=20, fill="x")

        #Creates the background image for the canvas
        self.bg_item = self.canvas.create_image(0, 0, image=self.bg_photo, anchor="center")

        self.canvas.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        if event.width < 200 or event.height < 200:
            return
        if not self.winfo_viewable():
            return
        self.place_items(event.width, event.height)

    #Placement of each widget cx and cy being the center 
    def place_items(self, width, height):
        cx, cy = width // 2, height // 2
        self.canvas.coords(self.bg_item, cx, cy)
        self.canvas.coords(self.back_win, 20, 20)

class CreatePlayers(ctk.CTkFrame):
    MAX_PLAYERS = 8
    MIN_PLAYERS = 2

    def __init__(self, parent, decorations, controller):
        super().__init__(parent)
        self.controller = controller
        self.decorations = decorations

        #Grabs the background image from App class
        self.bg_photo = controller.bg_photo

        #Background canvas, how the bg img gets displayed
        self.canvas = tk.Canvas(self, highlightthickness=0, bd=0, bg="#cde6d0")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        self.players_frame = ctk.CTkFrame(
            self,
        
            #Background Color 
            fg_color= decorations["Frames"]["Background Color"],

        
            #Border Properties
            border_color = decorations["Frames"]["Border Color"],
            border_width= decorations["Frames"]["Border Size"],
            corner_radius= decorations["Frames"]["Corner Radius"]
        )

        #Places the frame on the window and lift make sure it's on top
        self.players_frame.place(relx=0.5, rely=0.5, relheight=0.95, relwidth=0.45, anchor="center")
        self.players_frame.lift()

        #Two eqal-ish columns: labels on the left, enteries on the right
        self.players_frame.grid_columnconfigure(0, weight=1)
        self.players_frame.grid_columnconfigure(1, weight=0)
        self.players_frame.grid_columnconfigure(2, weight=0)
        self.players_frame.grid_columnconfigure(3, weight=1)

        #Title for Create Players Frame
        self.header =ctk.CTkLabel(
            self.players_frame,
            text="Enter Players:",
            text_color=decorations["Header"]["Text Color"],
            font=(decorations["Header"]["Font"], 32, "bold")
        )
        self.header.grid(row=0, column=0, columnspan=4, pady=(20, 5))

        #Hints to the players how many players are allowed
        self.hint = ctk.CTkLabel(
            self.players_frame,
            text=f"Minimum {self.MIN_PLAYERS} players, maximum {self.MAX_PLAYERS} players!",
            text_color="#BFBBBB",

            font=("Kabel Heavey", 16, "bold"), 
        )
        self.hint.grid(row=1, column=0, columnspan=4, pady=(0, 15))

        #One label + entry per player
        self.player_entries = []
        for i in range(self.MAX_PLAYERS):
            label = ctk.CTkLabel(
                self.players_frame,
                text=f"Player {i + 1}:",
                text_color=decorations["Header"]["Text Color"],
                font=(decorations["Header"]["Font"], 24),
                anchor="e",
            )
            label.grid(row=i + 2, column=0, padx=(0,10), pady=8, sticky="e")

            entry = ctk.CTkEntry(
                self.players_frame,
                placeholder_text="Required" if i < self.MIN_PLAYERS else "Optional",
                text_color="#000000",
                fg_color="#FFFFFF",
                border_color=decorations["Buttons"]["Border Color"],
                border_width=2,
                height=40,
                width=200,
                font=(decorations["Header"]["Font"], 18, "bold")
            )
            entry.grid(row=i + 2, column=1, padx=(10, 0), pady=8, sticky="w")
            self.player_entries.append(entry)

        # Error Message (empty until needed)
        self.error_label = ctk.CTkLabel(self.players_frame, text='', text_color="#C70000", font=(decorations["Header"]["Font"], 18, "bold"))
        self.error_label.grid(row=self.MAX_PLAYERS + 2, column=0, columnspan=4, pady=(0, 0))

        # Start Button
        self.start_btn = ctk.CTkButton(
            self.players_frame,
            text="Start Game",
            command=self.start_game,
            width=200,
            height=45,
            font=(decorations["Buttons"]["Font"], 18, "bold"),
            text_color=decorations["Buttons"]["Text Color"],
            fg_color=decorations["Buttons"]["Background Color"],
            border_color=decorations["Buttons"]["Border Color"],
            border_width=decorations["Buttons"]["Border Size"],
            hover=True,
            hover_color=decorations["Buttons"]["Hover Color"]
        )
        self.start_btn.grid(row=self.MAX_PLAYERS + 3, column=0, columnspan=4, pady=(10, 10))

        #Creates the back button
        self.back_btn = ctk.CTkButton(self.canvas,
        text="← Back",
        command=lambda: (self.clear_entries(), controller.show_page(MenuPage)),

        border_width=decorations["Buttons"]["Border Size"],
        border_color=decorations["Buttons"]["Border Color"],

        hover=True,
        hover_color=decorations["Buttons"]["Hover Color"],
        
        fg_color=decorations["Buttons"]["Background Color"],

        #Font Properties 
        font=(decorations["Buttons"]["Font"], 14, "bold"),
        text_color=decorations["Buttons"]["Text Color"],
        )

        #Create window on canvas for back button
        self.back_win = self.canvas.create_window(0, 0, window=self.back_btn, anchor="nw")
        
        #Creates the image for the background from the canvas
        self.bg_item = self.canvas.create_image(0, 0, image=self.bg_photo, anchor="center")

        self.canvas.bind("<Configure>", self.on_resize)

    def clear_entries(self):
        for e in self.player_entries:
            if e.get() != "":
                e.delete(0, "end")
        self.error_label.configure(text="")

    def get_player_names(self):
        #Returns the names of the players, that were filled in (in order).
        names = [e.get().strip().title() for e in self.player_entries]
        return [n for n in names if n]
    
    def start_game(self):
        names = self.get_player_names()

        if len(names) < self.MIN_PLAYERS:
            self.error_label.configure(text=f'"Please Enter At Least {self.MIN_PLAYERS} Player Names."')
            return
        if len({n.lower() for n in names}) != len(names):
            self.error_label.configure(text='"Players Names Must Be Different"')
            return

        self.error_label.configure(text="")
        self.controller.player_names = names
        print(names)    #TODO: Replace with show page (Game Page)


    def place_items(self, width, height):
        cx, cy = width // 2, height // 2
        self.canvas.coords(self.bg_item, cx, cy)
        self.canvas.coords(self.back_win, 20, 20)

    def on_resize(self, event):
        if event.width < 200 or event.height < 200:
            return
        if not self.winfo_viewable():
            return
        self.place_items(event.width, event.height)

if __name__ == '__main__':
    App().mainloop()



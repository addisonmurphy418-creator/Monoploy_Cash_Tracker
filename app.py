import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

class Main_Window:
    background_color = "#C70000"

    def __init__(self, window):
        super().__init__()

        #Initialize Window and Hide Window
        self.window = window
        window.withdraw()

        window.title("Monopoly Cash Tracker")
        window.resizable(0, 0)
        window.configure(fg_color="#cde6d0")
        window.after(0, lambda:window.state('zoomed'))

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
        self.canvas = tk.Canvas(window, highlightthickness=0, bd=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        tk.Misc.lower(self.canvas)

        #Creates logo and background with canvas
        self.bg_item = self.canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')
        self.logo_item = self.canvas.create_image(0, 0, image=self.logo_photo, anchor="center", state="hidden")
        

        #logo is now revered as a cell in the grid layout
        window.rowconfigure(0, minsize=500)
        window.columnconfigure(2, minsize=500)


    
        #New Game button for players to start a new game and assign Players
        self.new_game_btn = ctk.CTkButton(window,
            text="Create New Game",
            width=200,
            height=50,
            font=("Kabel Heavy",20,"bold"),
            fg_color=self.background_color,
            hover=True,
            hover_color="#B10404",
            )

        #Places the button in the middle of the screen, 
        self.new_game_btn.grid(
            row=1,
            column=2,
            rowspan=1,
            columnspan=1,
        )

        #Load Button for players to load a saved game. 
        self.load_game_btn = ctk.CTkButton(window,
            text="Load Game",
            width=200,
            height=50,
            font=("Kabel Heavy",20,"bold"),
            fg_color=self.background_color,
            hover=True,
            hover_color="#B10404",
            )

        """Places load button in the middle of the screen, 
        with a padding to keep it away from {new_game} button"""
        self.load_game_btn.grid(
            row=2,
            column=2,
            rowspan=1,
            columnspan=1,
            pady=20
        )

        self.creator_label = ctk.CTkLabel(
            window,
            text="Creator - Addison Murphy",
            text_color="#E7E7E7",
            fg_color="#333333",
            font=("", 16, "bold"),
            padx=10
        )

        self.creator_label.grid(
            row=5,
            column=0,
            sticky='w',
            pady=(0,5), padx=(10,0)
        )


        #Fills in the empty spaces to push the content to the center
        window.columnconfigure(1, weight=1)
        window.columnconfigure(3, weight=2)

        #Fills the space in the rows and pushes content to the middle
        window.rowconfigure(4, weight=1)

        self.finish_setup()

    def finish_setup(self):
        # Maximize while still hidden, then let tkinter lay everything out
        self.window.state("zoomed")
        self.window.update()

        w, h = self.window.winfo_width(), self.window.winfo_height()
        x, y, bw, bh = self.window.grid_bbox(2, 0)
       

        # Background scaled once to the final window size
        resized = self.background_raw.resize((w, h), Image.BILINEAR)
        self.bg_photo = ImageTk.PhotoImage(resized)
        self.canvas.itemconfigure(self.bg_item, image=self.bg_photo)

        #Logo into its grid cell
        self.canvas.coords(self.logo_item, x + bw // 2, y + bh // 2)
        self.canvas.itemconfigure(self.logo_item, state='normal')
        

        #Small pause, then show everything at once
        self.window.deiconify()
   
if __name__ == '__main__':
    root = ctk.CTk()
    w = Main_Window(root)
    root.mainloop()



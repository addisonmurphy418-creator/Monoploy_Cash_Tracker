import customtkinter as ctk
from PIL import Image

class Main_Window:
    background_color = "#C70000"

    def __init__(self, window):
        super().__init__()

        self.window = window
        window.minsize(1100, 500)
        window.configure(fg_color="#cde6d0")
        window.after(0, lambda:window.state('zoomed'))

        self.logo = ctk.CTkImage(light_image=Image.open("images/Monoploy-logo.png"), size=(400, 400))

        self.logo_label = ctk.CTkLabel(window, text="", image=self.logo)
        self.logo_label.grid(row=0, column=2) 

        self.new_game_btn = ctk.CTkButton(window,
            text="Create New Game",
            width=200,
            height=50,
            font=("Kabel Heavy",20,"bold"),
            fg_color=self.background_color,
            hover=True,
            hover_color="#B10404",
            )

        self.new_game_btn.grid(
            row=1,
            column=2,
            rowspan=1,
            columnspan=1,
        )

        self.load_game_btn = ctk.CTkButton(window,
            text="Load Game",
            width=200,
            height=50,
            font=("Kabel Heavy",20,"bold"),
            fg_color=self.background_color,
            hover=True,
            hover_color="#B10404",
            )

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
            text_color="#333333",
            font=("", 16)
        )

        self.creator_label.grid(
            row=5,
            column=0,
            sticky='w',
            pady=(0,5), padx=(10,0)
        )

        
        window.columnconfigure(1, weight=1)
        window.columnconfigure(3, weight=2)

        window.rowconfigure(4, weight=1)



if __name__ == '__main__':
    root = ctk.CTk()
    w = Main_Window(root)
    root.mainloop()



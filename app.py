import customtkinter as ctk

class Main_Window:
    background_color = "#C70000"

    def __init__(self, window):
        super().__init__()

        self.window = window
        window.geometry("500x400")
        window.configure(fg_color="#cde6d0")
        window.after(0, lambda:window.state('zoomed'))


        self.title = ctk.CTkLabel(window,
            text='Monopoly Cash Tracker',
            width=40, height=28, 
            fg_color='transparent',
            text_color="#000000",
            font=("", 38, "bold")
            )
        
        self.title.grid(
            row=0, column=1,
            rowspan=1, columnspan=2,
            pady=15,
            sticky="nsew"
        )

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
            row=2,
            column=1,
            rowspan=1,
            columnspan=2,
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
            row=3,
            column=1,
            rowspan=1,
            columnspan=2,
            pady=20
        )

        
        window.columnconfigure(0, weight=1)
        window.columnconfigure(3, weight=1)

        window.rowconfigure(1, weight=1)
        window.rowconfigure(4, weight=1)



if __name__ == '__main__':
    root = ctk.CTk()
    w = Main_Window(root)
    root.mainloop()


        
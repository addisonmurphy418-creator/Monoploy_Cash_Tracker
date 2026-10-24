import customtkinter as ctk

class Main_Window:
    def __init__(self, window):
        super().__init__()

        self.window = window
        window.geometry("500x400")
        window.after(0, lambda:window.state('zoomed'))


        self.title = ctk.CTkLabel(window,
                                        text='Monopoly Cash Tracker',
                                        width=40, height=28, 
                                        fg_color='transparent',
                                        )
        self.title.grid(
            row=0, column=1,
            rowspan=1, columnspan=2,
            sticky="nsew"
        )

if __name__ == '__main__':
    root = ctk.CTk()
    w = Main_Window(root)
    root.mainloop()


        
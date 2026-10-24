import customtkinter as ctk

class Main_Window(ctk.CTkFrame):
    def __init__(self, window):
        super().__init__()

        self.Title = ctk.CTkLabel(window,
                                        text='Monopoly Cash Tracker',
                                        width=40, height=28, 
                                        fg_color='transparent',
                                        )

if __name__ == '__main__':
    root = ctk.CTk()
    w = Main_Window(root)
    root.main_loop()


        
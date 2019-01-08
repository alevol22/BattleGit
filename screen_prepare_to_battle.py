import tkinter

class Screen_prepare_to_battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, call_on_next):
        super(Screen_prepare_to_battle, self).__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.call_on_selected = call_on_next
        
        self.create_widgets()
        self.grid()

    def create_widgets (self):
        tkinter.Label(self, text='You').grid(row=1, column=1)
        tkinter.Label(self, text='Computer').grid(row=1, column=3)

        imageSmall = tkinter.PhotoImage(file="images/" + self.player1.small_image)
        w = tkinter.Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=2, column=0)

        imageSmall = tkinter.PhotoImage(file="images/" + self.player2.small_image)
        w = tkinter.Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=2, column=1)

        tkinter.Label(self, text=self.player1.hit_points + ' HP').grid(row=3, column=1)
        tkinter.Label(self, text=self.player2.hit_points + ' HP').grid(row=3, column=3)
        tkinter.Label(self, text=self.player1.dexterity + ' Dexterity').grid(row=4, column=1)
        tkinter.Label(self, text=self.player2.dexterity + ' Dexterity').grid(row=4, column=3)
        tkinter.Label(self, text=self.player1.strength + ' Strength').grid(row=5, column=1)
        tkinter.Label(self, text=self.player2.strength + ' Strength').grid(row=5, column=3)

    def continue_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.call_on_selected()
            
        
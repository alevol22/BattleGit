import tkinter

from Battle.characters import Character

class Screen_Battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, call_on_next):
        super(Screen_Battle, self).__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.call_on_selected = call_on_next

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        self.attack_bttn = tkinter.Button(self, text='Attack', command=self.attack_clicked()).grid(row=1, column=0)

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

        tkinter.Label(self, text=self.player1.hit_points + '/' + self.player1_max_hp).grid(row=3, column=1)
        tkinter.Label(self, text=self.player2.hit_points + '/' + self.player2_max_hp).grid(row=3, column=3)

    def attack_clicked(self):

        while self.player1.hit_points > 0 and self.player2.hit_points > 0:

            Character.attack(self, self.player1)
            Character.attack(self, self.player2)

        if self.player1.hit_points <= 0:
            print()
        else:
            print()

        self.attack_bttn.destroy()
        self.exit_bttn = tkinter.Button(self, text='Exit', command=self.exit_clicked()).grid(row=1, column=0)

        ''' 
            2) Updates the labels on the top right with the result of the attacks.    
        '''
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.call_on_selected()
  
            
            
            
            
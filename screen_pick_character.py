import tkinter
from Battle.characters import Character

class Screen_character_selector (tkinter.Frame):
    def __init__ (self, master, char_list, call_on_selected):
        super(Screen_character_selector, self).__init__(master)
        
        # Save the list of characters 
        self.char_list = char_list
        
        # Save the method reference to which we return control after the player hits "Next"
        self.call_on_selected = call_on_selected
        
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        tkinter.Label(self, text="Hit Points Dexterity Strength").grid(row=1, column=0)
        self.character = tkinter.StringVar()
        self.character.set(None)
        row = 2
        val = 0
        for i in range(0, 4):
            char = self.char_list.get_and_remove_character
            imageSmall = tkinter.PhotoImage(file="images/" + char.small_image)

            w = tkinter.Label(self, image=imageSmall)
            w.photo = imageSmall
            w.grid()

            tkinter.Radiobutton(self, text=char + w.photo + char.hit_points + char.dexterity + char.strength,
                                variable=self.character, value=val).grid(row=row, column=1)

            row += 1
            val += 1
        tkinter.Button(self, text='Continue to Battle!', command=self.continue_clicked()).grid(row=7, column=4)

    def continue_clicked(self):
        ''' This method is called when the Next button is clicked. 
            Notice that it passes self.character back to the callback method. '''         
        self.call_on_selected(self.character.get())
            
        
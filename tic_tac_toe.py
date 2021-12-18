from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty

class MainApp(MDApp):
    title = "Tic Tac Toe"
    def build(self):
        self.icon = "tic-tac-toe.ico"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("tic_tac_toe.kv")

    turn= "X"
    winner= False
    X_wins = 0
    O_wins = 0

    def disable_buttons(self):
        self.root.ids.btn1.disabled = True
        self.root.ids.btn2.disabled = True
        self.root.ids.btn3.disabled = True
        self.root.ids.btn4.disabled = True
        self.root.ids.btn5.disabled = True
        self.root.ids.btn6.disabled = True
        self.root.ids.btn7.disabled = True
        self.root.ids.btn8.disabled = True
        self.root.ids.btn9.disabled = True

    def is_all_disabled(self):
        if self.root.ids.btn1.disabled == True and \
        self.root.ids.btn2.disabled == True and \
        self.root.ids.btn3.disabled == True and \
        self.root.ids.btn4.disabled == True and \
        self.root.ids.btn5.disabled == True and \
        self.root.ids.btn6.disabled == True and \
        self.root.ids.btn7.disabled == True and \
        self.root.ids.btn8.disabled == True and \
        self.root.ids.btn9.disabled == True:
            return True
        else:
            return False

    def is_tie(self):
        if self.winner== False and self.is_all_disabled() == True:
            self.root.ids.instruct.text = "It's a Tie"

    def end_game(self,a,b,c):
        a.color="green"
        b.color="green"
        c.color="green"
        if a.text == "X":
            self.X_wins = self.X_wins +1
            self.root.ids.instruct.text="Hurray! X won!"
        else:
            self.O_wins = self.O_wins +1
            self.root.ids.instruct.text="Hurray! O won!"
        self.winner = True
        self.root.ids.score.text = f'X Wins: {self.X_wins}  |   O Wins: {self.O_wins}'
        self.disable_buttons()


    def is_win(self):
        # Rows
        if (self.root.ids.btn1.text!="") and (self.root.ids.btn1.text==self.root.ids.btn2.text and self.root.ids.btn1.text==self.root.ids.btn3.text):
            self.end_game(self.root.ids.btn1,self.root.ids.btn2,self.root.ids.btn3)

        if (self.root.ids.btn4.text!="") and (self.root.ids.btn4.text==self.root.ids.btn5.text and self.root.ids.btn4.text==self.root.ids.btn6.text):
            self.end_game(self.root.ids.btn4,self.root.ids.btn5,self.root.ids.btn6)
            
        if (self.root.ids.btn7.text!="") and (self.root.ids.btn7.text==self.root.ids.btn8.text and self.root.ids.btn8.text==self.root.ids.btn9.text):
            self.end_game(self.root.ids.btn7,self.root.ids.btn8,self.root.ids.btn9)


        # Diagonals
        elif (self.root.ids.btn1.text!="") and (self.root.ids.btn1.text==self.root.ids.btn5.text and self.root.ids.btn1.text==self.root.ids.btn9.text):
            self.end_game(self.root.ids.btn1,self.root.ids.btn5,self.root.ids.btn9)

        elif (self.root.ids.btn5.text!="") and (self.root.ids.btn3.text==self.root.ids.btn5.text and self.root.ids.btn5.text==self.root.ids.btn7.text):
            self.end_game(self.root.ids.btn7,self.root.ids.btn5,self.root.ids.btn3)


        # Columns
        elif (self.root.ids.btn1.text!="") and (self.root.ids.btn1.text==self.root.ids.btn4.text and self.root.ids.btn1.text==self.root.ids.btn7.text):
            self.end_game(self.root.ids.btn1,self.root.ids.btn4,self.root.ids.btn7)
            
        elif (self.root.ids.btn2.text!="") and (self.root.ids.btn2.text==self.root.ids.btn5.text and self.root.ids.btn8.text==self.root.ids.btn5.text):
            self.end_game(self.root.ids.btn2,self.root.ids.btn5,self.root.ids.btn8)

        elif (self.root.ids.btn6.text!="") and (self.root.ids.btn3.text==self.root.ids.btn6.text and self.root.ids.btn6.text==self.root.ids.btn9.text):
            self.end_game(self.root.ids.btn3,self.root.ids.btn6,self.root.ids.btn9)


    def presser(self,btn):
        if self.turn == "X":
            btn.text = "X"
            btn.disabled = True
            self.root.ids.instruct.text = "O's turn"
            self.turn = "O"
        else:
            btn.text = "O"
            btn.disabled = True
            self.root.ids.instruct.text = "X's turn"
            self.turn = "X"
        self.is_tie()
        self.is_win()

    def restart(self):
        self.turn = "X"
        self.winner = False
        self.root.ids.instruct.text = "X Goes First!"
        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False

        self.root.ids.btn1.text = ""
        self.root.ids.btn2.text = ""
        self.root.ids.btn3.text = ""
        self.root.ids.btn4.text = ""
        self.root.ids.btn5.text = ""
        self.root.ids.btn6.text = ""
        self.root.ids.btn7.text = ""
        self.root.ids.btn8.text = ""
        self.root.ids.btn9.text = ""

        self.root.ids.btn1.color = "black"
        self.root.ids.btn2.color = "black"
        self.root.ids.btn3.color = "black"
        self.root.ids.btn4.color = "black"
        self.root.ids.btn5.color = "black"
        self.root.ids.btn6.color = "black"
        self.root.ids.btn7.color = "black"
        self.root.ids.btn8.color = "black"
        self.root.ids.btn9.color = "black"

    def new_match(self):
        self.root.ids.score.text= 'X Wins: 0    |   O Wins: 0'
        self.X_wins = 0
        self.O_wins = 0
        self.restart()


if __name__=="__main__":
    MainApp().run()
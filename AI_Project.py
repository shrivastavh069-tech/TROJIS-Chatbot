import sys
import webbrowser
import subprocess
import time
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtGui import QMovie
from ass import Ui_MainWindow as my_ai


class my_assistant(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=my_ai()
        self.ui.setupUi(self)
        self.movie=QMovie("tro.gif")
        self.ui.label.setMovie(self.movie)
        self.movie.start()
        self.brain()
        self.ui.send_btn.returnPressed.connect(self.tasks)
        QTimer.singleShot(500,self.listen)
        #self.ui.label_2.mousePressEvent=lambda:self.show
        
                 
        
    def computer (self,text):
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)
        engine.say(text)
        engine.runAndWait()
        engine.stop()


    def intro(self):
        self.computer("Good evening everybody. ")
        time.sleep(0.10)
        self.computer("I will introduce your projects and also do some basic things ")
        time.sleep(0.10)
        self.computer("like opening apps.")
       
    def batana(self):
        self.computer(
            "I will introduce your projects and also do some basic things "
            "like opening apps."
            )
       

    def open_youtube(self):
        self.computer("Sure. opening youtube")
        webbrowser.open("https://www.youtube.com/")
        
    

    def open_snake(self):
        self.computer("Sure. opening snake and ladder game ")
        subprocess.Popen(
            ["python", r"C:\snake_game\main.py"],
            cwd=r"C:\snake_game"
        )
        

    def open_sps(self):
        self.computer("Sure. opening stone paper scissor game ")
        subprocess.Popen(
            ["python", r"C:\Help_coder\help_coder\main.py"],
            cwd=r"C:\Help_coder\help_coder"
        )
        
    
    def des_snake (self):
        self.computer("The game starts with an animated intro screen, background music, and a Play button to begin the game.")
        time.sleep(1.5)
        self.computer("Players can choose between Player vs Bot and 2 Player game modes before starting.")
        time.sleep(1)
        self.computer("first i will tell you about Player vs player board")
        time.sleep(1.5)
        self.computer("This is the player vs player board .")
        time.sleep(1)
        self.computer("on upper side there is An accessible menu bar lets players resume the game, return to the menu, or exit while playing.")
        time.sleep(1)
        self.computer("we are returning into menu ")
        self.computer("it is an completely diffrent board of player vs bot ")
        time.sleep(1)
        self.computer("TO save your time i would play this gameplay into 4x")
        time.sleep(180)
        self.computer("we can access the menubar from here also")
        time.sleep(120)
        self.computer("victory secene of bot wins")
        time.sleep(1)
        time.sleep("now showing your more winning screen")
        
       
        
    def des_stone(self):
        self.computer("The game starts with an animated intro screen, background music, and a Play button to begin the game.")
        time.sleep(1)
        self.compter("The story tells about coder life.")
        time.sleep(53)
        self.computer("this a game play mode in which the battle begins with brain and a coder to fix the bug right now or fix bug at tommorrow")
        time.sleep(60)
        self.computer("Here the coder is win")
        time.sleep(6)
        self.timer("showing you winnig screen of brain")
        time.sleep(1)
        
        
    def listen(self):
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        command = r.recognize_google(audio).lower()
        self.ui.send_btn.setText(command)
        self.tasks()
        QTimer.singleShot(100,self.listen)
    
    def greeting (self):
        import time
        luck=(time.strftime("%H:%M:%S"))
        if "6" < luck <="11":
            self.computer("good morning.")
            time.sleep(0.10)
            self.computer("how can i help you")
        if "12" < luck <="15":
            self.computer("good afternoon.")
            time.sleep(0.10)
            self.computer("how can i help you")

             
        if "14" < luck <="20":
            self.computer("good evening.")
            time.sleep(0.10)
            self.computer("how can i help you")
        if "21" < luck <="4":
            
            self.computer("good night."
                          "how can i help you")
          

    def brain (self):    
        self.commands = {
            "hello":self.greeting,
            "yourself": self.intro,
            "youtube": self.open_youtube,
            "can you do":self.batana,
            #"tell me about ":self.des_snake,
            "tell me about my stone paper scissor game":self.des_stone,
            "snake and ladder game":self.open_snake,
            "stone paper scissor":self.open_sps,
        }
        
    def tasks (self):
        command = self.ui.send_btn.text().lower()
        for keyword, action in self.commands.items():
            if keyword in command:
                action()
                break
            


app=QApplication(sys.argv)
Window=my_assistant()
Window.show()
sys.exit(app.exec())



                

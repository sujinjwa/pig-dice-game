from controller import Controller

class App:
    def play(self):
        controller = Controller.Controller()
        controller.play()

app = App()
app.play()
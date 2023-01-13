from view import OutputView, InputView

class Controller:
    def __init__(self):
        self.outputView = OutputView.OutputView()
        self.inputView = InputView.InputView()
        self.username = ''

    def play(self):
        self.outputView.print_start_message()

        self.read_username()
    
    def read_username(self):
        self.username = self.inputView.username()
        
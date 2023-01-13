from view import OutputView, InputView
from model import Dice, User, Computer

class Controller:
    def __init__(self):
        self.outputView = OutputView.OutputView()
        self.inputView = InputView.InputView()
        self.user = User.User()
        self.computer = Computer.Computer()

    def play(self):
        self.outputView.print_start_message()

        self.read_username()
    
    def read_username(self):
        username = self.inputView.validate_username()
        self.user.set_name(username)

        self.roll()
    
    def roll(self):
        new_dice = Dice.Dice()
        new_dice.roll()
    
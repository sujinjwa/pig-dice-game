from view import OutputView, InputView
from model import Dice, User, Computer, Player

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
        # username을 User 에 넘겨주기

        self.roll()
    
    def roll(self):
        new_dice = Dice.Dice()
        new_dice.roll()
        print(new_dice.get_number())
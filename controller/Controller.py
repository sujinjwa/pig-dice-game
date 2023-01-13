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
    
        self.print_current_status()
    
    def print_current_status(self):
        self.outputView.print_total_score(self.user, self.computer)
        self.outputView.print_current_total_score(self.user)

        self.read_command()
    
    def read_command(self):
        command = self.inputView.go_stop()
        if(command == 'Go'):
            self.roll()
        else:
            self.change_turn()
    
    def roll(self):
        new_dice = Dice.Dice()
        new_dice.roll()
        self.user.set_score(new_dice.get_number())
        
        print('\n')
        self.outputView.print_current_score(self.user)

        return self.print_current_status()
    
    def change_turn(self):
        print('상대방 차례입니다')
class OutputView:
    def print_start_message():
        print('주사위 게임을 시작합니다')
    
    def print_success_message():
        print('축하합니다! 게임에 이기셨습니다!')
    
    def print_fail_message():
        print('안타깝네요. 컴퓨터가 이겼습니다..')
    
    def print_total_score(user_score, computer_score):
        print(f'[ Sujin Jo의 최종 점수: {user_score} | 상대방(컴퓨터)의 최종 점수: {computer_score} ]')
    
    def print_current_total_score(player_name, total_score):
        print(f'[ 이번 턴의 {player_name}의 점수 : {total_score} ]')
    
    def print_current_score(score):
        print(f'{score}점이 나왔습니다!')

    def print_reset_message():
        print('이번 턴의 점수가 초기화됩니다.')

    def print_close_message():
        print('게임을 종료합니다.')

    def print_current_turn(player_name):
        print('----- {player_name}의 차례입니다 -----')
class InputView:
    def username():
        while True:
            username = input("이름을 입력하세요: ")
            try:
                username = int(username)
                print(('이름에 숫자 혹은 문자를 입력하셨습니다.'))
                continue
            except ValueError:
                return username
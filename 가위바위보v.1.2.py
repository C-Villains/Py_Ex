import random

win = 0
lose = 0
draw = 0

def cls():
    print('\n' * 100)

print('가위바위보 프로그램')




while True:
    
    select = int(input('0.화면 지우기  아무 키나 누르면 시작됩니다. >> '))
    if select == 0 :
        cls()
    else :
        print('{}승 {}무 {}패'.format(win, lose, draw))
        player = int(input('1.가위  2.바위 3. 보 >> '))

        print('가위!')
        print('바위!')
        print('보!')
        if player == 1:
            print('가위를 냈다!')
        elif player == 2:
            print('바위를 냈다!')
        elif player == 3:
            print('보를 냈다!')
        else :
            print('1부터 3까지 숫자를 입력해주세요. 무작위로  냅니다.>> ')
            player = random.randint(1,3)
            if player == 1 :
                print('가위를 냈다!')
            elif player == 2 :
                print('바위를 냈다!')
            elif player == 3 :
                print('보를 냈다!')
                
        print('상대는?')
        cpu = random.randint(1, 3)
        if cpu == 1:
            print('가위')
        elif cpu == 2:
            print('바위')
        elif cpu == 3:
            print('보 ')

        if player == 1 and cpu == 2:
            print('졌습니다!')
            lose += 1
        elif player == 1 and cpu == 3:
            print('이겼습니다!')
            win += 1
        elif player == 2 and cpu == 1:
            print('이겼습니다!')
            win += 1
        elif player == 2 and cpu == 3:
            print('졌습니다')
            lose += 1
        elif player == 3 and cpu == 1:
            print('졌습니다!')
            lose += 1
        elif player == 3 and cpu == 2:
            print('이겼습니다')
            win += 1
        else:
            print('비겼습니다!')
            draw += 1


            





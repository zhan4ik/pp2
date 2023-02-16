list = [1,2,4,0,0,7,5]

def spy_game():
    s = ''.join(str(i) for i in list)
    if s.find('007'):
        print(True)
    else:
        print(False)

spy_game()



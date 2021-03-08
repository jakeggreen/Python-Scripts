game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def game_board(player=0,row=0,column=0,just_display=True):
    print("   1  2  3")
    game[row - 1][column - 1] = player
    for num, row in enumerate(game):
        print(num + 1, row)
    return game

player = input("Player: ")
print(player)

#game = game_board(2,1,0)







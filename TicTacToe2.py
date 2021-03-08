#define what the game looks like
game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def addition():
    test_row = game[1][1:3]
    print(test_row)

#input the details for the start of a game and display the starting layout
def game_board(game, player=0, row=0, column=0):
    print("   1  2  3")
    for num, row in enumerate(game):
        print(num + 1, row)

#input the player
def player_select():
    global player
    player = int(input("Player (1 or 2): "))
    if player == 1 or player == 2:
        row_select()
    elif player != 1 or player != 2:
        print("Please select player 1 or 2...")
        player_select()

#input the row for the player's move
def row_select():
    global row
    row = int(input("Row: "))
    if row <= 3 and row > 0:
        column_select()
    elif row > 3 or row <= 0:
        print("Please select row 1, 2 or 3...")
        row_select()
        
#input the column for the player's move
def column_select():
    global column
    column = int(input("Column: "))
    if column <= 3 and column > 0:
        free_space()
    elif column > 3 or column <= 0:
        print("Please select column 1, 2 or 3...")
        column_select()
   
#handling for a move on an occupied space
def free_space():
    if game[row - 1][column - 1] == 0:
        game[row - 1][column - 1] = player
    elif game[row - 1][column - 1] != 0:
        print("Move already taken, try another move...")
        
#play a game and loop
def new_move():
    game_board(game)
    player_select()
    new_move()

#executable code
new_move()






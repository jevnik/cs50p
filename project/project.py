import pygame
import os
import time


def main():
    global screen
    global board
    global red_chip_path
    global yellow_chip_path
    global round

    script_dir = os.path.dirname(os.path.abspath(__file__))

    os.system('cls')
    round = 0
    board = [
        ['','','','','','','',],
        ['','','','','','','',],
        ['','','','','','','',],
        ['','','','','','','',],
        ['','','','','','','',],
        ['','','','','','','',],
    ]

    print(f"{'WELCOME TO THE GAME OF INLINE 4':>37}")
    print()
    print('Players take turns choosing columns in whitch to place their marker.')
    print('first player to connect 4 in row, column or diagonal, wins!')
    print()
    input('press enter to continue')

    os.system('cls')
    ply_one,ply_two = get_names()
    input('press enter to start')

    pygame.init()

    running = True
    s_w = 697
    s_h = 600
    screen = pygame.display.set_mode((s_w, s_h))
    font = pygame.font.Font(None,50)
    pygame.display.flip()

    board_path = os.path.join(script_dir, 'board2.png')
    board_image = pygame.image.load(board_path)

    red_chip_path = os.path.join(script_dir, 'red.png')
    yellow_chip_path = os.path.join(script_dir, 'yellow.png')


    screen.blit(board_image, (0, 0))
    pygame.display.flip()


    while running:          # MAIN GAME LOOP
        if round % 2 == 0:
            pygame.display.set_caption(f"INLINE 4: {ply_one} (Yellow) is on the move")
        else:
            pygame.display.set_caption(f"INLINE 4: {ply_two} (Red) is on the move")


        if check_win(board): # IF WIN COND IS MET, DISPLAYS WIN MESSAGE AND BREAKS MAIN GAME LOOP
            if round % 2 == 0:
                text = font.render(f"{ply_two} WON THE GAME", True, (255,0,0))
                screen.blit(text,(150,300))
                pygame.display.update()
                time.sleep(3)
            else:
                text = font.render(f"{ply_one} WON THE GAME", True, (255,255,0))
                screen.blit(text,(150,300))
                pygame.display.update()
                time.sleep(3)
            break

        pos = (-1,-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # QUITS IF CLICKED ON X
                running = False

            elif event.type == pygame.MOUSEBUTTONUP: #LISTENS FOR MOUSE CLICK
                pos = pygame.mouse.get_pos()


        round = add_piece(board,drop_piece(pos,board),round)

        os.system('cls')

        pygame.display.flip()

    pygame.quit()

def add_piece(board, choice, round): #ADDS A PIECE TO THE BOARD
    round += 1
    if choice != -1: #  CHOICE -1 IF NONE OF THE COLUMNS ARE SELECTED
        for i in range(len(board)-1,-1,-1):
            if board[i][choice] == '':
                if round % 2 == 0:
                    board[i][choice] = 'R'
                    red_chip = pygame.image.load(red_chip_path)
                    screen.blit(red_chip, (choice*99+15, 20+i*98))
                    break
                else:
                    board[i][choice] = 'Y'
                    yellow_chip = pygame.image.load(yellow_chip_path)
                    screen.blit(yellow_chip, (choice*99+15, 20+i*98))
                    break
        return round
    return round-1 # STAYS IN SAME ROUND WHEN CONDITION IS NOT MET


def check_win(board): #CHECKS IF ANY OF WIN CONDITIONS IS MET. COULD BE OPTIMISED SO IT DOESNT CHECK WHOLE BOARD EVERY TIME
    for i in range(len(board)):
        for j in range(len(board[i])):
            try:
                if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] != '':
                    return True
            except:
                pass

            try:
                if i-1 > 0 and i-2 > 0 and i-3 >= 0: # NEEDED TO CHECK SO THAT ROW OR COLUMN IS NOT A LOOP
                    if board[i][j] == board[i-1][j] == board[i-2][j] == board[i-3][j] != '':
                        return True
            except:
                pass

            try:
                if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] != '':
                    return True
            except:
                pass

            try:
                if j-1 > 0 and j-2 > 0 and j-3 >= 0:
                    if board[i][j] == board[i][j-1] == board[i][j-2] == board[i][j-3] != '':
                        return True
            except:
                pass

            try:
                if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] != '':
                    return True
            except:
                pass

            try:
                if board[i][j] == board[i-1][j-1] == board[i-2][j-2] == board[i-3][j-3] != '':
                    return True
            except:
                pass

            try:
                if i-1 > 0 and i-2 > 0 and i-3 >= 0:
                    if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] != '':
                        return True
            except:
                pass

            try:
                if j-1 > 0 and j-2 > 0 and j-3 >= 0:
                    if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] != '':
                        return True
            except:
                pass

def drop_piece(pos,board):
    choice = -1 # NONE OF COLUMNS MATCH
    match pos: # IF CLICK COORDINATE MATCHES ANY ROW, ADDS PIECE TO THAT ROW IF THERE IS FREE SPACE
        case _ if 0 < pos[0] < 91:
            if board[0][0] == '':
                #round = add_piece(board,choice,round)
                choice = 0


        case _ if 112 < pos[0] < 190:
            if board[0][1] == '':
                choice = 1
                #round = add_piece(board,choice,round)

        case _ if 215 < pos[0] < 287:
            if board[0][2] == '':
                #round = add_piece(board,choice,round)
                choice = 2

        case _ if 310 < pos[0] < 390:
            if board[0][3] == '':
                #round = add_piece(board,choice,round)
                choice = 3

        case _ if 414 < pos[0] < 486:
            if board[0][4] == '':
                #round = add_piece(board,choice,round)
                choice = 4

        case _ if 510 < pos[0] < 584:
            if board[0][5] == '':
                #round = add_piece(board,choice,round)
                choice = 5

        case _ if 610 < pos[0] < 681:
            if board[0][6] == '':
                #round = add_piece(board,choice,round)
                choice = 6

    return choice


def get_names():
    ply_one = input('Name Player One: ')
    ply_two = input('Name Player Two: ')
    return (ply_one,ply_two)

if __name__ == '__main__':
    main()
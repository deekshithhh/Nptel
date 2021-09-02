theBoard={'Top_L':' ','Top_m':' ','Top_r':' ','Mid_L':' ','Mid_m':' ','Mid_r':' ','Low_L':' ','Low_m':' ','Low_r':' '}
def printBoard(board):
    print(board['Top_L']+'|'+board['Top_m']+'|'+board['Top_r'])
    print('-+-+-')
    print(board['Mid_L'] + '|' + board['Mid_m'] + '|' + board['Mid_r'])
    print('-+-+-')
    print(board['Low_L'] + '|' + board['Low_m'] + '|' + board['Low_r'])
    
turn='X'
for i in range(9):
    printBoard(theBoard)
    print("Turn for"+turn+"Move on which space")
    move=input()
    theBoard[move]=turn
    if turn=='X':
        turn='O'
    else:
        turn='X'
printBoard(theBoard)

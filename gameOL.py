board = list(range(1,10))
combination = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
def board_paint():
     print("*************")
     for i in range(3):
          print('*', board[0 + i *3],'*', board[1 + i *3],'*', board[2 + i *3],'*')
     print("*************")
def move(playar_token):
     while True:
          a = input("какой Ваш ход " + playar_token + " ?")
          if not (a in '123456789'):
              print('Такой клетки нет, повнимательней, пожалуйста')
              continue
          a = int(a)
          if str(board[a -1]) in 'XO':
               print('Эта клетка занята, поробуйте еще раз')
               continue
          board[a - 1] = playar_token
          break
def chek():
     for e in combination:
          if board[e[0]-1] == board[e[1]-1] == board[e[2]-1]:
               return board[e[1]-1]
     else:
          return False
def main():
     ch = 0
     while True:
          board_paint()
          if ch % 2 == 0:
               move("X")
          else:
               move("O")
          if ch > 3:
               viktory = chek()
               if viktory:
                    doska_paint()
                    print(viktory, 'ПОБЕДА!!!')
                    break
          ch += 1
          if ch > 8:
               board_paint()
               print('Увы, это ничья.')
               break
main()

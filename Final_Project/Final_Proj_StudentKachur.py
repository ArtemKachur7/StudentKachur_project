from random import randrange

def display_board(board):#Виведення ігрової дошки
    for row in range(7):
        if row % 2 == 0:
            print("+-------" * 3 + "+")
        else:
            for col in range(3):
                print("|", end="")
                print(f"   {board[row // 2][col]}   ", end="")
            print("|")
        if row % 2 == 0 and row != 6:
            print("|       " * 3 + "|")
            print("|       " * 3 + "|")


def enter_move(board): #Введення ходу гравця
    free_fields = make_list_of_free_fields(board)
    while True:
        try:
            move = int(input("Виберіть клітинку (від 1 до 9): "))
            if move in free_fields:
                break
            else:
                print("Вибрана клітинка вже зайнята!Спробуйте знову.")
        except ValueError:
            print("Помилка!Некоректне введення , введіть число.")

    mark_move(board, move, 'O')

def make_list_of_free_fields(board):#Створення списку вільних полів
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free_fields.append(board[row][col])
    return free_fields

def victory_for(board, sign):   # Перевірка перемоги;перевірка рядків та стовпців
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True

    return False

def draw_move(board): #Функція ходу комп'ютера
    free_fields = make_list_of_free_fields(board)
    move = randrange(1, 10)
    while move not in free_fields:
        move = randrange(1, 10)
    mark_move(board, move, 'X')

def mark_move(board, move, sign): #Функція позначення ходу на дошці
    for row in range(3):
        for col in range(3):
            if board[row][col] == move:
                board[row][col] = sign

def when_draw(board): #Варіант коли відбулася нічия
    for row in board: # Перевірка, чи дошка заповнена
        for cell in row:
            if cell not in ['O', 'X']:
                return False
    return True
def play_game(): #Функція самої гри
    board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
    display_board(board)

    for _ in range(4):
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("Ви перемогли!")
            break
        elif when_draw(board):
            print("Нічия!Спробуйте зіграти знову.")
            return play_game()

        draw_move(board)
        display_board(board)

        if victory_for(board, 'X'):
            print("Комп'ютер переміг!")
            break
        elif when_draw(board):
            print("Нічия!Спробуйте зіграти знову.")
            return play_game()


play_game()

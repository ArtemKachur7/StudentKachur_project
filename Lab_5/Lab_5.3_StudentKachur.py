matrix_of_chessboard = [['_'] * 8 for _ in range(8)]# Створюємо матрицю 8x8 з пустими клітинками
# Розставляємо тури по кутках шахівниці:
matrix_of_chessboard[0][0] = 'Т' # Лівий верхній кут
matrix_of_chessboard[0][7] = 'Т(білі)' # Правий верхній кут
matrix_of_chessboard[7][0] = 'Т' # Лівий нижній кут
matrix_of_chessboard[7][7] = 'Т(чорні)' # Правий нижній кут:

for row in matrix_of_chessboard: # Виводимо шахівницю
    print(' '.join(row))

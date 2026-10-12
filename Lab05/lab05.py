matrix = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

players = ["X", "O"]
turns = 0
winner = None

while turns < 9 and winner == None:
    print ("\n Tic Tac Toe")
    for row in matrix:
        print(" | ".join(row))

    player = players[turns % 2]
    print(f"\n{player}'s turn")

    row = input("Enter row (1-3): ")
    column = input("Enter column (1-3): ")

    if not row.isdigit() or not column.isdigit():
        print("Please enter numbers only")
        input("Press Enter to continue.")
        continue

    row = int(row) - 1
    column = int(column) - 1

    if row < 0 or row > 2 or column < 0 or column > 2:
        print("Please enter a row and column between 1 and 3")
        input("Press Enter to continue.")
        continue

    if matrix[row][column] != "-":
        print(f"Someone has already claimed {row + 1}, {column + 1}:")
        input("Press Enter to continue.")
        continue

    matrix[row][column] = player
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == player:
            winner = player
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == player:
            winner = player

    if matrix[0][2] == matrix[1][1] == matrix[2][0] == player:
        winner = player

    if matrix[0][0] == matrix[1][1] == matrix[2][2] == player:
        winner = player

    turns += 1
    
print("\nTic Tac Toe")

for row in matrix:
    print(" | ".join(row))

if winner != None:
    print(f"\n{winner} won!")
else:
    print("\nIt's a draw!")

print("\nGame Over")
print("Thanks for playing!")

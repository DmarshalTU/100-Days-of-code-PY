row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

map_1 = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("Where to put the treasure? ")

col = int(position[0]) - 1
row = int(position[1]) - 1

print(col, row)
map_1[row][col] = "X"
print(f"{row1}\n{row2}\n{row3}\n")

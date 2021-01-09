print('''
*****************************************************
     ____...------------...____
               _.-"` /o/__ ____ __ __  __ \\o\\_`"-._
             .'     / /                    \\ \\     '.
             |=====/o/======================\\o\\=====|
             |____/_/________..____..________\\_\\____|
             /   _/ \\_     <_o#\\__/#o_>     _/ \\_   \\
             \_________\\####/_________/
              |===\\!/========================\\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \\() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \\__     '-.\\uuu/.-'    __/ \\__ |
              |==== .'.'^'.'.====|
              |  _\\o/   __  {.' __  '.} _   _\\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
*****************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

direction = input("Where to go? (L)eft or (R)ight? ").lower()
if direction == "r":
    print("Fall into a hole.\nGame Over.")
else:
    action = input("(S)wim or (W)ait? ").lower()
    if action == "s":
        print("Attacked by trout.\nGame Over.")
    else:
        door = input("(R)ed, (B)lue or (Y)ellow? ")
        if door == "r":
            print("Burned by fire.\nGame Over.")
        elif door == "b":
            print("Eaten by beasts.\nGame Over.")
        elif door == "y":
            print("You win!")
        else:
            print("Game Over.")


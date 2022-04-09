import os, pathlib, time
from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title='Rules and how to play')

# For good user experience
console.print('IT TREASURE HUNT', style='bold cyan', justify='center')
print()
table.add_column(' ', style='magenta')
table.add_column('RULES', style='blue')
table.add_column('IMPORTANT INFO', style='red')

table.add_row("1.", "You cannot view the source code file.", "The passwords may be hidden in the file provided.")
table.add_row("2.", "There are no hints provided, so carefully think with the clues provided to figure out the password for the next level.", "The exe file should be open at all times or else, you would have to restart the whole game.")
table.add_row("3.", "Please do not change any settings of the file explorer.", "Make sure you have read the README file before playing the game.")
table.add_row("4.", "It's a game so enjoy 🙂 ", "To exit, press CTRL+C")
console.print(table)

level = 1

while level <= 10:

    print()
    print(f'LEVEL {level}')

    pwd = input('Type the password here: ')
        
    if level == 1:
        if pwd == 'abcdef':
            console.print("\tCongratulations! You have unlocked level 2 😀")

            path = str(pathlib.Path(__file__).parent.resolve()).rstrip('\\1') #c:\Users\zaidd\Documents\Treasure Hunt\
            os.chdir(path) 
            os.system(f"attrib -h {level + 1}")
            level += 1
        
        else:
            print()
            console.print("Whoops! Wrong password, looks like you'll need to try again 😥")

    elif level == 2:
        if pwd == 'mcbook':
            console.print("\tCongratulations! You have unlocked level 3 😀")

            path = str(pathlib.Path(__file__).parent.resolve()).rstrip('\\1') 
            os.chdir(path) 
            os.system(f"attrib -h {level + 1}")
            level += 1
        else:
            print()
            console.print("Awww maaan 😣 Wrong password, try again")
    
    elif level == 3:
        if pwd == 'random':
            console.print("\tCongratulations! You have unlocked level 4 😀")

            path = str(pathlib.Path(__file__).parent.resolve()).rstrip('\\1') 
            os.chdir(path) 
            os.system(f"attrib -h {level + 1}")
            level += 1
        else:
            print()
            console.print("Wrong password mate 😟 Try again ")
        
    elif level == 4:
        if pwd == 'random2':
            console.print("\tAyy, you're half way there 👍 You have unlocked level 5 😀")

            path = str(pathlib.Path(__file__).parent.resolve()).rstrip('\\1') 
            os.chdir(path) 
            os.system(f"attrib -h {level + 1}")
            level += 1
        else:
            print()
            console.print("Uh oh, wrong one!")

    elif level == 5:
        if pwd == 'random3':
            console.print("\tOn the way to level 6 you go! 😃")

            path = str(pathlib.Path(__file__).parent.resolve()).rstrip('\\1') 
            os.chdir(path) 
            os.system(f"attrib -h {level + 1}")
            level += 1
        else:
            print()
            console.print("Wrong!")

    elif level == 6:
        if pwd == 'random4':
            console.print("\t7 level unlocked! Congo 🎉")

            path = str(pathlib.Path(__file__).parent.resolve()).rstrip('\\1') 
            os.chdir(path) 
            os.system(f"attrib -h {level + 1}")
            level += 1
        else:
            print()
            console.print("My friend, you're wrong 🥺")

    elif level == 7:
        if pwd == 'random5':
            console.print("\tGah damn, 8 level unlocked 😎")

            path = str(pathlib.Path(__file__).parent.resolve()).rstrip('\\1') 
            os.chdir(path) 
            os.system(f"attrib -h {level + 1}")
            level += 1
        else:
            print()
            console.print("Nope, thats incorrect but you got this!!")

    elif level == 8:
        if pwd == 'random6':
            console.print("\tOMG only 1 level left 🤯")
            console.print("\tLEVEL 9 unlocked 😁")

            path = str(pathlib.Path(__file__).parent.resolve()).rstrip('\\1') 
            os.chdir(path) 
            os.system(f"attrib -h {level + 1}")
            level += 1
        else:
            print()
            console.print("Welp, that's incorrect 😶")

    elif level == 9:
        if pwd == 'random7':
            console.print("\tOMG BRUHHH YOU UNLOCKED THE FINAL LEVEL 🎉🎉🎉🎉")

            path = str(pathlib.Path(__file__).parent.resolve()).rstrip('\\1') 
            os.chdir(path) 
            os.system(f"attrib -h {level + 1}")
            level += 1
        else:
            print()
            console.print("C'mon you got this 💪")
    
    elif level == 10:
        if pwd == 'final':
            print()
            console.log('\t\tCONGRATS, you did it 🎉 HERE is a cake for you 🎂')
            level += 1
        else:
            print()
            console.print("Bro you are so close to winning!! ")
    

print()
print()
print('\t\t\tIt was a pleasure to play with you!')
console.log('\t\t\tUntil next time, bye 👋')

time.sleep(7)
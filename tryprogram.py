
try:
    text = open('text.txt')
except FileNotFoundError:
    print('File does not exist')

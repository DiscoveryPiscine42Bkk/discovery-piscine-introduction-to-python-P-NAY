'''Main file - includes both Success and Fail cases''' 
from checkmate import checkmate

def main():
    board = """\
....
.K..
P...
.R.."""
    checkmate(board)

if __name__ == "__main__":
    main()
    
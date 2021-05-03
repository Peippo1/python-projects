import random

# lets create a board object to represent the minesweeper game
# this is so that we can just say "create a new board object", 0r
# "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        # le's keep track of these parameters. they'll be helpful later\
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function!
        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which locations we've uncovered
        # we'll save (row,col) tuples into this set
        self.dug = set() # if we dig at 0, 0, then self.dug = {(0,0)}

    def make_new_board(self):       
        # construct a new board based on the dim size and num bombs
        # we should construct the list of the lists here (or whatever representation you prefer,
        # but since we have a 2-D board, list of lists is most natural) 

        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this creates an array like this:
        # [[None, None, ..., None],
        #  [None, None, ..., None],
        #  [    ,                ],
        #  [None, None, ..., None]]
        # we can see how this represents a board!

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1) # return a random integer N such that a <= N <= b
            row = loc // self.dim_size # we want the number of times dim_size goes into loc to tell us
            col = loc % self.dim_size # we want the remainder to tell us what index in that row to look 

            if board[row] [col] == '*':
                # this means we've actually planted a bomb there already so keep going
                continue
            
            board[row] [col] = '*' # plant the bomb
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        # now that we have the bombs planted, let's assign a number 0-8 for all the empty spaces, which
        # represents how many neighboring bombs there are. we can precompute these and it'll save us some
        # effort checking what's around the board later on :) 
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r] [c] == '*':
                    # if this is already a bomb, we don't want to calculate anything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # lets iterate through each of the neighboring positions and sum number of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        # make sure not to go out of bounds!

        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max (0, col-1), min(self.dim_size - 1, col+1)+1):
                if r in row and c == col:
                    #our original location, don't check
                    continue
                if self.board[r] [c] == '*':
                    num_neighboring_bombs += 1
        
        return num_neighboring_bombs
                    
    

# play the game
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)



    # Step 2: show the user the board and ask for where they want to dig
    # Step 3a: if location is a bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # Step 4: repeat steps 2 & 3a/b until there are no more places to dig -> VICTORY!
    pass
from player import Player


class Board():
    def __init__(self, height, width, players: list[Player]):
        self.height = height
        self.width = width
        self.players = players
        self.turn = self.players[0]
        self.board = [[" "] * self.width for _ in range(self.height)]
        self.colHeight = [self.height - 1] * self.width

    def draw(self):

        # Draw the opening line
        print("╔", end="")

        for _ in range(self.width - 1):
            print("═══╦", end="")
        print("═══╗")

        # Draw the actual cells w/ content

        left, bottom, right = "╠", "═══╬", "═══╣"
        for y in range(self.height):
            # Content
            print("║", end="")
            for x in range(self.width):
                print(f" {self.board[y][x]} ║", end="")
            print()

            if y == self.height - 1:
                left, bottom, right = "╚", "═══╩", "═══╝"

            # Roof for next content
            print(left, end="")
            for x in range(self.width-1):
                print(bottom, end="")
            print(right)

    def changeTurn(self):
        if self.turn == self.players[0]:
            self.turn = self.players[1]
        else:
            self.turn = self.players[0]

    def isColValid(self, curCol):
        if curCol < 0 or curCol >= self.width:
            return False
        if self.colHeight[curCol] < 0:
            return False

        return True

    def putPiece(self, curCol):
        self.board[self.colHeight[curCol]][curCol] = self.turn.symbol

    def verifyVertical(self, curCol):
        if self.height - self.colHeight[curCol] < 4:
            return False
        for i in range(3):
            if self.board[self.colHeight[curCol]+i+1][curCol] != self.turn.symbol:
                return False
        return True

    def verifyHorizontal(self, curCol):
        count = 0
        for i in range(self.width):
            if self.board[self.colHeight[curCol]][i] != self.turn.symbol:
                count = 0
            else:
                count += 1
                if count == 4:
                    return True
        return False

    def verifyDownDBir(self, curCol):
        x = curCol
        y = self.colHeight[curCol]

        if y < x:
            tly, tlx = 0, x-y
        else:
            tly, tlx = y-x, 0

        i = 0
        ct = 0
        while tly + i < self.height and tlx + i < self.width:
            if self.board[tly+i][tlx+i] != self.turn.symbol:
                ct = 0
            else:
                ct += 1
                if ct == 4:
                    return True
            i += 1

        return False

    def verifyUpDBir(self, curCol):
        x = curCol
        y = self.colHeight[curCol]

        if self.height - y - 1 < x:
            tly, tlx = self.height - 1, x - (self.height - y - 1)
        else:
            tly, tlx = y+x, 0

        i = 0
        ct = 0
        while tly - i >= 0 and tlx + i < self.width:
            if self.board[tly-i][tlx+i] != self.turn.symbol:
                ct = 0
            else:
                ct += 1
                if ct == 4:
                    return True
            i += 1

        return False

    def verifyDiagonalBir(self, curCol):
        return self.verifyDownDBir(curCol) or self.verifyUpDBir(curCol)

    def verifyDiagonal(self, curCol):
        ...

    def verifyWin(self, curCol):
        return self.verifyVertical(curCol) or self.verifyHorizontal(curCol) or self.verifyDiagonalBir(curCol)

    def putPieceAndVerify(self, curCol):
        self.putPiece(curCol)
        if self.verifyWin(curCol):
            return True
        self.colHeight[curCol] -= 1
        return False


# board = Board(7, 6, (Player("X"), Player("Y")))
# board.colHeight[2] = 1
# board.isColValid(2)
# board.verifyUpDBir(2)
# board.draw()

class Image:
    def __init__(self, data):
        self.process_image(data)

    HEART = '("## ##"," ### ", " ### ","  #  ", "  #  ")'
    HEART_SMALL = '(""," # # ", " ### ","  #  ", "     ")'
    HAPPY = '("     "," # # ", "#   #"," # # ", "  #  ")'
    SMILE = '("     ","     ", "#   #"," # # ", "  #  ")'
    SAD = ''
    CONFUSED = ''
    ANGRY = ''
    ASLEEP = ''
    SURPRISED = ''
    SILLY = ''
    FABULOUS = ''
    MEH = ''
    YES = ''
    NO = ''
    CLOCK12 = ''
    CLOCK11 = ''
    CLOCK10 = ''
    CLOCK9 = ''
    CLOCK8 = ''
    CLOCK7 = ''
    CLOCK6 = ''
    CLOCK5 = ''
    CLOCK4 = ''
    CLOCK3 = ''
    CLOCK2 = ''
    CLOCK1 = ''
    ARROW_N = ''
    ARROW_NE = ''
    ARROW_E = ''
    ARROW_SE = ''
    ARROW_S = ''
    ARROW_SW = ''
    ARROW_W = ''
    ARROW_NW = ''
    TRIANGLE = '("  #  "," ### ", " ### ","#####", "#####")'
    TRIANGLE_LEFT = ''
    CHESSBOARD = ''
    DIAMOND = ''
    DIAMOND_SMALL = ''
    SQUARE = ''
    SQUARE_SMALL = ''
    RABBIT = ''
    COW = ''
    MUSIC_CROTCHET = ''
    MUSIC_QUAVER = ''
    MUSIC_QUAVERS = ''
    PITCHFORK = '("# # #","#####", "  #  ","  #  ", "  #  ")'
    XMAS = '("  #  "," ### ", " ### ","#####", "  #  ")'
    PACMAN = '(" ### ","#####", "#### ","####", " ### ")'
    TARGET = ''
    TSHIRT = ''
    ROLLERSKATE = ''
    DUCK = ''
    HOUSE = ''
    TORTOISE = ''
    BUTTERFLY = ''
    STICKFIGURE = '("  #  ","#####", "  #  "," # # ", "#   #")'
    GHOST = ''
    SWORD = '("  #  ","  #  ", "# # #","#####", "  #  ")'
    GIRAFFE = ''
    SKULL = ''
    UMBRELLA = ''
    SNAKE = '("#####","# # #", "#####"," ### ", " ### ")'



    def process_image(self, data):
        #todo make this behave more like the actual api
        print(str(data))

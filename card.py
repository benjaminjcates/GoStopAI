from PIL import ImageTk, Image
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
#root.title("Click me!")

img_dir = r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\""
print("balls")

class Card:
    # initialize function
    #def __init__(self, name: str, month: int, category: int):
    def __init__(self, name: str, month: int, category: int, image: Image):
        # Run validations on the received arguments
        # assert month >= 0, f"Month {month} is not greater than zero"
        # assert category >= 0, f"Month {category} is not greater than zero"

        self.name = name
        self.month = month  # 0 is bonus cards, 1~12 are the month
        self.category = category
        self.image = image

    def show_card(self):
        print(self.name)
        print(self.month)
        print(self.category)

    #def load_images(self):
        #img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))


class Month(object):
    JAN = 1
    FEB = 2
    MAR = 3
    APR = 4
    MAY = 5
    JUN = 6
    JUL = 7
    AUG = 8
    SEP = 9
    OCT = 10
    NOV = 11
    DEC = 12
    BMB = 13
    BON = 14


class Category(object):
    BRIGHT = 1
    ANIMAL = 2
    RIBBON = 3
    JUNK = 4
    JUNK_TWO = 5
    SKIP_BOMB = 6
    BONUS_TWO = 7
    BONUS_THREE = 8

#def create_images():
 #   """create all card images as a card_name:image_object dictionary"""
 #   card_list = ALL_CARDS
 #   image_dict = {}
 #   for card in card_list:
 #       # all images have filenames the match the card_list names + extension .gif
 #       image_dict[card] = PhotoImage(file=image_dir+card+".gif")
 #       #print image_dir+card+".gif"  # test
 #   return image_dict

#image_dir = "D:/Python24/Atest/images/Cards_gif/"

#image_dict = create_images()

#root.mainloop()

class Images(object):
    CRANE_GIF = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    PINE_RED_POEM_GIF = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    PINE_ONE_GIF = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    PINE_TWO_GIF = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    BUSH_WARBLER_GIF = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    PLUM_RED_POEM_GIF = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    PLUM_ONE_GIF = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    PLUM_TWO_GIF = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    CURTAIN = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    CHERRY_RED_POEM = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    CHERRY_ONE = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    CHERRY_TWO = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    CUCKOO = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    WISTERIA_RED = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    WISTERIA_ONE = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    WISTERIA_TWO = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    BRIDGE = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    IRIS_RED = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    IRIS_ONE = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    IRIS_TWO = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    BUTTERFLY = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    PEONY_BLUE_POEM = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    PEONY_ONE = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    PEONY_TWO = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    BOAR = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    BUSH_CLOVER_RED = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    BUSH_CLOVER_ONE = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    BUSH_CLOVER_TWO = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    MOON = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    GEESE = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    PAMPAS_GRASS_ONE = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    PAMPAS_GRASS_TWO = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    CUP = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    CHRYSANTHEMUM_BLUE_POEM = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    CHRYSANTHEMUM_ONE = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    CHRYSANTHEMUM_TWO = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    DEER = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    MAPLE_BLUE_POEM = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    MAPLE_ONE = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    MAPLE_TWO = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    PHOENIX = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    PAULOWNIA_ONE = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    PAULOWNIA_TWO = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    PAULOWNIA_DOUBLE = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    RAIN = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    SWALLOW = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    WILLOW_RED = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    WILLOW_DOUBLE = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    BOMB = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    BONUS_TWO = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
    BONUS_THREE = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))


CRANE = Card('Pine and Crane', Month.JAN, Category.BRIGHT, Images.CRANE_GIF)
PINE_RED_POEM = Card('Pine and Red Poem Ribbon', Month.JAN, Category.RIBBON, Images.PINE_RED_POEM_GIF)
PINE_ONE = Card('Pine 1', Month.JAN, Category.JUNK, Images.PINE_RED_POEM_GIF)
PINE_TWO = Card('Pine 2', Month.JAN, Category.JUNK, Images.PINE_RED_POEM_GIF)

BUSH_WARBLER = Card('Plum Blossom and Bush Warbler', Month.FEB, Category.ANIMAL, Images.PINE_RED_POEM_GIF)
PLUM_RED_POEM = Card(u'Plum Blossom and Red Poem Ribbon', Month.FEB, Category.RIBBON, Images.PINE_RED_POEM_GIF)
PLUM_ONE = Card('Plum Blossom 1', Month.FEB, Category.JUNK, Images.PINE_RED_POEM_GIF)
PLUM_TWO = Card('Plum Blossom 2', Month.FEB, Category.JUNK, Images.PINE_RED_POEM_GIF)

CURTAIN = Card('Cherry Blossom and Curtain', Month.MAR, Category.BRIGHT, Images.PINE_RED_POEM_GIF)
CHERRY_RED_POEM = Card('Cherry Blossom and Red Poem Ribbon', Month.MAR, Category.RIBBON, Images.PINE_RED_POEM_GIF)
CHERRY_ONE = Card('Cherry Blossom 1', Month.MAR, Category.JUNK, Images.PINE_RED_POEM_GIF)
CHERRY_TWO = Card('Cherry Blossom 2', Month.MAR, Category.JUNK, Images.PINE_RED_POEM_GIF)

CUCKOO = Card('Wisteria and Cuckoo', Month.APR, Category.ANIMAL, Images.PINE_RED_POEM_GIF)
WISTERIA_RED = Card(u'Wisteria and Red Ribbon', Month.APR, Category.RIBBON, Images.PINE_RED_POEM_GIF)
WISTERIA_ONE = Card('Wisteria 1', Month.APR, Category.JUNK, Images.PINE_RED_POEM_GIF)
WISTERIA_TWO = Card('Wisteria 2', Month.APR, Category.JUNK, Images.PINE_RED_POEM_GIF)

BRIDGE = Card('Iris and Bridge', Month.MAY, Category.ANIMAL, Images.PINE_RED_POEM_GIF)
IRIS_RED = Card(u'Iris and Red Ribbon', Month.MAY, Category.RIBBON, Images.PINE_RED_POEM_GIF)
IRIS_ONE = Card('Iris 1', Month.MAY, Category.JUNK, Images.PINE_RED_POEM_GIF)
IRIS_TWO = Card('Iris 2', Month.MAY, Category.JUNK, Images.PINE_RED_POEM_GIF)

BUTTERFLY = Card('Peony and Butterfly', Month.JUN, Category.ANIMAL, Images.PINE_RED_POEM_GIF)
PEONY_BLUE_POEM = Card('Peony and Blue Poem Ribbon', Month.JUN, Category.RIBBON, Images.PINE_RED_POEM_GIF)
PEONY_ONE = Card('Peony 1', Month.JUN, Category.JUNK, Images.PINE_RED_POEM_GIF)
PEONY_TWO = Card('Peony 2', Month.JUN, Category.JUNK, Images.PINE_RED_POEM_GIF)

BOAR = Card('Bush Clover and Boar', Month.JUL, Category.ANIMAL, Images.PINE_RED_POEM_GIF)
BUSH_CLOVER_RED = Card('Bush Clover and Red Ribbon', Month.JUL, Category.RIBBON, Images.PINE_RED_POEM_GIF)
BUSH_CLOVER_ONE = Card('Bush Clover 1', Month.JUL, Category.JUNK, Images.PINE_RED_POEM_GIF)
BUSH_CLOVER_TWO = Card('Bush Clover 2', Month.JUL, Category.JUNK, Images.PINE_RED_POEM_GIF)

MOON = Card('Pampas Grass and Moon', Month.AUG, Category.BRIGHT, Images.PINE_RED_POEM_GIF)
GEESE = Card('Pampas Grass and Geese', Month.AUG, Category.ANIMAL, Images.PINE_RED_POEM_GIF)
PAMPAS_GRASS_ONE = Card('Pampas Grass 1', Month.AUG, Category.JUNK, Images.PINE_RED_POEM_GIF)
PAMPAS_GRASS_TWO = Card('Pampas Grass 2', Month.AUG, Category.JUNK, Images.PINE_RED_POEM_GIF)

# CUP = Card('Chrysanthemum and Cup', Month.SEP, (Category.ANIMAL, Category.JUNK_TWO))
CUP = Card('Chrysanthemum and Cup', Month.SEP, Category.JUNK_TWO, Images.PINE_RED_POEM_GIF)
CHRYSANTHEMUM_BLUE_POEM = Card('Chrysanthemum and Blue Poem Ribbon', Month.SEP, Category.RIBBON, Images.PINE_RED_POEM_GIF)
CHRYSANTHEMUM_ONE = Card('Chrysanthemum 1', Month.SEP, Category.JUNK, Images.PINE_RED_POEM_GIF)
CHRYSANTHEMUM_TWO = Card('Chrysanthemum 2', Month.SEP, Category.JUNK, Images.PINE_RED_POEM_GIF)

DEER = Card('Maple and Deer', Month.OCT, Category.ANIMAL, Images.PINE_RED_POEM_GIF)
MAPLE_BLUE_POEM = Card('Maple and Blue Poem Ribbon', Month.OCT, Category.RIBBON, Images.PINE_RED_POEM_GIF)
MAPLE_ONE = Card('Maple 1', Month.OCT, Category.JUNK, Images.PINE_RED_POEM_GIF)
MAPLE_TWO = Card('Maple 2', Month.OCT, Category.JUNK, Images.PINE_RED_POEM_GIF)

PHOENIX = Card('Paulownia and Phoenix', Month.NOV, Category.BRIGHT, Images.PINE_RED_POEM_GIF)
PAULOWNIA_ONE = Card('Paulownia 1', Month.NOV, Category.JUNK, Images.PINE_RED_POEM_GIF)
PAULOWNIA_TWO = Card('Paulownia 2', Month.NOV, Category.JUNK, Images.PINE_RED_POEM_GIF)
PAULOWNIA_DOUBLE = Card(u'Paulownia Double', Month.NOV, Category.JUNK_TWO, Images.PINE_RED_POEM_GIF)

RAIN = Card('Willow and Rain', Month.DEC, Category.BRIGHT, Images.PINE_RED_POEM_GIF)
SWALLOW = Card('Willow and Swallow', Month.DEC, Category.ANIMAL, Images.PINE_RED_POEM_GIF)
WILLOW_RED = Card('Willow and Red Ribbon', Month.DEC, Category.RIBBON, Images.PINE_RED_POEM_GIF)
WILLOW_DOUBLE = Card('Willow Double', Month.DEC, Category.JUNK_TWO, Images.PINE_RED_POEM_GIF)

BOMB = Card('Bomb', Month.BMB, Category.SKIP_BOMB, Images.PINE_RED_POEM_GIF)

BONUS_TWO = Card('Bonus Two', Month.BON, Category.BONUS_TWO, Images.PINE_RED_POEM_GIF)
BONUS_THREE = Card('Bonus Three', Month.BON, Category.BONUS_THREE, Images.PINE_RED_POEM_GIF)

ALL_CARDS = (
    CRANE, PINE_RED_POEM, PINE_ONE, PINE_TWO,
    BUSH_WARBLER, PLUM_RED_POEM, PLUM_ONE, PLUM_TWO,
    CURTAIN, CHERRY_RED_POEM, CHERRY_ONE, CHERRY_TWO,
    CUCKOO, WISTERIA_RED, WISTERIA_ONE, WISTERIA_TWO,
    BRIDGE, IRIS_RED, IRIS_ONE, IRIS_TWO,
    BUTTERFLY, PEONY_BLUE_POEM, PEONY_ONE, PEONY_TWO,
    BOAR, BUSH_CLOVER_RED, BUSH_CLOVER_ONE, BUSH_CLOVER_TWO,
    MOON, GEESE, PAMPAS_GRASS_ONE, PAMPAS_GRASS_TWO,
    CUP, CHRYSANTHEMUM_BLUE_POEM, CHRYSANTHEMUM_ONE, CHRYSANTHEMUM_TWO,
    DEER, MAPLE_BLUE_POEM, MAPLE_ONE, MAPLE_TWO,
    PHOENIX, PAULOWNIA_DOUBLE, PAULOWNIA_ONE, PAULOWNIA_TWO,
    RAIN, SWALLOW, WILLOW_RED, WILLOW_DOUBLE,
    BONUS_TWO, BONUS_THREE
)


# Define the geometry of the window
root.geometry("700x500")

frame = Frame(root, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
#img = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
#img = ImageTk.PhotoImage(Image.open(r"C:\Users\GIGABYTE\PycharmProjects\GoStopAI\card_gif\CRANE.gif"))
#img = ImageTk.PhotoImage(Image.open(CRANE.image)
#img = CRANE.image

# Create a Label Widget to display the text or Image
button = Button(frame, image=CRANE.image)
button.pack()
button.mainloop()
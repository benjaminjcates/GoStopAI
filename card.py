class Card:
    # initialize function
    def __init__(self, name, month, category):
        self.name = name
        self.month = month  #0 is bonus cards, 1~12 are the month
        self.category = category

    def show_card(self):
        print(self.month)
        print(self.category)


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


class Category(object):
    BRIGHT = 1
    ANIMAL = 2
    RIBBON = 3
    JUNK = 4
    JUNK_TWO = 5


CRANE = Card('Pine and Crane', Month.JAN, Category.BRIGHT)
PINE_RED_POEM = Card('Pine and Red Poem Ribbon', Month.JAN, Category.RIBBON)
PINE = Card('Pine', Month.JAN, Category.JUNK)

BUSH_WARBLER = Card('Plum Blossom and Bush Warbler', Month.FEB, Category.ANIMAL)
PLUM_RED_POEM = Card(u'Plum Blossom and Red Poem Ribbon', Month.FEB, Category.RIBBON)
PLUM = Card('Plum Blossom', Month.FEB, Category.JUNK)

CURTAIN = Card('Cherry Blossom and Curtain', Month.MAR, Category.BRIGHT)
CHERRY_RED_POEM = Card('Cherry Blossom and Red Poem Ribbon', Month.MAR, Category.RIBBON)
CHERRY = Card('Cherry Blossom', Month.MAR, Category.JUNK)

CUCKOO = Card('Wisteria and Cuckoo', Month.APR, Category.ANIMAL)
WISTERIA_RED = Card(u'Wisteria and Red Ribbon', Month.APR, Category.RIBBON)
WISTERIA = Card('Wisteria', Month.APR, Category.JUNK)

BRIDGE = Card('Iris and Bridge', Month.MAY, Category.ANIMAL)
IRIS_RED = Card(u'Iris and Red Ribbon', Month.MAY, Category.RIBBON)
IRIS = Card('Iris', Month.MAY, Category.JUNK)

BUTTERFLY = Card('Peony and Butterfly', Month.JUN, Category.ANIMAL)
PEONY_BLUE_POEM = Card('Peony and Blue Poem Ribbon', Month.JUN, Category.RIBBON)
PEONY = Card('Peony', Month.JUN, Category.JUNK)

BOAR = Card('Bush Clover and Boar', Month.JUL, Category.ANIMAL)
BUSH_CLOVER_RED = Card('Bush Clover and Red Ribbon', Month.JUL, Category.RIBBON)
BUSH_CLOVER = Card('Bush Clover', Month.JUL, Category.JUNK)

MOON = Card('Pampas Grass and Moon', Month.AUG, Category.BRIGHT)
GEESE = Card('Pampas Grass and Geese', Month.AUG, Category.ANIMAL)
PAMPAS_GRASS = Card('Pampas Grass', Month.AUG, Category.JUNK)

CUP = Card('Chrysanthemum and Cup', Month.SEP, (Category.ANIMAL, Category.JUNK_TWO))
CHRYSANTHEMUM_BLUE_POEM = Card('Chrysanthemum and Blue Poem Ribbon', Month.SEP, Category.RIBBON)
CHRYSANTHEMUM = Card('Chrysanthemum', Month.SEP, Category.JUNK)

DEER = Card('Maple and Deer', Month.OCT, Category.ANIMAL)
MAPLE_BLUE_POEM = Card('Maple and Blue Poem Ribbon', Month.OCT, Category.RIBBON)
MAPLE = Card('Maple', Month.OCT, Category.JUNK)

PHOENIX = Card('Paulownia and Phoenix', Month.NOV, Category.BRIGHT)
PAULOWNIA = Card('Paulownia', Month.NOV, Category.JUNK)
PAULOWNIA_TWO = Card(u'Paulownia 2', Month.NOV, Category.JUNK_TWO)

RAIN = Card('Willow and Rain', Month.DEC, Category.BRIGHT)
SWALLOW = Card('Willow and Swallow', Month.DEC, Category.ANIMAL)
WILLOW_RED = Card('Willow and Red Ribbon', Month.DEC, Category.RIBBON)
WILLOW_TWO = Card('Willow', Month.DEC, Category.JUNK_TWO)


ALL_CARDS = (
    CRANE, PINE_RED_POEM, PINE, PINE,
    BUSH_WARBLER, PLUM_RED_POEM, PLUM, PLUM,
    CURTAIN, CHERRY_RED_POEM, CHERRY, CHERRY,
    CUCKOO, WISTERIA_RED, WISTERIA, WISTERIA,
    BRIDGE, IRIS_RED, IRIS, IRIS,
    BUTTERFLY, PEONY_BLUE_POEM, PEONY, PEONY,
    BOAR, BUSH_CLOVER_RED, BUSH_CLOVER, BUSH_CLOVER,
    MOON, GEESE, PAMPAS_GRASS, PAMPAS_GRASS,
    CUP, CHRYSANTHEMUM_BLUE_POEM, CHRYSANTHEMUM, CHRYSANTHEMUM,
    DEER, MAPLE_BLUE_POEM, MAPLE, MAPLE,
    PHOENIX, PAULOWNIA_TWO, PAULOWNIA, PAULOWNIA,
    RAIN, SWALLOW, WILLOW_RED, WILLOW_TWO
)
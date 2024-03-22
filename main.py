from typing import List, Dict, Any, Tuple
import pyxel


class C:
    BLACK = 0
    DARKBLUE = 1
    PURPLE = 2
    GREEN = 3
    BROWN = 4
    BLUE = 5
    LIGHTBLUE = 6
    WHITE = 7
    PINK = 8
    ORANGE = 9
    YELLO = 10
    LIGHTGREEN = 11
    MEDIUMBLUE = 12
    GRAY = 13
    SALMON = 14
    BEGE = 15


SPRITE = Tuple[int, int, int, int, int]


def sprite(tile_x, tile_y, img=0, size=16, null_color=C.DARKBLUE) -> SPRITE:
    return (img, tile_x * size, tile_y * size, size, size, null_color)


class Sprite:
    TREE = sprite(0, 1, img=2)
    HOUSE = sprite(1, 2, img=2)
    TOWER = sprite(2, 0, img=2)

    # colunm 1
    BLANK = sprite(0, 0)
    FARM = sprite(0, 2)
    ANVIL = sprite(0, 3)
    # colunm 2
    WALL = sprite(1, 0)

    TEST = sprite(2, 1, img=2)


HOUSES = [Sprite.HOUSE, Sprite.WALL, Sprite.FARM, Sprite.ANVIL, Sprite.TOWER]
HOUSES = []
for x in range(10):
    for y in range(10):
        HOUSES.append((2, x * 16, y * 16, 16, 16, C.DARKBLUE))

ENTITY = Dict[str, Any]
VEC2 = Tuple[int, int]

WIDTH = 320
HEIGHT = 240

N_BOX = 50


def new(pos: VEC2 = (0, 0), size: VEC2 = (10, 10), color: int = 9) -> ENTITY:
    entity = {"pos": pos, "size": size, "color": color}
    return entity


def move_rand(ent: ENTITY) -> None:
    x = ent["pos"][0] + pyxel.rndi(-1, 1)
    y = ent["pos"][1] + pyxel.rndi(-1, 1)
    ent["pos"] = x, y


def collision(entity1, entity2):
    # Get the center positions and half sizes of the entities
    entity1_pos = entity1["pos"]
    entity1_half_w, entity1_half_h = entity1["size"][0] / 2, entity1["size"][1] / 2
    entity2_pos = entity2["pos"]
    entity2_half_w, entity2_half_h = entity2["size"][0] / 2, entity2["size"][1] / 2

    return (
        abs(entity1_pos[0] - entity2_pos[0]) < entity1_half_w + entity2_half_w
        and abs(entity1_pos[1] - entity2_pos[1]) < entity1_half_h + entity2_half_h
    )


class Screen:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="My Pyxel Game", fps=60, display_scale=3)
        self.load_assets()  # Load assets before starting the game loop
        pyxel.mouse(True)

        self.entities: Dict[str, List[ENTITY]] = dict()
        self.map: Dict[Tuple[int, int], Any] = dict()

        self.house_n = 0

        pyxel.run(self.update, self.draw)  # Start the game loop

    # Load your image and sound assets (optional)
    def load_assets(self):
        # Use pyxel.img(x) and pyxel.sound(x) to load images and sounds
        pyxel.load("src.pyxres")
        # pyxel.images[2].load(0, 0, "my_image.png")
        pyxel.images[2].load(0, 0, "imgs/c1.png")
        # pyxel.sound(0).set("my_sound.wav", loop=True)
        pass

    def mouse(self):
        self.house_n += pyxel.mouse_wheel
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            x = pyxel.mouse_x // 16
            y = pyxel.mouse_y // 16
            i = self.house_n % len(HOUSES)
            self.map[(x, y)] = HOUSES[i]

    def keyboard(self, player: ENTITY):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_T):
            new_enemy = new(pos=(pyxel.mouse_x, pyxel.mouse_y), color=C.WHITE)
            self.entities["enemy"].append(new_enemy)

        x, y = player["pos"]
        if pyxel.btn(pyxel.KEY_UP):
            y -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            y += 1
        if pyxel.btn(pyxel.KEY_LEFT):
            x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            x += 1
        player["pos"] = x, y

    def update(self):
        self.mouse()

    def draw(self):
        pyxel.cls(C.BLACK)

        m_x = pyxel.mouse_x // 16
        m_y = pyxel.mouse_y // 16
        colors = [C.WHITE, C.GREEN, C.PURPLE, C.MEDIUMBLUE, C.ORANGE]
        BOX_SIZE = 16

        for pos, sprite in self.map.items():
            pyxel.blt(pos[0] * BOX_SIZE, pos[1] * BOX_SIZE, *sprite)

        i = pyxel.frame_count % len(colors)
        ii = self.house_n % len(HOUSES)

        pyxel.rectb(m_x * 16, m_y * 16, BOX_SIZE, BOX_SIZE, colors[i])
        pyxel.blt(m_x * 16, m_y * 16, *HOUSES[ii])

        mouse_tile = (
            f"{pyxel.mouse_x // 16}\n{pyxel.mouse_y // 16}\n{pyxel.mouse_wheel}"
        )
        pyxel.text(0, 0, mouse_tile, C.PINK)
        pyxel.blt(100, 100, *Sprite.TOWER)
        pyxel.rectb(100, 100, BOX_SIZE, BOX_SIZE, colors[i])


if __name__ == "__main__":
    Screen()

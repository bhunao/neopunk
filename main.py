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


ENTITY = Dict[str, Any]
VEC2 = Tuple[int, int]

WIDTH = 600
HEIGHT = 400

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
    entity1_half_w, entity1_half_h = entity1["size"][0] / \
        2, entity1["size"][1] / 2
    entity2_pos = entity2["pos"]
    entity2_half_w, entity2_half_h = entity2["size"][0] / \
        2, entity2["size"][1] / 2

    return (
        abs(entity1_pos[0] - entity2_pos[0]) < entity1_half_w + entity2_half_w
        and abs(entity1_pos[1] - entity2_pos[1]) < entity1_half_h + entity2_half_h
    )


class Screen:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="My Pyxel Game", fps=60)
        self.load_assets()  # Load assets before starting the game loop
        pyxel.mouse(True)

        self.entities: Dict[str, List[ENTITY]] = dict()
        self.entities["player"] = [new(color=C.WHITE)]

        self.entities["enemy"] = []
        # for _ in range(35):
        #     x = pyxel.rndi(0, WIDTH)
        #     y = pyxel.rndi(0, HEIGHT)
        #     entity = new(pos=(x, y), color=C.PINK)
        #     self.entities["enemy"].append(entity)

        self.entities["pink"] = []
        for _ in range(N_BOX):
            x = pyxel.rndi(0, WIDTH)
            y = pyxel.rndi(0, HEIGHT)
            entity = new(pos=(x, y), color=C.PINK)
            self.entities["pink"].append(entity)

        self.entities["blue"] = []
        for _ in range(N_BOX):
            x = pyxel.rndi(0, WIDTH)
            y = pyxel.rndi(0, HEIGHT)
            entity = new(pos=(x, y), color=C.BLUE)
            self.entities["blue"].append(entity)

        self.entities["green"] = []
        for _ in range(N_BOX):
            x = pyxel.rndi(0, WIDTH)
            y = pyxel.rndi(0, HEIGHT)
            entity = new(pos=(x, y), color=C.GREEN)
            self.entities["green"].append(entity)

        pyxel.run(self.update, self.draw)  # Start the game loop

    # Load your image and sound assets (optional)
    def load_assets(self):
        # Use pyxel.img(x) and pyxel.sound(x) to load images and sounds
        # For example:
        pyxel.images[0].load(0, 0, "my_image.png")
        # pyxel.sound(0).set("my_sound.wav", loop=True)
        pass

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
        player = self.entities["player"][0]
        self.keyboard(player)

        for entity in self.entities["pink"]:
            for entity2 in self.entities["green"]:
                if collision(entity, entity2):
                    entity2["color"] = C.PINK

        for entity in self.entities["green"]:
            for entity2 in self.entities["blue"]:
                if collision(entity, entity2):
                    entity2["color"] = C.GREEN

        for entity in self.entities["blue"]:
            for entity2 in self.entities["pink"]:
                if collision(entity, entity2):
                    entity2["color"] = C.BLUE

    def draw(self):
        pyxel.cls(C.DARKBLUE)

        player = self.entities["player"][0]
        x, y = player["pos"]
        w, h = player["size"]
        color = player["color"]

        pyxel.rect(x, y, w, h, color)

        for name in ("pink", "green", "blue"):
            for entity in self.entities[name]:
                move_rand(entity)
                x, y = entity["pos"]
                w, h = entity["size"]
                color = entity["color"]
                pyxel.rect(x, y, w, h, color)
                # if collision(entity, player):
                #     entity["color"] = C.ORANGE

        pyxel.bltm(0, 0, 0, 8, 8, 8, 8, 3)
        pyxel.text(100, 20, str(len(self.entities["pink"])), C.PINK)
        pyxel.text(100, 25, str(len(self.entities["green"])), C.GREEN)
        pyxel.text(100, 30, str(len(self.entities["blue"])), C.BLUE)


if __name__ == "__main__":
    Screen()

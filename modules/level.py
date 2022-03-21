import pygame, os, random
from modules import tile as t

class Level():
    def __init__(self, game, level):
        self.game = game
        self.level = level
        self.level_complete = False
        self.all_cards = [f for f in os.listdir('pics/cards') if os.path.join('pics/cards', f)]

        self.img_width, self.img_height = (64, 64)
        self.padding = 20
        self.margin_top = 160
        # self.cols = 3
        # self.rows = 4
        self.width = 800

        self.tiles_group = pygame.sprite.Group()

        self.flipped = []
        self.frame_count = 0
        self.block_game = False

        self.generate_level(self.level)

    def update(self, event_list):
        self.check_level_complete(event_list)
        self.draw()

    def check_level_complete(self, event_list):
        if not self.block_game:
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for tile in self.tiles_group:
                        if tile.rect.collidepoint(pygame.mouse.get_pos()):
                            self.flipped.append(tile.name)
                            tile.show()
                            if len(self.flipped) == 2:
                                if self.flipped[0] != self.flipped[1]:
                                    self.block_game = True
                                else:
                                    self.flipped = []
                                    for tile in self.tiles_group:
                                        if tile.shown:
                                            self.level_complete = True
                                        else:
                                            self.level_complete = False
                                            break
        else:
            self.frame_count += 1
            if self.frame_count == self.game.fps:
                self.frame_count = 0
                self.block_game = False

                for tile in self.tiles_group:
                    if tile.name in self.flipped:
                        tile.hide()
                self.flipped = []

    def generate_level(self, level):
        self.level_complete = False
        self.rows = 4
        self.cols = self.level + 2
        self.cards = self.select_random_cards(self.level)
        self.generate_tileset(self.cards)

    def select_random_cards(self, level):
        cards = random.sample(self.all_cards, ((self.rows*self.cols)//2))
        cards_copy = cards.copy()
        cards.extend(cards_copy)
        random.shuffle(cards)
        return cards

    def generate_tileset(self, cards):
        self.cols = self.rows = self.cols if self.cols >= self.rows else self.rows

        TILES_WIDTH = (self.img_width * self.cols + self.padding * 3)
        LEFT_MARING = (self.width - TILES_WIDTH) // 2
        self.tiles_group.empty()

        for i in range(len(cards)):
            x = LEFT_MARING + ((self.img_width + self.padding) * (i % self.cols))
            y = self.margin_top + (i // self.rows * (self.img_height + self.padding))
            tile = t.Tile(cards[i], x, y)
            self.tiles_group.add(tile)

    def draw(self):
        self.tiles_group.draw(self.game.display)
        self.tiles_group.update()

        if self.level_complete:
            self.game.draw_text('Congratulations!', 64, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 1.2)

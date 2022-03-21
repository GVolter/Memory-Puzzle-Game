import pygame
from modules import tile as t
from modules import level as l
from modules import menu as m

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.fps = 30
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.caption = pygame.display.set_caption('MEMO.it')
        self.icon = pygame.display.set_icon(pygame.image.load('pics/logo.png'))
        self.font_name = 'fonts/Minecraft.ttf'
        self.BLACK, self.WHITE, self.PASTELBLUE = (0, 0, 0), (255, 255, 255), (174, 198, 207)
        self.main_menu = m.MainMenu(self)
        self.difficulty = m.DifficultyMenu(self)
        self.tile = t.Tile('cloud.png', 200, 200)
        self.lvl = self.difficulty.lvl
        self.level = l.Level(self, self.lvl)
        self.curr_menu = self.main_menu
        self.clock = pygame.time.Clock()

    def game_loop(self):
        while self.playing:
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.PASTELBLUE)
            # self.tile.draw()
            # self.level.draw()
            self.level.update(self.check_events())
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()
            self.clock.tick(self.fps)



    def check_events(self):
        self.event_list = pygame.event.get()
        for event in self.event_list:
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
        return self.event_list


    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
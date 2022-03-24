import pygame
from modules import tile as t
from modules import level as l
from modules import menu as m

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing_easy, self.playing_medium, self.playing_hard = True,  False, False, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        self.fps = 30
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.caption = pygame.display.set_caption('MEMO.it')
        self.icon = pygame.display.set_icon(pygame.image.load('pics/logo.png'))
        self.font_name = 'fonts/Minecraft.ttf'
        self.BLACK, self.WHITE, self.PASTELBLUE = (0, 0, 0), (255, 255, 255), (174, 198, 207)
        self.main_menu = m.MainMenu(self)
        self.difficultyMenu = m.DifficultyMenu(self)
        self.endMenu = m.EndMenu(self)
        self.easyLevel = l.Level(self, 1)
        self.mediumLevel = l.Level(self, 2)
        self.hardLevel = l.Level(self, 3)
        self.curr_menu = self.main_menu
        self.clock = pygame.time.Clock()

    def game_loop(self):
        while self.playing_easy:
            if self.START_KEY:
                self.playing_easy = False
            self.display.fill(self.PASTELBLUE)
            self.easyLevel.update(self.check_events())
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()
            self.clock.tick(self.fps)

        while self.playing_medium:
            if self.START_KEY:
                self.playing_medium = False
            self.display.fill(self.PASTELBLUE)
            self.mediumLevel.update(self.check_events())
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()
            self.clock.tick(self.fps)
        
        while self.playing_hard:
            if self.START_KEY:
                self.playing_hard = False
            self.display.fill(self.PASTELBLUE)
            self.hardLevel.update(self.check_events())
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()
            self.clock.tick(self.fps)


    def check_events(self):
        self.event_list = pygame.event.get()
        for event in self.event_list:
            if event.type == pygame.QUIT:
                self.running, self.playing_easy, self.playing_hard, self.playing_medium = False, False, False, False
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
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
        return self.event_list


    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
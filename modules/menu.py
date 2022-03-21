import pygame, sys

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 150

    def draw_cursor(self):
        self.game.draw_text('*', 40, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.exitx, self.exity = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.PASTELBLUE)
            self.game.draw_text('MEMO.it', 128, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 - 20)
            self.game.draw_text("Start Game", 40, self.startx, self.starty)
            self.game.draw_text("Exit", 40, self.exitx, self.exity)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.curr_menu = self.game.difficulty
            elif self.state == 'Exit':
                pygame.quit()
                sys.exit()
            self.run_display = False

class DifficultyMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.lvl = 1
        self.state = 'Easy'
        self.easyx, self.easyy = self.mid_w, self.mid_h + 20
        self.mediumx, self.mediumy = self.mid_w, self.mid_h + 60
        self.hardx, self.hardy = self.mid_w, self.mid_h + 100
        self.backx, self.backy = self.mid_w, self.mid_h + 140
        self.cursor_rect.midtop = (self.easyx + self.offset, self.easyy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.PASTELBLUE)
            self.game.draw_text('Difficulty:', 64, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 60)
            self.game.draw_text("Easy", 40, self.easyx, self.easyy)
            self.game.draw_text("Medium", 40, self.mediumx, self.mediumy)
            self.game.draw_text("Hard", 40, self.hardx, self.hardy)
            self.game.draw_text("Back", 40, self.backx, self.backy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.DOWN_KEY:
            if self.state == 'Easy':
                self.state = 'Medium'
                self.cursor_rect.midtop = (self.mediumx + self.offset, self.mediumy)
            elif self.state == 'Medium':
                self.state = 'Hard'
                self.cursor_rect.midtop = (self.hardx + self.offset, self.hardy)
            elif self.state == 'Hard':
                self.state = 'Back'
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy)
            elif self.state == 'Back':
                self.state = 'Easy'
                self.cursor_rect.midtop = (self.easyx + self.offset, self.easyy)
        elif self.game.UP_KEY:
            if self.state == 'Easy':
                self.state = 'Back'
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy)
            elif self.state == 'Medium':
                self.state = 'Easy'
                self.cursor_rect.midtop = (self.easyx + self.offset, self.easyy)
            elif self.state == 'Hard':
                self.state = 'Medium'
                self.cursor_rect.midtop = (self.mediumx + self.offset, self.mediumy)
            elif self.state == 'Back':
                self.state = 'Hard'
                self.cursor_rect.midtop = (self.hardx + self.offset, self.hardy)
        elif self.game.START_KEY:
            # TO-DO: Create different levels
            if self.state == 'Back':
                self.game.curr_menu = self.game.main_menu
            if self.state == 'Easy':
                self.lvl=1
                self.game.playing = True
            if self.state == 'Medium':
                self.lvl=2
                self.game.playing = True
            if self.state == 'Hard':
                self.lvl=3
                self.game.playing = True
            self.run_display = False








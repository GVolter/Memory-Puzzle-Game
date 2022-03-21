from modules import game as g

game = g.Game()

while game.running:
    game.curr_menu.display_menu()
    game.game_loop()
def on_button_pressed_a():
    global tempo
    if sprite.get(LedSpriteProperty.X) == 2:
        game.add_score(1)
        tempo = tempo - game.score()
    else:
        game.game_over()
input.on_button_pressed(Button.A, on_button_pressed_a)

tempo = 0
sprite: game.LedSprite = None
sprite = game.create_sprite(2, 2)
tempo = 1000

def on_forever():
    sprite.move(1)
    basic.pause(tempo)
    sprite.if_on_edge_bounce()
basic.forever(on_forever)

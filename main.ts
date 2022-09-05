input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (sprite.get(LedSpriteProperty.X) == 2) {
        game.addScore(1)
        tempo = tempo - game.score()
    } else {
        game.gameOver()
    }
    
})
let tempo = 0
let sprite : game.LedSprite = null
sprite = game.createSprite(2, 2)
tempo = 1000
basic.forever(function on_forever() {
    sprite.move(1)
    basic.pause(tempo)
    sprite.ifOnEdgeBounce()
})

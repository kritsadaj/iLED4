input.onButtonPressed(Button.A, function () {
    ht16k33.ShowDot(2, true)
})
input.onButtonPressed(Button.B, function () {
    ht16k33.ShowDot(2, false)
})
ht16k33.init_()
ht16k33.ShowHexNumber(36554)

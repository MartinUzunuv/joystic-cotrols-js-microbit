function fill(x: any, y: any) {
    led.plot(x, y);
}
function mapToPi(value: any) {
    return (value / 1030) * Math.PI;
}
let interval = 10
basic.forever(function () {
    basic.clearScreen()
    let y = mapToPi(pins.analogReadPin(AnalogPin.P2))
let x = mapToPi(pins.analogReadPin(AnalogPin.P1))
for(let l = 0; l < 2; l += 0.2){
        fill(2 - Math.round(Math.cos(x) * l),
             2 + Math.round(Math.sin(y*2) * l))
    }
basic.pause(interval)
})

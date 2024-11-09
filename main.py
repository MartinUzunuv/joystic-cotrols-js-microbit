def on_pin_pressed_p0():
    global centerY
    centerY += 0 - 1
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global centerX
    centerX += 0 - 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    global speed
    speed = 0 - speed
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    global centerX
    centerX += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    global centerY
    centerY += 1
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

speed = 0
chA = 0
def fill(x: any, y: any):
    led.plot(x, y)
interval = 10
r = 0.5
dencity = 0.1
length = Math.PI * 8
centerX = 2
centerY = 2
speed = -0.2

def on_forever():
    global chA
    basic.clear_screen()
    a = 0
    while a < length:
        fill(Math.round(centerX + Math.cos(a + chA) * a * r),
            Math.round(centerY + Math.sin(a + chA) * a * r))
        a += Math.PI * dencity
    chA += speed
    basic.pause(interval)
basic.forever(on_forever)

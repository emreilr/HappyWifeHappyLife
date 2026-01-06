import turtle
import time
import random
import math

# --- Ekran ayarı ---
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("skyblue")
screen.title("Süslü Papatya")
screen.tracer(0, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def draw_petal(radius, angle, color="white"):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.left(180 - angle)
    t.end_fill()

def draw_leaf(x, y, angle=0, size=80):
    t.up()
    t.goto(x, y)
    t.setheading(angle)
    t.down()
    t.fillcolor("forestgreen")
    t.pencolor("forestgreen")
    t.begin_fill()
    draw_petal(size/2, 60, color="forestgreen")
    t.end_fill()

def draw_stem(start_y, length):
    """Dal hafif kıvrımlı olsun"""
    t.up()
    t.goto(0, start_y)      # dal göbeğin altından başlasın
    t.setheading(-90)
    t.pensize(10)
    t.pencolor("forestgreen")
    t.down()
    for _ in range(length//20):
        t.setheading(-90 + random.randint(-10, 10))  # küçük kıvrımlar
        t.forward(20)

def draw_daisy(scale=1.0, rotation=0):
    t.clear()

    # --- Çiçek yaprakları (dönen kısım) ---
    t.up()
    t.goto(0, 0)
    t.setheading(rotation)   # sadece beyaz yapraklar dönecek
    t.down()
    for i in range(18):
        draw_petal(100*scale, 60)
        t.left(360/18)

    # --- Orta kısım (sarı nokta, sabit) ---
    t.up()
    t.goto(0, -35*scale)
    t.setheading(0)  # yönü sıfırla, kaymayı engelle
    t.down()
    t.fillcolor("gold")
    t.begin_fill()
    t.circle(35*scale)
    t.end_fill()

    # Göbeğin alt noktası
    stem_start_y = -35*scale - (35*scale)

    # --- Göbek ışıldaması (sabit, kaymaz) ---
    for _ in range(15):
        angle = random.uniform(0, 2*math.pi)
        r = random.uniform(40*scale, 70*scale)
        x = math.cos(angle) * r
        y = math.sin(angle) * r
        t.up()
        t.goto(x, y)
        t.down()
        t.dot(random.randint(4, 8), "yellow")

    # --- Dal ve yapraklar (sabit) ---
    draw_stem(stem_start_y, 250)
    draw_leaf(-60, stem_start_y-80, 150, size=70)
    draw_leaf(60, stem_start_y-160, 30, size=70)

    # --- Çimenler ---
    for i in range(-380, 400, 20):
        t.up()
        t.goto(i, -280)
        t.setheading(90)
        t.pencolor("forestgreen")
        t.pensize(2)
        t.down()
        t.forward(random.randint(40, 80))

# --- Animasyon: sadece yapraklar dönüyor ---
for step in range(1, 15):
    s = step/14
    draw_daisy(scale=s, rotation=step*5)
    screen.update()
    time.sleep(0.08)

# Son hali sabit bırak
draw_daisy(scale=1.0, rotation=0)
screen.update()

turtle.done()

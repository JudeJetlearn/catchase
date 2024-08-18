import pgzrun
import random

WIDTH = 500
HEIGHT = 500

cat = Actor("cat")
cat.pos = random.randint(0,500) , random.randint(0,500)

rat = Actor("rat")
rat.pos = random.randint(0,500) , random.randint(0,500)

score = 0
gameover = False

def draw ():
    screen.blit("bg1", (0,0))

    cat.draw()
    rat.draw()
    screen.draw.text("score: " + str(score),color = "white",topleft=(10,10))


    if gameover:
      screen.fill ("black")
      screen.draw.text("GAME OVER, YOUR FINAL SCORE WAS:" +str(score),midtop=(WIDTH/2,12),fontsize=35,color="red")


def update():
    global score
    if keyboard.a:
        cat.x = cat.x -5

    if keyboard.d:
        cat.x = cat.x +5

    if keyboard.w:
        cat.y = cat.y -5

    if keyboard.s:
        cat.y = cat.y +5


    if cat.colliderect(rat):
        moverat()
        score= score+1    

def moverat():
    rat.x = random.randint(0,500)
    rat.y = random.randint(0,500)

def time_up():
    global gameover
    gameover =True
clock.schedule(time_up, 10)        

pgzrun.go()
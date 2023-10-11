from random import randint
from pygame import *
width = 1440
height = 940
window = display.set_mode((width, height))
display.set_caption("depre??ed")
background = transform.scale(image.load('back.jpg'), (width, height))
font.init()
font1 = font.SysFont('Arial',80)
win = font1.render('победа',True ,(255,255,255))
lose = font1.render('луз',True,(100,0,0))
font2 = font.SysFont('Arial',36)
#mixer.init()
#mixer.music.load('musicc.mp3')
#mixer.music.play()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x ,player_y, player_speed,size_x , size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys =key.get_pressed()
        if keys[K_a] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < width - 80:
            self.rect.x += self.speed


score = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        if self.rect.y > height:
            self.rect.x = randint(80, width-80)
            self.rect.y = 0
            

player1 = Player('playerr.png', 800,700,13,130,150)
run = True
finish = False
health = 3
clock = time.Clock()
FPS = 60
monsters = sprite.Group()
asteroids = sprite.Group()
for a in range(3):
    asteroid = Enemy('mina.png', randint(80, 620), -40, randint(1, 3), 140, 140)
    asteroids.add(asteroid)
    monster = Enemy('ak.png', randint(80,width-80),-40,randint(1, 3),140,140)
    monsters.add(monster)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0, 0))

        asteroids.update()
        asteroids.draw(window)
        monsters.update()
        monsters.draw(window)
        player1.update()
        player1.reset()

        if score>=10:
            finish = True
            window.blit(win, (200,200))
        if sprite.spritecollide(player1, asteroids , True):
            health -=1
            asteroid = Enemy('ak.png', randint(80, 620), -40, randint(2, 5), 120, 120)
            asteroids.add(asteroid)
        if sprite.spritecollide(player1, monsters , True):
            score+=1
            monster = Enemy('mina.png', randint(80,width-80),-40,randint(2, 5),120,120)
            monsters.add(monster)

        if health == 0:
            finish = True
            window.blit(lose, (200,200))        
        text = font2.render("убил:" + str(score), 1, (255, 255, 255))
        window.blit(text,(10,50))
        
        text_health = font1.render('жизни:' + str(health), 1, (255, 255, 255))
        window.blit(text_health,(10,80))

        display.update()

        clock.tick(FPS)

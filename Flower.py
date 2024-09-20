import pygame
import sys
import random
import math
from pygame.locals import *

WINDOWWIDTH = 1000
WINDOWHEIGHT = 700
FPS = 60
SIZE = 4
SPEED_CHANGE_SIZE = 0.1
CHANGE_SPEED = 0.1
RAD = math.pi / 180
A_FALL = 1.5
NUM_BULLET = 45
SPEED_MIN = 1
SPEED_MAX = 6
TIME_CREATE_FIREWORK = 40
NUM_FIREWORKS_MAX = 6
NUM_FIREWORKS_MIN = 2
SPEED_FLY_UP_MAX = 15
SPEED_FLY_UP_MIN = 5
NUM_PARTICLES = 5

def random_color():
    return random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)

class Dot():
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        
    def update(self):
        if self.size > 0:
            self.size -= SPEED_CHANGE_SIZE
        else:
            self.size = 0
            
    def draw(self, surface):
        if self.size > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.size))
            
            
class BulletFlyUp():
    def __init__(self, speed, x):
        self.speed = speed
        self.x = x
        self.y = WINDOWHEIGHT
        self.dots = []
        self.size = SIZE / 2
        self.color = random_color()
        
    def update(self):
        self.dots.append(Dot(self.x, self.y, self.size, self.color))
        self.y -= self.speed
        self.speed -= A_FALL * 0.1
        for dot in self.dots:
            dot.update()
        for dot in self.dots:
            if dot.size <= 0:
                self.dots.pop(self.dots.index(dot))
                
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.size))
        for dot in self.dots:
            dot.draw(surface)
    
class Particle():
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(1, 3)
        
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.size > 0:
            self.size -= SPEED_CHANGE_SIZE
        else:
            self.size = 0
                
    def draw(self, surface):
        if self.size > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.size))

class Bullet():
    def __init__(self, x, y, speed, angle, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.size = SIZE
        self.color = color
        
    def update(self):
        speedX = self.speed * math.cos(self.angle * RAD)
        speedY = self.speed * -math.sin(self.angle * RAD)
        self.x += speedX
        self.y += speedY
        self.y += A_FALL
        if self.size > 0:
            self.size -= SPEED_CHANGE_SIZE
        else:
            self.size = 0
        if self.speed > 0:
            self.speed -= CHANGE_SPEED
        else:
            self.speed = 0
            
    def draw(self, surface):
        if self.size > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.size))
            
class FireWork():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dots = []
        self.bullets = self.create_bullets()
        
    def create_bullets(self):
        bullets = []
        for i in range(NUM_BULLET):
            angle = (800 / NUM_BULLET) * i
            speed = random.uniform(SPEED_MIN, SPEED_MAX)
            color = random_color()
            bullets.append(Bullet(self.x, self.y, speed, angle, color))
        return bullets
    
    def update(self):
        for bullet in self.bullets:
            bullet.update()
            self.dots.append(Dot(bullet.x, bullet.y, bullet.size, bullet.color))
        for dot in self.dots:
            dot.update()
        for dot in self.dots:
            if dot.size <= 0:
                self.dots.pop(self.dots.index(dot))
    
    def draw(self, surface):
        for bullet in self.bullets:
            bullet.draw(surface)
        for dot in self.dots:
            dot.draw(surface)
            
def draw_happy_new_year(surface):
    font = pygame.font.Font(None, 20)
    text = font.render("", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.centerx = WINDOWWIDTH // 2
    text_rect.centery = WINDOWHEIGHT // 2
    text_rect.x += int(math.sin(pygame.time.get_ticks() / 100) * 10)
    surface.blit(text, text_rect)
        
def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    pygame.display.set_caption("FIREWORKS")
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    fireWorks = []
    time = TIME_CREATE_FIREWORK
    bulletFlyUps = []
    particles = []
    
    while True:
        DISPLAYSURF.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        
        if time == TIME_CREATE_FIREWORK:
            for i in range(random.randint(NUM_FIREWORKS_MIN, NUM_FIREWORKS_MAX)):
                bulletFlyUps.append(BulletFlyUp(random.uniform(SPEED_FLY_UP_MIN, SPEED_FLY_UP_MAX), random.randint(int(WINDOWWIDTH * 0.2), int(WINDOWHEIGHT * 0.8))))
                    
        for bulletFlyUp in bulletFlyUps:
            bulletFlyUp.draw(DISPLAYSURF)
            bulletFlyUp.update()
                    
        for fireWork in fireWorks:
            fireWork.draw(DISPLAYSURF)
            fireWork.update()
                
        for bulletFlyUp in bulletFlyUps:
            if bulletFlyUp.speed <= 0:
                fireWorks.append(FireWork(bulletFlyUp.x, bulletFlyUp.y))
                bulletFlyUps.pop(bulletFlyUps.index(bulletFlyUp))
            
        for fireWork in fireWorks:
            if fireWork.bullets[0].size <= 0:
                fireWorks.pop(fireWorks.index(fireWork))
                    
        for bullet in fireWorks:
            if bullet.bullets[0].size <= 0:
                for _ in range(NUM_PARTICLES):
                    particle_x = bullet.bullets[0].x
                    particle_y = bullet.bullets[0].y
                    particle_size = random.uniform(1, 3)
                    particle_color = bullet.bullets[0].color
                    particles.append(Particle(particle_x, particle_y, particle_size, particle_color))
            
        for particle in particles:
            particle.update()
            particle.draw(DISPLAYSURF)
            
        draw_happy_new_year(DISPLAYSURF)
            
        if time <= TIME_CREATE_FIREWORK:
            time += 1
        else:
            time = 0
            
        pygame.display.update()
        FPSCLOCK.tick(FPS)
            
if __name__ == "__main__":
    main()
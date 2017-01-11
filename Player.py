import pygame
import Projectile
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW= (255, 255, 0)
PURPLE= (255, 0, 255)

GRAVITY = 1

class Player(pygame.sprite.Sprite):
    def __init__(self, game,x,y):
#         x,y
#         top, left, bottom, right
#         topleft, bottomleft, topright, bottomright
#         midtop, midleft, midbottom, midright
#         center, centerx, centery
#         size, width, height
#         w,h

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.top= x
        self.rect.left= y
        self.speed_x = 0
        self.speed_y = 0
        self.dir = "right"
        self.last = pygame.time.get_ticks()
        self.can_shoot=300
        
    def jump(self):
        self.rect.y += 2
        if self.rect.y > 0:
            hit_list = pygame.sprite.spritecollide(self, self.game.platforms, False)
                 
        self.rect.y -= 2
        if hit_list:
            self.speed_y = -15
            
    def shoot(self):
        
        if self.dir == "left":
            bullet = Projectile.Bullet(self,self.rect.top+10,self.rect.left-10,self.dir)
            self.game.all_sprites.add(bullet)
            self.game.bullets.add(bullet)
        elif self.dir == "right":
            bullet = Projectile.Bullet(self,self.rect.top+10,self.rect.left+30,self.dir)
            self.game.all_sprites.add(bullet)
            self.game.bullets.add(bullet)

        
            
    def check_collision(self, dir):
        if dir == 'x':
            hit_list = pygame.sprite.spritecollide(self, self.game.platforms, False)
            if hit_list:
                if self.speed_x > 0:
                    self.rect.right = hit_list[0].rect.left
                    self.dir = "left"
                elif self.speed_x < 0:
                    self.rect.left = hit_list[0].rect.right
                    self.dir = "right"
                self.speed_x *= -1
        if dir == 'y':
            hit_list = pygame.sprite.spritecollide(self, self.game.platforms, False)
            if hit_list:
                if self.speed_y > 0:
                    self.rect.bottom = hit_list[0].rect.top
                elif self.speed_y < 0:
                    self.rect.top = hit_list[0].rect.bottom
                self.speed_y = 0            
        
    def update(self):
        self.speed_x = 0
        self.speed_y += GRAVITY
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.dir = "left"
            self.speed_x = -5
        if keys_pressed[pygame.K_RIGHT]:
            self.dir = "right"
            self.speed_x = 5
        if keys_pressed[pygame.K_z]:
#             helloo=hello.Bullet(self,self.rect.top+10,self.rect.left+30,self.dir)
#             game.all_sprites.add(helloo)
#             game.bullets.add(helloo)
            self.jump()
            
        if keys_pressed[pygame.K_x]:
            now = pygame.time.get_ticks()
            if now - self.last >= self.can_shoot:
                self.last = now
                self.shoot()    
            
                
        self.rect.x += self.speed_x
        self.check_collision('x')
        self.rect.y += self.speed_y
        self.check_collision('y')
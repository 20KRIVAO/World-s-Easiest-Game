import pygame
import sys

class Sprite(pygame.sprite.Sprite):
   def __init__(self, pos):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface([20, 20])
       self.image.fill((255, 0, 0))
       self.rect = self.image.get_rect()

       self.rect.center = pos

class SpriteTwo(pygame.sprite.Sprite):
   def __init__(self, pos):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface([20, 20])
       self.image.fill((0, 0, 255))
       self.rect = self.image.get_rect()

       self.rect.center = pos

class SpriteThree(pygame.sprite.Sprite):
   def __init__(self, pos):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface([5, 1000])
       self.image.fill((0, 0, 255))
       self.rect = self.image.get_rect()

       self.rect.center = pos

class SpriteFour(pygame.sprite.Sprite):
   def __init__(self, pos):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface([1000, 5])
       self.image.fill((0, 0, 255))
       self.rect = self.image.get_rect()

       self.rect.center = pos

class SpriteFive(pygame.sprite.Sprite):
   def __init__(self, pos):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface([20, 20])
       self.image.fill((0, 255, 255))
       self.rect = self.image.get_rect()

       self.rect.center = pos

def main():
   pygame.init()
   clock = pygame.time.Clock()
   fps = 50
   bg = [255, 255, 255]
   size =[500, 500]


   screen = pygame.display.set_mode(size)

   player = Sprite([40, 50])
   player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
   player.vx = 5
   player.vy = 5


   wall = SpriteTwo([100, 60])
   wall_two = SpriteTwo([200, 120])
   wall_three = SpriteThree([0, 0])
   wall_four = SpriteThree([500, 0])
   wall_five = SpriteFour([0, 0])
   wall_six = SpriteFour([0, 500])

   wall_group = pygame.sprite.Group()
   wall_group.add(wall)
   wall_group.add(wall_two)
   wall_group.add(wall_three)
   wall_group.add(wall_four)
   wall_group.add(wall_five)
   wall_group.add(wall_six)

   finish = SpriteFive([400, 400])
   finish_group = pygame.sprite.Group()
   finish_group.add(finish)

   player_group = pygame.sprite.Group()
   player_group.add(player)

   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return False

       key = pygame.key.get_pressed()

       for i in range(2):
           if key[player.move[i]]:
               player.rect.x += player.vx * [-1, 1][i]

       for i in range(2):
           if key[player.move[2:4][i]]:
               player.rect.y += player.vy * [-1, 1][i]

       screen.fill(bg)

       # first parameter takes a single sprite
       # second parameter takes sprite groups
       # third parameter is a do kill command if true
       # all group objects colliding with the first parameter object will be
       # destroyed. The first parameter could be bullets and the second one
       # targets although the bullet is not destroyed but can be done with
       # simple trick bellow
       hit = pygame.sprite.spritecollide(player, wall_group, True)

       if hit:
           # if collision is detected call a function in your case destroy
           # bullet
           pygame.init()
           clock = pygame.time.Clock()
           fps = 50
           bg = [255, 255, 255]
           size = [500, 500]

           screen = pygame.display.set_mode(size)

           player = Sprite([40, 50])
           player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
           player.vx = 5
           player.vy = 5

           wall = SpriteTwo([100, 60])
           wall_two = SpriteTwo([200, 120])
           wall_three = SpriteThree([0, 0])
           wall_four = SpriteThree([500, 0])
           wall_five = SpriteFour([0, 0])
           wall_six = SpriteFour([0, 500])

           wall_group = pygame.sprite.Group()
           wall_group.add(wall)
           wall_group.add(wall_two)
           wall_group.add(wall_three)
           wall_group.add(wall_four)
           wall_group.add(wall_five)
           wall_group.add(wall_six)

           finish = SpriteFive([400, 400])
           finish_group = pygame.sprite.Group()
           finish_group.add(finish)

           player_group = pygame.sprite.Group()
           player_group.add(player)

       hit_two = pygame.sprite.spritecollide(player, finish_group, True)

       if hit_two:
           pygame.init()
           clock = pygame.time.Clock()
           fps = 50
           bg = [0, 0, 0]
           size = [500, 500]

           screen = pygame.display.set_mode(size)

       player_group.draw(screen)
       wall_group.draw(screen)

       pygame.display.update()
       clock.tick(fps)

   pygame.quit()
   sys.exit


if __name__ == '__main__':
   main()

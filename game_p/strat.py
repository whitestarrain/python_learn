import pygame

class plane(pygame.sprite.Sprite):
    def __init__(self,image,speed):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = image.rect
        self.speed = speed

    def update(self,*args):
        self.rect.y+=self.speed
        pass



pygame.init()

screen = pygame.display.set_mode((480, 700))


clock = pygame.time.Clock()

i = 0


while True:

    # 没秒中刷新60次
    clock.tick(60)
    print(i)
    i += 1


pygame.quit()

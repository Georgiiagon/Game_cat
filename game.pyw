import pygame
import random
 
window = pygame.display.set_mode((402, 402))
pygame.display.set_caption("Game_cat")
screen = pygame.Surface((402, 402))     
done = True
def draw_setka():
    x = 0
    x_x = 400
    y = 0
    y_y = 400
    for i in range(11):
        pygame.draw.line(screen, (255, 255, 255), (x, y), (x, y_y), 2)
        x += 40
    x = 0
    for i2 in range(11):
        pygame.draw.line(screen, (255, 255, 255), (x, y), (x_x, y), 2)
        y += 40 
class Cat():
    def __init__(self, xpos, ypos, filename):
        self.xpos = xpos
        self.ypos = ypos
        self.bitmap = pygame.image.load(filename)
    def render(self):
        screen.blit(self.bitmap, (self.xpos * 40 + 2,self.ypos * 40 + 2))
def going_hv():
    x = 2
    y = len(list)
    for i in reversed(list[1:]):
            i.xpos, i.ypos = list[y - x].xpos, list[y - x].ypos 
            x += 1
counter = 0 
hvost = Cat(4, 5, '4.png')
hero = Cat(4, 4, '4.png')
going = '' 
list = [hero, hvost] 

def do_going(going):
    if going == 'left':     
        going_hv()      
        list[0].xpos -= 1
        if list[0].xpos < 0:
            list[0].xpos = 9        
    if going == 'right':        
        going_hv()      
        list[0].xpos += 1
        if list[0].xpos > 9:
            list[0].xpos = 0        
    if going == 'up':       
        going_hv()      
        list[0].ypos -= 1
        if list[0].ypos < 0:
            list[0].ypos = 9
    if going == 'down':     
        going_hv()      
        list[0].ypos += 1
        if list[0].ypos > 9:
            list[0].ypos = 0
grib = Cat(10, 10, 'grib.png')
def grib_gen(list):
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    for i in list:
        if (i.xpos, i.ypos) == (x, y):
            x, y = grib_gen(list)
        else:
            continue
    return x, y     
grib.xpos, grib.ypos = grib_gen(list) 
while done:
    some_x = list[len(list) - 1].xpos 
    some_y = list[len(list) - 1].ypos 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                going = 'left'              
            if event.key == pygame.K_RIGHT:
                going = 'right'
            if event.key == pygame.K_UP:
                going = 'up'        
            if event.key == pygame.K_DOWN:
                going = 'down'
    do_going(going) 
    if list[0].xpos == grib.xpos and list[0].ypos == grib.ypos:
        counter += 1
        list.append(Cat( some_x, some_y, '4.png'))
        grib.xpos, grib.ypos = grib_gen(list)    
    screen.fill((0, 0, 0))
    draw_setka()
    for i in list:
        i.render()
    grib.render()
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(300)

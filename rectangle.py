import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill("blue")
red = "#FF0000"
pygame.display.update()

class Rect():
    def __init__(self, color, pos, width_line):
        self.rect_color = color
        self.rect_pos = list(pos) # Convert to list so we can modify size easily
        self.rect_width_line = width_line
        self.rect_surface = screen
        
    def draw(self):
        self.Draw_Rect = pygame.draw.rect(self.rect_surface, self.rect_color, self.rect_pos, self.rect_width_line)
        
    def grow(self, size_increase):
        # Increase both width (index 2) and height (index 3)
        self.rect_pos[2] = self.rect_pos[2] + size_increase
        self.rect_pos[3] = self.rect_pos[3] + size_increase
        self.Draw_Rect = pygame.draw.rect(self.rect_surface, self.rect_color, self.rect_pos, self.rect_width_line)

# Position format: (x, y, width, height)
# This places a 50x50 rectangle near the center
rectangle = Rect(red, (275, 275, 50, 50), 0)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Added to allow closing the window cleanly
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255, 255, 255))
            rectangle.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255, 255, 255))
            rectangle.grow(20)
            pygame.display.update()
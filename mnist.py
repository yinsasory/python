import pygame
import random
from pygame import mixer

class Bird:
    def __init__(self):
        pygame.init()
        self.xScreen, self.yScreen = 500, 600
        linkBackGround = '2024-02-09 (1).png'  # Chỉnh sửa lỗi gõ
        self.linkImgBird = './data/bird.png'
        self.screen = pygame.display.set_mode((self.xScreen, self.yScreen))
        pygame.display.set_caption("Flappy Bird")  # Thêm tiêu đề cho cửa sổ
        self.background = pygame.image.load(linkBackGround)  # Sử dụng đúng biến
        self.gamerunninng = True
        icon = pygame.image.load(self.linkImgBird)
        pygame.display.set_icon(icon)

        self.xSizeBird = 80
        self.ySizeBird = 60
        self.xBird = self.xScreen / 3
        self.yBird = self.yScreen / 2


if __name__ == "__main__":
    bird = Bird()
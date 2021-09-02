import pygame

class Ship():
    """Класс для управления кораблём"""
    def __init__(self,ai_game): # Экземпляр screen передаёт данные дисплея
        pygame.init()
        """Инициализирует корабль и задаёт его начальную позицию"""

        self.screen = ai_game.screen # Передаём экземпляр экрана
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/space_ship.bmp')
        self.new_image = pygame.transform.scale(self.image, (40, 40))# Изменяет размер изображения
        self.rect = self.new_image.get_rect() # Получает прямоугольник

        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x) # Типизированное изменение типа в 0.0

        # Флаги пермещения
        self.moving_right = False
        self.moving_left = False

    def blit_me(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.new_image,self.rect)

    def update(self):
        """Обновляет позицию корабля с учётом флагов"""
        # Обновляется атрибут x объекта ship, а не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed # Перемещение вправо
        if self.moving_left and self.rect.left > self.screen_rect.left :#чтобы не заходить за координату x=0 слева
            self.x -= self.settings.ship_speed # Перемещение влево
        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x # rect изменяет местоположение
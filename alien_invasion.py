import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы"""
        pygame.init()  # инициализирует настройки, необходимые Pygame для нормальной работы
        self.settings = Settings()
        self.size = self.settings.screen_width, self.settings.screen_height
        self.screen = pygame.display.set_mode(self.size)  # Cоздаёт окно,
        # в котором прорисовываются все графические элементы игры.
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # Передаём экземпляр класса

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self._update_events()
            self.ship.update()

    def _check_events(self):
        """Обрабатывает нажатие клавиш и события мыши"""
        for event in pygame.event.get():
            # Если нажатая клавиша X в правом верхнем углу --> exit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Иначе нажата и удержана клавиша
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Иначе клавиша отпущена
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        # Если нажатая клавиша == K_RIGHT --> передать значение True флагу moving_right
        if event.key == pygame.K_RIGHT:  # Передаёт значение True, чтобы классе Ship заработал цикл
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        # Если отпущенная клавиша == K_RIGHT --> передать значение False флагу moving_right
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_events(self):
        """Обновляет изображение на экране и отображает новый экран"""
        # При каждом проходе цикла перерисовывается экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blit_me()  # отображение корабля

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()

    ai.run_game()

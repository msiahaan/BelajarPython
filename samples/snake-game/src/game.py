class Game:
    def __init__(self):
        self.snake_pos = [[100, 50], [90, 50], [80, 50]]
        self.snake_direction = 'RIGHT'
        self.score = 0
        self.food_pos = [200, 50]
        self.game_over = False

    def start_game(self):
        self.score = 0
        self.snake_pos = [[100, 50], [90, 50], [80, 50]]
        self.snake_direction = 'RIGHT'
        self.food_pos = [200, 50]
        self.game_over = False

    def update(self):
        if self.game_over:
            return

        head_x, head_y = self.snake_pos[0]

        if self.snake_direction == 'UP':
            head_y -= 10
        elif self.snake_direction == 'DOWN':
            head_y += 10
        elif self.snake_direction == 'LEFT':
            head_x -= 10
        elif self.snake_direction == 'RIGHT':
            head_x += 10

        self.snake_pos.insert(0, [head_x, head_y])

        if self.snake_pos[0] == self.food_pos:
            self.score += 1
            self.food_pos = self.generate_food()
        else:
            self.snake_pos.pop()

        self.check_collision()

    def check_collision(self):
        head_x, head_y = self.snake_pos[0]
        if head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400 or self.snake_pos[0] in self.snake_pos[1:]:
            self.game_over = True

    def generate_food(self):
        import random
        return [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]

    def draw(self, surface):
        import pygame
        surface.fill((0, 0, 0))
        for pos in self.snake_pos:
            pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self.food_pos[0], self.food_pos[1], 10, 10))
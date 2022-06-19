class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """инициализация статистики"""
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.highscore = int(f.readline())

    def reset_stats(self):
        """статистика изменяющаяся во время игры"""
        self.lives_left = 3
        self.score = 0

    

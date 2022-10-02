from utils.unit import BaseUnit


class BaseSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Arena(metaclass=BaseSingleton):
    STAMINA_PER_ROUND = 1
    player = None
    enemy = None
    game_is_running = False
    battle_result = "Бой не завершен!"

    def start_game(self, player: BaseUnit, enemy: BaseUnit):
        self.enemy = enemy
        self.player = player
        self.game_is_running = True

    def _check_players_hp(self):
        if self.player.hp <= 0 and self.enemy.hp <= 0:
            self.battle_result = "Ничья!"
            return self._end_game()
        elif self.enemy.hp <= 0:
            self.battle_result = "Вы победили!"
            return self._end_game()
        elif self.player.hp <= 0:
            self.battle_result = "Вы проиграли!"
            return self._end_game()

    def _stamina_regeneration(self):
        player_stamina_growth = self.STAMINA_PER_ROUND * self.player.unit_class.stamina
        if self.player.stamina + player_stamina_growth > self.player.unit_class.max_stamina:
            self.player.stamina = self.player.unit_class.max_stamina
        else:
            self.player.stamina += player_stamina_growth
        enemy_stamina_growth = self.STAMINA_PER_ROUND * self.enemy.unit_class.stamina
        if self.enemy.stamina + enemy_stamina_growth > self.enemy.unit_class.max_stamina:
            self.enemy.stamina = self.enemy.unit_class.max_stamina
        else:
            self.enemy.stamina += player_stamina_growth

    def next_turn(self):
        result = self._check_players_hp()
        if result:
            return result
        self._stamina_regeneration()
        return self.enemy.hit(self.player)

    def _end_game(self):
        self._instances = {}
        self.game_is_running = False
        return self.battle_result

    def player_hit(self):
        result = self.player.hit(self.enemy)
        self.next_turn()
        return result

    def player_use_skill(self):
        result = self.player.use_skill(self.enemy)
        self.next_turn()
        return result

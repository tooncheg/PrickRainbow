class Dragon:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def talk(self):
        print(self.name, 'health', self.health)

    def get_damage(self, damage):
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0

def main():
    list_enemy = [Dragon('Smoke'), Dragon('Ukraine_IronBelly')]
    finish = False
    while not finish:
        enemy = list_enemy[0]
        enemy.talk()
        damage = int(input())
        enemy.get_damage(damage)
        if not enemy.is_alive():
            list_enemy.pop(0)
            print(enemy.name, 'defeated')
        if not list_enemy:
            finish = True
    print('You win!')


main()

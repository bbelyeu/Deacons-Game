import random
import time


class BadGuy():
    """this is a bad guy."""
    name = "bad guy"
    max_health = random.randint(5, 15)
    current_health = max_health

    def __init__(self, name):
        self.name = name

    def attack(self, hero):
        """attack the hero."""
        hero.current_health -= 1
        print(f"{self.name} attacked you! You have {hero.current_health} health left.")
        return True

    def block(self):
        """do math to see if the bad guy can block."""
        if int(time.time()) % 5 == 0:
            print(f"Oops! {self.name} blocked your attack.")
            return True
        else:
            return False

    def dodge(self):
        """try to dodge."""
        if random.randint(1, 3) == 1:
            print(f"{self.name} dodged!")
            return True
        return False

    def use_ability(self, hero):
        """see if enemy dodges attack."""
        rand = random.randint(1, 3)
        if rand == 1:
            return self.attack(hero)
        elif rand == 2:
            return self.block()
        else:  # 3
            return self.dodge()


class GoodGuy():
    """This is my Hero class."""

    name = "Doyal"
    max_health = random.randint(50, 70)
    current_health = max_health

    def __init__(self, name):
        self.name = name

    def say(self, message):
        """Use this to say something."""
        print(f"{self.name} says: {message}")

    def attack(self, enemy):
        """Use this to attack an enemy."""
        if not enemy.use_ability(self):
            enemy.current_health -= 1
            print(f"{self.name} attacks {enemy.name}")

            if enemy.current_health == 0:
                print("(✖╭╮✖)")
                print("Your enemy is dead!")
            else:
                print(f"{enemy.name} has {enemy.current_health} health left!")

        time.sleep(1)

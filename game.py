from beastiary import load_beastiary
import random


def roll_initiative(fighter):
    initiative = roll(1, 20) + modifier(fighter.dexterity)
    return initiative if initiative > 0 else 0


def modifier(score):
    return (score - 10) // 2


def roll(n, d):
    return sum([random.randint(1, d) for _ in range(n)])


beastiary = load_beastiary()
fighters = [random.choice(list(beastiary.values())) for _ in range(5)]

initiatives = {fighter: roll_initiative(fighter) for fighter in fighters}
initiatives = dict(sorted(initiatives.items(), key=lambda item: item[1], reverse=True))

for fighter, initiative in initiatives.items():
    print(f"{fighter}: {initiative}")
    print(random.choice(fighter.actions))
    print()

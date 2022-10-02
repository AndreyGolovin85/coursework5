from dataclasses import dataclass

from utils.skills import Skill, FuryPunch, HardShot


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name="Воин",
    max_health=100,
    max_stamina=20,
    attack=1,
    stamina=0.9,
    armor=10,
    skill=FuryPunch()
)

ThiefClass = UnitClass(
    name="Вор",
    max_health=100,
    max_stamina=20,
    attack=1,
    stamina=0.9,
    armor=10,
    skill=HardShot()
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}

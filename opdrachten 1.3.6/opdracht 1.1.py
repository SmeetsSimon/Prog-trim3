class Family:
    def __init__(self, race, sex, hair, relation, age, name ):
        self.race = race
        self.sex = sex
        self.hair = hair
        self.relation = relation
        self.age = age 
        self.name = name 

    def is_age(self):
        print(self.age)

    def is_sex(self):
        print(self.sex)

    def birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}"

    def related(self):
        return self.relation

    def paint_hair(self, color):
        self.hair = color

persoon1 = Family("human", "vrouw", "blond", "nicht", 20, "magrette")
persoon2 = Family("human", "man", "black", "neef", 23, "winston" )
persoon3 = Family("human", "vrouw", "zwart", "tante", 40, "wendy")
persoon4 = Family("human", "man", "bruin", "nonkel", 40, "jan")

print(persoon1.is_age())

print(persoon2.is_sex())

persoon3.paint_hair("blond")
print(persoon3.hair)

print(persoon4.related())
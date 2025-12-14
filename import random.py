import random
boys = ["پسر1", "پسر2", "پسر3", "پسر4", "پسر5",
        "پسر6", "پسر7", "پسر8", "پسر9", "پسر10"]
girls = ["دختر1", "دختر2", "دختر3", "دختر4", "دختر5",
         "دختر6", "دختر7", "دختر8", "دختر9", "دختر10"]

random.shuffle(girls)
pairs = list(zip(boys, girls))

for boy, girl in pairs:
    print(f"{boy} ❤️ {girl}")
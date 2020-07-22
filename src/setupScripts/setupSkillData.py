import json

elems = ["phys", "fire", "ice", "elec", "wind", "light", "dark", "almighty", "ailment", "recovery", "support", "passive"]
personas = list(json.load(open("src/data/p4g/golden-demon-data.json")).keys())

skillData = json.load(open("src/data/p4g/golden-skill-data.json"))
skills = list(skillData.keys())

# Main cycle
for skillName in skills:
    skill = skillData[skillName]
    skillKeys = list(skill.keys())
    print(elems.index(skill['element']) if ('element' in skillKeys) else '', end="|")
    print(skillName, end="|")
    print(skill['effect'] if ('effect' in skillKeys) else '', end="|")
    print(skill['power'] if ('power' in skillKeys) else '', end="|")
    print(skill['cost'] if ('cost' in skillKeys) else '', end="|")
    print(skill['hit'] if ('hit' in skillKeys) else '', end="|")
    print(skill['crit'] if ('crit' in skillKeys) else '', end="|")
    print(skill['rank'] if ('rank' in skillKeys) else '', end="|")
    print(skill['price'] if ('price' in skillKeys) else '', end="|")
    if 'card' in skillKeys:
        if skill['card'] != "Shuffle":
            print(personas.index(skill['card']), end="|")
        else:
            print(-1, end="|")
    else:
        print('', end="|")
    print(int('unique' in skillKeys))
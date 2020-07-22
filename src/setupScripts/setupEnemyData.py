import json

enemyData = json.load(open("src/p4/data/p4g/json/golden-enemy-data.json"))
arcanae = json.load(open("src/p4/data/p4g/json/unused/comp-config.json"))['races']
dungeons = json.load(open("src/p4/data/p4g/json/unused/comp-config.json"))['dungeons']
skillList = json.load(open("src/p4/data/p4g/json/unused/golden-skill-data.json"))


# lvl|name|arcana|area|resists|stats|skills|exp|price|material|gem|drops
for enemyName in enemyData.keys():
    enemy = enemyData[enemyName]
    print(enemy['lvl'], end="|")
    print(enemyName, end="|")
    print(arcanae.index(enemy['race']), end="|")
    # Area
    areaInfo = enemy['area'].split(" ")
    
    if len(areaInfo) == 3:
        # Evaluate floors
        floorData = areaInfo[2].split(",")
        newFD = []
        for group in floorData:
            if "-" in group:
                for floor in range(int(group.split("-")[0]), int(group.split("-")[1])):
                    newFD.append(str(floor))
            else:
                newFD.append(str(group))
        areaInfo[2] = ",".join(newFD)
        print("/".join(areaInfo), end="|")
    else:
        floorData = areaInfo[1].split(",")
        newFD = []
        for group in floorData:
            if "-" in group:
                for floor in range(int(group.split("-")[0]), int(group.split("-")[1])):
                    newFD.append(str(floor))
            else:
                newFD.append(str(group))
        areaInfo[1] = ",".join(newFD)
        print("/".join([areaInfo[0], '-', areaInfo[1]]), end="|")
    
    print(enemy['resists'], end="|")
    print("/".join(str(enemy['stats'])[1:][:-1].split(", ")), end="|")

    # Skills
    skills = enemy['skills']
    encSkills = []
    for skill in skills:
        encSkills.append(str(list(skillList.keys()).index(skill)))
    print("/".join(encSkills), end="|")

    print(enemy['exp'], end="|")
    print(enemy['price'], end="|")
    print(enemy['material'], end="|")
    print(enemy['gem'], end="|")
    print("/".join(enemy['drops']) if 'drops' in list(enemy.keys()) else '-')

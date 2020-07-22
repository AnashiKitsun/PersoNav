import json

skillData = json.load(open("src/data/p4g/golden-skill-data.json"))
allSkills = list(skillData.keys())

personaData = json.load(open("src/data/p4g/golden-demon-data.json"))
personas = list(personaData.keys())

# Main cycle
for personaName in personas:
    persona = personaData[personaName]
    arcana = persona['race']
    name = personaName
    level = persona['lvl']
    inherits = persona['inherits']
    affins = persona['resists']
    # Build stats
    statsInt = persona['stats']
    stats = []
    for stat in statsInt:
        stats.append(str(stat))
    stats = '/'.join(stats)
    # Build skills
    skillsPlain = persona['skills']
    skillList = []
    for skill in skillsPlain:
        skillList.append(str(allSkills.index(skill))+"-"+str(skillsPlain[skill]))
    skills = '/'.join(skillList)
    print(f'{arcana}|{name}|{level}|{inherits}|{affins}|{stats}|{skills}')
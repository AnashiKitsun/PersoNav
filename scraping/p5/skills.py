import requests
from bs4 import BeautifulSoup
import json

# Establish general skill reading function
def parseSkills(skillList, targeting, type, mapping):
    # Name is always col[0]
    # Then read type and targeting into data
    # Finally, use mapping scheme to read in the rest of the values, if they exist
    for row in skillList[1:]:
        cols = row.select("td")

        # Init skill vars read from name
        royal = False #/ Denoted with †
        equipped = False #/ Denoted with ⌃ #! ALSO ACTS AS †
        dlc = False #/ Denoted with ↓

        ## Get name from col[0], and read vars in.
        name = cols[0].text.strip()        
        # Check for †
        royal = ("†" in name)
        name = name.replace("†", "")
        # Check for ⌃
        equipped = ("⌃" in name)
        if (equipped):
            royal = True
        name = name.replace("⌃", "")
        # Check for ↓
        dlc = ("↓" in name)
        name = name.replace("↓", "")

        # Initialize skill data
        skills[name] = {}
        # Add type, targeting, and name read data
        skills[name]["Targeting"] = targeting
        skills[name]["Type"] = type
        skills[name]["Royal"] = royal
        skills[name]["Equip Only"] = equipped
        skills[name]["DLC"] = dlc

        ## Loop through cols and add to skill
        # Make an easier var to loop through
        colsNoName = cols[1:]
        for i, value in enumerate(mapping):
            if value != "None":
                if i+1 > len(colsNoName):
                    skills[name][value] = "None"
                else:
                    skills[name][value] = colsNoName[i].text.strip()

skills = {}
skillSource = requests.get("https://megamitensei.fandom.com/wiki/List_of_Persona_5_Royal_Skills").content
skillSoup = BeautifulSoup(skillSource, features="lxml")

map = ["Effect", "Cost", "Card"]
altMap = ["Effect", "None", "None", "Cost", "Card"]

tables = skillSoup.select(".table.p5")

###################
# PHYSICAL SKILLS #
###################

# Phys single target
parseSkills(tables[0].select("tr"), "e1", "Physical", map)

# Phys multi target
parseSkills(tables[1].select("tr"), "e*", "Physical", map)

# Gun general
parseSkills(tables[2].select("tr"), "e?", "Gun", map)

################
# MAGIC SKILLS #
################

# Fire General
parseSkills(tables[3].select("tr"), "e?", "Fire", map)

# Ice General
parseSkills(tables[4].select("tr"), "e?", "Ice", map)

# Electric General
parseSkills(tables[5].select("tr"), "e?", "Electric", map)

# Wind General
parseSkills(tables[6].select("tr"), "e?", "Wind", map)

# Psy General
parseSkills(tables[7].select("tr"), "e?", "Psy", map)

# Nuclear General
parseSkills(tables[8].select("tr"), "e?", "Nuclear", map)

# Bless General
parseSkills(tables[9].select("tr"), "e?", "Bless", altMap)

# Curse General
parseSkills(tables[10].select("tr"), "e?", "Curse", altMap)

# Almighty general
parseSkills(tables[11].select("tr"), "e?", "Almighty", altMap)

########
# TEST #
########
print(json.dumps(skills, indent=4))

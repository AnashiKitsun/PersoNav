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
        # Get name from col[0]
        if cols[0].text.strip()[-1] != "★":
            name = cols[0].text.strip()
        else:
            name = cols[0].text.strip()[:-1]
        # Initialize skill data
        skills[name] = {}
        # Detect DLC data
        dlc = (cols[0].text.strip()[-1] == "★")
        # Add type, targeting, and DLC data
        skills[name]["Targeting"] = targeting
        skills[name]["Type"] = type
        skills[name]["DLC Exclusive"] = dlc
        # Loop through mapping and add to skill
        for i, value in enumerate(mapping):
            if value != "None":
                # So that mapping can skip with the value "None", and set any nonexistant values to "None"
                if len(mapping)-1 <= i:
                    skills[name][value] = "None"
                else:
                    skills[name][value] = cols[i+1].text.strip()

skills = {}
skillSource = requests.get("https://megamitensei.fandom.com/wiki/List_of_Persona_5_Royal_Skills").content
skillSoup = BeautifulSoup(skillSource, features="lxml")

map = ["Effect", "Cost", "Card"]
altMap = ["Effect", "None", "None", "Cost", "Card"]

###################
# PHYSICAL SKILLS #
###################

# Phys single target
parseSkills(skillSoup.select_one("#tabber-440594ee4c55cc01260fd6895925888b > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1)").select("tr"), "e1", "Physical", map)

# Phys multi target
parseSkills(skillSoup.select_one("#tabber-440594ee4c55cc01260fd6895925888b > div:nth-child(3) > table:nth-child(2) > tbody:nth-child(1)").select("tr"), "e*", "Physical", map)

# Gun general
parseSkills(skillSoup.select("table.table")[1].select("tr"), "??", "Gun", map)

################
# MAGIC SKILLS #
################

# Fire General
parseSkills(skillSoup.select_one("table.table:nth-child(15) > tbody:nth-child(1)").select("tr"), "??", "Fire", map)

##################
# PASSIVE SKILLS #
##################
pasSource = requests.get("https://samurai-gamers.com/persona-5/passive-skills-list/").content
pasSoup = BeautifulSoup(pasSource, features="lxml")
pasMap = ["Effect"]

for table in pasSoup.select("tbody")[:7]:
    tableSkills = table.select("tr")
    parseSkills(tableSkills, "Passive", "Passive", pasMap, 2)

##################
# SUPPORT SKILLS #
##################
supSource = requests.get("https://samurai-gamers.com/persona-5/support-skills-list/").content
supSoup = BeautifulSoup(supSource, features="lxml")
supMap = ["Effect", "Cost"]

for table in supSoup.select("tbody")[:5]:
    tableSkills = table.select("tr")
    parseSkills(tableSkills, "Varied", "Support", supMap, 3)

##################
# HEALING SKILLS #
##################
healSource = requests.get("https://samurai-gamers.com/persona-5/healing-skills-list/").content
healSoup = BeautifulSoup(healSource, features="lxml")
healMap = ["Effect", "Cost"]

for table in healSoup.select("tbody")[:2]:
    tableSkills = table.select("tr")
    parseSkills(tableSkills, "Varied", "Healing", healMap, 3)

###################
# RECOVERY SKILLS #
###################
recSource = requests.get("https://samurai-gamers.com/persona-5/status-recovery-skills-list/").content
recSoup = BeautifulSoup(recSource, features="lxml")
recMap = ["Effect", "Cost"]

for table in recSoup.select("tbody")[:1]:
    tableSkills = table.select("tr")
    parseSkills(tableSkills, "SingleAll", "Healing", recMap, 3)

##################
# AILMENT SKILLS #
##################
ailSource = requests.get("https://samurai-gamers.com/persona-5/status-ailments-list/").content
ailSoup = BeautifulSoup(ailSource, features="lxml")
ailMap = ["Cost", "None", "Effect"]

for table in ailSoup.select("tbody")[:3]:
    tableSkills = table.select("tr")
    parseSkills(tableSkills, "Varied", "Ailment", ailMap, 3)

########
# TEST #
########
print(json.dumps(skills, indent=4))

import json

with open("data/settings.json", "r") as file:
    jsonsettings = json.load(file)

if jsonsettings["theme_mode"] == "light":
    jsonsettings["theme_mode"] = "dark"
else:
    jsonsettings["theme_mode"] = "light"


with open("data/settings.json", "w") as file2:
    json.dump(jsonsettings, file2)
acronyms = {}

acronyms["DTF"] = "down to Fuck"
acronyms["GGG"] = "good, giving, and game"
acronyms["FB"] = "fuck buddy"
acronyms["BDSM"] = "bondage, domination, sadism, and masochism"
acronyms["FWB"] = "friends with benefits"

print(acronyms)

del acronyms["FB"]
print(acronyms)

print(acronyms.get("FB"))

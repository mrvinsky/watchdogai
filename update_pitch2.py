import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replacements
replacements = {
    "costs<br>2 seconds": "costs<br>5 seconds",
    "2 seconds of a dealer": "5 seconds of a dealer",
    "across 45 tables": "across 100 tables",
    "all 45 tables": "all 100 tables",
    "just 45 tables": "just 100 tables",
    "18 recovered days": "101 recovered days",
    "18 lost days": "101 lost days",
    "18 additional days": "101 additional days",
    "18 days of": "101 days of",
    ">1.2h<": ">6.6h<",
    ">8.4h<": ">46.6h<",
    ">36h<": ">200h<",
    ">18<": ">101<",
    "2.0 seconds": "5.0 seconds",
    "3.3 rounds": "8.3 rounds",
    "3.3 extra rounds": "8.3 extra rounds",
    "3.3 extra games": "8.3 extra games",
    "+7,200 games": "+40,000 games",
    "+50,400 games": "+280,000 games",
    "+216,000 games": "+1,200,000 games",
    "+2,628,000 games": "+14,600,000 games",
    "2.6M+": "14.6M+",
    "1.2 hours": "6.6 hours",
    "8.4 hours": "46.6 hours",
    "36 hours": "200 hours",
    "18 days": "101 days",
    "45 tables": "100 tables",
    "360 tables": "500 tables",
    "~21M+": "~73M+",
    "2 seconds saved": "5 seconds saved",
    "45 active tables": "100 active tables"
}

for old, new in replacements.items():
    text = text.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
    
print("Updated values to 5s and 100 tables.")

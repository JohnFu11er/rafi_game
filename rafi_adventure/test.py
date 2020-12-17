import json

# Fetch enemy data from JSON file
with open('enemies.json', mode='rt') as _data:
    enemy_data = json.loads(_data.read())
    
print(enemy_data['Great Frost Dragon']['hp'])
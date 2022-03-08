import json
import csv

def generate_discordids_json():
    discord_ids = []

    with open('blocksmith.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            discord_id, wallet_address, role = row
            if discord_id:
                discord_ids.append(discord_id)

    with open('discordIds.json', 'w') as f:
        json.dump(discord_ids, f, indent=2)


if __name__ == '__main__':
    generate_discordids_json()
import os
import motor.motor_asyncio
from dotenv import load_dotenv

from model import OverwatchGame
from model import RocketGame
from model import Smash
from model import SmashGame
from model import ValorantGame

# App Configurations
load_dotenv()

# Database Connection
client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('DATABASE_URL'))
database = client.Esports

# Collections
collection_smash_players = database.Smash_Players
collection_Smash_Games = database.Smash_Games
collection_valorant_games = database.Valorant_Games
collection_overwatch_games = database.Overwatch_Games
collection_rocket_games = database.Rocket_Games


# Smash Players Database Functions
# Smash Players - Get one
async def fetch_one_smash(Gamerstag):
    document = await collection_smash_players.find_one({"Gamerstag": Gamerstag})
    return document


# Smash Players - Get all
async def fetch_all_smash():
    smashes = []
    cursor = collection_smash_players.find({})
    async for document in cursor:
        smashes.append(Smash(**document))
    return smashes


# Smash Players - Create
async def create_smash(smash):
    document = smash
    result = await collection_smash_players.insert_one(document)
    return document


# Smash Players - Update
async def update_smash(Gamerstag, Main, Name, Esport):
    await collection_smash_players.update_one({"Gamerstag": Gamerstag},
                                              {"$set": {"Main": Main},
                                               "Esport": Esport,
                                               "Name": Name})
    document = await collection_smash_players.find_one({"Gamerstag": Gamerstag})
    return True


# Smash Players - Delete
async def remove_smash(Gamerstag):
    await collection_smash_players.delete_one({"Gamerstag": Gamerstag})
    return True


# Rocket Game Database Functions
# Rocket Game - Get one
async def fetch_one_rocketg(OppSchool):
    document = await collection_rocket_games.find_one({"OppSchool": OppSchool})
    return document


# Rocket Game - Get all
async def fetch_all_rocketg():
    rockg = []
    cursor = collection_rocket_games.find({})
    async for document in cursor:
        rockg.append(RocketGame(**document))
    return rockg


# Rocket Game - Create
async def create_rocketg(rocketga):
    document = rocketga
    result = await collection_rocket_games.insert_one(document)
    return document


# Rocket Game - Update
async def update_rocketg(OppSchool, Player1, player2, Player3, MountScore, OppScore, Result):
    await collection_rocket_games.update_one({"OppSchool": OppSchool},
                                             {"$set": {"Player1": Player1},
                                              "Name": player2,
                                              "Player3": Player3,
                                              "MountScore": MountScore,
                                              "OppScore": OppScore,
                                              "Result": Result})
    document = await collection_rocket_games.find_one({"OppSchool": OppSchool})
    return True


# Rocket Game - Delete
async def remove_rocketg(OppSchool):
    await collection_rocket_games.delete_one({"OppSchool": OppSchool})
    return True


# Smash Game Database Functions
# Smash Game - Get one
async def fetch_one_sgames(OppSchool):
    document = await collection_Smash_Games.find_one({"OppSchool": OppSchool})
    return document


# Smash Game - Get all
async def fetch_all_sgames():
    smash_games = []
    try:
        cursor = collection_Smash_Games.find({})
        async for document in cursor:
            smash_games.append(SmashGame(**document))
    except Exception as e:
        print(e)
    return smash_games


# Smash Game - Create
async def create_sgames(sgames):
    document = sgames
    result = await collection_Smash_Games.insert_one(document)
    return document


# Smash Game - Update
async def update_sgames(OppSchool, Player, playerCharacter, OpponentCharacter, MountStocks, OpponentStocks, Result):
    await collection_Smash_Games.update_one({"OppSchool": OppSchool},
                                            {"$set": {"Player": Player},
                                             "OpponentCharacter": OpponentCharacter,
                                             "playerCharacter": playerCharacter,
                                             "MountStocks": MountStocks,
                                             "OpponentStocks": OpponentStocks,
                                             "Result": Result})
    document = await collection_Smash_Games.find_one({"OppSchool": OppSchool})
    return True


# Smash Game - Delete
async def remove_sgames(OppSchool):
    await collection_Smash_Games.delete_one({"OppSchool": OppSchool})
    return True


# Valorant Game Database Functions
# Valorant Game - Get one
async def fetch_one_valorantg(OppSchool):
    document = await collection_valorant_games.find_one({"OppSchool": OppSchool})
    return document


# Valorant Game - Get all
async def fetch_all_valorantg():
    valg = []
    cursor = collection_valorant_games.find({})
    async for document in cursor:
        valg.append(ValorantGame(**document))
    return valg


# Valorant Game - Create
async def create_valorantg(valorantga):
    document = valorantga
    result = await collection_valorant_games.insert_one(document)
    return document


# Valorant Game - Update
async def update_valorantg(OppSchool, player1, player2, player3, player4, player5,
                           player1Character, player2Character, player3Character, player4Character, player5Character,
                           opponent1Character, opponent2Character, opponent3Character, opponent4Character,
                           opponent5Character, MountScore, OppScore, Result):
    await collection_valorant_games.update_one({"OppSchool": OppSchool},
                                               {"$set": {"player1": player1},
                                                "player2": player2,
                                                "player3": player3,
                                                "player4": player4,
                                                "player5": player5,
                                                "Player1Character": player1Character,
                                                "player2Character": player2Character,
                                                "player3Character": player3Character,
                                                "player4Character": player4Character,
                                                "player5Character": player5Character,
                                                "opponent1Character": opponent1Character,
                                                "opponent2Character": opponent2Character,
                                                "opponent3Character": opponent3Character,
                                                "opponent4Character": opponent4Character,
                                                "opponent5Character": opponent5Character,
                                                "MountScore": MountScore,
                                                "OppScore": OppScore,
                                                "Result": Result})
    document = await collection_valorant_games.find_one({"OppSchool": OppSchool})
    return True


# Valorant Game - Delete
async def remove_valorantg(OppSchool):
    await collection_valorant_games.delete_one({"OppSchool": OppSchool})
    return True


# Overwatch Game Database Functions
# Overwatch Game - Get one
async def fetch_one_overwatchg(OppSchool):
    document = await collection_overwatch_games.find_one({"OppSchool": OppSchool})
    return document


# Overwatch Game - Get all
async def fetch_all_overwatchg():
    overg = []
    cursor = collection_overwatch_games.find({})
    async for document in cursor:
        overg.append(OverwatchGame(**document))
    return overg


# Overwatch Game - Create
async def create_overwatchg(overwatchga):
    document = overwatchga
    result = await collection_overwatch_games.insert_one(document)
    return document


# Overwatch Game - Update
async def update_overwatchg(OppSchool, player1, player2, player3, player4, player5,
                            player1Character, player2Character, player3Character, player4Character, player5Character,
                            opponent1Character, opponent2Character, opponent3Character, opponent4Character,
                            opponent5Character, MountScore, OppScore, Result):
    await collection_overwatch_games.update_one({"OppSchool": OppSchool},
                                                {"$set": {"player1": player1},
                                                 "player2": player2,
                                                 "player3": player3,
                                                 "player4": player4,
                                                 "player5": player5,
                                                 "Player1Character": player1Character,
                                                 "player2Character": player2Character,
                                                 "player3Character": player3Character,
                                                 "player4Character": player4Character,
                                                 "player5Character": player5Character,
                                                 "opponent1Character": opponent1Character,
                                                 "opponent2Character": opponent2Character,
                                                 "opponent3Character": opponent3Character,
                                                 "opponent4Character": opponent4Character,
                                                 "opponent5Character": opponent5Character,
                                                 "MountScore": MountScore,
                                                 "OppScore": OppScore,
                                                 "Result": Result})
    document = await collection_overwatch_games.find_one({"OppSchool": OppSchool})
    return True


# Overwatch Game - Delete
async def remove_overwatchg(OppSchool):
    await collection_overwatch_games.delete_one({"OppSchool": OppSchool})
    return True


# Search Function
async def search_player(search):
    # Rocket Game
    rocket_game_data = []
    async for document in collection_rocket_games.find({'Player1': {'$regex': search}}):
        rocket_game_data.append(RocketGame(**document))

    async for document in collection_rocket_games.find({'Player2': {'$regex': search}}):
        rocket_game_data.append(RocketGame(**document))

    async for document in collection_rocket_games.find({'Player3': {'$regex': search}}):
        rocket_game_data.append(RocketGame(**document))

    # Smash Game
    smash_game_data = []
    async for document in collection_Smash_Games.find({'Player': {'$regex': search}}):
        smash_game_data.append(SmashGame(**document))

    # Valorant Game
    valorant_game_data = []
    async for document in collection_valorant_games.find({'Player1': {'$regex': search}}):
        valorant_game_data.append(ValorantGame(**document))

    async for document in collection_valorant_games.find({'Player2': {'$regex': search}}):
        valorant_game_data.append(ValorantGame(**document))

    async for document in collection_valorant_games.find({'Player3': {'$regex': search}}):
        valorant_game_data.append(ValorantGame(**document))

    async for document in collection_valorant_games.find({'Player4': {'$regex': search}}):
        valorant_game_data.append(ValorantGame(**document))

    async for document in collection_valorant_games.find({'Player5': {'$regex': search}}):
        valorant_game_data.append(ValorantGame(**document))

    # Overwatch Game
    overwatch_game_data = []
    async for document in collection_overwatch_games.find({'Player1': {'$regex': search}}):
        overwatch_game_data.append(OverwatchGame(**document))

    async for document in collection_overwatch_games.find({'Player2': {'$regex': search}}):
        overwatch_game_data.append(OverwatchGame(**document))

    async for document in collection_overwatch_games.find({'Player3': {'$regex': search}}):
        overwatch_game_data.append(OverwatchGame(**document))

    async for document in collection_overwatch_games.find({'Player4': {'$regex': search}}):
        overwatch_game_data.append(OverwatchGame(**document))

    async for document in collection_overwatch_games.find({'Player5': {'$regex': search}}):
        overwatch_game_data.append(OverwatchGame(**document))

    data = {
        'rocket_game': rocket_game_data,
        'smash_game': smash_game_data,
        'valorant_game': valorant_game_data,
        'overwatch_game': overwatch_game_data
    }

    return data

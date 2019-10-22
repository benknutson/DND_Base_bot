# home_base_bot.py
import os
import discord
import random
#resoruces total
res=[80,0,0,0,0,0,0]
#population, lumber, stones, labor, magic,trasury

#resource generation
lumber_perday=0
stones_perday=0
income_perday=0
labor_perday=0
magic_perday=0
upkeep_perday=0

discord_token=""
#get details from file

def load_stats():
    f= open("stats.txt","r")
    i=0
    for line in f:
        res[i]=int(line)
        i+=1
    
    print (resource_totals())
    
def load_discord_token():
    with open("key.txt","r") as f:
        discord_token=f.readline()
    
    


#return a string that can be logged or printed
def resource_totals():
    return "Popululation:"+str(res[1])+"\nLumber:"+str(res[1])+"\nStones:"+str(res[2])+"\nLabor"+str(res[3])+"\nMagic:"+str(res[4])+"\nTreasury:"+str(res[5])

def upkeep_table():
    roll=random.randint(1,101)
    if roll > 0 and roll < 11:
        print("No income, bad day. Upkeep cost still applies")
    elif roll > 10 and roll < 51:
        print("standard day, profit =income-upkeep")
    elif roll > 50 and roll < 61:
        print("Good day, profit =(income-upkeep)*1.25 25% more profit")
    elif roll > 60 and roll < 81:
        print("Good day, profit =(income-upkeep)*1.5 50% more profit")
    elif roll > 80 and roll < 91:
        print("Good day, profit =(income-upkeep)*1.75 75% more profit")
    elif roll > 90 and roll < 101:
        print("Good day, profit =(income-upkeep)*2 100% more profit")






#from dotenv import load_dotenv

#load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author==client.user:
        return
    total=resource_totals()
    if message.content =='base totals please':
        await message.channel.send(total)
        print(total)
        
        
        
load_stats()
client.run(discord_token)
# home_base_bot.py
import os
import discord
import random
import schedule
import time



#resoruces total
res=[80,0,0,0,0,0,0,0,0,0,0,0]
#population, lumber, stones, labor, magic,trasury, lumber_perday,stones_perday,labor, magic, income_perday,upkeep



discord_token=""

#get details from file

def load_stats():
    f= open("stats.txt","r")
    i=0
    for line in f:
        res[i]=int(line)
        i+=1
    print(res)
    print (resource_totals())
    print (production_totals())
    
def load_discord_token():
    with open("key.txt","r") as f:
        return f.read().rstrip("\n")


#return a string that can be logged or printed
def resource_totals():
    return "Population:"+str(res[1])+"\nLumber:"+str(res[1])+"\nStones:"+str(res[2])+"\nLabor"+str(res[3])+"\nMagic:"+str(res[4])+"\nTreasury:"+str(res[5])


def production_totals():
    return "lumber Per Day:"+str(res[6])+"\nStones Per Day:"+str(res[7])+"\nLabor Per Day:"+str(res[8])+"\nMagic Per Day"+str(res[9])+"\nIncome Per Day:"+str(res[10])+"\nUpkeep Per Day:"+str(res[11])


token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    discord_channel=client.get_channel(634250073823510529)
    await discord_channel.send('I have awakened')
   
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author==client.user:
        return
    t
    if message.content =='base totals please':
        await message.channel.send(resource_totals())
        print(resource_totals())
    if message.content =='base productiom please':
        await message.channel.send(production_totals())
        print(production_totals())
        
        
        
load_stats()
client.run(load_discord_token())

# home_base_bot.py
import os
import discord
import random
import schedule
import time



#resoruces total
res=[80,0,0,0,0,0,0,0,0,0,0,0]
#population, lumber, stones, labor, magic,trasury, lumber_perday,stones_perday,labor, magic, income_perday,upkeep

def resource_totals():
    return "Population:"+str(res[0])+"\nLumber:"+str(res[1])+"\nStones:"+str(res[2])+"\nLabor"+str(res[3])+"\nMagic:"+str(res[4])+"\nTreasury:"+str(res[5])


def production_totals():
    return "lumber Per Day:"+str(res[6])+"\nStones Per Day:"+str(res[7])+"\nLabor Per Day:"+str(res[8])+"\nMagic Per Day"+str(res[9])+"\nIncome Per Day:"+str(res[10])+"\nUpkeep Per Day:"+str(res[11])






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
        
    
def random_event():
    pass

async def upkeep_event():
    return_string=""
    roll=random.randint(1,101)
    if roll > 0 and roll < 11:
        res[6]=res[6]-res[11]
        return_string ="No income, bad day. Upkeep cost still applies\n Income ="+str(-res[11])
        
    elif roll > 10 and roll < 51:
        res[6]=res[6]-res[11]+res[10]
        return_string="standard day, profit =income-upkeep\n income ="+str(-res[11]+(res[10]))
        
    elif roll > 50 and roll < 61:
        res[6]=res[6]-res[11]+1.25(res[10])
        return_string ="Good day, profit =(income-upkeep)*1.25 25% more profit\n Income ="+str(-res[11]+1.25*(res[10]))
        
    elif roll > 60 and roll < 81:
        res[6]=res[6]-res[11]+1.5(res[10])
        return_string= "Good day, profit =(income-upkeep)*1.5 50% more profit\n Income ="+str(-res[11]+1.5*(res[10]))
        
    elif roll > 80 and roll < 91:
        res[6]=res[6]-res[11]+1.75(res[10])
        return_string="Good day, profit =(income-upkeep)*1.75 75% more profit\n Income ="+str(-res[11]+1.75*(res[10]))
        
    elif roll > 90 and roll < 101:
        res[6]=res[6]-res[11]+2(res[10])
        return_string ="Good day, profit =(income-upkeep)*2 100% more profit\n Income ="+str(-res[11]+2*(res[10]))
        
    res[0]+=res[0]*.1#assumine 10% growth per week, will adjust as needed    
    res[1]+=res[6]
    res[2]+=res[7]
    res[3]+=res[8]
    res[4]+=res[9]
    
    return_string+="\n"+resource_totals()
    discord_channel=client.get_channel(634250073823510529)
    await discord_channel.send(return_string)
    
    



schedule.every(1).minutes.do(upkeep_event)
schedule.every(2).minutes.do(random_event)

    
        

#from dotenv import load_dotenv

#load_dotenv()
discord_token=load_discord_token()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    discord_channel=client.get_channel(634250073823510529)
    while True:
        schedule.run_pending()
        print ("tick")
        time.sleep(5)
    
   # await discord_channel.send('I have awakened')
   
    print(f'{client.user} has connected to Discord!')



        
        
discord_token=load_discord_token()

load_stats()
client.run(discord_token)






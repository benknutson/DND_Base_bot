# home_base_bot.py
import os
import discord
import random
import schedule
import time

   

client = discord.Client()
class town:
    def __init__(self):
        self._name=""
        self._res=[100,0,0,0,0,0,0,0,0,0,0,0]
        self._channel=634250073823510529
        self.message=""
    
    def __init__(self, name):
        self._name=name
        self._res=[100,0,0,0,0,0,0,0,0,0,0,0]
        self._channel=634250073823510529
        self.message=""
        
    def get_name(self):
        return self._name
    
    
    def get_res(self):
        return self._res
    
    def get_channel(self):
        return self._channel
    
    def get_message(self):
        return self.message
            
    def set_name(self, name_pass):
        self._name=name_pass

    def set_res(self, res_pass):
        self._res=res_pass
        
    def set_channel(self, channel_pass):
        self._channel=channel_pass
        
    def set_message(self, message_pass):
        self.message=message_pass

    def production_totals(self):
        return "lumber Per Day:"+str(self._res[6])+"\nStones Per Day:"+str(self._res[7])+"\nLabor Per Day:"+str(self._res[8])+"\nMagic Per Day"+str(self._res[9])+"\nIncome Per Day:"+str(self._res[10])+"\nUpkeep Per Day:"+str(self._res[11])

    def resource_totals(self):
        return "Population:"+str(self._res[0])+"\nLumber:"+str(self._res[1])+"\nStones:"+str(self._res[2])+"\nLabor"+str(self._res[3])+"\nMagic:"+str(self._res[4])+"\nTreasury:"+str(self._res[5])

    def save_to_file(self):
        filename=self._name+".txt"
        f=open(filename, "w")
        for each in self.get_res():
            f.write(str(each)+"\n")
        f.write(str(self.get_channel()))
        f.close()
        pass
    
    def load_from_file(self):
        
        filename=self._name+".txt"
        if os.path.isfile(filename):
            f= open(filename,"r")
            i=0
            for line in f:
                if i < len(self._res):
                    self._res[i]=int(line)
                else:
                    self._channel=int(line)
                i+=1
            f.close()
        else:
            self.save_to_file()
        pass

#I place my token in a key.txt file
def load_discord_token():
    with open("key.txt","r") as f:
        return f.read().rstrip("\n")
        
    
def random_event(town):
    pass

async def upkeep_event():
    for town in towns:
        res=town.get_res()
        return_string=""
        roll=random.randint(1,101)
        if roll > 0 and roll < 11:
            res[6]=res[6]-res[11]
            return_string ="No income, bad day. Upkeep cost still applies\n Income ="+str(-res[11])
        elif roll > 10 and roll < 51:
            res[6]=res[6]-res[11]+res[10]
            return_string="standard day, profit =income-upkeep\n income ="+str(-res[11]+(res[10]))
        elif roll > 50 and roll < 61:
            res[6]=res[6]-res[11]+1.25*(res[10])
            return_string ="Good day, profit =(income-upkeep)*1.25 25% more profit\n Income ="+str(-res[11]+1.25*(res[10]))
        elif roll > 60 and roll < 81:
            res[6]=res[6]-res[11]+1.5*(res[10])
            return_string= "Good day, profit =(income-upkeep)*1.5 50% more profit\n Income ="+str(-res[11]+1.5*(res[10]))
        elif roll > 80 and roll < 91:
            res[6]=res[6]-res[11]+1.75*(res[10])
            return_string="Good day, profit =(income-upkeep)*1.75 75% more profit\n Income ="+str(-res[11]+1.75*(res[10]))
        elif roll > 90 and roll < 101:
            res[6]=res[6]-res[11]+2*(res[10])
            return_string ="Good day, profit =(income-upkeep)*2 100% more profit\nIncome ="+str(-res[11]+2*(res[10]))
        
        res[0]+=int(res[0]*.1)#assumine 10% growth per week, will adjust as needed    
        res[1]+=int(res[6])
        res[2]+=int(res[7])
        res[3]+=int(res[8])
        res[4]+=int(res[9])
        town.set_res(res)
        town.save_to_file
        return_string+="\n"+town.resource_totals()
        town.set_message(return_string)
        town.save_to_file()
        await message_perhaps()
    
    

    

    



schedule.every(1).minutes.do(upkeep_event)
schedule.every(2).minutes.do(random_event)

    

async def message_perhaps():
    client.login(discord_token)
    for town in towns:
        discord_channel=client.get_channel(town.get_channel())
        await discord_channel.send(town.get_message())
        
    
    


@client.event
async def on_ready():
    await upkeep_event
    print(f'{client.user} has connected to Discord!')
    for town in towns:
        discord_channel=client.get_channel(town.get_channel())
        await discord_channel.send(town.get_message())
    
    while True:
        schedule.run_pending()
        print ("tick")
        time.sleep(5)
    
   
        
        
    
   # await discord_channel.send('I have awakened')
   
    
#load towns
towns=[]
f= open("towns.txt","r")
i=0
for line in f:
    towns.append(town(line.rstrip("\n")))
    i+=1
f.close()
       
for each in towns:
    each.load_from_file()
    print(each.get_name())        


discord_token=load_discord_token()
token = os.getenv('DISCORD_TOKEN')

discord_token=load_discord_token()

client.run(load_discord_token())







import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

token = "MTE2MTMwMDM2ODg0NDY3MzAzNA.GljyKh.yGKLw5foPj_xT-DrlZsx_v_XSnAj5VUQq022IM"

async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
@client.event
async def on_ready():
        print(f"Logged in as {client.user.name} Id is = {client.user.id}")
  
@client.command(name="ping")
async def ping(ctx):
  await ctx.send(f"Pong! Latency is {round(client.latency * 1000)}ms")

@client.command(name="send")
async def send(ctx, *, msg):
    if ctx.author.id == 863508137080127518:
        await ctx.send.embed(msg)
    
    client.run(token)
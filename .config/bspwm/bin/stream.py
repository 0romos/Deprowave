#!/usr/bin/python
import discord, asyncio, sys, time, os, io, shutil
client = discord.Client()
token = "ODg5MTQ1ODc5NTgyMzc1OTg3.Gtusz9.cJewqbX_VNT6XMSKW46ncTUq0QVSPxn1NPqIPA"
from discord.ext import (
    commands,
    tasks
)

intents = discord.Intents.all()

client = commands.Bot(
    description='Set Stream Status',
    command_prefix="<:>",
    intents=intents,
    self_bot=True
)

    
@client.event
async def on_connect():
    width = shutil.get_terminal_size().columns

    def ui():
        print()
        print("► Set Stream Status ".center(width))
        print("► Made by slash".center(width))
        print("► User: {0}".format(client.user).center(width))
    ui()

    stream = discord.Streaming(
        name="‎‎ ‎",
        url="https://twitch.tv/zzz", 
    )
    await client.change_presence(activity=stream) 
    print("")
    print("")
    print("→ You are currently streaming: {0} ".format("صليل الصوارم").center(width))



client.run(token, bot=False)

import os
import discord
from discord.ext import commands

cogs = [
    "create" #create clan
]

class Main(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

client = Main(
    command_prefix = "c.",
    help_commands = None,
    intents = discord.Intents.all()
)

@client.event
async def on_ready():
    print("I'm ready")

if __name__ == "__main__":
    for extension in cogs:
        cog = f"commands.{extension}"
        try:
            client.load_extension(cog)
        except Exception as e:
            print(e)


client.run("token")

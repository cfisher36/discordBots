import discord
from discord.ext import commands
from playerBot import Player

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix= "!", intents = intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} booting . . .")

async def setup():
    await bot.wait_until_ready()
    bot.add_cog(Player(bot))

bot.loop.create_task(setup())

#INSERT KEY
bot.run()

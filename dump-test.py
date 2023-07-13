import discord
from discord.ext import commands
from privateToken import Discord_api_K3y

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Logged on as', bot.user)
    guild = await bot.fetch_guild(1120727916528017638)
    member_count = guild.member_count
    print(f"Total member count: {member_count}")
    async for member in guild.fetch_members(limit=150):
        print(member.name)

@bot.event
async def on_member_join(member):
    welcome_channel = discord.utils.get(member.guild.channels, name='welcome')  # Replace 'welcome' with the name of your welcome channel

    if welcome_channel:
        await welcome_channel.send(f"Welcome, {member.mention}! Enjoy your stay in our server.")

bot.run(Discord_api_K3y())

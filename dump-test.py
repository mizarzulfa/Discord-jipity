## Discord members ongoing development
import discord
from discord.ext import commands
from privateToken import Discord_api_K3y
import asyncio

# intents = discord.Intents.default()
# intents.message_content = True
# intents.guilds = True
# intents.members = True
#enabling all intents 
intents = discord.Intents().all()

# bot = commands.Bot(command_prefix='!', intents=intents)
bot = discord.Bot(intents=intents)


class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="A button", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
      button.disabled = True # set button.disabled to True to disable the button
      button.label = "No more pressing!" # change the button's label to something else
      await interaction.response.edit_message(view=self) # edit the message's view
      
# @bot.slash_command() # Create a slash command
# async def button(ctx):
#     await ctx.respond("This is a button!", view=MyView()) # Send a message with our View class that contains the button

@bot.event
async def on_ready():
    print('Logged on as', bot.user)
    # guild = await bot.fetch_guild(1120727916528017638)
    # member_count = guild.member_count
    # print(f"Total member count: {member_count}")
    # async for member in guild.fetch_members(limit=150):
    #     print(member.name)

@bot.event
async def on_member_join(member):
    
    channel_name = f"{member.name}-gpt-convesation"  # Customize the channel name based on your preference
    # Create a new text channel for the member
    new_channel = await member.guild.create_text_channel(channel_name)
    
    # Set permissions for the new channel
    await new_channel.set_permissions(member, read_messages=True, send_messages=True)
    
    # Find the 'general' channel
    general_channel = discord.utils.get(member.guild.channels, name='gpt-conversation')

    # Modify permissions for the 'general' channel
    await general_channel.set_permissions(member, read_messages=False)
    
    view = MyView()
    await new_channel.send("This is a button!", view=view)
    
    welcome_channel = discord.utils.get(member.guild.channels, name=channel_name)
    if welcome_channel:
        await asyncio.sleep(2)
        
        ## Assign role
        role_names = ["Guest"]  # Specify the names of the roles you want to assign
        roles = [discord.utils.get(member.guild.roles, name=role_name) for role_name in role_names]
        # Filter out None values (roles that were not found)
        roles = [role for role in roles if role is not None]
        await member.add_roles(*roles)
        
        ## Welcome message
        await welcome_channel.send(f"Welcome {member.mention}! Enjoy your stay in our server.")
        
        ## Kick Period
        await asyncio.sleep(40)  # Wait for 10 sec
        guild = bot.get_guild(1120727916528017638)
        target_role_name = "Guest"  # Replace with the name of the target role
        target_member_name = "jackkmo"  # Replace with the name of the member you want to kick
        for member in guild.members:
            # Check if the member has the target role
            if target_role_name in [role.name for role in member.roles] and member.name == target_member_name:
                await member.kick(reason="Kicked after 40 seconds")
                delete_channel = discord.utils.get(guild.channels, name=channel_name)  # Replace 'channel_name' with something
                await delete_channel.delete()
                
    
async def button(ctx):
    await ctx.respond("This is a button!", view=MyView())
                
bot.run(Discord_api_K3y())
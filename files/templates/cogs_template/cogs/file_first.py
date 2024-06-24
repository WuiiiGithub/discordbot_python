# general imports
import discord
from discord.ext import commands
from discord import app_commands

# Let's say this file is about interacting with other users.

# The below class is inherited from commands.Cog class
class Talk(commands.Cog):
    # Class implementation goes here
    def __init__(self, bot):
        self.bot = bot
        print("Entered Cogs")
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Syncing Bot Tree")
        # As soon as the cog gets active or ready, the bot's tree of commands gets synced.
        await self.bot.tree.sync()

    # Example of message commands
    @commands.command()
    async def greet(self, ctx: commands.Context, user: discord.User, message: str):
        print("Entered greet command")
        # For you to be familiar with good looking messages also called embeds
        # I am going to give you the structure of it.
        embed = discord.Embed(title=f"Greetings from {user.display_name}", description=message, color=0x3498db)
        
        # Now sending the embed
        await ctx.send(content=user.mention, embed=embed)

    # Example of an app command
    @app_commands.command(name="announce", description="Announce something in a text channel.")
    async def announce(self, inter: discord.Interaction, channel: discord.TextChannel, title: str, message: str):
        embed = discord.Embed(title=title, description=message, color=0x3498db)
        # Get the channel first
        await channel.send(embed=embed)

        await inter.response.send_message("Your message has successfully been delivered.", ephemeral=True)
        # If ephemeral is True, only you can see this message.
        # This feature is not available for message context commands.

    # Registering events in this.
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return  # Ignore messages sent by the bot itself
        
        if "lol" in message.content.lower():
            await message.channel.send(":joy:")  # Sends laughing emoji

async def setup(bot):
    talk_cog = Talk(bot)
    await bot.add_cog(talk_cog)

    # If you have a list of guilds to load the bot's commands
    guild_ids = ["PASTE STRINGS OF LIST OF GUILD IDS"]  # Replace with your actual guild IDs if needed
    for guild_id in guild_ids:
        for command in talk_cog.__cog_app_commands__:
            print(f"Adding {command.name} in server with ID {guild_id}.")
            bot.tree.add_command(command, guild=discord.Object(id=guild_id))
    
    # If you want to sync things globally, use this instead
    # for command in talk_cog.__cog_app_commands__:
    #     bot.tree.add_command(command)

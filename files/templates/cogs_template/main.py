"""
Run this file while staying in the `cogs_template` folder.
"""
import discord
import asyncio, os
# if you are using app commands in main file import it
# from discord import app_commands
from discord.ext import commands

intents=discord.Intents.all()
bot=commands.Bot(command_prefix=".", intents=intents)
# bot=bot.tree
async def load():
    # We will put all those distributed files in a folder called cogs
    # Hence we are listing each and every filename from there bellow
    for filename in os.listdir('cogs'):
        # We got a file name from the list of file names
        # Note that this filename should be a python file to consider loading
        # So, we can avoid rest of the files by just checking weather it ends with '.py' 
        if filename.endswith('.py'):
            print(f"Loading {filename}")
            # Now we will just take name of file without extension for loading. 
            await bot.load_extension(f"cogs.{filename[:-3]}")
            # 'bot.load_extension' function loads the file given its path.
            # Here loading file means it makes the commands written by you there to execute.
            # (in simple terms)

            # similary there is an bot.unload_extension() function which helps in unloading

# making a function which would both load and run the bot.
async def main():
    await load() # This keeps loading
    await bot.start("YOUR BOT TOKEN HERE") # this is just to start the bot
    
    """
    The primary difference between bot.start() and bot.run() in discordpy lies in their approach to manage these event loops. bot.run() is a high-level method that handles the entire setup, including creating and running the event loop, managing exceptions, and ensuring a clean shutdown. This makes it ideal for simple codes where you want the library to manage everything automatically. Where as, bot.start() is a low-level function or method that you must run within an existing event loop, giving you more control and flexibility over the bot's execution. This is suitable for more complex applications where you need to manage multiple asynchronous tasks or integrate the bot with other asyncio-based code.
    """
# Now running the above made function asynchronously together
asyncio.run(main())
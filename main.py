import discord
from discord.ext import commands
from discord import app_commands
import logging
from dotenv import load_dotenv
import os
import random

# This bot is a simple Discord bot that demonstrates various functionalities such as role assignment, message handling, and command processing.
# It uses the discord.py library and dotenv for environment variable management.
# The bot includes commands for greeting users, assigning roles, removing roles, sending direct messages, and creating polls.
# It also handles specific message content and user join events.
# The bot is designed to be run in a Discord server and requires a valid Discord token to function.

# Load the bot token securely from a .env file (safer than hardcoding it)
# Ensure you have a .env file with the line DISCORD_TOKEN=your_token_here
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Set up logging to track bot activity and errors
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Define the bot's permissions (intents) -- what kind of data it can acess
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to read message content/text
intents.members = True          # Allows the bot to access member data (needed to welcome new members)
intents.presences = True        # Allows the bot to access presence data (online/offline status)

# Initialize the bot with a command prefix (/) and the specified intents
# The command prefix is what users will type before commands (e.g., /hello)
bot = commands.Bot(command_prefix='/', intents=intents)

secret_role = "Ghosts of Reach"  # Role name for the secret command

# Event triggered when the bot is ready and successfully connects to Discord
@bot.event
async def on_ready():
    await bot.tree.sync()  # Sync the command tree with Discord
    print(f'🟢 [FRET] System online. Logged in as {bot.user}.')

# Event triggered when a new member joins the server
# Sends a welcome message to the new member via direct message (DM) and a specific channel in the server
@bot.event
async def on_member_join(member):
    await member.send(f'Hey Spartan, {member.name}! 👋 Thanks for joining the Spartan Army Halo Community! 💪🔥 Please read the server rules & connect with Real Life Spartan on his socials! We cannot wait to see you on the battle field! HOORAH! 🫡')

    guild = member.guild # Get the guild (server) the member joined
    channel = discord.utils.get(guild.text_channels, name="・spartan・comms")  # Replace "testing-bot" with the name of your desired channel
    if channel:
        await channel.send(f'Welcome aboard, {member.mention}! You are now enlisted in the Spartan Army! 💪🔥 Real Life Spartan (RLS) has you on radar. 🫡')

# Event triggered when a member leaves the server
# Sends a farewell message to the server channel
@bot.event
async def on_member_remove(member):
    guild = member.guild  # Get the guild (server) the member left
    channel = discord.utils.get(guild.text_channels, name="・spartan・comms")  # Replace "testing-bot" with the name of your desired channel
    if channel:
        await channel.send(f'Farewell Spartan, {member.name}! 👋 We will remember your service and commitment to the Spartan Army. 🫡❤️‍🔥')

# Event triggered when a message is sent in the server
# Checks if the message contains certain words and deletes it if it does
# Sends a warning message to the user who sent the message
# This is a simple filter to prevent certain words from being used in the server
# This is a basic moderation feature to maintain a respectful environment in the server
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    NSFW_words = ["nsfw", "sex", "porn", "nude", "naked", "hentai", "xxx", "18+", "erotic", "fetish", "kink", "lewd", "smut", "perverted"]
    # Check if the message contains any violation words (NSFW_words)
    # If it does, delete the message and send a warning to the user, mods will take care of the rest
    # This is a simple filter to prevent certain words from being used in the server
    for word in NSFW_words:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send(f"🛑 {message.author.mention} - **NSFW content is restricted!** This is a warning. Remember the server rules, Spartan.")
            await message.author.send(f"🛑 {message.author.name} - Please follow the Real Life Spartan (RLS) server rules, for next time, Spartan!")
            return
    
    Politcal_words = ["politics", "political", "election", "government", "republican", "democrat"]
    # Check if the message contains any violation words (Politcal_words)
    # If it does, delete the message and send a warning to the user, mods will take care of the rest
    # This is a simple filter to prevent certain words from being used in the server
    for word in Politcal_words:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send(f"🛑 {message.author.mention} - **Political discussion detected!** This is a warning. Remember the server rules, Spartan.")
            await message.author.send(f"🛑 {message.author.name} - Please follow the Real Life Spartan (RLS) server rules, for next time, Spartan!")
            return


    Religous_words = ["religion", "religious", "bible", "gospel", "scripture", "sinful", "quaran", "mashallah", "allah", "inshallah", "christianty", "catholic", "jewish", "buddhist", "mormon", "hindu", "jehovah"]
    # Check if the message contains any violation words (Religous_words)
    # If it does, delete the message and send a warning to the user, mods will take care of the rest
    # This is a simple filter to prevent certain words from being used in the server
    for word in Religous_words:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send(f"🛑 {message.author.mention} - **Be advised -- no religous chats in the Spartan Army please!** This is a warning. Remember the server rules, Spartan.")
            await message.author.send(f"🛑 {message.author.name} - Please follow the Real Life Spartan (RLS) server rules, for next time, Spartan!")
            return
    
    await bot.process_commands(message)

# /status
# This command sends a message to the channel where it was invoked, mentioning the user who invoked it
@bot.command()
async def status(ctx):
    await ctx.send(f'🟢 All systems online. Hello, {ctx.author.mention}. Monitoring Spartan channels... Awaiting your command, Spartan.')

# /believe
# This command sends a message to the channel where it was invoked, mentioning the user who invoked it
@bot.command()
async def believe(ctx):
    await ctx.send(f'BELIEVEEEEE!!!!! 🔥🔥🔥')

# /spartan
# This command sends a message to the channel where it was invoked, mentioning the user who invoked it
@bot.command()
async def spartan(ctx):
    await ctx.send(f'Set a fire in your heart Spartan, {ctx.author.mention}! ❤️‍🔥')

# /hype
# This command sends a hype message to the channel where it was invoked
@bot.command()
async def hype(ctx):
    await ctx.send(f'HALO NIGHT STREAM HYPE!!! 🔥🔥🔥')

# /dm
# This command sends a direct message (DM) to the user who invoked it
@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f'🚀 DM delivery for {ctx.author.name}. You said: "{msg}"')
    await ctx.send(f'Copy that! 🫡 DM was sent to {ctx.author.name}! ')

# /reply
# This command replies to the user who invoked it with a message mentioning them
@bot.command()
async def reply(ctx):
    await ctx.send(f'Afirmative Spartan, {ctx.author.mention}! 🫡 This is a reply to your message!')

# /poll
# This command creates a poll with the given question and adds reactions for voting
@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="Poll", description=question, color=discord.Color.green())
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")

# /socials
# This command sends a message with links to RLS's social media accounts
@bot.command()
async def socials(ctx):
    await ctx.send(f'Support Real Life Spartan (RLS) and join the Spartan Army on every platform!')
    await ctx.send('🟣 Twitch: https://www.twitch.tv/reallifespartan')
    await ctx.send('🔵 Twitter/X: https://twitter.com/RealLifeSpartan')
    await ctx.send('🔴 YouTube: https://www.youtube.com/RealLifeSpartan')
    await ctx.send('⚪ Instagram: https://www.instagram.com/real_life_spartan/')
    await ctx.send('⚫ TikTok: https://www.tiktok.com/@reallifespartan ')
    await ctx.send('🟢 My Site: https://www.reallifespartan.com/')

# /8ball
# This command simulates an 8-ball fortune teller, responding to a question with a random answer
@bot.command(name='8ball')
async def eight_ball(ctx, *, question):
    responses = [
        "Affirmative.",
        "Negative.",
        "It is certain, Spartan.",
        "That's a hard copy.",
        "Reply hazy -- recalibrating...",
        "Ask again later, Spartan.",
        "BELIEVE.. it will happen.",
        "Do not proceed -- mission failure imminent.",
        "FRET advices caution.",
        "Confirmed. Victory is near.",
        "117% chance of success.",
    ]
    answer = random.choice(responses)
    await ctx.send(f'🗨️ {ctx.author.mention}, FRET the AI says: "{answer}"')

# /assign
# This command assigns a role to the user who invoked it
# The role is specified by the variable secret_role
# The role must exist in the server for this command to work
# If the role is not found, it sends a message indicating that the role was not found
@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention}, you have been assigned the {secret_role} role!")
    else:
        await ctx.send("Role not found, sorry Spartan!")

# /remove
# This command removes the specified role from the user who invoked it
# The role is specified by the variable secret_role
# The role must exist in the server for this command to work
# If the user does not have the role, it sends a message indicating that they don't have it
# If the role is not found, it sends a message indicating that the role was not found
@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role in ctx.author.roles:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention}, you have been removed from the {secret_role} role!")
    else:
        await ctx.send("You don't have that role, sorry Spartan!")

# This command is a secret command that can only be used by users with the specified role (secret_role)
# It sends a message to the user who invoked it, indicating that they have access to the secret command
@bot.command()
@commands.has_role(secret_role)
async def secret(ctx):
    await ctx.send(f"{ctx.author.mention}, you have access to the secret command! Welcome to the Noble Team, Spartan!")

# This command is an error handler for the secret command
# It checks if the user has the required role to use the command
# If the user does not have the role, it sends a message indicating that they don't have the required role
# This is a simple permission check to ensure that only users with the specified role can use the command
@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f"{ctx.author.mention}, you don't have the required role to use this command! Sorry, Spartan.")

# /ping
# This command checks if the bot is online and responds with a message indicating that it is online
# Used bot.tree.command to create a slash command (for Discord developer badge)
@bot.tree.command(name="ping", description="Check if the bot is online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'🏓 Pong! Spartan AI online, {interaction.user.mention}!')

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
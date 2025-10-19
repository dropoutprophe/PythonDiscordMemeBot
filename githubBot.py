import discord
from discord.ext import commands
import random

# Bot setup with command prefix
bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

# List of meme URLs (you can add your own meme links here)
MEME_URLS = [
    "https://i.imgflip.com/30b1gx.jpg",
    "https://i.imgflip.com/1bij.jpg",
    "https://i.imgflip.com/265k.jpg",
    "https://i.imgflip.com/1g8my4.jpg",
    "https://i.imgflip.com/26am.jpg"
]

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is ready to send memes!')

@bot.command(name='meme')
async def send_meme(ctx):
    """Sends a random meme when $meme is typed"""
    meme_url = random.choice(MEME_URLS)
    await ctx.send(meme_url)

# Replace 'YOUR_BOT_TOKEN_HERE' with your actual Discord bot token
bot.run('YOUR_BOT_TOKEN_HERE')
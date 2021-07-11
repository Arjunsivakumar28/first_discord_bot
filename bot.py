from discord.ext import commands
import random
from PyDictionary import PyDictionary

bot = commands.Bot(command_prefix='!')

"""
@bot.command(name="idea", help="send ideas if you don't have ideas")
async def idea(ctx):
    await ctx.send("Ideas ardcfvghbjnk")
    await ctx.send("i gotchu fam")

    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', "j"]
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bam = f'how about {random.choice(abc)} with {random.choice(num)}'
    await ctx.send(bam)



@bot.command(name='maths', help="perform basic maths")
async def maths(ctx, x: float, fn: str, y: float):
    if fn == '+':
        await ctx.send(x + y)
    elif fn == '-':
        await ctx.send(x - y)
    elif fn == '*':
        await ctx.send(x * y)
    elif fn == '/':
        await ctx.send(x / y)
    elif fn == '**':
        await ctx.send(x**y)
    else: 
        await ctx.send("Only basic 4 operations")

@bot.command()
async def thanks(ctx):
    await ctx.send("no problem!")

"""
class keyValue(dict):
    def __init__(self):
        self = dict()
    
    def add(self, key, value):
        self[key] = value

@bot.command(name="check", help="checks for repetition of words in text")
async def check(ctx, *args):
    list = keyValue()
    for arg in args:
        count = args.count(arg)
        if count > 1:
            list.add(arg, count)
    if len(list) == 0:
        await ctx.send("no repetition")
    else:
        await ctx.send(list)

with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)
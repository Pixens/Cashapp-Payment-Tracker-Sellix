import discord, datetime
from discord.ext import commands
from server import *
from log import *

config = json.load(open("config.json", encoding="utf-8"))

activity = discord.Activity(type=discord.ActivityType.watching, name = "Cashapp payments on boostup.cc")
bot = commands.Bot(command_prefix = ">", intents = discord.Intents.all(), activity = activity)


@bot.event
async def on_ready():
    print()
    info("[+]", f"{bot.user} is online.")
    print()

    

@bot.slash_command(guild_ids = [config["guildID"]], name="balance", description="Check cashapp balance.")
async def check_bal(ctx):
    
    if ctx.author.id not in config['whitelist']:
        return await ctx.respond(embed = discord.Embed(title = "**No Permission**", description = f"You don't have permission to run this command", colour = 0x880808))
    balance = json.load(open("balance.json", encoding="utf-8"))
    return await ctx.respond(embed = discord.Embed(title = "**Cashapp Balance**", description = f"${balance['current_balance']}", colour = 0x4598d2))

    
@bot.slash_command(guild_ids = [config["guildID"]], name="reset", description="Reset's the cashapp balance.")
async def reset_bal(ctx):

    if ctx.author.id not in config['whitelist']:
        return await ctx.respond(embed = discord.Embed(title = "**No Permission**", description = f"You don't have permission to run this command", colour = 0x880808))
    
    balance = json.load(open("balance.json", encoding="utf-8"))
    debug("[-]", f"Balance reset. Balance before reset: ${balance['current_balance']}")
    open("logs.txt", "a").write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}|[-] Balance reset. Balance before reset: ${balance['current_balance']}\n")
    
    balance = {
    "current_balance": 0
    }
    
    json_object = json.dumps(balance, indent=4)
    with open("balance.json", "w") as outfile:
        outfile.write(json_object)
    return await ctx.respond(embed = discord.Embed(title = "**Success**", description = f"Successfully reset the cashapp balance.", colour = 0x4598d2))

keep_alive()
try:
    bot.run(config['bot_token'])
except Exception as e:
    error(f'[!]', "Error starting bot", {"error": e})
    

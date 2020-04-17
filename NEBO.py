import discord
import random
from discord.ext import commands, tasks
from discord.utils import get
import youtube_dl
import os
from os import system
from itertools import cycle

# Bot_Prefix_Variable : 
prfx = '.'

# Bot_Setup :

client = commands.Bot(command_prefix=prfx)

# Bot_Remove_Existing_Help_Command :

client.remove_command('help')


# Bot_Status_Cycle

status = cycle(['Hello there!','I am NEBO',])


# Bot_Ready_Event:

@client.event
async def on_ready():
    change_status.start()
    print('NEBO v-1.7 Build \n')

# Bot_Status_Loop : 

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

# Bot_Error_Message : 

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('I don\'t remember my developers teaching me what to do on that command, Sorry.... I\'m helpless or WAIT, you can use (help) command to see what all I can do.')

# Member_Join_Message : 

@client.event
async def on_member_join(member):
    print(f'(member) has joined a server. ')

# Member_Leave_Message : 

@client.event
async def on_member_remove(member):
    print(f'(member) has left the server. ')

# Member_Kick_Message : 

@client.event
async def on_member_kick(member):
    print(f'(member) has been kicked from the server. ')

# Basic_Bot_Commands : 

# Ping command :

@client.command()
async def ping(ctx):
    await ctx.send(':regional_indicator_n::regional_indicator_e::b::regional_indicator_o: -- V-1.7 Ready.')
    ping = discord.Embed(title = "Servers Online!", colour = discord.Color.green())
    ping.add_field(name = ":  PING  :", value = f'{round(client.latency * 1000)} ms')
    await ctx.send(embed = ping)

#Easter Egg

@client.command()
async def fuck(ctx):
    await ctx.send(f'i am not suppose to tell this :nerd: \nfuck you!{ctx.author}:middle_finger:')

# 8ball command:

@client.command(aliases = ['8ball', 'fortune'])
async def _8ball(ctx, *, question):
    ball = discord.Embed(title = "8ball Says :8ball:", colour = discord.Color.greyple())
    responses = ['It is ceratin','It is decidely so','Without a doubt','Yes - definitely','As I see it, Yes','Most likely','Outlook good.','Yes.','Signs points to yes.','Reply hazy, try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Don\'t count on it','My reply is no','My sources say no','outlook not so good','Very doubtful' ]
    ball.add_field(name = f"{question}", value = f"{random.choice(responses)}")

    await ctx.send(embed = ball)

# 8ball error message :

@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('NEBO : Hey I didn\'t get enough information, Please try once again with enough info. : )')



# Roll a die.

@client.command(aliases = ['Roll'])
async def roll(ctx):
    roll = discord.Embed(title = "rolling :game_die:", colour = discord.Color.red())
    die_face = ['1','2','3','4','5','6']
    roll.add_field(name = "Rolled.. and it shows..", value = f"{random.choice(die_face)}")
    await ctx.send(embed = roll)
    
 


# Clear command :

@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = amount)

# clear error message :

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('NEBO : Hey I didn\'t get enough information, Please try once again with enough info. : )')

# Random emoji Generator :

@client.command(aliases=['emoji'])
async def Random_Emoji(ctx):
    emoji = discord.Embed(title = 'Here is the emoji', colour = discord.Color.gold())
    emoji_list = [':yawning_face:',':brown_heart:',':white_heart:',':pinching_hand:',':mechanical_arm:',':mechanical_leg:',':ear_with_hearing_aid:',':deaf_person:',':deaf_man:',':deaf_woman:',':man_kneeling:']
    emoji.add_field(name = "Emoji Generated", value = f'{random.choice(emoji_list)}')
    await ctx.send(embed = emoji)



# Bot_User_Info_Creator : 

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)


    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name='Guild name:', value=member.display_name)

    embed.add_field(name='Created at:', value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p IST"))
    embed.add_field(name='Joined at:', value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p IST"))

    embed.add_field(name=f'Roles ({len(roles)})', value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top role:", value=member.top_role.mention)

    embed.add_field(name="Bot?", value=member.bot)

    await ctx.send(embed=embed)

# Help command : 

@client.command()
async def help(ctx):
    author = ctx.message.author
    print(f'{author} has requested for general help')
    gnrl = discord.Embed(title = "NEBO : Help", colour = discord.Color.blue())

    gnrl.set_author(name = client.user.name, icon_url = client.user.avatar_url )

    gnrl.add_field(name = '.ping', value = 'Returns ping of NEBO\'s server', inline = False)
    gnrl.add_field(name = '.8ball <Question>', value = 'Let NEBO tell the fortune for your question', inline = False)
    gnrl.add_field(name = '.roll', value = 'NEBO rolls a die and tells you the output', inline = False)
    gnrl.add_field(name = '.emoji', value = 'NEBO throws a random emoji at you', inline = False)
    gnrl.add_field(name = '.clear <amount>', value = 'NEBO cleares the number of messages specified', inline = False)
    gnrl.add_field(name = '.voicehelp', value = 'Get help about the play music options for NEBO', inline = False) 

    
    await ctx.send(embed = gnrl)

@client.command()
async def voicehelp(ctx):
    author = ctx.message.author
    print(f'{author} has requested for voice help')
    voic = discord.Embed(title = "NEBO : Voice Help", colour = discord.Color.green())

    voic.set_author(name = client.user.name, icon_url = client.user.avatar_url)

    voic.add_field(name = '.join', value = 'NEBO joins the voice channel, you have to be in a voice channel', inline = False)
    voic.add_field(name = '.leave', value = 'NEBO leaves the voice channel', inline = False)
    voic.add_field(name = '.play <URL>', value = 'NEBO plays the music URL that you\'ve entered', inline = False)
    voic.add_field(name = '.pause', value = 'NEBO pauses the music you are playing', inline = False)
    voic.add_field(name = '.resume', value = 'NEBO resumes the music', inline = False)
    voic.add_field(name = '.stop', value = 'NEBO stops the music', inline = False)

    await ctx.send(embed = voic)


client.run(os.getenv('Token'))

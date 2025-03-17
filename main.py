#bot.py
#DISCORD BOT GRACEE, CURRENTLY STILL IN DEVELOPMENT
import os
import random
import requests
import json
import asyncio



from dotenv import load_dotenv
from googleapiclient.discovery import build
import discord
from discord.ext import commands
from discord import Color

from keep_alive import keep_alive
from music_cog import music_cog
load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="$", case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
  print(f"Logged in as {bot.user}")
  await bot.add_cog(music_cog(bot))
  print("Music Cog Loaded")


player1 = ""
player2 = ""
turn = ""
apikey1 = ""#insert api key from Google
greet= ["Nice to meet you!","How can i help you today?","can i help you with something?","and welcome!","and please enjoy your day!"]
greet2=["Here is the link!","Let's join the class!","Let's get in the class!","Welcome to","let's learn something new together"]
answers=['That is impossible.','Never have i ever think about it','Ask another question please:pray:','My sources say no.', 'Dont count on it.', 'cannot predict it now', 'Unfortunately no.','Yes.','It is fixed, fortunately','Undoubtedly yes!','It is decidedly so.','Most likely yes!','My sources told me yes.','Without a doubt!']
moves= ['rock','newspaper','scissors']
moves2 = ['rock','paper','scissors']
rps1 =["rpc1.jpg","rpc3.jpg"]

gameover = True
history = False
hangmangame = False
board = []
winning = [
  [0,1,2],
  [3,4,5],
  [6,7,8],
  [8,3,6],
  [1,4,7],
  [2,5,8],
  [0,4,8],
  [2,4,6]]

kebersamaan = ["all1.jpg","all2.jpg.jpeg","all3.jpg.jpeg","79950.jpg","image0.jpg","all4.jpg","all5.jpg","all6.jpg"]

reply = ["thx.jpg","thx2.jpg","thx3.jpg","thx4.jpg","thx5.jpg","thx7.jpg","thx8.jpg","thx6.jpeg"]
weeb = ["himeno.jpg","himeno2.jpg","yotsuba.jpg","yotsuba2.jpg","yotsuba3.jpg","komi1.jpg"]

mik = ["miku2.jpg","miku3.jpg","miku4.jpg"]
punpun =["sachi1.png","sachi2.png","sachi3.png","sachi4.png"]

moves= ['rock','newspaper','scissors']
moves2 = ['rock','paper','scissors']


@bot.event#displaying bot status as LISTENING
async def on_connect():
 #while True:
   print ("Bot is online")
   await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='NOW YOU CAN $PLAY MUSIC HERE!'))
   

target_channel_id = 1234

@bot.command()
async def h(ctx):#HELP COMMAND
  response="graceecover1.png"
  response2=random.choice(greet)
  file=discord.File(response, filename=response)
  await ctx.send(file=file)
  embed2=discord.Embed(title=f"\t\tThis is gracee rebuilt.\nformerly known as\n$play music here! use $mhelp also!\n$all = open our pics\n$ask me anything, i'll try to predict it.\n$search image from google! \n$misc = for other things!")
  await ctx.send("Server: ")
  await ctx.send(ctx.guild)
  await ctx.send("Hello "+ctx.message.author.mention+" "+response2)
  await ctx.send(embed=embed2)

@bot.command()
async def rps(ctx,message):
 answer =message.lower()
 computer=random.choice(moves)
 if answer not in moves2:
    await ctx.send("only select rock, paper, or scissors for this game!")
    return 
 else:
    if computer == answer:
      await ctx.send(f"Tie game! we both picked:{computer}:")
    if computer == "rock":
      if answer == "paper":
        await ctx.send(f"You win! gracee picked :{computer}: and you picked :newspaper:.")
    if computer == "newspaper":
      if answer == "rock":
        await ctx.send(f"gracee wins! gracee picked :{computer}: and you picked :rock:.")
    if computer == "scissors":
      if answer == "rock":
        await ctx.send(f"You win! gracee picked :{computer}: and you picked :rock:.")
    if computer == "rock":
      if answer == "scissors":
        await ctx.send(f"gracee wins! gracee picked :{computer}: and you picked :scissors:.")
    if computer == "newspaper":
      if answer == "scissors":
        await ctx.send(f"You win! gracee picked :{computer}: and you picked :scissors:.")
    if computer == "scissors":
      if answer == "paper":
        await ctx.send(f"Gracee wins! gracee picked :{computer}: and you picked :newspaper:.")

@bot.command()
async def rpshelp(message):
      response=random.choice(rps1)
      file=discord.File(response, filename=response)
      await message.channel.send(file=file)
      await message.channel.send("Use $rps rock/paper/scissors for this game! \nThe gamer will only play with gracee here! \nplease use lower case for the instructions! \nEnjoy guys!:thumbsup_tone1: ")

@bot.command(help="INSERT PICTURES OF THANKFUL QUOTES")
async def thx(message):
      response=random.choice(reply)
      file=discord.File(response, filename=response)
      await message.channel.send(file=file)




@bot.command(aliases=['show','search','s'], help="Search any image from google!")
async def see(ctx,*,search):
  response=random.randint(0,9)
  resource = build("customsearch","v1",developerKey=apikey1).cse()
  result = resource.list(q=f"{search}",cx="",searchType ="image").execute()
  url = result["items"][response]["link"]
  embed1=discord.Embed(title=f"This is what you searched for. Image of {search.title()}")
  embed1.set_image(url=url)
  await ctx.send(embed=embed1)


@bot.command(help="Tells you a joke!")
async def joke(message):
  url = ""

  response = requests.get(url)
  json_data1=(json.loads(response.text)['setup'])
  json_data2=(json.loads(response.text)['delivery'])
  await message.channel.send(json_data1)
  await asyncio.sleep(10)#DELAY BETWEEN SETUP AND JOKE DELIVERY
  await message.channel.send(json_data2)


@bot.command(help="Greet gracee here")
async def hello(ctx):
  await ctx.message.delete()
  await ctx.send("b-b-bakaa! (⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄")
  
@bot.command(help="Miku's pictures!")
async def miku(message):
      response=random.choice(mik)
      file=discord.File(response, filename=response)
      await message.channel.send(file=file)
  
@bot.command(help="Sachi's pictures!")
async def sachi(message):
      response=random.choice(punpun)
      file=discord.File(response, filename=response)
      await message.channel.send(file=file)

@bot.command(help="all our pictures gathered here!")
async def all(message):
  location = random.choice(kebersamaan)
  file=discord.File(location, filename=location)
  await message.channel.send("", file=file)

@bot.command(help="best girls are here!")
async def wibu(message):
  location = random.choice(weeb)
  file=discord.File(location, filename=location)
  await message.channel.send("enjoy i guess..", file=file)



@bot.command()
async def misc(ctx):
  await ctx.send("\n$ph for playing hangman! \n$joke = i'll tell you a joke! \n$wibu = best characters are here!! (add-ons : $sachi, $miku) \n$fpl = check out your Fantasy Premier League here!\n$rps = play rock paper scissors here! use the command and select rock, paper, or scissors! ($rpshelp for other functions!)\n$ttt = for playing TicTacToe with your friend! (tag you and your mate) ($p 1 until $p 9 for selecting the tile)\n$ping to know the current latency\n$thx = if you feel grateful to someone:pray_tone1:")
 
@bot.command()
async def mhelp(ctx):
  await ctx.send(":thumbsup_tone5: :thumbsup_tone1: :thumbsup_tone3: \n$play for playing music from youtube! \n$queue or $q = to check the music queue \n$clear or $c = to stop the music and queues at the same time! \n$leave or $l = to disconnect gracee from the vc \n$pause = to pause the current song! :pause_button: \n$resume = for resuming the current song! :arrow_forward: \n$thx = if you feel grateful to someone:pray_tone1:")



@bot.command(help="ask gracee something!")
async def ask(ctx,*,question):
  await ctx.message.delete()
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(answers)}')

  
@bot.command()
async def ping(ctx):
  await ctx.send(f'Latency:{round(bot.latency * 1000)}ms')
 
@bot.command(description='open your Fantasy Premier League here!')
async def fpl(ctx):
  await ctx.message.delete()
  await ctx.send("https://fantasy.premierleague.com/")

keep_alive()
token=os.environ.get("token")
bot.run(token)

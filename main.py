#this is the module for discord in python
#it is the main part for making the bot using python
#real name of module : Discord.py
#docs for reference : https://discordpy.readthedocs.io/en/stable/
#directory import
import sys

import discord

sys.path.append('./GIF')
sys.path.append('./important_files')


#boop emotion
import boop
#for the config_file.py in the directory
import config_file
#cry emotion
import cry
#cuddle emotion
import cuddle
#dance emotion
import dance
#floss emotion
import floss
#grin emotion
import grin
#highfive emotion
import highfive
#hug emmotion
import hug
#kick emotion
import kick
#kill emotion
import kill
#laugh emotion
import laugh
#pat emotion
import pat
#poke emotion
import poke
#reddit stuffs
import praw
#punch emotion
import punch
#roaster
import roast
#sing emotion
import sing
#slap emotion
import slap
#smug emotion
import smug
#snuggle emotion
import snuggle
#table flip
import table_flip
#teehee emotion
import teehee
#thonking emotion
import thonking
#twerk emotion
import twerk
#jokes import
from joke.jokes import *

reddit = praw.Reddit(client_id=config_file.reddit_client_id,
                     client_secret=config_file.reddit_client_secret,
                     user_agent=config_file.reddit_user_agent,
                     check_for_async=False)

#import for randomizing
import random
from random import choice

#dialect import
import dialect
#presence choice import
import Games

#this is for starting the bot
#here bot is a client
discord_client=discord.Client()

#it describes event
@discord_client.event
#when the bot it ready
async def on_ready():
    #print in console
    print("We are in the system as {0.user}".format(discord_client))
    #for the activity you can see on discord "Playing with you"
    random_game_num=random.randrange(0,len(Games.choice),1)
    game=discord.Game("{}".format(Games.choice[random_game_num]))
    await discord_client.change_presence(activity=game, status=discord.Status.dnd)

#it describes a event
@discord_client.event
async def on_message(message):
    #if the message's author is the bot itself:
    if message.author == discord_client.user:
        return

    #hello
    if message.content.startswith('hello') or message.content.startswith('Hello') or message.content.startswith('HELLO'):
        await message.channel.send('Hello!')
    
    #ayy
    if message.content.startswith('ayy') or message.content.startswith('Ayy') or message.content.startswith('AYY'):
        await message.channel.send('Lmao!')
    
    #if 'the message the user sends starts with the prefix' then:
    if message.content.startswith(config_file.prefix):
        #this line seperates the prefix and argument
        #this is a list type
        args = message.content.lstrip(config_file.prefix).split()
        # print(args)
        
        #if 'command' in argument: 
        
        if 'laugh' in args:
            #generate random number
            random_num=random.randrange(0,len(laugh.laugh_gif),1)
            random_num_dialect_start=random.randrange(0,len(dialect.laugh_start),1)
            random_num_dialect_end=random.randrange(0,len(dialect.laugh_end),1)
            laugh_embed=discord.Embed(
                title="{} {} {}".format(dialect.laugh_start[random_num_dialect_start],message.author.display_name,dialect.laugh_end[random_num_dialect_end]),  
                color=discord.Colour.random(),
                url=laugh.laugh_gif[random_num])
            laugh_embed.set_image(url=laugh.laugh_gif[random_num])
            await message.channel.send(embed=laugh_embed)

        elif 'cry' in args:
            #generate random number
            random_num=random.randrange(0,len(cry.cry_gif),1)
            random_num_dialect_start=random.randrange(0,len(dialect.cry_start),1)
            random_num_dialect_end=random.randrange(0,len(dialect.cry_end),1)
            cry_embed=discord.Embed(
                title="{} {} {}".format(dialect.cry_start[random_num_dialect_start],message.author.display_name,dialect.cry_end[random_num_dialect_end]),  
                color=discord.Colour.random(),
                url=cry.cry_gif[random_num])
            cry_embed.set_image(url=cry.cry_gif[random_num])
            await message.channel.send(embed=cry_embed)

        elif 'dance' in args:
            #generate random number
            random_num=random.randrange(0,len(dance.dance_gif),1)
            random_num_dialect_start=random.randrange(0,len(dialect.dance_start),1)
            random_num_dialect_end=random.randrange(0,len(dialect.dance_end),1)
            dance_embed=discord.Embed(
                title="{} {} {}".format(dialect.dance_start[random_num_dialect_start],message.author.display_name,dialect.dance_end[random_num_dialect_end]), 
                color=discord.Colour.random(),
                url=dance.dance_gif[random_num])
            dance_embed.set_image(url=dance.dance_gif[random_num])
            await message.channel.send(embed=dance_embed)

        elif 'sing' in args:
            #generate random number
            random_num=random.randrange(0,len(sing.sing_gif),1)
            random_num_dialect_start=random.randrange(0,len(dialect.sing_start),1)
            random_num_dialect_end=random.randrange(0,len(dialect.sing_end),1)
            sing_embed=discord.Embed(
                title="{} **{}** {}".format(dialect.sing_start[random_num_dialect_start],message.author.display_name,dialect.sing_end[random_num_dialect_end]), #lmao #stendup
                color=discord.Colour.random(),
                url=sing.sing_gif[random_num])
            sing_embed.set_image(url=sing.sing_gif[random_num])
            await message.channel.send(embed=sing_embed)

        elif 'highfive' in args:
            #generate random number
            random_num=random.randrange(0,len(highfive.highfive_gif),1)
            if not message.mentions:
                await message.channel.send("Apparently that's clapping!")#i forgot the spelling#there you go#how's the joke
            else:
                user=message.mentions[0]
                if user== message.author:
                    await message.channel.send("Apparently that's clapping!")
                else:    
                    highfive_embed=discord.Embed(
                        title="Up high {}, down low {}".format(message.author.display_name,user.display_name), #goes to dialects
                        color=discord.Colour.random(),
                        url=highfive.highfive_gif[random_num])
                    highfive_embed.set_image(url=highfive.highfive_gif[random_num])
                    await message.channel.send(embed=highfive_embed)

        elif 'smug' in args:
            #generate random number
            random_num=random.randrange(0,len(smug.smug_gif),1)
            smug_embed=discord.Embed(
                title="GROSS!! **{}** smugged!".format(message.author.display_name), #hehe
                color=discord.Colour.random(),
                url=smug.smug_gif[random_num])
            smug_embed.set_image(url=smug.smug_gif[random_num])
            await message.channel.send(embed=smug_embed)

        elif 'twerk' in args:
            #generate random number
            random_num=random.randrange(0,len(twerk.twerk_gif),1)
            twerk_embed=discord.Embed(
                title="**{}** is shaking some booty".format(message.author.display_name),  
                color=discord.Colour.random(),
                url=twerk.twerk_gif[random_num])
            twerk_embed.set_image(url=twerk.twerk_gif[random_num])
            await message.channel.send(embed=twerk_embed)

        elif 'floss' in args:
            #generate random number
            random_num=random.randrange(0,len(floss.floss_gif),1)
            floss_embed=discord.Embed(
                title="EWW! **{}** is a Fortnite simp!".format(message.author.display_name),  
                color=discord.Colour.random(),
                url=floss.floss_gif[random_num])
            floss_embed.set_image(url=floss.floss_gif[random_num])
            await message.channel.send(embed=floss_embed)

        elif 'hug' in args:
            #generate random number
            random_num=random.randrange(0,len(hug.hug_gif),1)
            if not message.mentions:
                await message.channel.send("How are you going to achieve that! Don't worry I will give you a hug.")#i forgot the spelling#there you go#how's the joke
            else:
                user=message.mentions[0]
                if user== message.author:
                    await message.channel.send("How are you going to achieve that! Don't worry I will give you a hug.")
                else:    
                    hug_embed=discord.Embed(
                        title="{} hugged {}".format(message.author.display_name,user.display_name),  
                        color=discord.Colour.random(),
                        url=hug.hug_gif[random_num])
                    hug_embed.set_image(url=hug.hug_gif[random_num])
                    await message.channel.send(embed=hug_embed)

        elif 'pat' in args:
            #generate random number
            random_num=random.randrange(0,len(pat.pat_gif),1)
            if not message.mentions:
                await message.channel.send("How are you going to achieve that! Don't worry I will give you a pat.")#i forgot the spelling#there you go#how's the joke
            else:
                user=message.mentions[0]
                if user== message.author:
                    await message.channel.send("How are you going to achieve that! Don't worry I will give you a pat.")
                else:    
                    pat_embed=discord.Embed(
                        title="{} patted {}".format(message.author.display_name,user.display_name),  
                        color=discord.Colour.random(),
                        url=pat.pat_gif[random_num])
                    pat_embed.set_image(url=pat.pat_gif[random_num])
                    await message.channel.send(embed=pat_embed)

        elif 'poke' in args:
            #generate random number
            random_num=random.randrange(0,len(poke.poke_gif),1)
            if not message.mentions:
                await message.channel.send("How are you going to achieve that! Don't worry I will give you a poke.")#i forgot the spelling#there you go#how's the joke
            else:
                user=message.mentions[0]
                if user== message.author:
                    await message.channel.send("How are you going to achieve that! Don't worry I will give you a poke.")
                else:    
                    poke_embed=discord.Embed(
                        title="{} poked {}".format(message.author.display_name,user.display_name),  
                        color=discord.Colour.random(),
                        url=poke.poke_gif[random_num])
                    poke_embed.set_image(url=poke.poke_gif[random_num])
                    await message.channel.send(embed=poke_embed)
        
        elif 'slap' in args:
            #generate random number
            random_num=random.randrange(0,len(slap.slap_gif),1)
            if not message.mentions:
                await message.channel.send("How are you going to achieve that! Don't worry I will give you a slap.")#i forgot the spelling#there you go#how's the joke
            else:
                user=message.mentions[0]
                if user== message.author:
                    await message.channel.send("How are you going to achieve that! Don't worry I will give you a slap.")
                else:    
                    slap_embed=discord.Embed(
                        title="{} slapped {}".format(message.author.display_name,user.display_name),  
                        color=discord.Colour.random(),
                        url=slap.slap_gif[random_num])
                    slap_embed.set_image(url=slap.slap_gif[random_num])
                    await message.channel.send(embed=slap_embed)

        elif 'kick' in args:
            #generate random number
            random_num=random.randrange(0,len(kick.kick_gif),1)
            if not message.mentions:
                await message.channel.send("Can you turn around?")#i forgot the spelling#there you go#how's the joke
            else:
                user=message.mentions[0]
                if user== message.author:
                    await message.channel.send("Can you turn around?")
                else:    
                    kick_embed=discord.Embed(
                        title="{} kicked {}".format(message.author.display_name,user.display_name),  
                        color=discord.Colour.random(),
                        url=kick.kick_gif[random_num])
                    kick_embed.set_image(url=kick.kick_gif[random_num])
                    await message.channel.send(embed=kick_embed)

        elif 'boop' in args:
            #generate random number
            random_num=random.randrange(0,len(boop.boop_gif),1)
            if not message.mentions:
                await message.channel.send("How are you going to achieve that! Don't worry I will give you a boop.")#i forgot the spelling#there you go#how's the joke
            else:
                user=message.mentions[0]
                if user== message.author:
                    await message.channel.send("How are you going to achieve that! Don't worry I will give you a boop.")
                else:    
                    boop_embed=discord.Embed(
                        title="{} booped {}".format(message.author.display_name,user.display_name),  
                        color=discord.Colour.random(),
                        url=boop.boop_gif[random_num])
                    boop_embed.set_image(url=boop.boop_gif[random_num])
                    await message.channel.send(embed=boop_embed)
       
        elif 'punch' in args:
            #generate random number
            random_num=random.randrange(0,len(punch.punch_gif),1)
            if not message.mentions:
                await message.channel.send("How are you going to achieve that! Don't worry I will give you a punch.")#i forgot the spelling#there you go#how's the joke
            else:
                user=message.mentions[0]
                if user== message.author:
                    await message.channel.send("How are you going to achieve that! Don't worry I will give you a punch.")
                else:    
                    punch_embed=discord.Embed(
                        title="{} punched {}".format(message.author.display_name,user.display_name),  
                        color=discord.Colour.random(),
                        url=punch.punch_gif[random_num])
                    punch_embed.set_image(url=punch.punch_gif[random_num])
                    await message.channel.send(embed=punch_embed)       

        elif 'kill' in args:
            #generate random number
            random_num=random.randrange(0,len(kill.kill_gif),1)
            if not message.mentions:
                await message.channel.send("How are you going to achieve that! Don't worry I will give you a kill.")#i forgot the spelling#there you go#how's the joke
            else:
                user=message.mentions[0]
                if user== message.author:
                    await message.channel.send("How are you going to achieve that! Don't worry I will give you a kill.")
                else:    
                    kill_embed=discord.Embed(
                        title="{} killed {}".format(message.author.display_name,user.display_name),  
                        color=discord.Colour.random(),
                        url=kill.kill_gif[random_num])
                    kill_embed.set_image(url=kill.kill_gif[random_num])
                    await message.channel.send(embed=kill_embed)

        elif 'cuddle' in args:
            #generate random number
            random_num=random.randrange(0,len(cuddle.cuddle_gif),1)
            if not message.mentions:
                await message.channel.send("How are you going to achieve that! Don't worry I will give you a cuddle.")#i forgot the spelling#there you go#how's the joke
            else:
                user=message.mentions[0]
                if user== message.author:
                    await message.channel.send("How are you going to achieve that! Don't worry I will give you a cuddle.")
                else:    
                    cuddle_embed=discord.Embed(
                        title="{} cuddleed {}".format(message.author.display_name,user.display_name),  
                        color=discord.Colour.random(),
                        url=cuddle.cuddle_gif[random_num])
                    cuddle_embed.set_image(url=cuddle.cuddle_gif[random_num])
                    await message.channel.send(embed=cuddle_embed)
        
        elif 'snuggle' in args:
            #generate random number
            random_num=random.randrange(0,len(snuggle.snuggle_gif),1)
            if not message.mentions:
                await message.channel.send("How are you going to achieve that! Don't worry I will give you a snuggle.")#i forgot the spelling#there you go#how's the joke
            else:
                user=message.mentions[0]
                if user== message.author:
                    await message.channel.send("How are you going to achieve that! Don't worry I will give you a snuggle.")
                else:    
                    snuggle_embed=discord.Embed(
                        title="{} snuggleed {}".format(message.author.display_name,user.display_name),  
                        color=discord.Colour.random(),
                        url=snuggle.snuggle_gif[random_num])
                    snuggle_embed.set_image(url=snuggle.snuggle_gif[random_num])
                    await message.channel.send(embed=snuggle_embed)

        elif 'joke' in args:
            joke_embed=discord.Embed(
                title='**JOKE TIME**',  
                color=discord.Colour.random(),
                description=choice([geek, icanhazdad, chucknorris, icndb])()
                )
            joke_embed.set_author(name=message.author.display_name)  
            await message.channel.send(embed=joke_embed)
          
        elif 'meme' in args:
            meme=reddit.subreddit(choice(['dankmemes', 'memes', 'wholesomememes', 'comedyheaven'])).random()
            meme_embed=discord.Embed(
                title=meme.title,  
                color=discord.Colour.random()
                )
            meme_embed.set_author(name=meme.subreddit)
            meme_embed.set_image(url=meme.url)
            await message.channel.send(embed=meme_embed)
        
        elif 'thought' in args:
            thought=reddit.subreddit(choice(['showerthoughts','thoughts'])).random()
            thought_embed=discord.Embed(
                title=thought.title,  
                color=discord.Colour.random()
                )
            thought_embed.set_author(name=thought.subreddit)
            thought_embed.set_image(url=thought.url)
            await message.channel.send(embed=thought_embed)

        elif 'roast' in args:
            #generate random number
            random_num=random.randrange(0,len(roast.roaster),1)
            random_num_gif=random.randrange(0,len(roast.roast_gif),1)
            if not message.mentions:
                await message.channel.send("Don't worry I will roast you.")#i forgot the spelling#there you go#how's the joke
                roast_embed=discord.Embed(
                    title="I roasted {}".format(message.author.display_name),  
                    color=discord.Colour.random(),
                    description=roast.roaster[random_num]
                    )
                roast_embed.set_image(url=roast.roast_gif[random_num_gif])
                msg=await message.channel.send(embed=roast_embed)
                await msg.add_reaction("🔥")
            else:
                user=message.mentions[0]
                if user== message.author:
                    await message.channel.send("Don't worry I will roast you.")
                    roast_embed=discord.Embed(
                        title="I roasted {}".format(message.author.display_name),  
                        color=discord.Colour.random(),
                        description=roast.roaster[random_num]
                        )
                    roast_embed.set_image(url=roast.roast_gif[random_num_gif])
                    msg=await message.channel.send(embed=roast_embed)
                    await msg.add_reaction("🔥")
                else:    
                    roast_embed=discord.Embed(
                        title="{} roasted {}".format(message.author.display_name,user.display_name),  
                        color=discord.Colour.random(),
                        description=roast.roaster[random_num]
                        )
                    roast_embed.set_image(url=roast.roast_gif[random_num_gif])
                    msg=await message.channel.send(embed=roast_embed)
                    await msg.add_reaction("🔥")
        
        elif 'grin' in args:
            #generate random number
            random_num=random.randrange(0,len(grin.grin_gif),1)
            grin_embed=discord.Embed(
                title="**{}** grins!".format(message.author.display_name), #lmao #stendup
                color=discord.Colour.random(),
                url=grin.grin_gif[random_num])
            grin_embed.set_image(url=grin.grin_gif[random_num])
            await message.channel.send(embed=grin_embed)

        elif 'teehee' in args:
            #generate random number
            random_num=random.randrange(0,len(teehee.teehee_gif),1)
            teehee_embed=discord.Embed(
                title="**{}** teehees!".format(message.author.display_name), #lmao #stendup
                color=discord.Colour.random(),
                url=teehee.teehee_gif[random_num])
            teehee_embed.set_image(url=teehee.teehee_gif[random_num])
            await message.channel.send(embed=teehee_embed)

        elif 'thonking' in args:
            random_num=random.randrange(0,len(thonking.thonking_gif),1)
            thonking_embed=discord.Embed(
                title="**{}** is thonking!".format(message.author.display_name), #lmao #stendup
                color=discord.Colour.random(),
                url=thonking.thonking_gif[random_num])
            thonking_embed.set_image(url=thonking.thonking_gif[random_num])
            await message.channel.send(embed=thonking_embed)

    #table flip
    if message.content.startswith('(╯°□°）╯︵ ┻━┻') or message.content.startswith('┬─┬ ノ( ゜-゜ノ)'):
        random_choice=random.randrange(0,2,1)
        if random_choice==1:
            random_num_1=random.randrange(0,len(table_flip.table_flip_answer_1),1)
            await message.channel.send(table_flip.table_flip_answer_1[random_num_1])
        else:
            random_num_2=random.randrange(0,len(table_flip.table_flip_answer_2),1)
            await message.channel.send(table_flip.table_flip_answer_2[random_num_2])
        
#it connects the bot to discord
discord_client.run(config_file.token)
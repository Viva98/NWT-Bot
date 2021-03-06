import discord
from discord.ext import commands
import re
from InputHandler import Format
from OutputHandler import GetData
import languages
import books

des = 'A discord bot for getting Bible verses from the New World Translation'
prefix = '!'
client = commands.Bot(description=des, command_prefix=prefix)
online = '\n\nBot is online!\n\n'
TooLong = '**The passage is too long for me to grab, sorry!**'
WrongFormat = '**Wrong format used, try again:**\n```!language bookname chapter:verse(s)```'

@client.event
async def on_ready():
    print(online)
    await client.change_presence(game=discord.Game(name='https://github.com/Viva98/NWT-Bot'))

#SHOW SERVERS BOT IS CONNECTED TO IN CHAT
@client.command(pass_context=True)
async def servers(ctx):

    list = ''
    for server in client.servers:
        list += str(server)+',\n'
    await client.say('List of servers NWT-Bot is connected to: ```'+list+'```')

#SHOW AVAILABLE LANGUAGES IN CHAT
@client.command(pass_context=True)
async def language():
    available = ''
    for language in languages.languageURLs:
        available += '\n!'+language

    await client.say('**Languages available:**```'+available+'```')

#SHOW GITHUB LINK
@client.command(pass_context=True)
async def git():

    await client.say('https://github.com/Viva98/NWT-Bot')

#SHOW INVITE LINK
@client.command(pass_context=True)
async def invite():

    await client.say('https://discordapp.com/oauth2/authorize?client_id=360576523062870016&scope=bot')


#ENGLISH
@client.command(pass_context=True)
async def english(ctx, book, chapterANDverse, add='0'):
    await GetVerses('english', book, chapterANDverse, add)

#HEBREW
@client.command(pass_context=True)
async def hebrew(ctx, book, chapterANDverse, add='0'):
    await GetVerses('hebrew', book, chapterANDverse, add)

#GREEK
@client.command(pass_context=True)
async def greek(ctx, book, chapterANDverse, add='0'):
    await GetVerses('greek', book, chapterANDverse, add)

#FRENCH
@client.command(pass_context=True)
async def french(ctx, book, chapterANDverse, add='0'):
    await GetVerses('french', book, chapterANDverse, add)

#SPANISH
@client.command(pass_context=True)
async def spanish(ctx, book, chapterANDverse, add='0'):
    await GetVerses('spanish', book, chapterANDverse, add)

#GERMAN
@client.command(pass_context=True)
async def german(ctx, book, chapterANDverse, add='0'):
    await GetVerses('german', book, chapterANDverse, add)


def GetVerses(language, book, chapterANDverse, add):
    try:
        header, verse, data = Handler(book, chapterANDverse, language, add)
        try:
            return client.say('**'+header+':'+verse+' - New World Translation (NWT)**\n\n```css\n'+data+'```')

        except Exception:
            return client.say(TooLong)

    except Exception:
        return client.say(WrongFormat)
        pass

def Handler(book, chapterANDverse, language, add):

    booknumber, chapter, verse, fromVerse, toVerse = Format(book, chapterANDverse, language, add)
    header, verse, data = GetData(booknumber, chapter, verse, fromVerse, toVerse, language)
    return(header, verse, data)

client.run('token')

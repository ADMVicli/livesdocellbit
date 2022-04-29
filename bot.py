from functions.twitchAPI import verifyGame, isOnline, getImageGame, getTitle, getVideo

import os
from time import sleep

import discord
from discord.ext import tasks

import tweepy

global currentGame, online

auth = tweepy.OAuthHandler("GPRorX0IZ7wp4s9EcmD1Y3Vzp", "icHW0EvWkmbPXZUoukUZY2ow9BAeiGvKrMwdWm9zlZiNJ926z7")
auth.set_access_token("1278567210991210502-sEmyQXOYI4HMPBHxYP2MEzo9RKKGuQ", "o4uhnyVCnuq5INQc3EqGpLEeGvf5JaJPzdgjtuURwCvZY")
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")

online = False
currentGame = None
bot = discord.Bot()

if isOnline():
    online = True
    currentGame = verifyGame()['game']

@bot.event
async def on_ready():
    print('Online!')
    checkGame.start()

@tasks.loop(seconds=15)
async def checkGame():
    if isOnline() == True and online == False:
        api.update_status(f'Cellbit entrou ao vivo!\nTítulo: {getTitle}\nhttps://twitch.tv/cellbit')
    if online == True and isOnline() == False:
        api.update_status('Cellbit encerrou a live!')
    global currentGame
    if isOnline():
        infos = verifyGame()
        game = infos['game']
        timestampVod = f'{infos["vodHours"]}h{infos["vodMinutes"]}m{infos["vodSeconds"]}s'
        print(timestampVod)
        if game != currentGame:
            currentGame = game
            textPost = f'Cellbit está jogando: {game}\nMinutagem no VOD: ~{timestampVod} \nhttps://twitch.tv/cellbit'
            getImageGame(game)
            sleep(3)
            status = api.update_status_with_media(textPost, 'gameImg.jpg')
            api.update_status(f'Link do VOD: {getVideo()}?t={timestampVod}', status)

bot.run("OTY4MTkzMzE0NTk3Nzc3NDc5.YmbSSg.IKhoiWVe7GWtFWncUGrBJ07304Q")

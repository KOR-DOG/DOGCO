import discord


client = discord.Client()



@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("-------------------")
    await client.change_presence(game=discord.Game(name='', type=1))


@client.event
async def on_message(message):
    if message.content.startswith("hi"):
        await client.send_message(message.channel, "HI")


client.run('NTU3NDI0NTMzNjQ1MDMzNDcz.D3KBmg.cHRvirzwxryZp2YO5QqW_lurVe8')
    

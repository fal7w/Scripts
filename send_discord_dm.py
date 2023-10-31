import discord
import sys
import json

async def send_dm(token, response_persons):
    client = discord.Client()

    @client.event
    async def on_ready():
        for person in response_persons:
            user = await client.fetch_user(person['id'])
            await user.send(person['messge'])
        await client.close()

    await client.start(token)


tocken =sys.argv[1]
response_persons = json.load(sys.argv[1])
discord.run(send_dm(token, response_persons))   
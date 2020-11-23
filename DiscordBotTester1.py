print("dev was here")
# id      763152432477372430
# token     NzYzMTUyNDMyNDc3MzcyNDMw.X3zjFg.qGUD0qmL-MlYrJHQW3dLe0hpm3E
# permission int      34670656

# https://discordapp.com/oauth2/authorize?client_id={CLIENTID}&scope=bot&permissions={PERMISSIONINT}
# https://discordapp.com/oauth2/authorize?client_id=763152432477372430&scope=bot&permissions=34670656

import discord

print(discord.__version__)

client = discord.Client()
token = "NzYzMTUyNDMyNDc3MzcyNDMw.X3zjFg.qGUD0qmL-MlYrJHQW3dLe0hpm3E"

@client.event 
async def on_ready():
	print(f"we have logged in as {client.user}")

@client.event
async def on_message(message):
	print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

	dave_guild = client.get_guild(390332470068903936)

	if "TestBot1.0.1.1.member_count()" == message.content.lower():
		await message.channel.send(f"```py\n{dave_guild.member_count}```")

	if "hi there" == message.content.lower():
		await message.channel.send("you look good")

	if "TestBot1.0.1.1.logout()" == message.content.lower():
		await client.close()	

client.run(token)
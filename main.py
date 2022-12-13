
token = "BOT_Token"
bloxlink_token = "API"

import discord, requests, json, datetime, time


bot = discord.Bot()

@bot.event
async def on_ready():
  print("RoSearch | v.1.0.0")
  print("------------------")
  
  time.sleep(1)
  print(f"BOT NAME: {bot.user}")
  time.sleep(0.1)
  print(f"BOT ID: {bot.user.id}")
  



@bot.command(description="Last Online For A Roblox Account")
async def lastonline(ctx, user_id: str):
  try:
    last_online = datetime.datetime.strptime(requests.get('https://api.roblox.com/users/%s/onlinestatus/' % userid).json()['LastOnline'], '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y/%m/%d | %H:%M %p')
    embed = discord.Embed(title="Last online")
    embed.add_field(name="Last Online:", value=last_online)
    await ctx.send(embed=embed)
  except KeyError:
    embed2 = discord.Embed(title="username is invalid")
    embed2.add_field(name="User", value=user)
    await ctx.send(embed=embed2)
@bot.command(description="Join Date For A Roblox Command ")
async def join_date(ctx, user_id: str):
  join_date = datetime.datetime.strptime(requests.get('https://users.roblox.com/v1/users/%s' % user_id).json()['created'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y/%m/%d | %H:%M %p')
  embed = discord.Embed(title="Join Date")
  embed.add_field(name="Join Date:", value=join_date)
  await ctx.send(embed=embed)
  
@bot.command(description="Search For A Roblox User")
async def search(ctx, user: str):
  try:
    user_id = requests.get(f"https://api.roblox.com/users/get-by-username?username={user}").json()['Id']
    isbanned = requests.get(f"https://users.roblox.com/v1/users/{user_id}").json()['isBanned']
    verfied = requests.get(f"https://users.roblox.com/v1/users/{user_id}").json()['hasVerifiedBadge']
    friends = requests.get(f"https://friends.roblox.com/v1/users/{user_id}/friends/count").json()['count']
    avatar_url = 'https://www.roblox.com/headshot-thumbnail/image?userId=%s&width=420&height=420&format=png' % user_id
    join_date = datetime.datetime.strptime(requests.get('https://users.roblox.com/v1/users/%s' % user_id).json()['created'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y/%m/%d | %H:%M %p')
    last_online = datetime.datetime.strptime(requests.get('https://api.roblox.com/users/%s/onlinestatus/' % user_id).json()['LastOnline'], '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y/%m/%d | %H:%M %p')
    rap = requests.get(f"https://rblx.trade/api/v2/users/{user_id}/info").json()['accountRAP']
    user_value = requests.get(f"https://rblx.trade/api/v2/users/{user_id}/info").json()['accountValue']
    placevisit = requests.get(f"https://rblx.trade/api/v2/users/{user_id}/info").json()['placeVisitCount']
    embed = discord.Embed(title=f"RoSearch ")
    embed.add_field(name="`USERNAME:`", value=user)
    embed.add_field(name="`ID:`", value=user_id)
    embed.add_field(name="`Banned:`", value=isbanned)
    embed.add_field(name="`Verfied:`", value=verfied)
    embed.add_field(name="`Friends:`", value=friends)
    embed.add_field(name="`Last Online:`", value=last_online)
    embed.add_field(name="`created:`", value=join_date)
    embed.add_field(name="`Rap:`", value=rap)
    embed.add_field(name="`Value:`", value=user_value)
    embed.add_field(name="Place Visit Count:", value=placevisit)
    embed.set_thumbnail(url=avatar_url)
    await ctx.respond(f"[profile](https://rblx.name/{user_id}) ", embed=embed)
  except KeyError:
    embed2 = discord.Embed(title="username is invalid")
    embed2.add_field(name="User", value=user)
    await ctx.send(embed=embed2)



@bot.command(description="Discord To Roblox ")
async def dtr(ctx, discord_id: str):
  try:
    id = requests.get(f"https://v3.blox.link/developer/discord/{discord_id}", headers = {'api-key': bloxlink_token}).json()
    data = id['user']['robloxId']

    username = requests.get(f"https://users.roblox.com/v1/users/{data}").json()['name']

    isbanned = requests.get(f"https://users.roblox.com/v1/users/{data}").json()['isBanned']

    verfied = requests.get(f"https://users.roblox.com/v1/users/{data}").json()['hasVerifiedBadge']
  
    friends = requests.get(f"https://friends.roblox.com/v1/users/{data}/friends/count").json()['count']
  
    avatar_url = 'https://www.roblox.com/headshot-thumbnail/image?userId=%s&width=420&height=420&format=png' % data
  
    join_date = datetime.datetime.strptime(requests.get('https://users.roblox.com/v1/users/%s' % data).json()['created'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y/%m/%d | %H:%M %p')
  
    last_online = datetime.datetime.strptime(requests.get('https://api.roblox.com/users/%s/onlinestatus/' % data).json()['LastOnline'], '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y/%m/%d | %H:%M %p')

    rap = requests.get(f"https://rblx.trade/api/v2/users/{data}/info").json()['accountRAP']

    user_value = requests.get(f"https://rblx.trade/api/v2/users/{data}/info").json()['accountValue']
  
    placevisit = requests.get(f"https://rblx.trade/api/v2/users/{data}/info").json()['placeVisitCount']
  
    embed = discord.Embed(title="DTR", description="RoSearch | blox.link datbase")
    embed.add_field(name="`Discord ID`", value=f"<@{discord_id}>")
    embed.add_field(name="`Roblox ID`", value=data)
    embed.add_field(name="`Roblox User`", value=username)
    embed.add_field(name="`Last Online`", value=last_online)
    embed.add_field(name="`Join Date`", value=join_date)
    embed.add_field(name="`Verfied`", value=verfied)
    embed.add_field(name="`banned`", value=isbanned)
    embed.add_field(name="`Rap`", value=rap)
    embed.add_field(name="`Value`", value=user_value)
    embed.add_field(name="Place Visit Count", value=placevisit)
    embed.set_thumbnail(url=avatar_url)
  
    await ctx.respond(embed=embed)
  except KeyError:
    embed2 = discord.Embed(title="User Does Not Exist")
    embed2.add_field(name="Discord User", value=discord_id)
    await ctx.send(embed=embed2)

@bot.command(description="Checks If A Username is Valid")
async def validator(ctx, username: str):
  validate = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={username}&request.birthday=1999-02-02T23%3A00%3A00.000Z&request.context=Signup").json()['message']

  embed = discord.Embed(title="Username validator")
  embed.add_field(name="Response", value=validate)

  await ctx.respond(embed=embed)

@bot.command()
async def check_cookie(ctx, cookie: str):
  try:
    check = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie}).json()
    

    await ctx.send(check)
  except json.JSONDecodeError as e:
    embed2 = discord.Embed(title="Roblox Cookie")
    embed2.add_field(name="VALID", value="false")
    embed2.add_field(name="Invalid cookie", value=f"```{cookie}```")
    await ctx.send(embed=embed2)

@bot.command(description="Help command")
async def help(ctx):
  embed=discord.Embed(title="**HELP | Menu**", description="** RoSearch Roblox Best Search Bot**")
  embed.add_field(name="</validator:0>", value=" **Checks if a roblox username is valid or if its in use.**", inline=True)
  embed.add_field(name="</search:0>", value="** Search for a roblox user and it will give you last online join date + many more things about the certain account.**", inline=True)
  embed.add_field(name="</dtr:0>", value="** DTR/ Discord To Roblox this command gets the roblox account from their  discord ID and it checks their roblox account info if its verfied last online and more.**", inline=True)
  embed.add_field(name="</check_cookie:0>", value="** We Have built in cookie checker in our discord bot wich checks for robux balance and if the cookie is valid we also check if the account has premium and if account has any builders club**", inline=True)
  embed.add_field(name="RTD", value="Roblox To Discord find discord users with roblox easily")
  embed.set_footer(text="RoSearch")
  await ctx.send(embed=embed)

@bot.command()
async def rtd(ctx, robloxid: str):
  r = requests.get(f'https://verify.nezto.re/api/reverse/{robloxid}')
  if r.status_code == 200:
    discID = r.json()[0]['discordId']
    robloxname = requests.get(f"https://users.roblox.com/v1/users/{robloxid}").json()['name']
    embed = discord.Embed(title="RTD (Roblox To Discord)")
    embed.add_field(name="Discord ID:", value=discID)
    embed.add_field(name="Roblox Username:", value=robloxname)
    await ctx.send(embed=embed)
  else:
    embed2 = discord.Embed(title="Bad Request")
    embed2.add_field(name="Error:", value="User is not found in Database")
    embed2.add_field(name="Database:", value="https://verify.nezto.re")
    await ctx.send(embed=embed2)


bot.run(token)

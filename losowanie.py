import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Włącz uprawnienia, by móc pobierać członków serwera
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} jest online!')

# Nadawanie roli nowym użytkownikom 
@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="h")  # Zmień na nazwę rangi, którą chcesz nadać
    if role:
        await member.add_roles(role)
        print(f'Nadano rolę {role.name} użytkownikowi {member.name}')
    else:
        print("Nie znaleziono roli.")

#dawanie ręczne rangi
#przykłowe polecenie !daj_role @Kuba VIP
@bot.command(name='daj_role')
@commands.has_permissions(manage_roles=True)  # Upewnij się, że tylko osoby z odpowiednimi uprawnieniami mogą nadawać role
async def daj_role(ctx, member: discord.Member, role_name: str):
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    
    if role:
        await member.add_roles(role)
        await ctx.send(f'Nadano rolę {role.name} użytkownikowi {member.mention}')
    else:
        await ctx.send(f'Rola o nazwie {role_name} nie istnieje.')

# Komenda losowania użytkownika z kanału tekstowego
@bot.command(name='losuj_uzytkownika')
async def losuj_uzytkownika(ctx):
    members = [member for member in ctx.channel.members if not member.bot]  # Lista osób na kanale (bez botów)
    
    if members:
        wylosowana_osoba = random.choice(members)
        await ctx.send(f'Wylosowana osoba to: {wylosowana_osoba.mention}')
    else:
        await ctx.send("Na tym kanale nie ma dostępnych użytkowników.")
@bot.command(name='losuj_glos')
async def losuj_glos(ctx):
    # Sprawdza, czy osoba wydająca komendę jest w kanale głosowym
    if ctx.author.voice and ctx.author.voice.channel:
        voice_channel = ctx.author.voice.channel
        members = [member for member in voice_channel.members if not member.bot]  # Lista osób w kanale głosowym (bez botów)
        
        if members:
            wylosowana_osoba = random.choice(members)
            await ctx.send(f'Wylosowana osoba z kanału głosowego to: {wylosowana_osoba.mention}')
        else:
            await ctx.send("W kanale głosowym nie ma użytkowników.")
    else:
        await ctx.send("Musisz być w kanale głosowym, aby wykonać tę komendę.")
#pingowanie osób
@bot.command(name='ping')
async def ping(ctx):
    members = [member for member in ctx.channel.members if not member.bot]  # Lista osób na kanale (bez botów)
    if members:
        await ctx.send(f'@dealerfromthehood ')
@bot.command(name='ping1')
async def ping1(ctx):
    members = [member for member in ctx.channel.members if not member.bot]  # Lista osób na kanale (bez botów)
    if members:
        wylosowana_osoba = random.choice(members)
        await ctx.send(f'{wylosowana_osoba.mention}')
#pingowanie losowych osób
@bot.command(name='ping2')
async def ping2(ctx, *members: discord.Member):  # Przyjmuje dowolną liczbę użytkowników
    if members:
        wylosowana_osoba = random.choice(members)
        await ctx.send(f'Wylosowana osoba to: {wylosowana_osoba.mention}')
    else:
        await ctx.send("Nie podano żadnych osób do losowania.")
# Token bota
bot.run('')

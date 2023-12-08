import discord
import discord_token
from pass_gen import gen_pass
from discord.ext import commands
import time
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents) #help_command=None

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')
    time.sleep(0.5)
    await ctx.send("Kanalımıza hoşgeldin!")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def topla(ctx, s1=1, s2=1):
    await ctx.send(s1+s2)
    
@bot.command()
async def topla2(ctx, *args):
    try:
        toplam = 0 #toplam = sum(float(arg) for arg in args)
        for i in args:
            toplam += int(i)
        await ctx.send(toplam)
    except:
        await ctx.send("Hata alındı!")
        
@bot.command()
async def harf(ctx, *args):
    kelime = "" #kelime  = ' '.join(args)
    for i in args:
        kelime += i
    await ctx.send(i)
    
@bot.command()
async def zar(ctx):
    x = [1, 2, 3, 4]
    oranlar = [0.2, 0.6, 0.1, 0.1]
    await ctx.send(random.choices(x, weights=oranlar, k=1)[0])
        
@bot.command()
async def cikar(ctx, s1=1, s2=1):
    await ctx.send(s1-s2)

@bot.command()
async def carp(ctx, s1=1, s2=1):
    await ctx.send(s1*s2)
    
@bot.command()
async def bol(ctx, s1=1, s2=1):
    await ctx.send(s1//s2)

@bot.command()
async def yazitura(ctx, yazitura='a'):
    x = random.randint(0,1)
    if yazitura.upper() in ['YAZI','TURA']:
        if (yazitura.upper() == 'YAZI' and x == 0) or (yazitura.upper() == 'TURA' and x == 1):
            await ctx.send(f"TUTTURDUN!! {yazitura}")
        else:
            await ctx.send("maalesef bilemedin.")
    else:
        await ctx.send("Yazı veya tura giriniz.")
        
@bot.command()
async def passgen(ctx, n=10):
    await ctx.send("passgen kodunun yazdıktan sonra yanına şifre uzunluğunu girin!!")
    sifre = gen_pass(n)
    await ctx.send(f"Şifreniz: {sifre}")
    
@bot.command()
async def help2(ctx):
    embed = discord.Embed(title="Bot Komutları", description="İçerik gösterme", color=discord.Color.green())
    embed.add_field(name='!passgen', value="passgen kodunun yazdıktan sonra yanına şifre uzunluğunu girin!!", inline=False)
    embed.add_field(name='!topla', value="toplamak için 2 veya daha fazla sayi girin", inline=False)
    await ctx.send(embed=embed)
    
@bot.command()
async def tahmin(ctx):
    x = random.randint(1,100)
    await ctx.send("1 ile 100 arasında bir sayı tuttum. Tahmin etmeye çalış:D")
    tahmin_hakki = 7
    while True:
        try:
            tahmin_mesaji = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
            kullanici_tahmini = tahmin_mesaji.content
            if int(kullanici_tahmini) == x:
                await ctx.send(f'BİLDİN! Hem de {7-tahmin_hakki} denemede.')
                break
            elif int(kullanici_tahmini) < x:
                tahmin_hakki -= 1
                await ctx.send(f'Düşük girdin, {tahmin_hakki} tahmin hakkın kaldı.')
            elif int(kullanici_tahmini) > x:
                tahmin_hakki -= 1
                await ctx.send(f'Yüksek girdin, {tahmin_hakki} tahmin hakkın kaldı.')
        except:
            await ctx.send('Bir sayi girmen gerekiyor.')
            

@bot.command()
async def mem(ctx):
    x = os.listdir('images')
    posibilities = [0.7, 0.1, 0.1, 0.1]                          
    choice = random.choices(x, weights=posibilities, k=1)[0]
    with open(f'images/{choice}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    #duck komutunu çağırdığımızda, program get_duck_image_url fonksiyonunu çağırır.
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
    
bot.run(discord_token.token)

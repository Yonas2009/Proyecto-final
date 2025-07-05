import discord
from discord.ext import commands
import random 
a = random.randint(1,5)

def consejos():
    if a == 1:
        x = print(f"🌱 Reduce tu consumo de energía: Apaga luces y aparatos eléctricos cuando no los uses.")
    elif a == 2:
        y = print(f"🚶‍♀️ Cambia tu forma de moverte: Usa el transporte público, bicicleta o camina siempre que puedas.")
    elif a ==3:
        z = print(f"♻️ Reduce, reutiliza y recicla: Evita productos desechables: lleva tu botella, bolsas y tazas reutilizables.")

def bot():

    bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print(f"Bot conectado como {bot.user}")

    @bot.command()
    async def hola(ctx):
        await ctx.send(f"¡Hola, {ctx.author.mention}! 👋")

    @bot.command()
    async def help(ctx):
        await ctx.send(f"Comandos que puedes utilizar: paises, consejo, Q, caneca|papelera, WSC, FU, creator, RM, RQ, RB, REN")

    @bot.command()
    async def paises(ctx):
        await ctx.send(f"Claro con mucho gusto {ctx.author.mention} los paises mas afectados son los siguientes; 🌍 Impactos globales según informes recientes: Dominica, China y Honduras son los más afectados en el período 1993–2022, según el Climate Risk, o si quieres una informacion mucho mas resumida puedes entrar en el siguiente enlace: ")
        
    @bot.command()
    async def consejo(ctx):
        await ctx.send(f"De parte de mi informacion obtenida podria ser uno muy bueno el siguiente{consejos}")

    @bot.command()
    async def Q(ctx):
        await ctx.send(f"El cambio climático es la modificación a largo plazo del clima de la Tierra, especialmente en lo relacionado con la temperatura, las precipitaciones, los vientos y otros patrones climáticos.")
    
    @bot.command()
    async def caneca(ctx):
        await ctx.send(
        "♻️ ¿Para qué sirve cada caneca de basura?"
        "🟢 **Verde** – *Residuos orgánicos*: cáscaras de frutas, restos de comida, hojas, servilletas usadas."
        "🔵 **Azul** – *Papel y cartón (limpios y secos)*: cuadernos, cajas, hojas, bolsas de papel, periódicos."
        "🟡 **Amarilla** – *Plásticos y metales reciclables*: botellas PET, latas, empaques de snacks."
        "⚪ **Gris o blanca** – *No reciclables*: pañales, colillas, papel higiénico, residuos sanitarios."
        "🔴 **Roja** – *Residuos peligrosos*: pilas, medicamentos vencidos, baterías, electrónicos."
        "🟣 **Violeta o negra** – *Residuos tecnológicos*: celulares, cargadores, aparatos electrónicos."
    )

    @bot.command()
    async def WSC(ctx):
        await ctx.send(f"https://www.un.org/en/climatechange/what-is-climate-change/")

    @bot.command()
    async def FU(ctx):
        await ctx.send(f"https://350.org/es/piensa-local-lucha-global-5-logros-climáticos-en-2022/")
    
    @bot.command()
    async def creator(ctx):
        await ctx.send(
            "Si quieres saber sobre mi creador:"
            "Es una persona 😀"
            "Vive en un pais 😅"
            "Tiene un nombre(Yonas por si querias saber)"
            "Y este comando es medio troll solo para perder el tiempo 😴"
        )
    
    @bot.command()
    async def RM(ctx):
        await ctx.send(
            "RM significa reciclaje mecanico y junto al comando una breve informacion:"
            "El reciclaje mecánico es uno de los métodos más comunes para reciclar plásticos. Es un proceso físico que no cambia la composición química del material, sino que lo limpia, tritura y vuelve a fundir para fabricar nuevos productos. 😎"
            )

    @bot.command()
    async def RQ(ctx):
        await ctx.send(
            "RQ es la manera que mi creador tomo para abreviar Reciclaje Quimico y una breve descripcion de ello:"
            "El reciclaje químico es un proceso avanzado que transforma químicamente los plásticos en sus componentes básicos (monómeros o aceites), permitiendo que se reutilicen como si fueran materia prima virgen. A diferencia del reciclaje mecánico, sí cambia la estructura química del material.🧪"
            )

    @bot.command()
    async def RB(ctx):
        await ctx.send(
            "RB significa Reciclaje biologico y, ¿que es?:"
            "El reciclaje biológico es un proceso mediante el cual los materiales orgánicos biodegradables son descompuestos por organismos vivos, principalmente microorganismos, para convertirlos en sustancias naturales útiles, como abono o biogás. 🏝"
            )

    @bot.command()
    async def REN(ctx):
        await ctx.send(
            "REN para mi creador significaba Reciclaje Energetico y con ello una informacion del"
            "El reciclaje energético es un proceso en el cual los residuos, que no pueden ser reciclados mecánica o químicamente, se utilizan para generar energía, ya sea en forma de electricidad, calor o combustible. 🚕"
            )

    bot.run("")

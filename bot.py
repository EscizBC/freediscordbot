import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = '/') 
bot.remove_command('help')

TOKEN = input('TOKEN: ') 
print('BOT Started')

@bot.event
async def on_ready(): 
    await bot.change_presence(status = discord.Status.idle, activity = discord.Game(name = 'dedsec.exe')) 

@bot.event 
async def on_member_join(member):
    channel = client.get_channel( 737010855232667680 ) 
    
    role = discord.utils.get(member.guild.roles, id = 737264480794312825) 
    await member.add_roles( role ) 

@bot.command(pass_context = True) 
@commands.has_permissions(administrator = True)
async def qq (ctx):
    await ctx.channel.purge(limit  = 1 )
    await ctx.send(f'@everyone, {ctx.message.author.mention} приветствует чат! ') 

@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def bb (ctx):
    await ctx.channel.purge(limit  = 1 )
    await ctx.send(f'@everyone ,{ctx.message.author.mention} прощается со всеми!')

@bot.command(pass_content = True)
@commands.has_permissions( administrator = True)

async def clear (ctx , amount = 100):
    await ctx.channel.purge( limit = amount )

@bot.command( pass_context = True)
@commands.has_permissions( administrator = True) 

async def kick (ctx, member: discord.Member,*,reason = None ):
    await ctx.channel.purge( limit = 1 ) 
    await member.kick(reason = reason) 
    await ctx.send (f'kick user  { member.mention }') 
    
@bot.command(pass_context = True) 
@commands.has_permissions( administrator = True) 

async def ban (ctx,member: discord.Member,*, reason = None ): 
    await ctx.channel.purge( limit = 1 ) 
    await member.ban(reason = reason ) 
    await ctx.send (f'ban user  {member.mention}')    

@bot.command(pass_context = True ) 
@commands.has_permissions( administrator = True) 

async def unban (ctx , * , member): 
    await ctx.channel.purge( limit = 1) 
    ban_users = await ctx.guild.bans() 
    
    for ban_entery in ban_users : 
        user = ban_entry.user 
        
        await ctx.guild.unban( user ) 
        await ctx.send(f'unbaned user  { user.mention}' )
        
        return 

@bot.command(pass_context = True ) 
@commands.has_permissions( administrator = True) 

async def mute ( ctx, member :discord.Member ): 
    await ctx.channel.purge( limit = 1 ) 
    mute_role = discord.utils.get( ctx.message.guild.roles, name = 'mute') 
    await member.add_roles( mute_role)
    await ctx.send(f'Пользователь  {member.mention} ,получил бан за нарушение правил')
         


@bot.command(pass_context = True ) 
@commands.has_permissions( administrator = True)
async def ah (ctx): 
    await ctx.send('```1. /ban [@Пользователь] ```')
    await ctx.send('```2. /kick [@Пользователь]```')
    await ctx.send('```4. /mute [@Пользователь]```')
    await ctx.send('```5. /clear```') 
    await ctx.send('```6. /makeadmin [@Пользователь]```')

  
     

@bot.command(pass_content = True) 
@commands.has_permissions(administrator = True)
async def makeadmin ( ctx, member :discord.Member ): 
    await ctx.channel.purge( limit = 1 ) 
    admin_role = discord.utils.get( ctx.message.guild.roles, name = 'АДМИН') 
    await member.add_roles(admin_role) 
    await ctx.send(f'Пользователь  { member.mention } ,встал на пост Администратора,давайте поздравим его!')


bot.run(TOKEN)

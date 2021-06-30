import discord
import os
import random
from keep_running import keep_running

a = ['BOKACHODA RAZE MAIN', 'BHAIIIIIIII KIIII GAME!!!!@!@!', 'Eh yu-guh you know what fucking just get lost of- out of this fucking game man. 78 grenades left-er bachcha, overpowered, broken kothakarer ekta character, you useless, skill-less, kichui dorkar nei, third class ekta agent.', 'Carry dekhchis!! Carry Dekchis, Carry Dekchis!!!! Aro barbe, aro barbe', 'GAAND MAI NHI HAI GOODA TOH HUM PE KAHE KOODA', 'BHAAIII!! BHUL CALLOUT DILI BOLE MORE GELAM!!', 'EI JONYE KHELINA. Sala bullshit dogshit game ekta. KONO SKILL NEI RECOIL NEI. HEAD OFF KORE REKHECHE. Mane Amae Ekta kotha bol. Raze e ki ektuo skill laage? Ami satchel boosting er kotha bolchina obviously. But just bhab Tor dike Ekta boombot, duto raze nade and a fucking BAZOOKA asche. Tui ki korbi? MANE RIOT KISHOB BHUL BHAL BALANCING. JETAR NERF DORKAR SHETAI NERF KORENA. REYNA ER FLASH KE NERF KORTE HOTO, KINTU NA. OR HEALTH ORB KOMIYE DILO.', 'MALTA HEAD OFF KORE REKHECHE!!!', 'SOB HEADS SOB HEADS ATO HEAD MARCHI DEKHACCHE NA AMAKE', 'WHY AM I SO MUCH BETTER THAN YOU', 'RAJORSHI SHARAJIBON AMADER BOJHA HOYE THAKBI. KICHU TOH KOR. PLANT O KORCHISH NA FRAG O KORCHISH NA. DAILY 3O MINUTES AIMLAB E PRACTISE KORBI!!@@', "sage I don't like being toxic but LEAVE THE GAME BITCH WE WILL GET MORE MONEY", "NOOB KISKO BOL RHA HAI BE?! NOOB KISKO BOL RHA HAI?!!", "ABEY JETTTTTTTT!!!!! JETT COULD YOU FUCKING MOVE?!!@#", "BHAIIIIIII NORTE NORTEEEEEEEEEEEEEEEE!!!!@#$%^&*", 'TUI MAARIYE DILI AMAYE']

client = discord.Client();

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  message.content = message.content.lower()
  
  if message.content.startswith('$rage') :
    random.shuffle(a)
    await message.channel.send(a[0])
  elif message.content.startswith('$hello') :
    await message.channel.send('Hullo!')
  elif message.content.startswith('$raze'):
    await message.channel.send('BOKACHODA RAZE MAIN')
  elif message.content.startswith('$carry'):
    await message.channel.send('Carry dekhchis!! Carry Dekchis, Carry Dekchis!!!! Aro barbe, aro barbe')
  elif message.content.startswith('$gaand'):
    await message.channel.send('GAAND MAI NHI HAI GOODA TOH HUM PE KAHE KOODA')
  elif message.content.startswith('$game'):
    await message.channel.send('BHAIIIIIIII KIIII GAME!!!!@!@!')
  elif message.content.startswith('$callout'):
    await message.channel.send('BHAAIII!! BHUL CALLOUT DILI BOLE MORE GELAM!!')
  elif message.content.startswith('$bulldog'):
    bulldog = ['BULLDOG TA KII GUN!!! KONO AIM NEI PATTERN NEI KICHUI NEI', 'BULLDOG TA KHUB POTENT WEAPON, ATO HEAD MARCHI DAKHACHE NA']
    random.shuffle(bulldog)
    await message.channel.send(bulldog[0])
  elif message.content.startswith('$head'):
    head = ['SOB HEADS SOB HEADS ATO HEAD MARCHI DEKHACCHE NA AMAKE','MALTA HEAD OFF KORE REKHECHE!!!']
    random.shuffle(head)
    await message.channel.send(head[0])
  elif message.content.startswith('$better'):
    await message.channel.send('WHY AM I SO MUCH BETTER THAN YOU')
  elif message.content.startswith('$help'):
    await message.channel.send('Command list for Ichibot\n\n$help\t\t$warnim\t\t$rage\n$hello\t\t$raze\t\t$carry\n$gaand\t\t$game\t\t$callout\n$bulldog\t$head\t\t$better\n$bojha\t\t$toxic\t\t$noob\n$jett\t\t$norte\n\nCreated by xxEasterGrymm#2517')
  elif message.content.startswith('$warnim'):
    await message.channel.send("Yes that's me buaoa!")
  elif message.content.find('raze') != -1:
    await message.channel.send("RAZE ER NAAM NIBI NA!")
  elif message.content.find('swarnim') != -1 or message.content.find('ichizaya') != -1 or message.content.find('zwarnim') != -1 or message.content.find('shawarnim') != -1 or message.content.find('ichibot') != -1:
    await message.channel.send("KON BOKACHODA AMAR NAAM NILO?!")
  elif message.content.startswith('$bojha'):
    await message.channel.send("RAJORSHI SHARAJIBON AMADER BOJHA HOYE THAKBI. KICHU TOH KOR. PLANT O KORCHISH NA FRAG O KORCHISH NA. DAILY 3O MINUTES AIMLAB E PRACTISE KORBI!!@@")
  elif message.content.startswith('$toxic'):
    await message.channel.send("sage I don't like being toxic but LEAVE THE GAME BITCH WE WILL GET MORE MONEY")
  elif message.content.startswith('$noob'):
    await message.channel.send("NOOB KISKO BOL RHA HAI BE?! NOOB KISKO BOL RHA HAI?!!")
  elif message.content.startswith('$jett'):
    await message.channel.send("ABEY JETTTTTTTT!!!!! JETT COULD YOU FUCKING MOVE?!!@#")
  elif message.content.startswith('$norte'):
    await message.channel.send("BHAIIIIIII NORTE NORTEEEEEEEEEEEEEEEE!!!!@#$%^&*")
  elif message.content.find('69') != -1:
    await message.channel.send("Nice ;)")


keep_running()
client.run(os.getenv('TOKEN'))
'''
Ben Lepsch aka Dovahkiin
DovaBot

Bot for the Scandals Family Discord server
'''

import discord, asyncio, random

gaz_coins = {"<@!262637906865291264>" : 0, "<@!178876334095859712>" : 0, "<@!201509495220731906>" : 0,
             "<@!158033864562835456>" : 0, "<@389919287785160714>" : 0, "<@!187697102615216128>" : 0,
             "<@303235342935523330>" : 0, "<@180875776671875072>" : 0, "<@108833905552977920>" : 0,
             "<@251806188243648512>" : 0, "<@!210984200235515907>" : 0, "<@209575733989736448>" : 0}

            #Dovahkiin, JSD, NeatoBurrito, Mege, Gazorpazorp, Astrae, Bizna, Fone, Gen_1, Zenattra, pandabearkev, kevadrenaline

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
            
        if message.content.startswith('Ding! GG') and message.author.id == 159985870458322944:
            file = discord.File("levelupimg.png",filename="levelupimg.png")
            await message.channel.send("Level Up!", file=file)

        if message.content.startswith('!gazcoins'):
            command = message.content.split()
            if len(command) > 1:
                if command[1] in gaz_coins:
                    gaz_coins[command[1]] += 1
                    await message.channel.send(command[1] + " now has " + str(gaz_coins[command[1]]) + " gaz coins!")
            else:
                sender = "<@" + str(message.author.id) + ">"
                sender2 = "<@!" + str(message.author.id) + ">"
                if sender in gaz_coins:
                    gaz_coins[sender] += 1
                    await message.channel.send(sender + " now has " + str(gaz_coins[sender]) + " gaz coins!")
                if sender2 in gaz_coins:
                    gaz_coins[sender2] += 1
                    await message.channel.send(sender2 + " now has " + str(gaz_coins[sender2]) + " gaz coins!")
        if message.content.startswith('!spam'):
            command = message.content.split()
            command.pop(0)
            
            number = int(command[0])
            command.pop(0)
            
            print_string = ''
            for i in command:
                print_string += i
                print_string += ' '

            for i in range(number):
                await message.channel.send(print_string)

        if message.content.startswith('!badping'):
            await message.channel.send('<:Pingsock:485258651708424194>')

        if message.content.startswith('!diagnoseme'):
            responses = ['you have HIV.','you have coronary artery disease.','you are having a stroke.','you have lung cancer.','you have type 1 diabetes.','you have Alzheimer\'s disease.','you have tuberculosis.','you have melanoma.']
            number = random.randint(1,7)
            await message.channel.send('After researching your symptoms, I conclude that ' + responses[number])
        if message.content.startswith('!dovabotcommands'):
            await message.channel.send('''!hello : outputs "Hello <user>" \n!spam <number of times> <message> : spams the set message the number of times \n!badping : prints the pingsock emoji
!diagnoseme <symptoms> : Diagnoses your symptoms and outputs what disease you have.''')

client = MyClient()
client.run('NDkzOTM4MDM3MTg5OTAyMzU4.DosPTw.fUkMw5MEh7C1yoAcNMRK-MEKjmw')

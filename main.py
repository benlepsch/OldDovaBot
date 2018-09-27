'''
Ben Lepsch aka Dovahkiin
DovaBot

Bot for the Scandals Family Discord server
'''

import discord, asyncio, random, time

gaz_coins = {"<@!262637906865291264>" : 11, "<@!178876334095859712>" : 7, "<@!201509495220731906>" : 6,  # Dovahkiin, JSD, NeatoBurrito
             "<@!158033864562835456>" : 14, "<@389919287785160714>" : 6, "<@!187697102615216128>" : 7,   # Mege, Gazorpazorp, Astrae
             "<@303235342935523330>" : 1, "<@180875776671875072>" : 8, "<@108833905552977920>" : 12,     # Bizna, Fone, Gen_1
             "<@251806188243648512>" : 3, "<@!210984200235515907>" : 1, "<@209575733989736448>" : 4,     # Zenattra, PandaBearKev, Kevadrenaline
             "<@!252315498551836673>" : 11, "<@!348278804973748238>" : 0, "<@384489637193973767>" : 0,   # WhaleScience, SantaClaws, Corpsetaker
             "<@385092345814581260>" : 6, "<@420346616977817602>" : 2, "<@175784984655822848>" : 7,      # SlayinSteven, DevilOW, Matthzw
             "<@!257037119153897472> " : 16} # Liberosi/Aku

'''

Ding! GG @shadowburn to fuel pls, you j
1     2  3
'''

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        game = discord.Game("new torbjorn")
        await client.change_presence(status=discord.Status.idle, activity=game)
    
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
            
        if message.content.startswith('Ding! GG') and message.author.id == 159985870458322944:
            command = message.content.split()
            print_string = "Level up! "
            file = discord.File("levelupimg.png",filename="levelupimg.png")

            name = command[2]
            arr = []
            for char in name:
                arr += char

            arr.pop(len(arr) - 1)
            final_name = ''
            for i in arr:
                final_name += i
            command[2] = final_name
            
            if command[2] in gaz_coins:
                gaz_coins[command[2]] += 1
                print_string += command[2] + " now has " + str(gaz_coins[command[2]]) + " gaz coins!"

            await message.channel.send(print_string, file=file)

        if message.content.startswith('!gazcoins'):
            command = message.content.split()
            if len(command) > 1:
                if command[1] in gaz_coins:
                    await message.channel.send(command[1] + " has " + str(gaz_coins[command[1]]) + " gaz coins!")
            else:
                sender = "<@" + str(message.author.id) + ">"
                sender2 = "<@!" + str(message.author.id) + ">"
                if sender in gaz_coins:
                    await message.channel.send(sender + " has " + str(gaz_coins[sender]) + " gaz coins!")
                if sender2 in gaz_coins:
                    await message.channel.send(sender2 + " has " + str(gaz_coins[sender2]) + " gaz coins!")
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
        if message.content.startswith('!applause'):
            await message.channel.send('\U0001F44F' * 50)

        if message.content.startswith('!diagnoseme'):
            responses = ['you have HIV.','you have coronary artery disease.','you are having a stroke.','you have lung cancer.','you have type 1 diabetes.','you have Alzheimer\'s disease.','you have tuberculosis.','you have melanoma.']
            number = random.randint(1,7)
            await message.channel.send('After researching your symptoms, I conclude that ' + responses[number])
        if message.content.startswith('!dovabotcommands'):
            await message.channel.send('''!hello : outputs "Hello <user>" \n!spam <number of times> <message> : spams the set message the number of times \n!badping : prints the pingsock emoji
!diagnoseme <symptoms> : Diagnoses your symptoms and outputs what disease you have. \n!gazcoins <user(optional)> : outputs the number of gazcoins the user has. If there isn't a user entered, it gives the number you have.
!applause : prints the clapping emoji 50 times''')

client = MyClient()
client.run('NDkzOTM4MDM3MTg5OTAyMzU4.DosPTw.fUkMw5MEh7C1yoAcNMRK-MEKjmw')

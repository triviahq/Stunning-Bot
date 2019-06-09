import asyncio
import discord
import data

token = data.bot_token
client = discord.Client()

number1 = 0
number2 = 0
number3 = 0
game_running = False
local_game_running = False

def update_embed():
    global number1
    global number2
    global number3
    highlighter1 = highlighter2 = highlighter3 = ' '
    best_answer = '0'
    if (number1 == number2) and (number1 == number3):
        highlighter1 = highlighter2 = highlighter3 = ' '
    else:
        if number1 == max(number1, number2, number3):
            highlighter1 = '```'
            best_answer = ':one:'
        if number2 == max(number1, number2, number3):
            highlighter2 = '```'
            best_answer = ':two:'
        if number3 == max(number1, number2, number3):
            highlighter3 = '```'
            best_answer = ':three:'

    if data.embed is None:
        data.embed = discord.Embed(title='', color=0x89cff0)
        data.embed.add_field(name="Answer 1", value= highlighter1 + str(number1) + highlighter1, inline=False)
        data.embed.add_field(name="Answer 2", value= highlighter2 + str(number2) + highlighter2, inline=False)
        data.embed.add_field(name="Answer 3", value= highlighter3 + str(number3) + highlighter3, inline=False)
        data.embed.set_image(url='https://cdn.discordapp.com/attachments/559357612068700183/566999873430355968/13-26-52-nitro_1.gif')
        data.embed.set_footer(text= 'By: ')

        data.embed_best = discord.Embed(title='', color=0x89cff0)
        data.embed_best.add_field(name="Best answer:", value=best_answer, inline=True)
    else:
        data.embed.set_field_at(0, name="Answer 1", value= highlighter1 + str(number1) + highlighter1, inline=False)
        data.embed.set_field_at(1, name="Answer 2", value= highlighter2 + str(number2) + highlighter2, inline=False)
        data.embed.set_field_at(2, name="Answer 3", value= highlighter3 + str(number3) + highlighter3, inline=False)

        data.embed_best.set_field_at(0, name="Best answer:", value=best_answer, inline=True)


def update_data():

    global game_running
    global number1
    global number2
    global number3

    file1 = open('data/num1.txt', 'r')
    file2 = open('data/num2.txt', 'r')
    file3 = open('data/num3.txt', 'r')
    file4 = open('data/gamerunning.txt', 'r')

    try:
        number1 = float(file1.read())
        number2 = float(file2.read())
        number3 = float(file3.read())
        game_running = int(file4.read())
        game_running = True if game_running != 0 else False
    except:
        pass
    file1.close()
    file2.close()
    file3.close()
    file4.close()

async def check_for_updates():
    global local_game_running
    global game_running
    global number1
    global number2
    global number3

    await client.wait_until_ready()

    event = asyncio.Event()
    loop = asyncio.get_event_loop()
    async def waiter_proc(event):
        await asyncio.sleep(8)
        event.set()

    while not client.is_closed:
        await asyncio.sleep(1)
        update_data()
        if game_running and local_game_running == False:
            update_embed()
            data.message = await client.send_message(data.output_channel, embed=data.embed)
            local_game_running = True
            event.clear()
            waiter_task = loop.create_task(waiter_proc(event))

        elif game_running:
            update_embed()
            await client.edit_message(data.message, embed=data.embed)
            if event.is_set():
                await waiter_task
                event.clear()
                await client.send_message(data.output_channel,
                                          embed=data.embed_best)

        if game_running == False:
            local_game_running = False

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!say') and message.channel.id == data.admin_chat:
        await client.send_message(message.channel, 'What do you want to be announced?')
        response1 = await client.wait_for_message(author=message.author, timeout=60)
        if response1.clean_content:
            vw = response1
            return await client.send_message(data.output_channel, (vw.content))

    if message.content.startswith('!game') and message.channel.id in data.input_hq_private:
        #
        return await client.send_message(message.channel, 'time to next game: ')

@client.event
async def on_ready():
    print("Bot is ready!")

client.loop.create_task(check_for_updates())
client.run(token)

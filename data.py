import discord

def  init():
    global bot_token
    global self_bot_token
    global message
    global embed
    global output_channel
    global input_channels
    global command_channel

    global game_in_session
    global counter_public_1
    global counter_public_2
    global counter_public_3
    global counter_private_1
    global counter_private_2
    global counter_private_3
    global counter1
    global counter2
    global counter3
    global weight
    global weight_time
    global seconds_elapsed

bot_token = 'NTg3MTk5NTU4OTQ2MjU4OTc0.XPzg8Q.0S9ztlL5e7oz8n5DPuEG5g_IWx4'
self_bot_token = 'NTIzgzNTg1MjgzNTcxNzE1.XLjC0g.21ETRX-syGpr-W2m_-JPkqlaDS0
embed = None
embed_best = None

#trivia-answers
output_channel = discord.Object(id= '559357612068700183')

input_hq_private  = [
    "538176524470190090",
    "516780082619088905",
    "523360037067030530",
	"514915043796713482",
	"496855838703616032",
	"532833017706577930",
	"544381529829146645",
    "558136902885048329",
    "566979656083963918", # answers1
    "559442345674670082", #answers2
    '559357612068700183' #trivia-answers
]
input_hq_public = ['']
command_channel = '559357612068700183' #trivia-answers
admin_chat = '559442345674670082' # answers2

game_in_session = False
counter_public_1 = 0
counter_public_2 = 0
counter_public_3 = 0
counter_private_1 = 0
counter_private_2 = 0
counter_private_3 = 0
counter1 = 0
counter2 = 0
counter3 = 0
weight = 5
weight_time = 1
wronggone1 = 0
wronggone2 = 0
wronggone3 = 0

seconds_elapsed = 0

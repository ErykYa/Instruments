import telepot

token = '5425485399:AAGBw7iForvgDXjRkUfiBNtP12OE4hm7zVU'
my_id = -799345051
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(-799345051, text, parse_mode='Markdown')

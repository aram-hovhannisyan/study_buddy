import telebot
from telebot import types


TOKEN = "Add Your Tokhen"

bot = telebot.TeleBot(TOKEN)

commands = {
    'start': 'Get used to the bot 🤖',
    'help': 'Gives you information about the available commands❓',
    'reviews': 'Show reviews from other users 🌟',
    'becomeSolver': 'Become a solver and help others 👩‍🔧',
    'inviteFriend': 'Invite your friends to use the bot 📩',
    'statistics': 'Show statistics about bot usage 📊'
}

def create_inline_menu():
    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    button_pairs = [list(commands.items())[i:i + 2] for i in range(0, len(commands), 2)]
    for pair in button_pairs:
        row = []
        for key, value in pair:
            if value == "becomeSolver":
                value = "Become Solver"
            elif value == "inviteFriend":
                value = "Invite Friend"
            button_text = key.upper() + " " + value[-1]
            callback_data = "menu_" + key
            button = types.InlineKeyboardButton(text=button_text, callback_data=callback_data)
            row.append(button)
        inline_keyboard.row(*row)
    return inline_keyboard



@bot.message_handler(commands=['start'])
def command_start(message):
    cid = message.chat.id
    bot.send_message(cid, "Hello, this is the Study Buddy Bot 😊\n\nHere's how everything works:\n• You send your request.\n• Solvers propose their price.\n• You choose up to 3 people.\n• We take a prepayment.\n• Solvers are notified that they've been chosen.\n• We complete the order.\n• After completion, we pay the solver.\n• Guarantee for the solution — 10 days.\n\nYou can write to the manager via 'Main Menu' -> 'Ask a Question'. If something goes wrong, write 'Cancel'.")
    bot.send_message(cid, "To see the menu, use the /menu command.")


@bot.message_handler(commands=['menu'])
def command_menu(message):
    cid = message.chat.id
    bot.send_message(cid, "Here are all the features of Study Buddy:", reply_markup=create_inline_menu())

@bot.callback_query_handler(func=lambda call: call.data.startswith('menu_'))
def handle_inline_menu(call):
    cid = call.message.chat.id
    # print(call)
    command = call.data.split('_')[1]
    bot.send_message(cid, f"You clicked on '{command}' option.")
    # print(call.message)
    # bot.send_message(call.message.from_user.id,  f"/{command}")


# Start the bot
bot.infinity_polling()

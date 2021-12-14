from telethon.sync import TelegramClient
# api_id and api_hash you must take from https://my.telegram.org/. Create your app (any) and get it.
api_id =                                    # Your api_id in int format (for example, 1234567)
api_hash =                                  # Your api_hash in str format (for example, 'deadbeef1337600613')
username =                                  # Session name in str format (for example, 'Anon')
counter_deleted_message = 0
client = TelegramClient(username, api_id, api_hash)
client.start()
dialog_array = {}

for dialog in client.iter_dialogs():
    dialog_array[dialog.id] = dialog.name

print("You are currently in the following chats:")
for dialog in client.iter_dialogs():
    message_counter = 0
    
    for message in client.iter_messages(dialog.id, from_user='me'):
        message_counter += 1
    print('"{}" with ID {} contains \033[31m\033[43m {} \033[0m of your message(s)'.format(dialog.name, dialog.id, message_counter))
    message_counter = 0
    
while True:
    print()
    chat = int(input('Enter chat ID to remove your chat messages or "0" (without quotes) for exit: '))
    print()
    if chat == 0:
        print('Bye bye!')
        break
    else:
        for message in client.iter_messages(chat, from_user='me'):
            if message.raw_text is not None:
                client.delete_messages(chat, message)
                counter_deleted_message += 1
        print('Deleted {} post(s) from chat "{}"'.format(counter_deleted_message, dialog_array[chat]))
        counter_deleted_message = 0

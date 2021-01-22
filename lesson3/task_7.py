def int_func(user_text):
    return user_text[0].upper() + user_text[1:]


user_text = 'a good beginning is half the battle'
text_buffer = []
for i in user_text.split():
    text_buffer.append(int_func(i))

print(' '.join(text_buffer))

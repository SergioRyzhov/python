with open("file.txt", 'w') as f:
    while True:
        some_text_line = input('Input the empty string for end.\n'
                               'Input some text line: ')
        if some_text_line != '':
            f.write(some_text_line + '\n')
        else:
            break

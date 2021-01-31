with open("task_2.txt", "r") as f:
    q_words = 0
    for count, i in enumerate(f, 1):
        q_words = len(i.split())
        print(f'Line: {count}, words: {q_words}')

with open('task_4.txt', 'r', encoding='utf-8') as fr:
    with open('task_4.2.txt', 'w', encoding='utf-8') as fw:
        fw.write(fr.readline().replace('One', 'Один'))
        fw.write(fr.readline().replace('Two', 'Два'))
        fw.write(fr.readline().replace('Three', 'Три'))
        fw.write(fr.readline().replace('Four', 'Четыре'))

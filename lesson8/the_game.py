import random


class Game:

    def __init__(self):
        self.barrels = self.barrels_creator
        self.now = self.get_barrels()
        self.barrels_rem = self.barrels_remains()

    def __str__(self):
        return f'New barrel: {self.now} (remains {self.barrels_rem})'

    def start_game(self):
        """the main controller in the game"""
        self.user_choice = input(f'Do the cross out number? (y/n) \n')
        if self.user_choice == 'y':
            self.check_barrel()
            if self.human == False:
                self.stop_game()
                print('Computer win!')
                return ''
            if self.count_hum_dash() >= 15:
                self.stop_game()
                print('You win!')
                return ''
            if self.count_hum_dash() >= 15 and self.count_com_dash() >= 15:
                self.stop_game()
                print('the D R A W! It was hard! ;)')
                return ''
            self.get_barrels()
            self.barrels_remains()
            print('\n')
            print(g.__str__())
            c.output(c.human_card)
            c.output(c.comp_card)
        elif self.user_choice == 'n':
            self.check_barrel()
            if self.human == True:
                self.stop_game()
                print('Computer win!')
                return ''
            if self.count_com_dash() >= 15:
                self.stop_game()
                print('Computer win!')
                return ''
            self.get_barrels()
            self.barrels_remains()
            print('\n')
            print(g.__str__())
            c.output(c.human_card)
            c.output(c.comp_card)
        else:
            print('You should input (y/n)')

    def stop_game(self):
        self.user_choice = 'abort'

    def check_barrel(self):
        """check the barrel in the card"""
        self.human = False
        self.comp = False
        for i in c.human_card:
            if self.now in i:
                i[i.index(self.now)] = '-'
                # i.insert(i.index(self.now), '-')
                self.human = True
        for i in c.comp_card:
            if self.now in i:
                i[i.index(self.now)] = '-'
                # i.insert(i.index(self.now), '-')
                self.comp = True

    def count_hum_dash(self):
        """count the human dashes"""
        self.human_d = 0
        for i in c.human_card:
            self.human_d += i.count('-')
        return self.human_d

    def count_com_dash(self):
        """count the computer dashes"""
        self.comp_d = 0
        for i in c.comp_card:
            self.comp_d += i.count('-')
        return self.comp_d

    @property
    def barrels_creator(self):
        """generate a barrels list for the game"""
        barrels = []
        for i in range(1, 91):
            barrels.append(str(i))
            i += 1
        random.shuffle(barrels)
        return barrels

    def get_barrels(self):
        """get one barrel from the list"""
        barrel_now = random.choice(self.barrels)
        self.barrels.remove(barrel_now)
        self.now = barrel_now
        return barrel_now

    def barrels_remains(self):
        """count how many barrels remains in the list"""
        self.barrels_rem = len(self.barrels)
        return len(self.barrels)


class Cards:
    def __init__(self):
        """the cards data"""
        self.human_card = self.card_creator()
        self.comp_card = self.card_creator()

    def card_creator(self):
        """the cards generator"""
        num_data = []
        while len(num_data) < 15:
            num = random.randint(1, 90)
            if num_data.count(num) == 0:
                num_data.append(num)
        count = 0
        new_card = []
        for i in range(3):
            card_line = []
            for k in range(5):
                card_line.append(str(num_data[count]))
                count += 1
            for spaces in range(4):
                card_line.append(' ')
            random.shuffle(card_line)
            new_card.append(card_line)
        return new_card

    def output(self, arg):
        """view for the cards"""
        output = []
        if arg == self.human_card:
            print(f'-------------Your card----------------')
        else:
            print(f'------------Computer card-------------')
        for i in range(len(arg)):
            output.append('\t' + '\t'.join([str(j) for j in arg[i]]))
        print('\n'.join(output) + '\n--------------------------------------')


g = Game()
c = Cards()

print(g.__str__())
c.output(c.human_card)
c.output(c.comp_card)
# print(g.now)

while True:
    g.start_game()
    if g.user_choice == 'abort':
        break

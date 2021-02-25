import random


class Game:
    def __init__(self, h, c):
        self.human_card = h
        self.comp_card = c
        self.user_choice = 'y'
        self.barrels = self.barrels_creator
        self.now = self.get_barrels
        self.barrels_rem = self.barrels_remains
        self.count_dash_h = 0
        self.count_dash_c = 0

    def __str__(self):
        return f'New barrel: {self.now} (remains {self.barrels_rem})'

    def start_game(self):
        """the main controller in the game"""
        print(self.output(self.human_card))
        print(self.output(self.comp_card))
        print(self.__str__())
        self.count_dash_h = self.count_dash(self.human_card)
        self.count_dash_c = self.count_dash(self.comp_card)
        self.check_barrel(self.human_card)
        self.check_barrel(self.comp_card)
        self.get_barrels
        self.barrels_remains
        if self.count_dash_c == 15:
            print('Computer win!')
            self.stop_game()
        u_c = input(f'Do the cross out number? (y/n) \n')
        if u_c == 'y':
            if self.count_dash_h == self.count_dash(self.human_card):
                print('Computer win!')
                self.stop_game()
            if self.count_dash_h == 14:
                print('CONGRATULATIONS! You win! ')
                self.stop_game()
        elif u_c == 'n':
            if self.count_dash_h != self.count_dash(self.human_card):
                print('Computer win!')
                self.stop_game()


    def stop_game(self):
        self.user_choice = 'abort'
        print('good bye')

    def check_barrel(self, who):
        """check the barrel in the card"""
        for i in who:
            if self.now in i:
                i[i.index(self.now)] = '-'

    def count_dash(self, card):
        """count the dashes"""
        count = 0
        for i in card:
            count += i.count('-')
        return count

    @property
    def get_barrels(self):
        """get one barrel from the list"""
        barrel_now = random.choice(self.barrels)
        self.barrels.remove(barrel_now)
        self.now = barrel_now
        return barrel_now

    @property
    def barrels_creator(self):
        """generate a barrels list for the game"""
        barrels = []
        for i in range(1, 91):
            barrels.append(str(i))
            i += 1
        random.shuffle(barrels)
        return barrels

    @property
    def barrels_remains(self):
        """count how many barrels remains in the list"""
        self.barrels_rem = len(self.barrels)
        return len(self.barrels)

    def output(self, matrix):
        """view for the cards"""
        output = []
        if matrix == self.human_card:
            for i in range(len(matrix)):
                output.append('\t'.join([str(j) for j in matrix[i]]))
            return f'-----------Your card--------------\n' + '\n'.join(
                output) + '\n----------------------------------'
        else:
            for i in range(len(matrix)):
                output.append('\t'.join([str(j) for j in matrix[i]]))
            return f'----------Computer card-----------\n' + '\n'.join(
                output) + '\n----------------------------------'


class Card:
    @property
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
            card_line_n = []
            card_line_s = [' ', ' ', ' ', ' ']
            for k in range(5):
                card_line_n.append(num_data[count])
                count += 1
            card_line_n.sort()
            card_line_n = [str(card_line_n[i]) for i in range(5)]
            card_line = []
            for i in range(9):
                if random.randint(0, 1) == 0:
                    try:
                        card_line.append(card_line_n[0])
                        card_line_n.pop(0)
                    except IndexError:
                        card_line.append(card_line_s[0])
                        card_line_s.pop(0)
                else:
                    try:
                        card_line.append(card_line_s[0])
                        card_line_s.pop(0)
                    except IndexError:
                        card_line.append(card_line_n[0])
                        card_line_n.pop(0)
            new_card.append(card_line)
        return new_card


c_h = Card()
c_c = Card()
g = Game(c_h.card_creator, c_c.card_creator)

while True:
    g.start_game()
    if g.user_choice == 'abort':
        break

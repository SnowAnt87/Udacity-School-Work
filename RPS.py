import random
import time

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class Human(Player):
    def move(self):
        print("""The Chioces:
                 Rock
                 Paper
                 Scissors""")
        return your_pick(input('Your Choice: ').lower())


class cycle_Player(Player):
    def move(self):
        return moves[0]

    def learn(self, my_move, their_move):
        moves.remove(my_move)
        moves.append(my_move)


class reflect_Player(Player):
    def move(self):
        return moves[0]

    def learn(self, my_move, their_move):
        moves.remove(their_move)
        moves.insert(0, their_move)


class random_Player(Player):
    def move(self):
        return random.choice(moves)


def your_pick(pick):
    if pick not in moves:
        print('Please pick a valid choice')
        time.sleep(2)
        your_pick(input('Your Choice: ').lower())
    else:
        return pick


def beats(one, two):
    if one == two:
        return 0
    elif ((one == 'rock' and two == 'scissors') or
          (one == 'scissors' and two == 'paper') or
          (one == 'paper' and two == 'rock')):
        return 1
    else:
        return -1


def check_win(total):
    if total > 0:
        return print('Player 1 Wins')
    elif total < 0:
        return print('Player 2 Wins')
    else:
        return print('It\'s a Tie')


def Choices():
    print("""Choose Players
          1. Simple(Rock)
          2. Easy(Cycle)
          3. Medium(Reflect)
          4. Hard(Random)
          5. Expert(Human)""")
    list_choices = [Player(), Player()]
    players = 0
    while players < 2:
        choice = input(f'Choose Player {players + 1}: ')
        try:
            if int(choice) == 1:
                list_choices[players] = Player()
            elif int(choice) == 2:
                list_choices[players] = cycle_Player()
            elif int(choice) == 3:
                list_choices[players] = reflect_Player()
            elif int(choice) == 4:
                list_choices[players] = random_Player()
            elif int(choice) == 5:
                list_choices[players] = Human()
            else:
                print('Please choose valid number')
                players -= 1
                time.sleep(2)
            players += 1
        except ValueError:
            print('Please choose a number')
            time.sleep(2)
    return list_choices


def Rounds():
    rounds = input('How many Rounds would you like: ')
    try:
        if int(rounds) > 0:
            return int(rounds)
        else:
            print('Please choose valid number')
            time.sleep(2)
            return Rounds()
    except ValueError:
        print('Please choose valid number')
        time.sleep(2)
        return Rounds()


def play_again(yes_no):
    try:
        if yes_no.lower() == 'yes':
            return True
        elif yes_no.lower() == 'no':
            return False
        else:
            return play_again(input('Please use valid input '))
    except ValueError:
        return play_again(input('Please use valid input '))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f'\nPlayer 1: {move1}  Player 2: {move2}')
        check_win(beats(move1, move2))
        time.sleep(1)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        return beats(move1, move2) + 1

    def play_game(self, rounds):
        total_score = [0, 0, 0]
        print('Game start!')
        for round in range(rounds):
            print(f'\n\nRound {round + 1}:')
            total_score[self.play_round()] += 1
            print(f'Current Score- P1:{total_score[2]} <-->' +
                  f' P2:{total_score[0]} <--> Ties:{total_score[1]}')
            time.sleep(3)
        print('Game over!')
        time.sleep(2)
        print(f'\n\nFinal Score- P1:{total_score[2]} <-->' +
              f' P2:{total_score[0]} <--> Ties:{total_score[1]}')
        time.sleep(2)
        check_win(total_score[2] - total_score[0])
        time.sleep(3)


def start():
    replay = True
    while replay:
        player_list = Choices()

        round_number = Rounds()

        game = Game(player_list[0], player_list[1])

        game.play_game(round_number)

        replay = play_again(input('Play again Yes/No '))


if __name__ == '__main__':
    start()

# You can use this workspace to write and submit your adventure game project.
import time
import random


def play_game():
    enemy = random.choice(["Jiu Jitsu", "Karate", "Tae Kwon Do",
                           "MMA Brute", "Grand Pirate", "Muay Thai"])
    direction = random.choice(["North", "South", "East", "West"])
    gender = random.choice(["he", "she"])
    skills = []

    intro(enemy, direction, gender)
    strength = weekly_training(skills)

    outro(strength, enemy, direction, gender, skills)
    replay(input("Would you like another chance "
                 "at your Kung Fu Journey?(yes/no)\n"))


def print_sleep(statement, pause_time):
    print(statement)
    time.sleep(pause_time)


def intro(enemy, direction, gender):
    print_sleep('You awaken from your slowly from your delirium.', 3)
    print_sleep('Your memory slams into your head.', 2)
    print_sleep('How could they all be gone.', 3)
    print_sleep('Wait, where are you?', 2)
    print_sleep('You see a monk standing over you, looking quizzically.', 3)
    print_sleep('"I see you\'ve finally awoken", ' + gender + ' said.', 2)
    print_sleep('"I take it from your face you\'re beginning to remember."', 2)
    print_sleep('The image of your family in chains flashes before you.', 2)
    print_sleep('"They\'ve been taken by the ' + enemy +
                ' master from the ' + direction + '."', 2)
    print_sleep('"I know ' + gender + ' did a terrifying job hiring minions,'
                ' they are beyond sinister,'
                ' but it is ' + gender + ' you must defeat."', 3)
    print_sleep('"Your Destiny has transformed today and you '
                'must begin your Kung Fu training as well '
                'fulfill your true potential, save your family,'
                ' and save the WORLD!!!!!!!!"', 3)
    print_sleep('"Three weeks stand between you and Glory!"', 3)
    print_sleep('"YOUR TRAINING BEGINS"', 2)


def weekly_training(skills):
    week = 0
    strength = "balance"
    while week < 3:
        week += 1
        print_sleep('"You are starting WEEK ' + str(week) +
                    ' of your training."', 2)
        print_sleep('"There are 3 temples of study at this monastery,'
                    ' choose your upcoming WEEK of training wisely:"', 2)
        print_sleep('1. Wing Chun Temple of Flexability', 0)
        print_sleep('2. Wudang Temple of Strength', 0)
        print_sleep('3. Shaolin Temple of Technique', 0)
        new_skill = input('Which Temple? ')
        if new_skill == "1":
            print_sleep('Your flexability shows great improvement'
                        ' after a week at the Monastery', 3)
            if "flexability" in skills:
                strength = "flexability"
                print_sleep('"I see you have chosen to give'
                            ' flexability extra attention."', 3)
            skills.append("flexability")
        elif new_skill == "2":
            print_sleep('Your strength shows great improvement'
                        ' after a week at the Monastery', 3)
            if "strength" in skills:
                strength = "strength"
                print_sleep('"I see you have chosen to give'
                            ' strength extra attention."', 3)
            skills.append("strength")
        elif new_skill == "3":
            print_sleep('Your technique shows great improvement'
                        ' after a week at the Monastery', 3)
            if "technique" in skills:
                strength = "technique"
                print_sleep('"I see you have chosen to give'
                            ' technique extra attention."', 3)
            skills.append("technique")
        else:
            week -= 1
            print_sleep('You must not have understood me,'
                        ' which number temple, lets begin again', 3)
    return strength


def outro(strength, enemy, direction, gender, skills):
    print_sleep('"You have finally completed your Kung Fu training."', 2)
    print_sleep('"It is time for you to complete your'
                ' journey and fulfill your Destiny!"', 3)
    print_sleep('As you journey to your family, ' + strength +
                ' is the only thing on your mind,', 2)
    print_sleep(strength + ' is the focus of your Kung Fu training, ' +
                strength + ' is your guide.', 2)
    print_sleep('You head ' + direction + ', ' + gender +
                ' is ' + direction + '.', 3)
    print_sleep('As you approach the house of the ' + enemy +
                ' master, you know now is the time.', 3)
    print_sleep('Your eyes lock with the ' + enemy +
                ' master from the ' + direction + '.', 3)
    print_sleep('"WHERE IS MY FAMILY!!," '
                'you yell at the top of your lungs.', 2)
    print_sleep('The ' + enemy + ' master gives you a sinister sneer.', 2)
    print_sleep('"We only answer to POWER in the ' + direction +
                '," ' + gender + ' said, "AHAHAHA!"', 3)

    if strength == "balance":
        print_sleep('Serenity surrounds you, balance holds you, you speak', 2)
        print_sleep('"You can not shake me, my goal is true,'
                    ' release my Family or face defeat"', 2)
        print_sleep('The serene look on your face enrages the ' +
                    enemy + ' master. ' + gender +
                    ' lunges forward, the fight begins!', 3)
        print_sleep('Every move the ' + enemy +
                    ' master makes you have the counter.', 0)
        print_sleep('Always one step ahead, counter on the ready', 2)
        print_sleep('After what doesn\'t feel like to long to you, ' +
                    gender + ' falls exhausted.', 2)
        print_sleep('"You\'ve won for now," a smoke bomb and ' +
                    gender + ' has disappeared.', 2)
        print_sleep('After defeating the ' + enemy +
                    ' master of the ' + direction + ',', 2)
        print_sleep('you collect your family, and vow to use Kung Fu'
                    ' to bring lasting balance to the ' + direction + ','
                    'and in time the world!', 6)
    else:
        if "flexability" not in skills:
            weakness = "flexability"
        elif "strength" not in skills:
            weakness = "strength"
        elif "technique" not in skills:
            weakness = "technique"
        print_sleep('As rage fills you, you yell, '
                    '"Then you will answers to the power of my Kung Fu!!', 2)
        print_sleep('You throw everything you\'ve got at the ' + enemy +
                    ' master, but ' + gender +
                    ' is ready for everything you bring', 2)
        print_sleep('After the fight goes on a while you '
                    'start to lose more and more ground', 2)
        print_sleep('Your ' + strength + ' is supreme, but without ' + weakness
                    + ' you have no connection with your true power.', 2)
        print_sleep('The ' + enemy + ' master smiles, ' + gender +
                    ' delivers the final blows of the battle.', 2)
        print_sleep('Your thoughts slip to your family as '
                    'you blackout before the worst that is to come.', 0)
        print_sleep(':(', 6)


def replay(again):
    if again == "yes":
        play_game()
    elif again != "no":
        print_sleep("Speak Clearly!!!!", 1)
        replay(input('Would you like another chance at'
                     ' your Kung Fu Journey?(yes/no)\n').lower())


play_game()

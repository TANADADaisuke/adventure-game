import random
import time


def print_pause(mentions_to_display):
    print(mentions_to_display)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    response = input(prompt).lower()
    if str(option1) == response or str(option2) == response:
        return response
    else:
        return valid_input(prompt, option1, option2)


def intro(monster):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + monster +
                " is somoewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")


def field_event(item, monster, weapon, players_life, monsters_life):
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    house_or_cave = valid_input("(Please enter 1 or 2.)\n", "1", "2")
    if house_or_cave == "1":
        house_event(item, monster, weapon, players_life, monsters_life)
    elif house_or_cave == "2":
        cave_event(item, monster, weapon, players_life, monsters_life)


def house_event(item, monster, weapon, players_life, monsters_life):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and "
                "out steps a " + monster + ".")
    print_pause("Eep! This is the " + monster + "'s house!")
    print_pause("The " + monster + " attacks you!")
    if item == "dagger":
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    fight_or_runaway(item, monster, weapon, players_life, monsters_life)


def cave_event(item, monster, weapon, players_life, monsters_life):
    print_pause("You peer cautiously into the cave.")
    if item == "dagger":
        if weapon == "sword":
            print_pause("It turns out to be only a very small cave.")
            print_pause("Your eye catches a glint of metal behind a rock.")
            print_pause("You have found the magical Sword of Ogoroth!")
            print_pause("You discard your silly old dagger "
                        "and take the sword with you.")
            item = "sword"
        elif weapon == "stick":
            print_pause("It turns out to be only a very small cave.")
            print_pause("Your eye catches a tinny woody box behind a rock.")
            print_pause("In the box, you have found the "
                        "magical Stick of Ogoroth!")
            print_pause("You discard your silly old dagger and "
                        "take the stick with you.")
            item = "stick"

    elif item == weapon:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
    print_pause("You walk back out to the field.")
    field_event(item, monster, weapon, players_life, monsters_life)


def fight_or_runaway(item, monster, weapon, players_life, monsters_life):
    print_pause(f"\nYour Life: {players_life}  "
                f"{monster.capitalize()}'s Life: {monsters_life}")
    fight_or_runaway = valid_input("Would you like to "
                                   "(1) fight or "
                                   "(2) run away?\n", "1", "2")
    if fight_or_runaway == "1":
        fight(item, monster, weapon, players_life, monsters_life)
    elif fight_or_runaway == "2":
        runaway(item, monster, weapon, players_life, monsters_life)


def fight(item, monster, weapon, players_life, monsters_life):
    # Player's turn
    monsters_life = player_attack(item, monster, monsters_life)
    if monsters_life == 0:
        player_win(monster)
    else:
        # monster's turn
        players_life = monster_attack(monster, players_life)
        if players_life == 0:
            player_defeated()
        else:
            fight_or_runaway(item, monster, weapon,
                             players_life, monsters_life)


def runaway(item, monster, weapon, players_life, monsters_life):
    print_pause("You run back into the field. "
                "Luckily, you don't seem to have been followd.")
    field_event(item, monster, weapon, players_life, monsters_life)


def player_attack(item, monster, monsters_life):
    if item == "dagger":
        return player_attack_with_dagger(monster, monsters_life)
    elif item == "sword":
        return player_attack_with_sword(monster, monsters_life)
    elif item == "stick":
        return player_attack_with_stick(monster, monsters_life)


def player_attack_with_dagger(monster, monsters_life):
    attack_or_miss = random.randint(1, 6)
    if attack_or_miss > 1:
        print_pause("You attack! But your dagger is no match "
                    f"for the {monster}.")
        monsters_life -= 0
    else:
        print_pause("You attack! But it misses.")

    return monsters_life


def player_attack_with_sword(monster, monsters_life):
    attack_or_miss = random.randint(1, 6)
    if attack_or_miss > 1:
        print_pause("The Sword of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.")
        print_pause(f"You attack! The {monster} recieve 1 damage.")
        monsters_life -= 1
    else:
        print_pause("You attack! But it misses.")

    return monsters_life


def player_attack_with_stick(monster, monsters_life):
    attack_or_miss = random.randint(1, 6)
    if attack_or_miss > 1:
        print_pause("The magical stick shines brightly with your magical "
                    f"words and a lightning attacks the {monster}.")
        print_pause(f"The {monster} recieve 1 damage.")
        monsters_life -= 1
    else:
        print_pause("You attack! But it misses.")

    return monsters_life


def monster_attack(monster, players_life,):
    attack_or_miss = random.randint(1, 6)
    if attack_or_miss > 1:
        print_pause(f"{monster.capitalize()} attacks! You recieve 1 damaged.")
        players_life -= 1
    else:
        print_pause(f"{monster.capitalize()} attacks! But it miss.")

    return players_life


def player_win(monster):
    print_pause(f"You defeated the {monster}! You are victorious!")
    # You win the game. Ask if play again.
    ask_play_again()


def player_defeated():
    print_pause("You do your best...")
    print_pause("But you have been defeated!")
    # You loose and the game end. Ask if play again.
    ask_play_again()


def ask_play_again():
    play_again = valid_input("Would you like to play again? (y/n)\n",
                             "y", "n").lower()
    if "y" in play_again:
        print_pause("Excellent! Restarting the game ...")
        # go back to the game
        play_game()
    if "n" in play_again:
        # end of the game
        print_pause("Thanks for playing! See you next time.")


def play_game():
    item = "dagger"
    weapon = random.choice(["sword", "stick"])
    monster = random.choice(["wicked fairie",
                             "dragon",
                             "troll",
                             "pirate",
                             "gorgon"])
    players_life = 3
    monsters_life = 3
    intro(monster)
    field_event(item, monster, weapon, players_life, monsters_life)


play_game()

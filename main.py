from room import Room
from item import Item
from item import Medicine
from character import Character
from character import Enemy
import inspect

kitchen = Room("Kitchen")
kitchen.set_description("A bright and airy room with an expensive espresso machine.")

dining_room = Room("Dining Room")
dining_room.set_description("A dingy room with a large mahogany table with candles on either side of it.")

ballroom = Room("Ballroom")
ballroom.set_description("A lavishly decorated room with ostentatious furniture and floor-to-ceiling windows.")

billiard_room = Room("Billiard Room")
billiard_room.set_description("A dilapidated room that has seen better days, with a billiard table in the middle of it.")

smoking_room = Room("Smoking Room")
smoking_room.set_description("A dingy room with yellowing wallpaper. The smell indicates that it has been used as its name would suggest.")

kitchen.link_room(dining_room, "south")
kitchen.link_room(billiard_room, "west")
dining_room.link_room(kitchen, "north")
dining_room.link_room(ballroom, "west")
ballroom.link_room(dining_room, "east")
billiard_room.link_room(ballroom, "south")
billiard_room.link_room(kitchen, "east")
billiard_room.link_room(smoking_room, "north")
smoking_room.link_room(billiard_room, "south")

dagger = Item("dagger")
dagger.set_description("Sharp and pointy. Good for stabbing things.")

dictionary = Item("dictionary")
dictionary.set_description("Very heavy. Contains lots of words")

tome = Item("feminist anthology")
tome.set_description("A judicious selection of women's writing. It would be hard to find fault with it.")

chemex = Item("chemex coffee maker")
chemex.set_description("You could make yourself a mean cup of coffee with this. You could even reheat it later if you get distracted by fighting enemies...")

dave = Enemy("Dave", "A tedious mansplainer")
dave.set_conversation("Actually, I think you'll find that...")
dave.set_weakness("feminist anthology")
dining_room.set_character(dave)

kim = Enemy("Kim", "An irritating 'influencer'")
kim.set_conversation("Which dubious snake oil weight loss product should I endorse today?")
kim.set_weakness("dictionary")
kitchen.set_character(kim)


jeff = Enemy("Jeff", "An obnoxious self-help guru")
jeff.set_conversation("Have you read my latest book, 'Achieving Success Through Flagrant Sabotage and Indefatigable Self-Promotion'?")
jeff.set_weakness("dagger")
ballroom.set_character(jeff)

horatio = Enemy("Horatio", "A loafer-clad hipster")
horatio.set_conversation("Do you have any Aeropress filter papers on you?")
horatio.set_weakness("chemex coffee maker")
billiard_room.set_character(horatio)

sage = Character("Sage", "An incredibly cute black and white cat")
sage.set_conversation("Meow! Could you put on the hot wall? It's a bit chilly in here.")
smoking_room.set_character(sage)

potion = Medicine("magic potion")
potion.set_description("A refreshing-looking magic elixer")
potion.set_healthscore(int(1))

kitchen.set_item(chemex)
ballroom.set_item(tome)
dining_room.set_item(dictionary)
billiard_room.set_item(dagger)
smoking_room.set_item(potion)

print("Explore an eccentric house, acquire weapons and do combat with some of the most fearful villains that modern life has to offer. Type a direction to move between rooms, talk to speak to the people in the rooms, take to pick up weapons, list to see what weapons you have, health to check your health, score to check your score and fight to engage your enemies in battle! \n \nIf you use the wrong weapon against an enemy, you will lose health. If you defeat an enemy, you get a point.")

inventory = []

current_room = kitchen

score = 0

dead = False

health = 4

while dead == False and score < 4:
	print("\n")
	current_room.get_details()
	inhabitant = current_room.get_character()
	room_item = current_room.get_item()

	if inhabitant is not None:
		inhabitant.describe()
	if room_item is not None:
		room_item.describe()

	command = input("> ")
	if command.lower() in ["north", "south", "east", "west"]:
		current_room = current_room.move(command)

	elif command.lower() == "talk":
		if inhabitant is not None:
			inhabitant.talk()
		else:
			print("There's no one to talk to here. Well this is embarrassing...")

	elif command.lower() == "take":
		if room_item is not None:
                        if isinstance(room_item, Medicine) == True:
                                health += room_item.healthscore
                                print("Much better! Your health is " + str(health) + ".")
                        else:
                                inventory.append(room_item.name)
                                print("You now have the following weapons in your arsenal: ")
                                for weapon in inventory:
                                        print(weapon)
                        current_room.item = None

		else:
			print("There's nothing here for you to take!")

	elif command.lower() == "fight":
		if isinstance(inhabitant, Enemy) == False:
			print(inhabitant.name + " is a friend! There's no need to fight!")
		elif len(inventory) > 0:
			print("What do you want to fight with? You have: ")
			for weapon in inventory:
				print(weapon)
			chosen_weapon = input("> ")
			if chosen_weapon.lower() not in inventory:
				print("You don't have this! Pick something else!")
			else:
	#			inhabitant.fight(chosen_weapon)
				if inhabitant.fight(chosen_weapon.lower()) == True:
					score += 1
					print("Your score is " + str(score) + ".")
					current_room.character = None
					if score == 4:
						print("You win - hurrah!")
				else:
					health -= 1
					print(inhabitant.name + " has defeated you! Ouch, your health score has dropped to " + str(health) + ".")
					if health == 0:
						dead = True
						print("Game over! Your score was " + str(score) + ".")
		else:
			print("You can't fight anyone just now, you're unarmed, you fool!")

	elif command.lower() == "list":
		if len(inventory) >= 1:
			print("You have the following weapons in your arsenal: ")
			for weapon in inventory:
				print(weapon)
		else:
			print("You're currently unarmed - eek!")

	elif command.lower() == "health":
		print("Your health is " + str(health) + ".")

	elif command.lower() == "score":
		print("Your score is " + str(score) + ".")

	elif command.lower() == "quit":
                dead = True
	else:
		print("I don't understand")

import time
#display header for adventure game
print ('Welcome to my adventure game!!!')
print ('+++++++++++++++++++++++++++++++++')
time.sleep(1)
print ('You are going on a journey and can bring one item with you.')
time.sleep(2)
print ('You can choose a flashlight(f), a water bottle(w), a candy bar(c) or a shoe(s)')
time.sleep(1)
choice = input('Do you want to bring a flashlight(f), a water bottle(w), a candy bar(c) or a shoe(s)? ')
while not (choice == 'f' or choice == 'w' or choice == 'c' or choice == 's'):
    choice = input('Please enter f for flashlight, w for water bottle, c for candy bar or s for shoe')
print ('You hear a noise behind you, what should you do?')
time.sleep(1)
follow = input('Do you want to follow the sound? yes(y) or no(n)')
if follow == 'y':
    print ('You proceed cautiously down the path but suddently, the noise stops')
    print ('You turn around and start walking back to the starting point but you are LOST!')
    print ('You pull out your cell phone and try to make a call but there is no signal')
    time.sleep(1)
    print('In front of you are three paths, which should you choose?')
    direction = input('Do you want to take the left, right, or middle paths?: ')
    if direction.lower() == 'left':
        print('There is a bear blocking your path')
        time.sleep(2)
        if choice == 'c':
            print ('Good thing you have a candy bar to distract the bear, you use it an escape to safety!')
            time.sleep(1)
            print ('CONGRATULATIONS! YOU WIN!!!')
        else:
            print ('Too bad you did not bring a candy bar to distract the bear - it eats you!!')
            time.sleep(1)
            print ('SORRY, YOU LOSE!')
    elif direction.lower().strip() == 'middle':
        print('You keep walking but darkness falls and you are lost in the forest')
        time.sleep(1)
        if choice == 'f':
            print('Good thing you brought a flashlight! You find the path to safety')
            time.sleep(1)
            print ('CONGRATULATIONS! YOU WIN!!!')
        else:
            print ('Too bad you did not bring a flashlight, you fall in a hole and die')
            time.sleep(1)
            print ('SORRY, YOU LOSE!')
    else:
        print('You continue walking but fall into quicksand and no one is there to save you')
        time.sleep(1)
        print ('SORRY, YOU LOSE!')
else:
    print ('Good plan, it is best not to take risks')  
    print ('You keep walking and hear a noise coming behind you, it is gettig louder and louder')
    run = input('Do you want to make a call(c) or start to run(r)')
    while not run == 'r':
        print('Your call failed, do you want to call again(c) or run(r)')
        run = input('What will you do, call(c) or run(r)')
    print ('You start running and the noise behind you gets really loud')
    time.sleep(2)
    print ('You are running really fast and suddenly, the noise stops')
    time.sleep(1)
    print ('You reach a bridge but it is guarded by the biggest Troll you have ever seen')
    time.sleep(1)
    print ('The troll bellows, "Who goes there? Answer my riddle and give me candy and you can pass')
    answer = input('What is the best program for DLCS certification?: ')
    if answer.lower().strip() == 'lesley':
        print('You are correct, Lesley University has the best program for DLCS Certification')
        if choice == 'c':
            print('You brought me a candy bar and have great taste in education!')
            print ('CONGRATULATIONS! YOU WIN')
        else:
            print ('You know education but I am hungry and I must eat you now')
            print ('SORRY, YOU LOSE!')
    else:
        print ('Wrong answer, I will eat you now!')
        print ('SORRY, YOU LOSE!')
#Pet Age Calculator
print ('You can use this program to calculate the age of your dog or cat in human years')
#User inputs for pet type and age of pet
pet = input('Do you have a dog or a cat?: ')
while not (pet.lower() == 'dog' or pet.lower() == 'cat'):
    pet = input('Please enter "dog" or "cat"')
pet_age = input ('Please enter the age of your dog in years (1,2,5 etc.): ')
pet_age = int(pet_age)
#Dog logic
if pet.lower() == 'dog':
    age_diff = pet_age - 2  
    if age_diff >= 0:
        print ('The age of your dog in human years is: ', age_diff * 4 + 24)
    elif pet_age == 1:
        print ('The age of your dog in human years is 12')
    else:
        print ('Awwwww, look at the baby pup! They are so cute!')
#Cat Logic
else:
    age_diff = pet_age - 2  
    if age_diff >= 0:
        print ('The age of your cat in human years is: ', age_diff * 4 + 24)
    elif pet_age == 1:
        print ('The age of your cat in human years is 15')
    else:
        print ('Awwwww, look at the little kitten! They are so cute!')

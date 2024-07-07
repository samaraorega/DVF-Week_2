#While loop

digit = 4
while digit > 0:
    print(digit)
    digit -=1
print("The digit reached", digit, "so the while loop's condition became False and stopped execution")

#Break and continue statements

numbers = list(range(0, 30))
new_list = []
for num in numbers:
    if len(new_list) > 4:
        print(f'We have enough even numbers in new_list ({len(new_list)}). break will stop the for loop now')
        break
    elif num % 2 == 0:
        new_list.append(num)
    elif num % 2 != 0:
        continue
        print('i never get executed')
    print(num, 'is even.')
    print('this does not print for odd numbers\nbecause the continue statement skips\nthe code that follows in the for loop\nand goes straight back to the next element in the for loop')


for i in list(range(0, 5)):
    if True:
        print(i)
        continue
    print("I'll never get executed")

names = ['aNNE', 'JaNe', 'willIAM', 'WanDA', 'WeSt', 'HELEN', 'tHoMaS', 'HENrY', 'John', 'Marshall', 'May']
formatted_names = []
check_count = 0

for name in names:
    if name.startswith('w') or name.startswith('W'):
        check_count += 1
        continue
    elif len(formatted_names) >= 4:
        check_count += 1
        break
    else:
        formatted_names.append(name.title())

print('before', names)
print('after', formatted_names)
print(check_count)   




time_for_breakfast = 1468 # in seconds
number_of_cooked_pancakes = 0

# write your while loop here
    
# use a while loop to make 5 pancakes for breakfast
while number_of_cooked_pancakes < 5:
    time_for_breakfast =- 37
    number_of_cooked_pancakes =+ 1
    continue
    

# each pancake takes 27 seconds to cook on each side
# it takes an average of 5 seconds to flip a pancake, add or remove a pancake from the pan.
# you must decrease the time_for_breakfast each time you
# add a pancake to the skillet (frying pan) or flip a pancake (i.e. 2 times per pancake)
# there is only room for one pancake at a time



# print out how much time is remaining

print(time_for_breakfast)
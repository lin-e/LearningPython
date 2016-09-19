import random
iteration_count = 1000
picked_numbers = [1, 2, 3, 4, 5, 6] # it doesn't matter what numbers are picked, since it has the same statistical chance
matches = [0, 0, 0, 0, 0, 0, 0]
for i in range (0, iteration_count): # do 1m times
    drawn_numbers = list()
    for x in range (0, 6):
        pick_number = True
        new_number = 0
        while pick_number:
            new_number = random.randint(1, 59)
            if new_number not in drawn_numbers:
                pick_number = False
        drawn_numbers.append(new_number)
    match_count = 0
    for item in picked_numbers:
        if item in drawn_numbers:
            match_count += 1
    matches[match_count] += 1
for k in range (0, 7):
    match_text = "matches"
    if k == 1:
        match_text = "match  "
    print(str(k) + " " + match_text + " : " + str(matches[k]))

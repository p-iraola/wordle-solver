from collections import Counter

#Creating list of playable words
flist = open('scrabble_words.txt').readlines()
words = [i.rstrip('\n') for i in flist if len(i) == 6]

guesses = 1
while True:
	
	#Removing words that contain an incorrect letter
	incorrect_letters = input('Enter any incorrect letters from your guess: ').strip()
	new_words = []
	flag = 1
	for i in words:
		for x in incorrect_letters:
			if x not in i:
				flag = 1
			else:
				flag = 0
				break
		if flag == 1:
			new_words.append(i)

	words = new_words

	#Correct letter positioning
	answer1 = input('\nAre there any letters in the correct position (y/n)? ').strip()

	while answer1 == 'y':
		correct_words = []
		position = int(input('\nWhich position (1,2,3,4,5)? '))
		
		if position == 1:
			letter = input('\nEnter letter: ').strip()
			for i in words:
				if i[0] == letter:
					correct_words.append(i)

		if position == 2:
			letter = input('\nEnter letter: ').strip()
			for i in words:
				if i[1] == letter:
					correct_words.append(i)

		if position == 3:
			letter = input('\nEnter letter: ').strip()
			for i in words:
				if i[2] == letter:
					correct_words.append(i)

		if position == 4:
			letter = input('\nEnter letter: ').strip()
			for i in words:
				if i[3] == letter:
					correct_words.append(i)

		if position == 5:
			letter = input('\nEnter letter: ').strip()
			for i in words:
				if i[4] == letter:
					correct_words.append(i)

		words = correct_words
		answer1 = input('\nAny more (y/n)? ').strip()


	#Incorrect letter positioning
	answer2 = input('\nAre there any letters in an incorrect position (y/n)? ').strip()
	if answer2 == 'y':
		
		must_haves = []
		first = input('\nEnter first letter, or leave this blank: ').strip()
		if first:
			must_haves.append(first)

		second = input('Enter second letter, or leave this blank: ').strip()
		if second:
			must_haves.append(second)

		third = input('Enter third letter, or leave this blank: ').strip()
		if third:
			must_haves.append(third)

		fourth = input('Enter fourth letter, or leave this blank: ').strip()
		if fourth:
			must_haves.append(fourth)

		fifth = input('Enter fifth letter, or leave this blank: ').strip()
		if fifth:
			must_haves.append(fifth)

		incorrect_position = []
		for i in words:
			if i[0] == first:
				incorrect_position.append(i)
			if i[1] == second:
				incorrect_position.append(i)
			if i[2] == third:
				incorrect_position.append(i)
			if i[3] == fourth:
				incorrect_position.append(i)
			if i[4] == fifth:
				incorrect_position.append(i)
		
		new_words = []
		for i in words:
			for x in incorrect_position:
				if x not in i:
					flag = 1
				else:
					flag = 0
					break
			if flag == 1:
				new_words.append(i)

		if new_words:
			words = new_words

		new_words = []
		for i in words:
			for x in must_haves:
				if x in i:
					flag = 1
				else:
					flag = 0
					break
			if flag == 1:
				new_words.append(i)
		
		words = new_words
	print('\nPossible words: ' + str(words))

	#Guessing the next word
	counts = Counter()
	for word in words:
		counts.update(word)

	#Scoring the words based on counts     
	#This will be a list of tuples (score, word)     
	word_scores = []
	for word in words:
		unique_chars = set(word)
		word_score = sum([counts.get(c) for c in unique_chars])
		word_scores.append((word_score, word))
	
	#Sorting the list and picking the word with the highest score     
	comp_guess = sorted(word_scores, reverse=True)[0][1]
	print('\nBest guess out of ' + str(len(words)) + ' words: ' + comp_guess.upper())
	guesses += 1
	if guesses == 5:
		print("You're a failure.")
		break

	#Reseting or ending loop
	result = input('Was this right (y/n)? ').strip()
	if result == 'y':
		print('\n'+ comp_guess.upper() + ' was the correct word!')
		print('It only took ' + str(guesses) + ' guesses.')
		break
	else:
		print("\nLet's try again.",
		'\nThere is no need to re-enter any information from the previous guesses.')
		print('\n')
		words.remove(comp_guess)
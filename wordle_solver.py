from collections import Counter

#Creating list of playable words
flist = open('scrabble_words.txt').readlines()
words = [word.rstrip('\n') for word in flist if len(word) == 6]

guesses = 0
while True:
	
	#Removing words that contain an incorrect letter
	incorrect_letters = input('Enter any incorrect letters from your guess: ').strip()
	new_words = []
	for word in words:
		for incorrect_letter in incorrect_letters:
			if incorrect_letter in word:
				break
		else:
			new_words.append(word)

	words = new_words

	#Correct letter positioning
	answer1 = input('\nAre there any letters in the correct position (y/n)? ').strip()

	while answer1 == 'y':
		correct_words = []
		position = int(input('\nWhich position (1,2,3,4,5)? '))
		
		if position == 1:
			letter = input('\nEnter letter: ').strip()
			for word in words:
				if word[0] == letter:
					correct_words.append(i)

		if position == 2:
			letter = input('\nEnter letter: ').strip()
			for word in words:
				if word[1] == letter:
					correct_words.append(i)

		if position == 3:
			letter = input('\nEnter letter: ').strip()
			for word in words:
				if word[2] == letter:
					correct_words.append(i)

		if position == 4:
			letter = input('\nEnter letter: ').strip()
			for word in words:
				if word[3] == letter:
					correct_words.append(i)

		if position == 5:
			letter = input('\nEnter letter: ').strip()
			for word in words:
				if word[4] == letter:
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
		for word in words:
			if word[0] == first:
				incorrect_position.append(word)
			if word[1] == second:
				incorrect_position.append(word)
			if word[2] == third:
				incorrect_position.append(word)
			if word[3] == fourth:
				incorrect_position.append(word)
			if word[4] == fifth:
				incorrect_position.append(word)
		
		new_words = []
		for word in words:
			for incorrect in incorrect_position:
				if incorrect in word:
					break
			else:
				new_words.append(word)

		if new_words:
			words = new_words

		new_words = []
		for word in words:
			for must in must_haves:
				if must not in word:
					break
			else:
				new_words.append(word)
		
		words = new_words
	print('\nPossible words: ' + str(words))

	if len(words) == 1:
		print('\nThe answer has to be: ' + str(words[0]).upper())
		break
	
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
		print("Even when you're cheating you're still a failure.")
		break

	#Reseting or ending loop
	result = input('Was this right (y/n)? ').strip()
	if result == 'y':
		print('\n'+ comp_guess.upper() + ' was the correct word!')
		print('And it only took ' + str(guesses) + ' guesses.')
		break
	else:
		words.remove(comp_guess)
		if len(words) == 1:
			guesses += 1
			print('\nThen correct answer has to be: ' + str(words[0]).upper())
			print('\nAnd it only took ' + str(guesses) + ' guesses.')
			break
		print("\nLet's try again.",
		"\nThere's no need to re-enter any information from your previous guesses.")
		print('\n')

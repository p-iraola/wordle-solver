from collections import Counter
flist = open('scrabble_words.txt').readlines()
words = [word.rstrip('\n') for word in flist if len(word) == 6]

incorrect_letters = []
right_letter_wrong_place = []
right_letter_right_place =[]
guesses = 1
comp_guess = ''

while True:
	if guesses > 7:
		print('Even while cheating you still managed to fail.')

	if comp_guess:
		guess = comp_guess
		guesses += 1
	else:
		guess = input('Enter your guess: ').strip()
		while len(guess) != 5:
			guess = input(str('Please enter a valid guess: ')).strip()
		guesses += 1

	print('\nEnter the results of the guess. '
	'\nType 1 for a grey letter, 2 for a yellow letter, ' 
	'or  3 for green letter.')

	results = input('\nResults: ').strip()
	while len(results) != 5 :
		results = input(str('Please enter valid results: ')).strip()

	#Match guess to results
	for i, letter in enumerate(guess):
		if results[i] == '1':
			if letter not in incorrect_letters:
				incorrect_letters.append(letter)
		if results[i] == '2':
			right_letter_wrong_place.append((i, letter))
		if results[i] == '3':
			right_letter_right_place.append((i, letter))

	#Remove words with wrong letters
	new_words = []
	for word in words:
		for incorrect in incorrect_letters:
			if incorrect in word:
				break
		else:
			new_words.append(word)
	words = new_words

	#Ensure all yellow letters are in the word
	new_words = []
	for word in words:
		for i in range(len(right_letter_wrong_place)):
			if right_letter_wrong_place[i][1] not in word:
				break
		else:
			new_words.append(word)
	words = new_words

	#Remove words with incorrect yellow positioning
	new_words = []
	for word in words:
		for position, letter in right_letter_wrong_place:
			if word[position] == letter:
				break
		else:
			new_words.append(word)
	words = new_words

	#Remove words without correct green positioning
	new_words = []
	if right_letter_right_place:
		for word in words:
			for position, letter in right_letter_right_place:
				if word[position] != letter:
					break
			else:
				new_words.append(word)
		words = new_words
	
	if len(words) == 2:
		print('\nLooks like you gotta guess between ' + str(words[0]) +
		' and ' + str(words[1]) + '.')
		break

	if len(words) == 0:
		print('There are no words that match your parameters.')
		break
	elif len(words) == 1:
		print('\nThe correct word is ' + str(words[0].upper()) + '.')
		print('It only took ' + str(guesses) + ' guesses.')
		break
	else:
		print('Possible words: ' + str(words))
	
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
	print('\nBest guess out of ' + str(len(words)) + ' words: ' + 
	comp_guess.upper())

	#Reseting or ending loop
	result = input('Was this right (y/n)? ').lower().strip()
	while result != 'y' and result != 'n':
		print('\nPlease enter y for yes or an n for no.')
		result = input('Was this right (y/n)? ').lower().strip()
	if result == 'y':
		print('\n'+ comp_guess.upper() + ' was the correct word!')
		print('It only took ' + str(guesses) + ' guesses.')
		break
	elif result == 'n':
		print("\nOk, then let's try again.")

import nltk 
nltk.download('words')

from nltk.corpus import words # type: ignore

def check(word):
    if word in words.words() and len(word)==5:
        is_word=True
    else:
        is_word=False
    return is_word

secret_word=input('Enter the secret 5-letter word: ')
while not check(secret_word):
    print('Not a valid word, try again!')
    secret_word=input('Enter the secret 5-letter word: ')

N=int(input('Input allowed number of attempts: '))
attempts=0

for i in range(0+1,N+1):
    print(f'Enter your attempt #{i}')
    player_word=input()
    while not check(player_word):
        if not player_word in words.words():
            print('Not a  valid word, try again')
        elif len(player_word)!=5:
            print(f'You entered a {len(player_word)}-letter word, but a 5-letter word is needed. Try again')
        
        print(f'Enter your attempt #{i}')
        player_word=input()
    print('You entered a 5-letter word')
    attempts+=1
    letter_in_the_right_spot=0
    for k in range(len(secret_word)):
        for j in range(len(player_word)):
            if secret_word[k]==player_word[j] and k==j:
                print(f'{secret_word[k]} is in the secret_word and in the correct spot #{k+1}')
                letter_in_the_right_spot+=1
                print(f'Correct letters in the correct spot: {letter_in_the_right_spot}')
            
            elif secret_word[k]==player_word[j]:
                print(f'{secret_word[k]} is in the secret_word but not in the correct spot')
            else:
                continue 
    if attempts<=N and letter_in_the_right_spot==5:
        print(f'Congrats you won using {attempts} attempt(s)')
        break
    if attempts==N:
        print(f'You already used #{N} attempts. Better luck tomorrow!')
        break
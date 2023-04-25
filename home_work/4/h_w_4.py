hard = {'передача': 'transmission', 'будівля': 'building', 'космос': 'space'}
medium = {'слово': 'word', 'світ': 'world', 'океан': 'ocen'}
easy = {'собака': 'dog', 'кіт': 'cat', 'око': 'eye'}
scores = 0
answers = {}

print('Enter your level. easy, medium, hard')
player_choice = input('-> ')
if player_choice == 'easy':
    words = easy
elif player_choice == 'medium':
    words = medium
elif player_choice == 'hard':
    words = hard
else:
    words = None

if not words:
    print("Неправильний вибір")
    exit()

print(f'Вибраний рівень складності, {player_choice}')

for word in words:
    print(f'пропонуємо вгадати {len(words)} слів, підберіть переклад')
    print('Переведіть слово')
    print(f'{word} {len(word)} букв, починається на {word[0]}')
    player_answer = input('-> ')
    if player_answer.lower() == word:
        scores += 1
        answers[]

dict_scores = {0: 'погано', 1: "незадовільно", 2: "нормально", 3: "добре"}
print(f'Ваш рівень {dict_scores.get(scores)}')

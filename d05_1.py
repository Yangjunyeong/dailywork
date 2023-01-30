import random

def making_card_list() -> list:
	card_list = []

	for shape in ["spade", "heart", "diamond", "clover"]:

		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:

			card_list.append((shape, number))

	return card_list
# 순서를 비교하기 위해 문자를 숫자로 변환하는 함수 
def decision_winner(player):
	if player == "A":
		return 14
	elif player == "K":
		return 13	
	elif player == "Q":
		return 12
	elif player == "J":
		return 11
	else:
		return player
# 숫자부분이 같을 경우 비교할 문양을 숫자로 변환하는 함수
def shape_win(s):
	if s == "spade":
		return 4
	elif s == "diamond":
		return 3	
	elif s == "heart":
		return 2
	elif s == "clover":
		return 1

trump_card_list = making_card_list()


score =[0,0]
while max(score) < 6: # 리스트 내의 최대값이 6이 될 때 까지 반복하기
	Player1 = random.choice(trump_card_list)
	trump_card_list.remove(Player1) #뽑았던 카드를 트럼프 리스트에서 제거
	Player2 = random.choice(trump_card_list)
	trump_card_list.remove(Player2)
	
	# 숫자함수에 5이상의 수를 곱한 값에 문양함수를 더한 값을 비교하면 
	# 뽑은 숫자가 같을 때는 더한 값으로 비교 가능!
	if decision_winner(Player1[1])*5 + shape_win(Player1[0]) > decision_winner(Player2[1])*4 + shape_win(Player2[0]):
		
		print(Player1, Player2, 'player1 win!')
		score[0] += 1
	else: 
		print(Player1, Player2, 'player2 win!')
		score[1] += 1
	
#스코어가 6이 되는 값을 갖고 있는 인덱스를 찾기
print(f'{score[0]}:{score[1]} Finally player{score.index(6)+1} win')

	
	

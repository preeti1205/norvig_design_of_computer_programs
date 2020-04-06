import random
import itertools


def best_hand(hand):
	"Return the 5 cards that will be make the best hand out of the 5+ cards you have"
	return max( itertools.combinations(hand, 5), key=hand_rank )

def poker(hands):
	""" Return list of winning hands"""
	return allmax(hands, key=hand_rank)

all_ranks = '23456789TJQKA'
red_cards = [r + s for r in all_ranks for s in 'HD']
black_cards = [r + s for r in all_ranks for s in 'SC']

def best_wild_hand(hand):
	"Try all values for jokers in all 5-card selections. ? signifies Joker."
	
	# map(replacements, card)
	# test_cards = ['2D', '?B']
	# print  (map(replacements, test_cards))
	# for h in itertools.product(*map(replacements, test_cards)): #star in important. Multiply by itself as many times
	# 	print h

	hands = set(best_hand(h) 
		        for h in itertools.product(*map(replacements, hand)))
	return max(hands, key=hand_rank)



def replacements(card):
	if card == '?B':
		return black_cards
	if card == '?R':
		return red_cards
	else:
		return [card] #notice how we return a list

def allmax(iterable, key=None):
	result = []
	max_val = None
	key = key or (lambda x:x)
	for x in iterable:
		val = key(x)
		if val > max_val or not result:
			result, max_val = [x], val
		elif xval == max_val:
			result.append(x)
	return result


def hand_rank(hand):
	ranks = card_ranks(hand)    #returns in sorted order
	if straight(ranks) and flush(hand):            # straight flush
		return (8, max(ranks))
	elif kind(4, ranks):                            # 4 of a kind
		return (7, kind(4, ranks), kind(1, ranks))
	elif kind(3, ranks) and kind(2, ranks):        # full house
		return (6, kind(3, ranks), kind(2, ranks))
	elif flush(hand):                              # flush
		return (5, ranks )
	elif straight(ranks):                          # straight
		return (4, max(ranks))
	elif kind(3, ranks):                           # 3 of a kind
		return (3, kind(3, ranks), ranks)
	elif two_pairs(ranks):                          # 2 pair
		return (2, two_pairs(ranks), ranks)
	elif kind(2, ranks):                           # kind
		return (1, kind(2, ranks), ranks)
	else:                                          # high card
		return (0, ranks)


def card_ranks(cards):
	ranks = ['--23456789TJQKA'.index(r) for r, s in cards]
	ranks.sort(reverse = True)

	return [5,4,3,2,1] if ranks == [14, 5, 4, 3, 2] else ranks

def straight(ranks):
	return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5

def flush(hand):
	suits = [s for r,s in hand]
	return len(set(suits)) == 1

def kind(n, ranks):
	"""Return the first rank that this hand has exactly n of.
	Return None if there is no n-of-a-kind in the hand."""
	for r in ranks:
		if ranks.count(r) == n:
			return r
	return None

def two_pairs(ranks):
	"""If there are two pair, return the two ranks as a
	tuple: (highest, lowest); otherwise return None."""
	pair_1 = kind(2, ranks)
	pair_2 = kind(2, list(reversed(ranks)))
	if pair_1 and pair_1 != pair_2:
		return (pair_1, pair_2)
	return None


def test():
	"Test cases for the functions in poker program"
	sf = "6C 7C 8C 9C TC".split() # Straight Flush
	fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
	fh = "TD TC TH 7C 7D".split() # Full House	
	assert poker([sf, fk, fh]) == sf
	assert poker([fk, fh]) == fk
	assert poker([fh, fh]) == fh
	assert poker([sf]) == sf
	assert poker([sf] + 99*[fh]) == sf

	assert hand_rank(sf) == (8, 10)
	assert hand_rank(fk) == (7, 9, 7)
	assert hand_rank(fh) == (6, 10,7) 

	assert card_rank(sf) == [10, 9, 8, 7, 6]
	assert card_rank(fk) == [9, 9, 9, 9, 7]
	assert card_rank(fh) == [10, 10, 10, 7, 7]

	assert straight([9, 8, 7, 6, 5]) == True
	assert straight([9,8,7,6,6]) == False
	assert flush(sf) == True
	assert flush(fh) == False
	return 'tests passed'

def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(num_players, num_cards_in_hand=5, deck=mydeck):
	random.shuffle(mydeck)
	hands = []
	for i in range(num_players):
		hand = mydeck[i*num_cards_in_hand: (i+1)*num_cards_in_hand]
		hands.append(hand)
	return hands

print deal(2)
print best_hand("JD TC TH 7C 7D 7S 7H".split())
print test_best_hand()



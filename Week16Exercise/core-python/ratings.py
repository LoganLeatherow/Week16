"""Restaurant rating lister."""

print("hello")

def create_scores():
    scores_txt = open('scores.txt')

    scores = {}

    for line in scores_txt:
        line=line.rstrip()
        restaurant, score = line.split(':')
        scores[restaurant] = int(score)
    
    return scores


def add_restaurant(scores):
    print("Add a new restaurant!")
    restaurant = input('Add a name:')
    rating = int(input('Rating:'))

    scores[restaurant] = rating


def display_scores(scores):
    for restaurant, rating in sorted(scores.items()):
        print(f"{restaurant} is rated at {rating}.")

scores= create_scores()

add_restaurant(scores)

display_scores(scores)
# put your code here

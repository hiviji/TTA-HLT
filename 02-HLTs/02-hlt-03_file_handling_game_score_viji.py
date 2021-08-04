import csv
from pprint import pprint 
import operator
from operator import itemgetter

def csv_to_list_of_dicts(csv_file_to_convert):
    list_of_dicts = []
    with open("game_scores.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            list_of_dicts.append(line)
    return list_of_dicts

# Read the CSV file
game_scores_list = csv_to_list_of_dicts("game_scores.csv")
#pprint(game_scores_list)

# Convert Score to integers so sort will work properly
for score in game_scores_list:
    score["score"] = int(score["score"])

# Sort by Score
scores_by_sorted = sorted(game_scores_list, key=itemgetter("score"))

# get the top score
def get_max_score(data):
      top_score=0
      for line in data:
         score = int(line["score"])
         if score>top_score:
           top_score = score
         return(top_score)

#get the bottom score
def get_min_score(data):
     min_score=0
     for line in data:
        score = int(line["score"])
        if min_score<score:
           min_score = score
     return(min_score)

#Average score
def get_average_score(data):
     total_score=0
     average_score=0
     count=len(game_scores_list)
     for line in data:
        score = int(line["score"])
        total_score += score
     average_score=total_score//count
     return(average_score)

average_score=get_average_score(game_scores_list)
print (f" \n Average Score is {average_score}")

#display the results
print(f" Top score is {scores_by_sorted[-1]['score']}")
print(f" Bottom score is {scores_by_sorted[0]['score']}")

#Average age of players in Germany
number_of_germany_players=0
total_age=0
for line in game_scores_list:
    if 'Germany' == line['country']:
     number_of_germany_players = number_of_germany_players + 1 
     age = int(line["age"])
     total_age += age
average_age=total_age//number_of_germany_players

print( f" Average age of Germany players is {average_age} \n")
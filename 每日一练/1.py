# -*- coding=utf-8 -*-
scores_string = input("enter scores:")
scores = [int(score) for score in scores_string.split(",")]
avg = sum(scores)/len(scores)
print("avg:", avg)
new_scores = [score for score in scores if score > avg]
print("new scores:", new_scores)


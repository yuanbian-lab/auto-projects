# -*- coding=utf-8 -*-
scores = []
for i in range(5):
    score = float(input(f"请输入第 {i+1} 个裁判的分数："))
    scores.append(score)

min_score = min(scores)
max_score = max(scores)
scores.remove(min_score)
scores.remove(max_score)

average_score = sum(scores) / len(scores)
print(f"得分为：{average_score}")
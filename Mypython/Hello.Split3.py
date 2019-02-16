score = "chinese=100,math=90,english=80"
score_dict = dict(item.split("=") for item in score.split(","))
print(score_dict)

print(score_dict.get("math"))

scores = 'chinese=70,math=90,english=80'
x = dict(item.split("=") for item in scores.split(","))
print(x)
print(x.get('chinese'))
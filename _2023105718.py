import random

nickname = 'khu_faker'

def rock_paper_scissors():
    method = int(random.random()*3)+1
    if method == 1:
        return "scissors"
    elif method == 2:
        return "paper"
    if method == 3:
        return "rock"
    

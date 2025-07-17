import random

# a function that generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet plus the space
#   essentially pick 'strlen' amount of chars randomly from 27 (alphabet + space)
def generate_string(strlen):
    alphabet_char_string = list(map(chr, (random.sample(range(97, 123), k = 26)))) + [' ']
    # generated_string = "".join(random.choices(alphabet_char_string, k = 28))
    return "".join(random.choices(alphabet_char_string, k = strlen))
    
def score_generated(goal_str, gen_str):
    numSame = 0
    for i in range(len(goal_str)):
        if goal_str[i] == gen_str[i]:
            numSame += 1
    return numSame / len(goal_str)

def validate_str(goal_str, current_str):
    alphabet_char_string = list(map(chr, (random.sample(range(97, 123), k = 26)))) + [' ']
    current_str = list(current_str)
    for i in range(len(goal_str)):
        if goal_str[i] == current_str[i]:
           continue 
        else:
            current_str[i] = random.choice(alphabet_char_string)
    return "".join(current_str)

def main():
    goalstring = "methinks it is like a weasel"
    newstring = generate_string(28)
    runcount = 0
    best_score = 0
    new_score = score_generated(goalstring, newstring)
    while new_score < 1:
        print(new_score, newstring)
            
        if new_score > best_score :
            best_score = new_score
        # newstring = generate_string(28)
        newstring = validate_str(goalstring, newstring)
        new_score = score_generated(goalstring, newstring)
        runcount += 1

    best_score = new_score
    print(best_score, newstring)

main()
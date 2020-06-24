import json
message = 'no message'
def new_user():
    NameJudge=input('Enter your name:')
    filename=NameJudge+'.json'
    with open(filename, 'w') as f_obj:
        json.dump(NameJudge, f_obj)

def greet_user():
    NameJudge=input('Enter Your Load Name:')
    filename=NameJudge+'.json'

    try:
        with open(filename) as f_obj:
            User=json.load(f_obj)
    except FileNotFoundError:
        print(message)
    else:
        print('Welcome Home, '+User)

judgment=input("Do you have the Accounts? Yes/No\n")
if judgment.title()=='Yes':
    greet_user()
if judgment.title()=='No':
    new_user()
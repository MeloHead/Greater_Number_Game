from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    print('********we are creating the session********')
    print('-------------------------------------------')
    if 'random_num' not in request.session:
        request.session['random_num'] = random.randint(1,100)
        print('the new random_num is---->', request.session['random_num'])
    else:
        print('random number in session is -----> ', request.session['random_num'])
    return render(request,'index.html')


def start_game(request):
    print("---------------I want to play a Game!-------------------")
    
    print(f"number in session ------> {request.session['random_num']}")
    userGuess = int(request.GET['user_guess'])
    randomNumber = request.session['random_num']
    print("Playuh guessed number ---->", request.GET['user_guess'])
    
    outcome = ""
    if userGuess > randomNumber:
        print('user guessed too HIGH')
        outcome = "too High"
    elif userGuess < randomNumber:
        print('user guessed too LOW')
        outcome = "too Low"
    else:
        print("User got it Correct")
        outcome = "Correct"
    context = {
        "outcome1": outcome,
        "userGuess": userGuess
    }
    return render(request,'index.html',context)


def delete(request):
    request.session.clear()
    # del request.session['random_num'] 
    return redirect('/')

# make an algorithm that reads the random numbers
    # use if statements to determine high or low
    # save user guess in session
    #redirect the pages for too high and too low
    # to clear put in <a> and redirect

    #create a button to destroy random number to delete session
    #redirect back to index


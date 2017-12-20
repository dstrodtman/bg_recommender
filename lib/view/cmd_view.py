import pickle

from lib.model import recommender

with open('data/gname', 'rb') as f:
    gname = pickle.load(f)
    
with open('data/gs', 'rb') as f:
    gs = pickle.load(f)
    
with open('data/gid', 'rb') as f:
    gid = pickle.load(f)

Rec = recommender.Recommender()


print("""
    Welcome to the BoardGameGeek Recommender System!

    This application is designed to provide quick, personalized 
    board game recommendations based on the games you like.

    Commands:
    like <board game name> : adds a game to your liked list
    get : fetches your personalized recommendations
    list : lists the board games you've added to your liked list
    new : clears your liked list
    quit : exit the program

    Type like and the name of your favorite game to get started! (ex: like Catan)
    """)

liked = set()
liked_gs = set()

session = True

while session == True:
    command = input()

    if command[:4] == 'like':
        game = command[5:]
        try:
            liked_gs.add(gs[game])
            liked.add(game)
            print('    {} added to list.\n'.format(game))
        except:
            print("    No listing found for {}. Please check spelling and punctuation.\n".format(game))
    elif command[:3] == 'get':
        if liked:  
            print('    Fetching your recommendations\n')
            Rec.update([e for e in liked_gs])
            print(Rec.recs)
        else:
            print("    You haven't liked any games yet. Try typing\n\nlike Catan\n")
    elif command[:4] == 'list':
        if liked:
            print("    Games you've liked:\n    {}\n".format('\n    '.join(liked)))
        else:
            print("    You haven't liked any games yet. Try typing\n\nlike Catan\n")
    elif command[:3] == 'new':
        print('    Starting new session\n')
        liked = set()
        liked_gs = set()
    elif command[:4] == 'quit':
        session = False
    else:
        print("""
    I don't understand! Please try one of the commands:

    like <board game name> : adds a game to your liked list
    get : fetches your personalized recommendations
    list : lists the board games you've added to your liked list
    new : clears your liked list
    quit : exit the program\n""")

exit()
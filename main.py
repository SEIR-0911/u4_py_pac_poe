# Global Variables
game_state = {
    "board":{},
    "turn":None,
    "turn_counter":None,
    "winner":None,
    "winner_message":None,
    "game_over":None
}
# print("game_state", game_state)

def welcome_message():
    print("----------------------")
    print("Let's play Py-Pac-Poe!")
    print("----------------------")
# welcome_message()

def reset_game_state():
    # game_state['board'] = {}
    game_state["board"]["A1"] = " "
    game_state["board"]["A2"] = " "
    game_state["board"]["A3"] = " "
    game_state["board"]["B1"] = " "
    game_state["board"]["B2"] = " "
    game_state["board"]["B3"] = " "
    game_state["board"]["C1"] = " "
    game_state["board"]["C2"] = " "
    game_state["board"]["C3"] = " "
    game_state["turn"]="X"
    game_state["turn_counter"]=0
    game_state["winner"]=""
    game_state["winner-message"]=""
    game_state["game_over"]=False
# reset_game_state()

def print_board():
    print(f"    A   B   C")
    print(f"1)  {game_state['board']['A1']} | {game_state['board']['B1']} | {game_state['board']['C1']} ")
    print(f"   -----------")
    print(f"2)  {game_state['board']['A2']} | {game_state['board']['B2']} | {game_state['board']['C2']} ")
    print(f"   -----------")
    print(f"3)  {game_state['board']['A3']} | {game_state['board']['B3']} | {game_state['board']['C3']} ")
# print_board()


def check_win():

    # A1 A2 A3
    if game_state["board"]["A1"] == game_state["board"]["A2"] == game_state["board"]["A3"] and game_state["board"]["A1"] != " ":
        game_state["game_over"] = True
        game_state["winner"] = game_state["board"]["A1"]
        game_state["winner_message"] = f"{game_state['winner']} wins after {game_state['turn_counter']+1} turns!"
    # B1 B2 B3
    elif game_state["board"]["B1"] == game_state["board"]["B2"] == game_state["board"]["B3"] and game_state["board"]["B1"] != " ":
        game_state["game_over"] = True
        game_state["winner"] = game_state["board"]["B1"]
        game_state["winner_message"] = f"{game_state['winner']} wins after {game_state['turn_counter']+1} turns!"
    # C1 C2 C3
    elif game_state["board"]["C1"] == game_state["board"]["C2"] == game_state["board"]["C3"] and game_state["board"]["C1"] != " ":
        game_state["game_over"] = True
        game_state["winner"] = game_state["board"]["C1"]
        game_state["winner_message"] = f"{game_state['winner']} wins after {game_state['turn_counter']+1} turns!"
     # A1 B1 C1
    elif game_state["board"]["A1"] == game_state["board"]["B1"] == game_state["board"]["C1"] and game_state["board"]["A1"] != " ":
        game_state["game_over"] = True
        game_state["winner"] = game_state["board"]["A1"]
        game_state["winner_message"] = f"{game_state['winner']} wins after {game_state['turn_counter']+1} turns!"
    # A2 B2 C2
    elif game_state["board"]["A2"] == game_state["board"]["B2"] == game_state["board"]["C2"] and game_state["board"]["A2"] != " ":
        game_state["game_over"] = True
        game_state["winner"] = game_state["board"]["A2"]
        game_state["winner_message"] = f"{game_state['winner']} wins after {game_state['turn_counter']+1} turns!"
    # A3 B3 C3
    elif game_state["board"]["A3"] == game_state["board"]["B3"] == game_state["board"]["C3"] and game_state["board"]["A3"] != " ":
        game_state["game_over"] = True
        game_state["winner"] = game_state["board"]["A3"]
        game_state["winner_message"] = f"{game_state['winner']} wins after {game_state['turn_counter']+1} turns!"
    # A1 B2 C3    
    elif game_state["board"]["A1"] == game_state["board"]["B2"] == game_state["board"]["C3"] and game_state["board"]["A1"] != " ":
        game_state["game_over"] = True
        game_state["winner"] = game_state["board"]["A1"]
        game_state["winner_message"] = f"{game_state['winner']} wins after {game_state['turn_counter']+1} turns!"
    # A3 B2 C1
    elif game_state["board"]["A3"] == game_state["board"]["B2"] == game_state["board"]["C3"] and game_state["board"]["A3"] != " ":
        game_state["game_over"] = True
        game_state["winner"] = game_state["board"]["A1"]
        game_state["winner_message"] = f"{game_state['winner']} wins after {game_state['turn_counter']+1} turns!"

    
def check_valid_input(input):
    if len(input)==2 and (input[0].upper()=="A" or input[0].upper()=="B" or input[0].upper()=="C") and (input[1]=="1" or input[1]=="2" or input[1]=="3") and game_state['board'][input.upper()] == " ":
        return True
    else: return False
# print(check_valid_input("a3"))
# print(check_valid_input("B2"))
# print(check_valid_input("2B"))
# print(check_valid_input("a31"))

def player_turn():
    #Starting of turn variables
    valid_input = False
    move = ""
    print(f"{game_state['turn']}'s turn.")
    # Enter move
    while not valid_input:
        print("Enter your move (e.g., B1):")
        move = input()
        valid_input = check_valid_input(move)
        if not valid_input: print(f"'{move}' is not a valid move. Try again.")
    game_state['board'][move.upper()] = game_state['turn']
# player_turn()


# def take_move(player, input):

def play_game():
    # Initialize Game
    reset_game_state()

    # Game Loop
    while not game_state["game_over"]:
        if game_state["turn_counter"]%2==0: game_state["turn"]="X"
        else: game_state["turn"]="O"
        print_board()
        player_turn()
        check_win()
        game_state["turn_counter"] += 1 
        if game_state["turn_counter"]>=9:
            game_state["game_over"] = True
            game_state["winner_message"] = "Cat's Game - It's a tie!"
    #Upon Game Over
    print_board()
    print(game_state["winner_message"])

# play_game()

def play_match():    
    welcome_message()
    # Initial Match
    X_score = 0
    O_score = 0
    Tie_score = 0
    game_count = 0
    print("How many games is your match?")
    match_length = int(input())
    
    # Game Loops
    for i in range(match_length):
        game_count+=1
        print(f"GAME {game_count}")
        play_game()
        if game_state["winner"] == "X": X_score += 1
        elif game_state["winner"] == "O": O_score += 1
        else: Tie_score += 1

    #Math Recap
    print(f"{match_length}-game match is complete!")
    print(f"Match Stats: X Wins: {X_score}, O Wins: {O_score}, Ties: {Tie_score}")

play_match()
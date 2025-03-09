from datetime import datetime

class Team:
    def __init__(self,team_name,budget):
        self.team_name = team_name
        self.budget = budget
        self.players = [] # list for all players in the team
        self.transaction = [] # log for all transactions 

    def log_transaction(self,transaction_type,description,amount=None):
        """log for team activities with dates and time."""
        timestamp = datetime.now()
        self.transaction.append({
            "type": transaction_type,
            "description": description,
            "amount": amount,
            "date": timestamp.strftime("%Y-%M-%D"),
            "time": timestamp.strftime("%H-%M-%S")
        })
    def get_transaction_log(self): #retrieve all transactions.
        return self.transaction

    def display_team_info(self): #displays team name,budget and players.
        print(f"team name:{self.team_name}")
        print(f"budget:{self.budget}")
        print(f"players:",",".join(self.players) if self.players else "no player yet")
class PlayerManagement(Team):
    def buy_player(self,player_name,price):
        if price <=self.budget:
            self.players.append(player_name)
            self.budget -= price
            self.log_transaction("player Transfer",f"bought player{player_name}",-price)
            print(f"player{player_name} bought for Ksh{price}.Remaining balance:Ksh{self.budget}")
        else:    
            print(f"insufficient budget to buy{player_name}.Available budget: Ksh{self.budget}")
    def sell_player(self,player_name,price):
        if player_name in self.players:
            self.players.remove(player_name)
            self.budget += price
            self.log_transaction("player Transfer",f"player{player_name} was sold, price")
            print(f"player {player_name} was sold for Ksh{price}.New budget is {self.budget}")
        else:
            print(f"player{player_name} is not in the team")            
class MatchManagement(Team):

    def log_match_results(self,opponent,team_score,opponent_score):
        result = "Win" if team_score > opponent_score else "Loss" if team_score < opponent_score else "Draw"
        self.log_transaction("Results",f"Match vs {opponent}:{team_score}-{opponent_score}({result})")
        print(f"Match results logged: {self.team_name} vs {opponent}:{team_score}-{opponent_score}({result})")
    def schedule_training(self,date,time):
        self.log_transaction("Training session",f"Training scheduled on {date} at {time}")
        print(f"training scheduled on {date} at {time}")
if __name__ == "__main__":
    team = PlayerManagement("City Rangers", 30000000) #team initial budget


    #Buy and sell players
    team.buy_player("Henry cook", 21000000)
    team.buy_player("Caleb chris",3000000)
    team.buy_player("Christopher cap", 2000000)
    team.buy_player("Kenny carol", 2000000)
    team.sell_player("Henry cook", 24000000)
    team.sell_player("Caleb chris", 14000000)


    match_mgmt = MatchManagement(team.team_name, team.budget)
    match_mgmt.players = team.players
    Player_mgmt = PlayerManagement(team.team_name,team.budget)
    match_mgmt.log_match_results("Rivals cf",4,1)
    match_mgmt.schedule_training("2025-3-15", "9:00 AM")

    team.display_team_info()
    print("\nTransaction Log:")
    for transaction in match_mgmt.get_transaction_log():
        print(transaction)            
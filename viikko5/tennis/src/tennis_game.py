class TennisGame:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    GAME = 4

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def tied_score(self):
        tied_scores = {
            self.LOVE: "Love-All",
            self.FIFTEEN: "Fifteen-All",
            self.THIRTY: "Thirty-All",
        }
        return tied_scores.get(self.m_score1, "Deuce")
    
    def advantage_or_win(self):
        score_difference = self.m_score1 - self.m_score2
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def running_score(self):
        score_names = {
            self.LOVE: "Love",
            self.FIFTEEN: "Fifteen",
            self.THIRTY: "Thirty",
            self.FORTY: "Forty",
        }
        player1_score = score_names[self.m_score1]
        player2_score = score_names[self.m_score2]
        return f"{player1_score}-{player2_score}"
    
    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.tied_score()
        elif self.m_score1 >= self.GAME or self.m_score2 >= self.GAME:
            return self.advantage_or_win()
        else:
            return self.running_score()

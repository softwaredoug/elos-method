
teams = {
        "orioles": 1.0,
        "yankees": 2.0,
        "redsox": 3.0,
        "bluejays": 4.0,
        }

def logistic10(x):
    return 1.0 / (1.0 + 10.0**x)


class EloModel:
    def __init__(self, teams, K=400.0):
        self.K = K
        self.teams = teams

    def expectedScore(self, rankA, rankB):
        return (logistic10((rankA - rankB) / self.K), logistic10((rankB - rankA) / self.K))

    def contest(self, teamA, scoreA, teamB, scoreB):

        scaledScoreA = scoreA / (scoreA + scoreB)
        scaledScoreB = scoreB / (scoreA + scoreB)

        rankA = self.teams[teamA]
        rankB = self.teams[teamB]
        scaledExpectedA = logistic10((rankB - rankA) / self.K)
        expectedA = scaledExpectedA * (scoreA + scoreB)
        scaledExpectedB = logistic10((rankA - rankB) / self.K)
        expectedB = scaledExpectedB * (scoreA + scoreB)
        print("Predicted %s(%s) %s --  %s(%s) %s" % (teamA, rankA, expectedA, teamB, rankB, expectedB))

        newRankA = rankA + self.K * (scaledScoreA - scaledExpectedA)
        newRankB = rankB + self.K * (scaledScoreB - scaledExpectedB)

        self.teams[teamA] = newRankA
        self.teams[teamB] = newRankB



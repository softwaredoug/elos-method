
teams = {
        "orioles": 1.0,
        "yankees": 2.0,
        "redsox": 3.0,
        "bluejays": 4.0,
        }

def logistic10(x):
    return 1.0 / (1.0 + 10.0**x)


class EloModel:
    def __init__(self, teams, K=400.0, learningRate=1.0):
        # K parameter is a conversion between rank differences and scores
        # to compute predicted scores from ranks AND to update ranks from a score
        self.K = K
        # Optionally, you may not want the impact of a contest to
        # have as direct an impact, so optionally a learning rate can tweak
        # how agressively the rankings are updated from a contest
        self.learningRate = learningRate
        self.teams = teams

    def contest(self, teamA, scoreA, teamB, scoreB):
        """ Report a contest between team A with scoreA and teamB with scoreB
        """
        scaledScoreA = scoreA / (scoreA + scoreB)
        scaledScoreB = scoreB / (scoreA + scoreB)

        rankA = self.teams[teamA]
        rankB = self.teams[teamB]
        scaledExpectedA = logistic10((rankB - rankA) / self.K)
        expectedA = scaledExpectedA * (scoreA + scoreB)
        scaledExpectedB = logistic10((rankA - rankB) / self.K)
        expectedB = scaledExpectedB * (scoreA + scoreB)
        print("Predicted %s(%s) %s --  %s(%s) %s" % (teamA, rankA, expectedA, teamB, rankB, expectedB))

        newRankA = rankA + self.learningRate * self.K * (scaledScoreA - scaledExpectedA)
        newRankB = rankB + self.learningRate * self.K * (scaledScoreB - scaledExpectedB)

        self.teams[teamA] = newRankA
        self.teams[teamB] = newRankB



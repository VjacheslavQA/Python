class MatchResult:

    def __init__(self, wins, draws, loses, scored, missed):
        self.wins = wins
        self.draws = draws
        self.loses = loses
        self.scored = scored
        self.missed = missed

    def match_result(self, scored, missed):
        self.scored += scored
        self.missed += missed
        if scored > missed:
            self.wins += 1
            print("Win")
        elif scored < missed:
            self.loses += 1
            print("Lose")
        else:
            self.draws += 1
            print("Draw")

    def count_score(self):

        return (self.wins * 3) + self.draws

    def goals_difference(self):
        return self.scored - self.missed


class CountsAllGames(MatchResult):

    def counts_all_games(self):
        return self.wins + self.draws + self.loses


if __name__ == '__main__':
    game = MatchResult(2, 2, 2, 2, 2)
    counts = CountsAllGames(2, 2, 2, 3, 2)
    print("Number of points earned by the club:", game.count_score())
    print("Calculation of the difference between goals scored and missed:", game.goals_difference())
    print("Total number of games for the team:", counts.counts_all_games())
    game.match_result(scored=1, missed=3)
    print("Number of points earned by the club:", game.count_score())
    print("Calculation of the difference between goals scored and missed:", game.goals_difference())


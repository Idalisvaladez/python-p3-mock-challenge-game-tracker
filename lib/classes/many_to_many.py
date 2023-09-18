import ipdb 
class Game:

    all = []

    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, "title"):
            print("You cannot change the title of Game.")
        elif isinstance(title, str) and len(title) > 0:
            self._title = title


    def results(self):
        #returns result in Result class attribute if the current game equals self
        return [result for result in Result.all if result.game == self]

    def players(self):
        #returns unique list of players using the results() to access the value for the passed self
        return list(set([result.player for result in self.results()]))

    def average_score(self, player):
        #grabs scores for current self using results() if it's player equals passed in player
        scores = [result.score for result in self.results() if result.player == player]
        #adds the scores and divides it by the length for average
        average = sum(scores) / len(scores)
        return average

class Player:

    all = []
    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        #returns list of results for the speciidic self from Result class attribute
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        #returns unique list of ALL games played by the particular self(player)
        return list(set([result.game for result in self.results()]))

    def played_game(self, game):
        # returns a game if it's in the objects games_played list
        return game in self.games_played()

    def num_times_played(self, game):
        # len returns the the number of items in an object
        # returning the result for specific self using results() if the results game is passed game
        return len([result for result in self.results() if result.game == game])

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if hasattr(self, 'score'):
            print("Sorry! Score cannot be changed.")
        elif isinstance(score, int) and 1 <= score <= 5000:
            self._score = score



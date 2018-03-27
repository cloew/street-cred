
class StreetCreditScore:
    """ Represents a person's calculated Street Credit Score """
    
    def __init__(self, category_scores):
        """ Initialize with the CategoryScores """
        self.category_scores = category_scores
        
    @property
    def score(self):
        """ Return the total Street Credit Score """
        return sum(category_score.score for category_score in self.category_scores)
        
    def add_score(self, category_score):
        """ Add the given score to the list of Scores """
        self.category_scores.append(category_score)
        
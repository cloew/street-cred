
class ScoreContext:
    """ Helper class to contain the context a Score was calculated in """
    
    def __init__(self, score, **kwargs):
        """ Initialize with the Score and any keyword arguments that helped calculate that score """
        self.score = score
        self.data = kwargs

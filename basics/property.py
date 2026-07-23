class apple:
    def __init__(self, shape):
        self.shape= shape 

        @property
        def word_count(self):
            return len(self.body.split())
        
a= apple("made in california")
print(a.word_count())
import random

class HangMan():
    
    """docstring for HangMan."""
    
    def __init__(self,Name):
        self.word_list = ['python','sksjti','4thsem','pakis']
        self.guess_word = random.choice(self.word_list)
        self.guess_List = list(self.guess_word)
    

    def Counter_Function(self):
        counter = 0
        for i in range(0,len(Problem1.guess_word)):

            Problem1.Label('guess the word of length ' + Problem1.guess_word + str(len(Problem1.guess_word)) + '\n')
            Problem1.EntryInput()
            Inpu = input('guess the word of length ' + Problem1.guess_word + str(len(Problem1.guess_word)) + '\n')
            Input = Problem1.submit('Input')
            if (Input == Problem1.guess_List[counter]):
                counter += 1
                Problem1.Label('correct ' + str(len(Problem1.guess_word)-counter) + ' words reamining')
            else:
                rem = str(5 - i)
                Problem1.Label('You have '+ rem + 'chances')
        if(counter != len(Problem1.guess_word)):
            Problem1.Label('Better try next time')


Problem1 = HangMan('New1')
Problem1.Counter_Function()
      

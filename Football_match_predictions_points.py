class Match(object):
    '''class docstring'''
    predicts = list()
    trueResults = list()
    def Points(self)->int :
        '''This function returns an integer as your point from matches that you have predicted .
        ten points for true predict 
        seven points for draw with goal difference 
        five points for true guess the winner
        two points for other results'''
        total_point = 0
        for i in range(len(self.trueResults)) :
            true = self.trueResults[i].split('-')
            pred = self.predicts[i].split('-')
            if true[0] == pred[0] and true[1]==pred[1]:
                total_point += 10
            elif true[0] == true[1] and pred[0] == pred[1] :
                total_point += 7
            elif true[0]>true[1] and pred[0]>pred[1] :
                total_point += 5
            elif true[0]<true[1] and pred[0]<pred[1] :
                total_point +=5 
            else :
                total_point += 2
        return total_point

match_results = ['1-1','0-1','2-1','0-3','1-1','1-3','0-0','3-0']
Predicts = ['2-2','0-3','2-1','1-3','0-0','2-2','2-0','2-0']
sample = Match()
sample.predicts = Predicts
sample.trueResults = match_results
my_score = sample.Points()
print(sample.Points.__doc__)
print('---------------------------------------------')
print('Your score is :')
print(my_score)
exit = input('Enter any key to exit :')

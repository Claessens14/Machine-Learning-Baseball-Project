import numpy as np

class GameStats(object):          
    
    def __init__(self, homeTeamNameIndex, homeTeamScoreIndex, homeTeamStatsIndex, visitorTeamNameIndex, visitorTeamScoreIndex, visitorTeamStatsIndex):
        #parse the text file
        self.statsFile = open("baseball2016.txt", "r")
        self.topArray = []
        self.sideArray = []  
        self.sc = np.zeros((30,30,30), np.int32) 
        self.sc[:,:,:] = -1  
        self.am = np.zeros((30,30), np.float32)
        self.gameList = []
        
        for line in self.statsFile:
            homeTeam = ""
            awayTeam = ""
            homeScore = 0
            awayScore = 0

            token = line.split(',')  #tokenize the string
            tokenIndex = [homeTeamNameIndex, homeTeamScoreIndex, visitorTeamNameIndex, visitorTeamScoreIndex] + [i for i in homeTeamStatsIndex] + [i for i in visitorTeamStatsIndex]
            attributes = dict()
            
            for i in xrange(len(token)):
                if(i in tokenIndex):
                    attributes[i] = removeQuotes(token[i])
                        
            self.addScore(attributes[homeTeamNameIndex], attributes[visitorTeamNameIndex], attributes[homeTeamScoreIndex], attributes[visitorTeamScoreIndex])
                       
            self.addGame(attributes[homeTeamNameIndex], attributes[homeTeamScoreIndex], [attributes[i] for i in homeTeamStatsIndex], attributes[visitorTeamNameIndex], attributes[visitorTeamScoreIndex], [attributes[i] for i in homeTeamStatsIndex])
            
        self.buildAvgMatrix()
        self.statsFile.close()      
       
    def removeQuotes(string):
        if (string.startswith('"') and string.endswith('"')) or (string.startswith("'") and string.endswith("'")):
            print("here")
            return string[1:-1]
        return string  
    
    def addGame(self, team1, score1, stats1, team2, score2, stats2):
        self.gameList.append([team1, score1, stats1, team2, score2, stats2])
    
    #give it two teams, the scores, and it will add it to the matrix
    def addScore(self, team1, team2, score1, score2):
        '''
        for a team in top array, the index in the array corrisponds to the matrix column there located in
        for a team in side array, the index in the array corrisponds to the matrix row there located in
        '''
        #team 1 score entry
        try:
            row = self.sideArray.index(team2)    

        except:
            self.sideArray.append(team2)
            row = self.sideArray.index(team2)    

        try:
            col = self.topArray.index(team1)
        except:
            self.topArray.append(team1)
            col = self.topArray.index(team1)
        temp = self.sc[row, col]
        counter = 0
        for e in temp:
            if (e == -1):
                temp[counter] = score1
                break
            counter += 1
        self.sc[row, col] = temp
        
        #team 2 score entry
        try:
            row = self.sideArray.index(team1)    
        except:
            self.sideArray.append(team1)
            row = self.sideArray.index(team1)    
            
        try:
            col = self.topArray.index(team2)
        except:
            self.topArray.append(team2)
            col = self.topArray.index(team2)
        temp = self.sc[row, col]
        counter = 0
        for e in temp:
            if (e == -1):
                temp[counter] = score2
                break
            counter += 1
        self.sc[row, col] = temp
    
    #returns the score(s) for match up
    def getScore(self, team1, team2, gameSelect = None):
        print(team1, team2)
        try:
            score1 = self.sc[self.sideArray.index(team2), self.topArray.index(team1)]
            score2 = self.sc[self.sideArray.index(team1), self.topArray.index(team2)]
            if (gameSelect == None):
                print(team1, score1)
                print(team2, score2)
            else:
                print(team1, score1[gameSelect])
                print(team2, score2[gameSelect])
        except:
            print('Invalid input of teams')
    
    def getGameList(self):
        return self.gameList
    
    #constructs a matrix of the avg score in a matchup
    def buildAvgMatrix(self): 
        for col in range(len(self.sc[:,0])):   #depth
            for row in range(len(self.sc[0, :])):  #width
                tempScore = self.sc[row, col]
                avgScore = 0.0
                count = 0.0
                for j in tempScore:
                    if (j != -1):
                        avgScore += j
                        count += 1
                    else:
                        break
                try:
                    avgScore = avgScore / count
                except:
                    avgScore = -1
                self.am[row, col] = avgScore
    
    #get the value of the avg score for a match up
    def getAvgScore(self, team1, team2):
        try:
            score1 = self.am[self.sideArray.index(team2), self.topArray.index(team1)]
            score2 = self.am[self.sideArray.index(team1), self.topArray.index(team2)]
            print(team1, score1)
            print(team2, score2)        
        except:
            print('Invalid input of teams')
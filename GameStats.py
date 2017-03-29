class GameStats:

    def __init__(self):
        #parse the text file
        self.statsFile = open("baseball2016.txt", "r")
        self.topArray = []
        self.sideArray = []  
        self.sc = np.zeros((30,30,30), np.int32) 
        self.sc[:,:,:] = -1  
        self.am = np.zeros((30,30), np.float32)

        for line in self.statsFile:
            homeTeam = ""
            awayTeam = ""
            homeScore = 0
            awayScore = 0
            i=0
            token = line.split(',')  #tokenize the string
            '''
            away team name @ i =3
            home team name @ i = 6
            away score @ i = 9
            home score @ i = 10
            '''
            for i in xrange(token):
                if(i in tokenIndex):
                    list.append(removeQuotes(token[i])
            
            for str in token:
                if ((i == 3) or (i == 6)):   #find the word i want
                    noQuotes = str.split('"')
                    if (i == 3): awayTeam = noQuotes[1]
                    if (i == 6): homeTeam = noQuotes[1]
                if (i == 9): 
                    awayScore = str
                    print(awayTeam + ": " + awayScore + " (away)")
                if (i == 10): 
                    homeScore = str
                    print(homeTeam + ": " + homeScore + " (home) ")
                    print('-------')
                i += 1
            self.addScore(homeTeam, awayTeam, homeScore, awayScore)  
        self.buildAvgMatrix()
        self.statsFile.close()
        
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
    
    #constructs a matrix of the avg score in a matchup
    def buildAvgMatrix(self): 
        for col in range(len(self.sc[:,0])):   #depth
            for row in range(len(self.sc[0, :])):  #width
                tempScore = self.sc[row, col]
                avgScore = 0.0
                count = 0.0
                for j in tempScore:
                    print(tempScore)
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
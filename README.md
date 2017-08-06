# Machine-Learning-Baseball

## Baseball
The movie Money Ball, which is based on a true story, shows in game baseball statistics can be collected and analyzed in such a way that provides accurate answers to specific questions. This relies on the fact that, over the course of a season, teams experience patterns and react to factors in a repetitive manner, this ultimately affects their in-game performances. Essentially, the MLB is one large complexity system with feedback, stocks, and other system qualities as a result it can theoretically be understood.

## Hypothesis
We theorized that there is indeed a relationship between the statistics to a game and its outcome. As a result, the group focused on implementing a model that predicted the score of a particular game using the statistics of that game.

## Model Overview
Both the teams in a game are given their individual ID values and are made into vectors. Relevant data like the home and away team, home runs, RBI’s, and walk’s are all taken into account and passed through layers. There’s no need to reinvent the wheel here, there's a multitude of libraries that enable a coder to implement machine learning theories efficiently. In this case we will be using a library called TFlearn, documentation available from http://tflearn.org. The program will output the home and away teams as well as their respective score predictions.
 
 ## Implementation
 As mentioned earlier, the model was built using TFLearn, which is a API to Tensorflow. The model’s input data is the 2015/2016 baseball season statistics, score, and matchups. The model learns what statistics are useful for deciding a score, it also recognizes the different team by feeding the teams ID into a separate layer first. To train the model we used back propagation with gradient descent, this was handled by TFLearn during the training process. An in depth description of the model used is given in the notebook that is proved with the report. We chose to train the model on the 2015 season, using that data to learn what statistics are import in a game, that trained model could then make a predictions. We applied the model to the 2016 season, for each game we gave the model the statistics, scores and teams in that game to base a prediction from, even though the statistic are not determined until after a game. We originally tried using input as the team's average statistics for all their previous games, however these predictions were no better than coin flip.
 
## Results
In the end the model predicted games quite well. Scores were within 1 or 2 points off the actual values for the score and have about a 90% prediction rate of who would win games. The high accuracy of the model helps prove the hypothesis that baseball game statistics are highly correlated to the final score of the game. Such that the amount of home runs a team achieves in a game, has an direct effect of high there score is. Also when team achieves more hits than their opponent, they have a higher probability of scoring more runs than the other team. For defence, if a team completes a substantial amount of double plays in a game, then it demonstrates that there defense is effective, and that the other team will have a harder time scoring runs. The neural net was able to detect these subtle relations, to make effective predictions on who wins the game, and what the score is.


Resources
*********
baseball data source
http://www.retrosheet.org/gamelogs/index.html

Tensflor Library
https://www.tensorflow.org

TFlearn
http://tflearn.org

# nba_player_shooting_comparison

## This project is developed to collect data from [NBA database](stats.nba.com) and compare shooting performance of multiple NBA players. It classifies the shots into: 1. 3-point shots beyond the arc
2. 3-point corner shots 
3. 2-points shots in the paint
4. 2-points shots outside the paint
and plots the shot charts on an NBA court colored by the respected official team colors. 


![Sample](Curry_v_Harden.png?raw=true)


**Available Files:**
1. nba_player_shooting_comparison.ipynb: 
  -The notebook is segregated into 3 chapters:
    1. import modules and libraries and set parameters
    2. define functions to draw a 2D NBA courts
    3. find player ID and team ID of the players requested by the user
    4. get shot chart details of the basketball players (all shot attempts during regular season)
    5. compare the 3 point shots beyond the arc
    6. compare the corner 3 point shots
    7. compare the 2 point shots inside the paint
    8. compare the 2 point shos outside the paint 
      
  
8. environment.yml and requirements.txt:
  -The environment files necessary to recreate the python environment (python 3.6)
    
**DISCLAIMER**
1. The shots are limited to those attempted in the half court
    

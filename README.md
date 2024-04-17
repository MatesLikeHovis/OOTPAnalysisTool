# OOTPAnalysisTool
A companion app to bring even more fun to the **OOTP Baseball 25 Perfect Team** experience by helping to weight and rate players for tournaments, to build teams more quickly, and to have fun playing with projected stats, ratings, and more baseball.

## Virus Detection!
This project is packaged using PyInstaller, which is a fantastic library for building .exe files that are usable by people who don't have Python installed.  Unfortunately - it means that, according to VirusTotal, it will result in it being flagged as malicious software by 10 Antivirus vendors.  I'm not sure why that is - probably homebrewed malware written in Python is being packaged by PyInstaller, so anything packaged that way is being flagged.  If it comes up as flagged - I'm sorry that it happened to you.  The source code is all on the website, so you're free to download the scripts needed (main.py, batter.py, classes.py, main.py, pitcher.py and teambuilder.py, as well as the \Data folder with its subfolders) and run it using Python directly or in your preferred IDE, of course.

### Quick Disclaimer
First and foremost, this is (hopefully clearly) not a replacement for OOTP 25, nor for OOTP 25 Go, nor for any other OOTP products.  It's just a tool that I wanted because I thought it would help me have more fun with the game, and I was right!  If you have fun with it, I'm delighted, and if not - I'm sorry that it isn't for you!  Anyway - enjoy the game...   

## Basic Usage
The anticipated use of this app is to help build teams for tournaments and gameplay in OOTP Baseball 25's Perfect Team game mode.  Tournaments restrict the 'Card Value' ratings of players to specific amounts, and within those card value ratings, there are large gaps in the actual quality of players.  It can be hard to predict which ratings are more important than others: would pitchers with very low control ratings, but high stuff ratings (i.e., lots of walks but lots of strikeouts) perform better or worse than pitchers with ratings which are generally in the middle?  This app doesn't claim to answer that question, but is intended to provide a tool to explore what we would expect to happen, by using data derived from real-world experience and how it aligns with in-game ratings, so that managers can engage with the game in, hopefully, new and fun ways.
The basic methodology used in this app were to derive 'linear regression' models for each rating and their real-world equivalents.  The BABIP rating in the game correlates to real-world BABIP statistics, the Stuff rating for pitchers correlates to real-world Strikeout percentage statistics for pitchers, and so on, and these models provide a sort of 'compression' of the spread of how those ratings and statistics align, so that while the models will almost always be 'incorrect' in what happens in the game for any number of reasons, they do give a starting point to compare statistics.  If we would expect a player with a certain 'Eye' rating to have a certain number of average walks, and to have a certain number of strikeouts based on the 'Avoids K's' rating, then we can start to give very rough estimates for statistics like batting average, on-base percentage and slugging percentage that are impossible to do from ratings alone.

So, the basic questions which this app attempts to help with are "If my player would strike out a lot, but get a lot of walks and a lot of homeruns, is that better than another player who gets a good amount of hits and extra-base hits but never walks?" and questions like that.  There is no definitive answer.  The ratings don't answer the question directly.  This app also does not really answer the question - but it provides an incorrect answer that could be a starting point for thinking about ratings and statistics in-game.  If I'm comparing two catchers, and the rough estimates guessed at by this app would predict that one has a higher OPS than the other, it at least gives me something to work from.  For me, it helps me have more fun, because baseball is often about predictions of what should happen, and the crazy things that happen when those predictions are wrong.
The caveat then is, simply (and with apologies): 'If you like the statistical metrics, have fun!  If not - don't use them!'

With that said, the basic idea of the app is not centered on the metrics, but on self-weighting of factors.  I am probably not the only OOTP manager who doesn't give anywhere near as much emphasis to defensive skills in Right Field than I do in Center Field, or Shortstop.  I wanted a tool that would help me to quickly find players that had the skills I'm looking for.  If I want a great defensive Shortstop, and only care 70% as much that they have good offensive production, then I want to be able to rate all of my shortstops, quickly, and to give them a value that is my own value for what they bring.  Especially if they go against the card values on the card - in which case you also have the bonus that they outperform their card type!
Each tool within this app then gives you a weighting system to quickly rate players, either at one position, or to quickly build a team with set parameters.  Presets can be saved as .json files to reload favorite 'card shapes,' as well as team settings in the Teambuilder section to do quick searches for your favorite kinds of players.

## App Structure
There are essentially four main sections within the app:
* The Loading (File Management) screen.  Here you will see the status of the .csv files and lists generated within the app.
* The Batter Analysis screen.  This tool is for comparing individual batters at one position.
* The Pitcher Analysis screen.  This tool is for comparing individual pitchers.
* The Teambuilder screen.  This tool is for setting up weighting systems for every position on a team, to get a brief list with 5 options at each position for quick team selection.

## The Loading Screen
When the app begins, you will see a welcome message, a very brief description, and a few indicators of the status of files needed for successful operation.  These indicators at the bottom of the window give the following information:
* **CSV Status**: A .csv file of the players in the OOTP database is needed for operation.  This needs to be the .csv file generated on the market screen, which contains all of the players in the game, both batters and pitchers, and contains all of the ratings, including batting, pitching and defensive data for every player, regardless of position.  All of this information is needed to correctly operate the app, so it's status is very important.  The app will attempt to load the default filename downloaded from OOTP ingame, although it expects to find that file within the _'Data/CSV Files'_ folder where the main app is located.  If it fails to find this file on startup, click the **'Locate CSV File'** option under the *'File'* menu, which will allow you to select the .csv file.  If you have correctly located the file, it will turn from red to green with an appropriate message.  At time of writing, the latest .csv file is being packaged in the .zip file containing the app architecture.
* **Custom CSV Status**: If you wish to filter the results to only include players which you have cards for, it must be loaded as well as the main .csv file.  The 'custom' csv file would be downloaded from within the game under **'Collection - Manage Cards'** under the **'Report'** button.  This will generate a .csv file with the players which are currently being inspected onscreen, so to use the app to filter ALL of your players, remove all filters from the view you are using within **'Collection - Manage Cards'** before clicking to download the report.  The app should work without the custom csv file, but note that trying to filter by **'my players'** __without__ the csv file may have unexpected results.  The app will automatically attempt to find a report in the *'Data/CSV Files'* folder.  If you need to manually point to your custom csv file, select **'Locate Team-only Custom CSV File'** from the *'File'* menu.
* **List Status**: The app generates usable lists derived from the csv file.  If there is an error in generating these files, you may see an error message, or you may simply see a red version of this indicator.  Otherwise, the indicator should show a green 'O.K.!' sign.  If you want to attempt to manually build lists because the data in the csv file may have changed, or you may have pointed the app to a different file in between list generation attempts, simply click the **'Create Player Lists'** option under the *'File'* menu.
* **Analyze** Menu: In the window menu, under *'Analyze'*, the three screen options are available.  To move from one tool to another, you may select one of the other tools from this menu at any time.

## The Batter Analysis Tool
The batter analysis tool is a system for weighing the relative value of players at a particular position.  The window is divided into three main sections:
* A series of *Weight* bars, representing the scores of each batter (BABIP, Avoid K's, etc.), with activation filters
* Tools to filter by *Card Value* at the bottom of the screen, with presets for major card value types (Iron, Bronze, Silver).
* Other helpful buttons, like *preset* management, standard or platoon searching, and the main search button.

Let's have a look at what happens within the tool:

* Each of the weights represents the value that you give to that attribute.  There are two types of attributes, the **subattributes** like Power, Avoid K's or BABIP, and the **main attributes** like Offense, Defense and Running.  Each subattribute slider sets the relative value of that subattribute within the main attribute, and then the main attribute slider lets you set the relative value compared to the other two.  You may activate or deactivate various weights depending on your needs, so that if you are not concerned with a particular value, it will not be used.  Remember that removing subattributes will not reduce the overall value of the main attribute it corresponds to, so adjusting BABIP will not change the weight Offense has compared to Defense.  It is recommended that you set your subattribute values and activation switches, then adjust the main attributes to get your desired player.

* The Card Value presets at the bottom of the screen, and the minimum and maximum slider directly above the presets, help you to select the card value you are looking for, especially useful for particular tournaments.  The filter is always *inclusive* of the minimum and maximum values, so if you only want Iron players, the slider should be (and will be if you click the Iron preset button) set to a minimum of 40.0, and a maximum of 59.9, as 60.0 values would result in the lowest value of Bronze players.  There is a selector switch to indicate if this card value filter should be active, or if all players should be shown.

* The position selector at the very bottom of the window is used to select the position you are searching for.  If you are unconcerned with defensive values, you should probably set this value to **DH**, which will always return a defensive value of 0.  The position search is *'main position agnostic'*, meaning that it is not concerned with the listed main position of any players, but only with their defensive values at that position.  If you are looking for Left Fielders, you may be interested to see how Aaron Judge would compare with other natural Left Fielders, and this tool does not discriminate against players' defensive values at other positions.  Also - pitchers and two-way players will be presented if they have defensive values at that position, or all players will be shown if **DH** is selected.

* On the right side of the window are some useful tools.  First are the **Import Weights JSON** and **Export Weights JSON** buttons.  These export or import 'preset' values that you may want to go back to, if you have card shapes of power or contact hitters, or with relative levels of defensive emphasis.  These save and load as *json* files, which are light-weight text files representing the data shown on the app.  Be sure to load only JSON files associated with batters.  The export and import buttons will default to the folder *'Data\Presets\Batters'* to help prevent any errors.

* Below the JSON preset buttons are buttons for **Standard (No Platoon)** and **Splits (vR/vL) Active**.  If Standard is selected, then the results will be based on the players' general scores for each offensive attribute.  If Splits is selected, then two windows will be generated, one with scores generated based on the players' scores versus Right-Handed pitching, and one for versus left.  This can be useful for determining a good platooning team at positions where you do not have a dominant player that should play against both left and right-handed pitching, or if you are looking for substitute players that will do well against specialist relievers.

*The **Only My Cards** button should be checked if you want to include only those cards which you own, taken from the custom csv file uploaded.  It wouldn't be recommended to check this if you have not loaded a custom csv file.

* Finally, the pink **Generate List** button at the bottom will - create the list of players!  More on that below.

## The Pitcher Analysis Tool
The pitcher analysis tool is, like the batter tool, a system for weighing the relative value of pitchers.  The window is similar to the Batter Analysis Tool in its construction, with the same slider sets, JSON export and import buttons, and a generate list button.  It does have the following unique characteristics:

* Within pitcher ratings, rather than using subattributes, as there is only one true attribute broken down into subattributes **(Movement)**, all of the attributes are treated equally.  
* Rather than field positions, the pitcher 'position' dropdown menu includes options for **SP**, **RP** and **CL** for single pitcher type searches.  It also includes **RP/CL** to search just relievers, and **SP/RP/CL** to search all pitchers.
* There are no platoon or split buttons, and all searches use the data against all batters without versus left or right consideration.

## The Team Builder Tool
The team builder tool is very similar to the batter tool, with the same slider sets and weighing methods, but there are a few unique considerations:

* At the bottom of the screen is a set of 'radio' buttons to select each of the positions on a team, from *'C'* to *'DH'*.
* The sliders on the screen show the weights for **ONLY** the position selected.  If you have the *'C'* button selected, you will be adjusting the weights for the catcher position.
* If you select another position button, the weight sliders will move to show the current status of **THAT** position.
* The **Export Weights JSON** and **Import Weights JSON** buttons will load or save data from or to **THAT** position's sliders only.
* To save the overall team set of weights, use the **Export Team Weights JSON** button below the **Export Weights JSON** button, and to load the overall team set of weights, use the similarly titled **Import** button.

## The Batter / TeamBuilder Results Windows
After clicking the **Generate List** button, one or two lists will be generated using your request details.  Contained will be familiar information, like the name of the player, but it is useful to know what the app means by each column.  First, we should look at what is calculated in the engine whenever a list is generated:

* An estimated BABIP percentage, calculated from *BABIP* Scores
* An estimated percentage per plate appearance of a Strikeout, calculated from *Avoid K* Scores
* An estimated percentage per plate appearance of a Walk, calculated from *Eye* Scores
* An estimated percentage per plate appearance of a Home Run, calculated from *Power* Scores
* An estimated percentage per ball in play of any Extra-base hit, calculated from *Gap Power* Scores
* After estimating those percentages, the number of hits, at-bats per plate appearance, balls-in-play per plate appearance, and similar internal statistics are generated.

  Once these statistics are generated internally, the table is created:

* **Name**: The name of the player given on the card.
* **ID**: The unique card ID number for the card.
* **Year**: The year of the card.  For *Live* players, this is 2024.
* **OVR**: The 'overall' value of the card based on *YOUR* weights.  This represents the results of the weights you provided in the Analysis Tool applied to each player.
* **VAL**: The 'card' value on the front of the card.  This should already be familiar to you!  This value determines the type of card (i.e., Iron, Bronze, etc.) but may not be directly applicable to player performance.
* **OFF**: The 'offense' aggregate value.  This is calculated by taking all of your offensive sub-attribute weights and calculating a new overall offensive value based on those weights.  Represents overall offensive value based on your criteria.
* **DEF**: The 'defense' value.  This is calculated by looking only at the 'Defense at **' value for that player at only that position.
* **RUN**: The 'running' aggregate value.  This is calculated by taking the three running sub-attribute weights and calculating a new overall running value based on those weights.  Represents overall base-running and stealing value based on your criteria.
* **AVG**: The first **projected** value, representing the player's batting average, calculated from estimated number of hits divided by estimated at-bats.
* **OBP**: Represents the player's On-base percentage, calculated from estimated hits and walks divided by estimated plate appearances.
* **SLG**: Represents the player's Slugging percentage.  The number of total bases expected is calculated by multiplying the hits on balls-in-play by the percentage chance for extra base hits per hit on a ball-in-play, multiplying this by an arbitrary 2.4 TB per non-Home Run extra base hit (The ratio of doubles to triples is hard to predict based on scores, so a fixed value was given) with singles and 4 total bases per home run added.
* **OPS**: Represents the player's OBP + SLG.  Calculated by adding these two scores.
* **HR**: Represents the number of home runs that the player would be estimated to hit over 600 Plate Appearances.

  You may sort by any column by clicking on the *Header* of the column.  Click again to swap the order to sort.

### Important
Bear in mind that these statistics are generated by linear regression of the relationship between real-world statistics and scores.  Scores are likely based on multi-year statistics.  Linear regression creates a **flattened** line of results, which removes the natural variation from a number of factors.  You **WILL NOT** actually see these results in game.  The statistics are provided as a kind of laboratory score of what would happen in a theoretical world where players are playing against a 'league average' of pitchers, without considering lineup placement, management, or variations in opposing pitching.  All of these will make the actual statistics vary considerably.  Think of these statistics as a kind of score to help, for comparison and entertainment purposes only.

## The Pitcher Results Window
After clicking the **Generate List** button, a list will be generated using your request details.

Contained will be familiar information, like the name of the player, but it is useful to know what the app means by each column.  First, we should look at what is calculated in the engine whenever a list is generated:

* An estimated BABIP percentage, calculated from *pBABIP* Scores
* An estimated percentage per plate appearance of a Strikeout, calculated from *Stuff* Scores
* An estimated percentage per plate appearance of a Walk, calculated from *Control* Scores
* An estimated percentage per plate appearance of a Home Run, calculated from *HRA* Scores
* After estimating those percentages, the number of hits, at-bats per plate appearance, balls-in-play per plate appearance, and similar internal statistics are generated.

  Once these statistics are generated internally, the table is created:

* **Name**: The name of the player given on the card.
* **ID**: The unique card ID number for the card.
* **Year**: The year of the card.  For *Live* players, this is 2024.
* **OVR**: The 'overall' value of the card based on *YOUR* weights.  This represents the results of the weights you provided in the Analysis Tool applied to each player.
* **VAL**: The 'card' value on the front of the card.  This should already be familiar to you!  This value determines the type of card (i.e., Iron, Bronze, etc.) but may not be directly applicable to player performance.
* **STF**: The 'Stuff' value.  Comes directly from card data.
* **MVM**: The 'Movement' aggregate value.  This is calculated by weighing the two Movement values you set earlier.
* **CNT**: The 'Control' value.   
* **OTH**: The 'Other' aggregate value, calculated by weighing the attributes not directly related to pitching results (i.e., Stamina, Hold, Defense).
* **pAVG**: The first **projected** value, representing opposing batters' batting average, calculated from estimated number of hits divided by estimated at-bats.
* **pOBP**: Represents opposing batters' On-base percentage, calculated from estimated hits and walks divided by estimated plate appearances.
* **pSLG**: Represents opposing batters' Slugging percentage.  Calculated using 'league average' extra-base hits per plate appearance, as there is no equivalent to 'Gap Power' for pitchers.
* **pOPS**: Represents OBP + SLG of opposing batters.  Calculated by adding these two scores.
* **HR**: Represents the number of home runs that the pitcher would be estimated to allow over 600 Batters Faced.
* **BB**: Represents the number of walks that the pitcher would be estimated to allow over 600 Batters Faced.
* **SO**: Represents the number of strikeouts that the pitcher would be estimated to allow over 600 Batters Faced.

  You may sort by any column by clicking on the *Header* of the column.  Click again to swap the order to sort.

### Important
Bear in mind that these statistics are generated by linear regression of the relationship between real-world statistics and scores.  Scores are likely based on multi-year statistics.  Linear regression creates a **flattened** line of results, which removes the natural variation from a number of factors.  You **WILL NOT** actually see these results in game.  The statistics are provided as a kind of laboratory score of what would happen in a theoretical world where players are playing against a 'league average' of pitchers, without considering lineup placement, management, or variations in opposing pitching.  All of these will make the actual statistics vary considerably.  Think of these statistics as a kind of score to help, for comparison and entertainment purposes only.

## About the Data

### Edge Cases
There are lots, lots and lots of edge cases here.  Much of the middle ground of statistics align quite comfortably to the model, but at the extremes the numbers do go off the rails a bit, tending to reduce the absolute value of slopes as they approach minimum and maximum values, especially for Strikeout and Walk-related statistics.  Initially, Tensorflow Keras Sequential Neural Networks were used to fit expected results numbers to observed real-world data better, but the cost in size (1.2gb!) makes the difference in quality of results not worth the data hit.  It might be worth bearing in mind that very high or low numbers in data should be approached with caution: they may simply play as very high skills that would exceed real-world stats, or there may be internal mechanisms in the game that self-correct larger differences in value.  Without knowing the mechanics: take all statistics generated with several grains of salt, but be particularly generous with those grains when coming to edge case score values.

### Defensive Values
Why aren't there defensive statistics supplied?  Because the scatter-plot of defensive scores to defensive real-world stats don't correlate well.  In many cases, it's impossible to predict what data was used - for players who had previously played positions but did not during a particular year, where do the defensive ratings come from, and what statistics would apply?  It's impossible to answer those questions, or to try to find a statistical relationship to individual statistics like framing, arm, etc.  With that in mind, it felt best to keep Defense simple, and just use the score as it is.

### Pitching Statistics
Of all the statistics, pitching stats tended to 'flatten' the most, with the majority of the data fitting within a much smaller margin than the corresponding data for batters.  Presumably this makes sense: pitchers will see good and bad batters in a year, so we would expect less variation from the league average in most statistics.  This was especially the case in an attempt at a linear regression of ERA estimates based on hits, walks, strikeouts and home runs given up per 9 innings from non-OOTP historical data.  It seemed that it might be useful, and there was a clear correlation, especially between hits per 9 innings and ERA, but the actual data generated was too flattened, with the vast majority of data falling between 3 and 5 projected values.  While other ratings seem useful despite the flattening, clouding characteristics of analysis through linear regression, ERA's analysis as a linear regression of values already analyzed by linear regression seemed to be exponentially flattened, and thus much less useful, especially when it suggests such importance.  So - it was left out!  Thus - no ERA, or Wins for starting pitchers, or other stats that might be useful, but seemed too speculative to be useful.

## Acknowledgements
Thanks to the Baseball Reference website for the statistical data used.  Invaluable!
Thanks to SmashIcons on Freepik for the icon used in the app and windows opened.  It adds a nice little extra!
Thanks to all of the developers of the invaluable Python core, and to the invaluable libraries used, from MatLibPlot and TensorFlow to Numpy, Pandas, and TKinter and PyInstaller!

## Have Fun!
Feel free to send comments, requests, etc.  Most requests probably won't be explored - after all, this was a project built to help **MEEEE** above anything else, so if you're hoping for a way to categorize players by hairstyle or non-MLB league, I can't help you much.  If you want to improve the codebase, feel free to fork and send in your thoughts, but bear in mind that I'll probably be making a permanent repo of this version for job applications and the like, so don't be offended if pull requests are ignored.  Well - I'll probably say the same thing rather than ignore you, but don't be offended if those requests aren't approved.

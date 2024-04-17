# OOTPAnalysisTool
A companion app to bring even more fun to the **OOTP Baseball 25** experience by helping to weight and rate players for tournaments, to build teams more quickly, and to have fun playing with projected stats, ratings, and more baseball.

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


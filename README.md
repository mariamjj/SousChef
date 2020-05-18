# SousChef

<br>
<br>

> Mariam Javed <br> 

<a name="problem-statement"></a>
## Problem statement

We all live busy lives! From work to chores to other responsibilities, we all have a lot on our plate (no pun intended. For this reason, SousChef is here to make your life a little easier by recommending the **easiest** recipe for you given the ingredients you have on hand. 

This web app is for all of those that want to spice things up in the kitchen, discover some new flavours, chop their time in half, and bite right into recipes that are new and delicous!


## Objectives

Build a personalized recipe recommender by:

 - Collecting recipes (text data) by webscraping All Recipes and preforming topic modeling analysis for recipe-tagging (comparing LDA vs NMF) (ie. clustering them into different meal types: breakfast/lunch/dinner/appetizer/dessert)
 - Predicting the category of a dish's cuisine given a list of ingredients (Kaggle dataset) and building a classification model (Neural Network)
 - Predict the cuisine for a user's ingredients and recommend a recipe that will be the quickest to make!
 - Deploy as a web app using Flask

## Executive summary

The goal for SousChef is to recommend personalised **quick** recipes to the user based on the ingredients the user has on hand.

In order to do this, I webscrpaed 5000+ recipes and ingredient from [AllRecipes](https://www.allrecipes.com/) which formed the recipe database. These webscraped recipes did not have any meal types (ie. dinner/breakfast/desser) tags associated with them so I used topic modelling with NMF to classify the recipes as:

- maindish
- breakfast
- dessert      
- drinks 

Furthermore, I used the [What's Cooking](https://www.kaggle.com/c/whats-cooking) Kaggle dataset to train and test a Neural Network to predict the cuisine based on inputted ingredients. The model was evaluated by looking at the training and testing accuracy and loss scores. This model was then used to predict the cuisine types for our 5000+ recipe database, the following are the cuisines in our database:

- Greek
- Southern_us
- Filipino
- Indian
- Jamaican
- Spanish
- Italian
- Mexican
- Chinese
- British
- Thai
- Vietnamese
- Cajun_creole
- Brazilian
- French
- Japanese
- Irish
- Korean
- Moroccan
- Russian

Finally, based on the user inputted ingredients, SousChef predicts the best suited cuisine type and recommends the recipe that would require the shortest amount of time. SousChef outputs the name, cuisine type, meal type, ingredients and instructions for the recommended recipe.


## Project notebooks

We divided our coding efforts into five notebooks:

Part 1: Data Collection 

Part 2: Topic Modelling

Part 3: Predicting Cuisines

Part 4: End to End Pipeline - Recommendation


## Conclusion

- Neural Network was effective at predicting the cuisine accuracy at 88 percent and 80 percent for training and testing respectively.
- SousChef web App can be found here: **TBD**


## Recommendations for Future

- Web scrape the recipe links, and recipe ratings along with the recipe information so that SousChef's output can be the link to the recipe as opposed to outputting all of the ingredients/instructions. Furthermore, the recipe ratings could be used to develop a rating-based recommendation system.
- Develp a CNN model for image classification so that the user can input ingredients via manual input or uploading a picture.
- For ease of use, save all data as SQL databases.

## Attributions

- [Ryan Lee](https://github.com/rtlee9/recipe-scraper/tree/4f3d38c1b99acff43410f9d72118f4a4fc87eefa)
- [Jhonsen Djajamuliadi](https://github.com/jhonsen/Produce2Recipe)



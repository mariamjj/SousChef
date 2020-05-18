# imports
import numpy as np
import pandas as pd
from utils import *

from flask import Flask, request, render_template, jsonify

#initialize the flask app
app = Flask('sousChef')

@app.route('/')
# create the controller
def home():
    # return the view
    return render_template('form.html')
	
#route 3:
@app.route('/submit')
#create the controller
def submit():
	user_input = request.args

	user_ing = [ ]

	user_ing.append(user_input['ing_1'])
	user_ing.append(user_input['ing_2'])
	user_ing.append(user_input['ing_3'])

	#call the dataframe
	df = pd.read_csv('../datasets/final_dataset.csv')

	# Find recipes with intersections
	d3, d2, d1, d = intersect(df, user_ing)

	# Output recipes
	out3 =outputRecipes(d3)
	out2 =outputRecipes(d2)
	out1 =outputRecipes(d1)

	#features
	titles3_name1 = out3.title[0]
	titles3_name2 = out3.title[1]
	titles3_name3 = out3.title[2]

	titles2_name1 = out2.title[0]
	titles2_name2 = out2.title[1]
	titles2_name3 = out2.title[2]

	titles1_name1 = out1.title[0]
	titles1_name2 = out1.title[1]
	titles1_name3 = out1.title[2]

	name = out3.title[2]
	meal_type = out3.meal_type[2]
	cuisine = out3.cuisine[2]

	ingredients = out3.ingredients[2]
	instructions = out3.instructions[2]

	return render_template('result.html', titles3_name1=titles3_name1, 
		titles3_name2=titles3_name2, titles3_name3=titles3_name3, titles2_name1=titles2_name1, 
		titles2_name2=titles2_name2, titles2_name3=titles2_name3, titles1_name1=titles3_name1, 
		titles1_name2=titles3_name2, titles1_name3=titles3_name3, name=name,
		meal_type=meal_type, cuisine=cuisine, ingredients=ingredients, 
		instructions=instructions)

#run the app
if __name__ == '__main__':
	app.run(debug = True)
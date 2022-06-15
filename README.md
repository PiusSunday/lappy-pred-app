# Lappy-Pred-App

![](C:\Users\parad\Pictures\Camera Roll\lappy-pred-logo.png)

# Laptop Prices Predictor
<ul>
  <li>Designed a Flask API that predicts the price a laptop given the configurations. </li>
  <li>Sourced the laptops data from ouedkniss.com, facebook marketplace and instagram laptop stores. </li>
  <li>Developed Different LINEAR_MODELS, NEURAL_NETWORKS, DECISION_TREES, NEAREST_NEIGHBORS, and SUPPORT VECTOR MACHINES Regressors to get the best model.</li>
  <li>Deployed the Machine Learning model to Heroku Server using flask</li>
</ul>

# Links and Resources Used
<li>OuedKniss MarketPlace: <a href="https://www.ouedkniss.com/">https://ouedkniss.com/</a></li>
<li>Heroku: <a href="https://www.heroku.com/">https://www.www.heroku.com/</a>
<li>Model Deployment Video: <a href="https://youtu.be/ax3WyB-_LJY">https://youtu.be/ax3WyB-_LJY</a></li>
<li>Packages: pandas, numpy, sklearn, flask, pickle</li>

# Web Scraping

I sourced my laptop data from OuedKniss website which is a major marketplace for different laptops in the Algerian Market. This page contains the specifications of different laptops. I tried to extract the different features of the laptops such as:
<ul>
  <li>BRAND</li>
  <li>CPU (BRAND, CORE, GENERATION, FAMILY)</li>
  <li>RAM</li>
  <li>DDR TYPE</li>
  <li>GPU BRAND</li>
  <li>SCREEN SIZES</li>
  <li>PRICE</li>
  <li>etc...</li>
</ul>
After extracting the laptop data from different sources, My dataset now consists of the information more than 200 different laptops.<br>
Link to complete dataset will be seen in the files.

# Feature Engineering
From the data I sourced from the different sources, I made the following changes and created new variables:
RAM - Made columns for RAM SIZE in GB, the RAM(DDR) version <br>
PROCESSOR - Made columns for CPU BRAND, CPU CORE, CPU GENERATION and CPU FAMILY <br>
STORAGE - Made new columns for the DISK TYPE and the SSD and HDD SIZES <br>
DISPLAY - Made new columns for the SCREEN SIZE(in inches) and SCREEN RESOLUTION <br>
GRAPHICS CARD - Made new columns for the GPU BRAND and GPU TYPE <br>

# Data Preprocessing
Since we can only feed numerical data to our models, The few columns which are categorical (String Columns), they need to converted to numerical columns. <br> 
This I did using sklearn's OneHotEncoder library. <br>
These converted columns are: BRAND, CPU BRAND, CPU CORE, CPU FAMILY, DISK TYPE, GPU BRAND, GPU TYPE, SCREEN RESOLUTION, and STATE.

# Exploratory Data Analysis
A file would be included for the Exploratory Data Analysis done in Jupyter NoteBook.

# Model Building
Used scikit-learn library for the Machine Learning tasks. Applied OneHotEncoding and converted the categorical variables into numerical ones. Then I split the data into training and test sets with a train size of 80% and test size of 20%. <br>
I tried 5 different Regression Models ( LINEAR MODELS, NEURAL NETWORKS, DECISION TREES, NEAREST NEIGHBORS, and SUPPORT VECTOR MACHINES) and evaluated them using Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE) and Root Square Score(R²).

# Model Deployment
I deployed the model as a flask API in JSON format to Heroku which is a Platform As A Service(PAAS)

Heroku API: <a href="https://lappy-pred-app.herokuapp.com">https://lappy-pred-app.herokuapp.com/</a>
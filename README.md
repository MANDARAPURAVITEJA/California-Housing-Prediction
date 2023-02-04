# California Housing Prediction Model

## 🪄 About
This is an End-to-End Machine Learning project. The project aims at developing a Regression model for predicting Median house value for households within a block in California.

The project was created using Python Flask framework and integrated with Web API. The Project was implemented using complete logging and custom exception handling.

## 📈 DataSource

The data pertains to the houses found in a given California district and some summary stats about them. In this dataset we have 10 columns which reflect various attributes of the households. The target column is median_house_value which tells Median house value for households within a block in California. In this dataset, we have information on geo-graphic data, total number of housholds, rooms, bedrooms, population, housingage, medianincome etc..

The datasource for this project was taken from Kaggle dataset California housing price.

Dataset download link: https://github.com/ageron/handson-ml/tree/master/datasets/housing

## 💡 Complete Project Workflow

### 1. 🏡 Home Page

Home page of this project contains complete overview of the project information, contents of the projects with appropriate descriptions and buttons to navigate between the pages.

<a><img src='Readme images/Home.png' width="60%" height="50%"></a><br>

### 2. 🧮 Estimate Housing Price
In this Estimate Housing Price page, user can able to enter the data about Housing features and then by clicking on "Predict Median House value" button, model can able to predict Median house value for households within a block and output for the same will be displayed on the Web page..

<a><img src='Readme images/Estimatehouseprice.png' width="60%" height="50%"></a><br>

### 3. 🗂️ View Trained Model
In the View Trained Model page, we will have all previously trained model files. Once the model is trained, then the model will be pickled to "model.pkl" file and saved to a folder with current time stamp. So, out of all previously trained models, latest model will be used to "Estimate Housing Price". 

Directory tree: 

📁saved_models<br>
    &emsp;|__ {"latest trained model folder name"}<br>
            &emsp;&emsp;|__ "model.pkl"

<a><img src='Readme images/viewtrainedmodel.png' width="60%" height="50%"></a><br>


### 4. 📜 Experiment History
In the Experiment history page, we can find complete information about our Model Training History. It contains details like experiment_id, when model training started and ended, whether Model accepted or not, and all timestamps related to Model training.

<a><img src='Readme images/experimenthistory.png' width="60%" height="50%"></a><br>

### 5. 📂 View Artifacts
This is one of the most important part of the project, where complete workflow history of the project can be found here.

#### Directory tree: 
In the below directory tree, we can see the files that we are creating for each stage of the project from Data Ingestion phase to Model Evaluation phase.<br>
Note: Below directory tree was just a blue print of file types at all stages, but in real time scenario we will be having a seperate folder with timestamp for every time model training starts..

<a><img src='Readme images/artifact.png' width="40%" height="50%"></a><br>

### 6. 🗄️ Update Model Config
This is one of the interesting part of the project, where we can re-train our model using a custom Regressor algorithm with hyper-parameters. <br>
Ex: We can re-train our model using DecisionTreeRegressor with hyper-parameters {max_depth:5}
#### Procedure: 
So, user can copy the existing Model config JSON file and will edit the text with custom model with hyper-paremeters. Next, he can check the JSON format in Validate Model config JSON, and will paste the new JSON text in Update model config. By this, our project will be trained based on the updated model config file. So, we can use the updated model for Predicting Median Housing price.

<a><img src='Readme images/updatemodelconfig.png' width="60%" height="50%"></a><br>


### 7. 📝 View logs
In View logs section, we can find complete logs for the project. It will be helpful for the developer to debug the code easily and to fix the errors.

<a><img src='Readme images/logs.png' width="60%" height="50%"></a><br>


### 🛠️ Requirement packages
* numpy
* pandas
* matplotlib
* sklearn
* Flask
* gunicorn
* PyYAML
* evidently
* dill

### ⚙️ SetUp

#### Software Requirements
1. Github account
2. VS code
3. Git cli
4. Anaconda

Creating conda environment
```
conda create -p Proj1 python==3.7 -y
```
For activating environment
```
conda activate Proj1/
```
For installing packages in requirements.txt
```
pip install -r requirements.txt
```
To add files to git
```
git add .
```
> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```
To check all versions maintained by git.
```
git log
```
To create version/commit all the changes to git.
```
git commit -m "Message"
```

To send version/changes to github
```
git push origin main
```
To check remote url
```
git remote -v
```

To setup CI/CD pipeline in Heroku, we need 3 things
1. Heroku Email - raviteja.vvss99@gmail.com
2. Heroku API key - <key_name>
3. Heroku app-name - machine-learning-proj-ravi

Create a Docket file named like "Dockerfile" and specify the commands to execute.

Create a .dockerignore file and specify the files to ignore.

Build Docker Image
```
docker build -t <image_name>:<tag_name> .
```
> Note: Image name for docker must be lowercase

To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image_id>
```

To check running container in docker
```
docker ps
```
To stop docker container.
```
docker stop <container_id>
```
Install ipykernel
```
pip install ipykernel
```

## 🦾 Tools & Technogies Used

<a><img src='Readme images/tools.png' width="60%" height="50%"></a><br>

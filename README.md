# Machine Learning End to End Project

## Software Requirements
1. Github account
2. VS code
3. Heroku account
4. Git cli

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
To check all versions maintained by git
```
git log
```
To create version/commit all the changes to git
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
To stop docker container
```
docker stop <container_id>
```
To run the setup.py file
```
python setup.py python
```

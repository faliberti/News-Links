# News-Links

## Introduction

This app is used to generate random news articles from user generated information need inputs.
This app is intended for people that need a quick read while they're on the go, whether in line or on the porcelain throne.

### Setup

1. Clone or download this repository into a local directory 

2. Create a developer account for this following website and record the provided API key
  * https://newsapi.org/
    
3. Make a Heroku account at https://signup.heroku.com/login 

### Intructions

1. Create or activate enironment were you can manage packages from
   * If using Anaconda as your language version manager 
   ```
   conda create -n yourenvname python=3.7
   ```

2. Ensure that your python is working in version 3.7
   ```
   python --version
   ```
3. Install all required packages
   ```
   pip install requirements.txt
   ```

4. create a .env file in your root directory for your environment variables and model it as thus with your own API key:

 **News API Key**
 ```
 NEWS_API_KEY="Key"
```

 5. Save and commit all changes and test working functionality from command line
 ```
 pytest
 ```

### Deployment

#### Heroku Command Line

If you have not used Heroku before go to https://devcenter.heroku.com/articles/heroku-cli#download-and-install to install comand line functionality

You can test if it is working by issuing these commands from the command line
```
heroku login

heroku apps
```

#### App Server Creation

Create a remote Heroku server:
```
heroku create server-of-app
# Use your own unique name!
```

Go to the Heroku online dashboard and find the app's "heroku git url" and associate this with your git repository: 
```
git remote add heroku REMOTE_ADDRESS 
```
Ensure this step worked by issuing
```
git remote -v
```
#### Heroku Environment Configuration

1. Instead of using a ".env" file, we will directly configure the server's environment variables by clicking "Reveal Config Vars" from the "Settings" tab in your application's Heroku dashboard. 

The key is NEWS_API_KEY and the value is your personal key from the API website.

At this point, you should be able to verify the production environment has been configured with the proper environment variable values:

```
heroku config
```

#### Deploy

After this configuration process is complete, you are finally ready to "deploy" the application's source code to the Heroku server:
```
git push heroku main
```

Once you've deployed the source code to the Heroku server, login to the server to see the files there, and take an opportunity to test your ability to run the script that now lives on the server:
```
heroku run bash
# or alternatively, run it from your computer, in "detached" mode:
heroku run "python -m app.news_link"
```

### Continous Integration Testing
To enable continous integration to run on each updated commit you will need to navigate to https://travis-ci.com and go to the settings of your repository and configure each of these environment variables once more.

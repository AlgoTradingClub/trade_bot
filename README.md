# USU Algo Club: Trade Bot
Apes Together!

# Introduction
- To show that we can make money, and our simple strategies are rock solid!

# Technologies
- Python 3.8
- Click 7.1
- Requests 2.5.1
- Pandas 1.2.1
- polygon-api-client 0.1.9
- 

# Setup
Add only by Pull Request. This paragraph should explain what that means.

## To run this project:

### Install Python and virtualenv
- Install [Python](https://www.python.org/downloads/)
- When installing python, click `add to path` option on the installation prompt.
- Install virtualenv. These are separate coding enviornments that allow you to code with the same software dependancies and environment that I am coding in. On windows, open `CMD`; on linux or mac, open `terminal`.
```$ python -m pip install virtualenv```
- Go to the location in your computer where you want to run the python program.
- Run 
```$ python -m virtualenv trading-bot-venv```
- Enter the project folder which was just created.
`$ cd trading-bot-venv`
- Activate the virtual environment
`$ source Scripts/activate
- Whenever you see `(trading-bot-venv)` in parathesis after every command in terminal, you know you are in an activatd virtual environment. To leave a virtual environment, close the terminal or `$ deactivate`
- Now, whenever you work on the project, activate the virtual environment before coding and you'll be good to go.

### Get the source code
- Install [git](https://git-scm.com/)
- Clone this repo into the folder `trading-bot-venv`

`$ cd trading-bot-venv`

`$ git clone https://github.com/AlgoTradingClub/trade-bot.git `

- Add the required dependancies. These libraries will only exist in this folder. Hence the name, a virtual environment.
`$ python -m pip install -r trade-bot/requirements.txt`


### Sign up for an alpaca account 
- After creating an account and getting a set of public and private alpaca api keys, follow these steps
- Add your alpaca keys to the path variable for extra security
	- Windows:
		- Follow [these steps to install alpaca keys on the windows path](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/)
	- Linux:
		- Follow [these steps to install alpaca keys on Linux](https://phoenixnap.com/kb/linux-set-environment-variable)
	- OS:
		- Follow [these steps to install alpaca keys on Mac OS X](https://osxdaily.com/2015/07/28/set-enviornment-variables-mac-os-x/)

- When writing code, create a new branch:
`$ git checkout -b myNewFeature`
- After writing code, add and commit the code to git
`$ git add .`
`$ git commit -m "this is what i did"`
- Then push your code to github
`$ git push -u origin myNewFeature`
- this will create a pull request that we will look over and add comments to. Go to https://github.com/AlgoTradingClub/trade-bot to see the pull request and add any additional comments. When someone has reviewed your pull request, then we can add it to the main branch of code.


# Table of contents
1. cli.py: This is the start of the system that initializes the rest of the functionality of the project
2. helpers:
   	- Scaffolding Code. This is where we put 'dirty code', code that does not contain core business rules but that's nonetheless needed for the project.
	- It's important to have a separate for this kind of code because if you place it together with actual business logic code, it will be increasingly hard to understand the business logic because there's so much other stuff mixed in.
3. models:
   	- This is where the core of your business logic goes. Here you write classes, modules and components that make up the domain you are writing code for.
4. tests:
   	- Tests are documentation and Tests allow you to update and modify your project
5. utils
   	- Here is where you should put code that you need for your application, but that is general enough that it could be used somewhere else.
	- Using a separate folder for these helps you remember to write this code in a way that is totally decoupled from the rest of your application.
6. docs: 
	- Documentation, requirements, and todo lists.



# Features
wow so easy to trade!
- Moving average crossover
- pairs trading
- risky or non risky settings
- trading #tothemoon!

# Code Examples
here you go, so easy, so algo

# Project status 
## Still very much in progress
- [ ] create a test folder
- [ ] implement simple cli file
- [x] structure the folders in the 'best' way?  
- [ ] import code from intelligent systems for data gathering from polygon
- [ ] import code for finding pairs

# Sources
This app is inspired by Andy Brim. You're the real MVP. 

# Other information
IDK 	
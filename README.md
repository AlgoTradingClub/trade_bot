# USU Algo Club: Trade Bot
Apes Together!

# Introduction
- A trading bot system that is designed to back test algorithms, perform paper trading, and live trading through Alpaca trading
  
- To show that we can make money, and our simple strategies are rock solid! 
  Combines the four parts necessary for a trade bot:
  1) An algorithm
	2) A source of market data
	3) An order reconciler that removes bad attempted orders and stops extra fines/ taxes from occuring
	4) Easy Access such that crontab or another automatic scheduler program can run this daily.

# Technologies
- Python >= 3.8
- polygon-api-client==0.1.9
- requests==2.25.1
- pandas==1.2.1
- numpy==1.20.1
- click==7.1.2
- pytest==6.2.2
- alpaca-trade-api==1.0.1
- pycoingecko==1.4.0


# Setup
Add only by Pull Request. This paragraph should explain what that means.

## To run this project:

### Install Python and virtualenv
- Install [Python](https://www.python.org/downloads/)
- When installing python, click `add to path` option on the installation prompt.
- Install virtualenv. These are separate coding environments that allow you to code with the same software dependencies and environment that I am coding in. On Windows, open `CMD`; on linux or mac, open `terminal`.
```$ python -m pip install virtualenv```
- Go to the location in your computer where you want to run the python program.
- Run `$ python -m virtualenv trading-bot-venv`
- Enter the project folder which was just created.
`$ cd trading-bot-venv`
- Activate the virtual environment
`$ source Scripts/activate`
  (This is for linux or IOS. When setting up a virtualenv, make sure to do this in a linux or Mac environment. 
  If you are using Windows, please download git and use the git bash that comes with this. https://appuals.com/what-is-git-bash/)
- Whenever you see `(trading-bot-venv)` in parentheses after every command in terminal, you know you are in an activated virtual environment. To leave a virtual environment, close the terminal or `$ deactivate`
- Now, whenever you work on the project, activate the virtual environment before coding, and you'll be good to go.
- If you want to use PyCharm or another IDE, simply open the folder `trading-bot-venv` in the IDE, and it should recognize that you are using a virtual environment.

### Get the source code
- Install [git](https://git-scm.com/)
- Clone this repo into the folder `trading-bot-venv`

`$ git clone https://github.com/AlgoTradingClub/trade-bot.git `

- Add the required dependencies. These libraries will only exist in this folder. Hence, the name, a virtual environment.
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

## Code Contribution Standards
- When writing code, create a new branch:
`$ git checkout -b myNewFeature`
- After writing code, add and commit the code to git
`$ git add .`
`$ git commit -m "this is what i did"`
- Then push your code to github
`$ git push -u origin myNewFeature`
- This will create a pull request that we will look over and add comments to. Go to https://github.com/AlgoTradingClub/trade-bot to see the pull request and add any additional comments. When someone has reviewed your pull request, then we can add it to the main branch of code.


# Table of contents
1. cli.py: This is the start of the system that initializes the rest of the functionality of the project
   - To run all tests: `python cli.py test`
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
wow, so easy to trade!
- Moving average crossover
- pairs trading
- risky or non risky settings
- trading #tothemoon!

# Code Examples
here you go, so easy, so algo

# Project status 
## Still, very much in progress
- [x] create a test folder
- [x] implement simple cli file
- [ ] make a better cli (colors and icons?)
- [x] structure the folders in the 'best' way?  
- [x] import code from intelligent systems for data gathering from polygon
- [ ] import code for finding pairs
- [ ] write engine to run algorithms
- [x] get the MAC algo to paper trade

# Sources
This app is inspired by Andy Brim. You're the real MVP. 

# Other information
IDK 	
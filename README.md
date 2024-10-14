# TheMoeWay Event Bot

📢 **New contributors [welcome](contribute.md)!**

## What is the Event Bot?
The Event bot automatically creates a role for a newly made event, allowing users to ping the people interested in that event, for discussion or when the event starts.

Powerful features that it provides:
- 📌 Ping the users interested in your event to discuss it or to make them aware it starts.
- ⚙️ Automatically creates the event role when an event is created and deletes the role when the event ends.

## Installation

Before you can install and run the bot, make sure you have the following:
1. Python 3.9.0
   You can download Python from [here](https://www.python.org/downloads/release/python-390/).
2. Discord Developer Account
   You need a Discord account and a registered bot in the Discord Developer Portal.
3. Git (to clone this  repository)
   Download Git from [here](https://git-scm.com/).
4. A text editor
   You can use any text editor (e.g., VC code, Sublime Text, Atom).

## Steps to Install
### 1. Clone the Repository
First, clone the bot repository to your local machine.
```
git clone https://github.com/themoeway/eventbot.git
cd eventbot
```
### 2. Create a Virtual Environment (Optional but Recommended)
It is recommended to create a virtual environment to manage dependencies cleanly.
```
python -m venv venv
source venv/bin/activate   # For Linux/MacOS
# or
venv\Scripts\activate      # For Windows
```
### 3. Install Dependencies
Use pip to install the required dependencies specified in the requirements.txt file.
```
pip install -r requirements.txt
```
### 4. Create a Discord Bot Application
  1. Go to the Discord Developer Portal and log in.
  2. Click New Application and give it a name.
  3. In the Bot section, create a new bot and copy its Token.
  4. Tick `Presence Intent`, `Server Members Intent` and `Message Content Intent`.
  5. Under OAuth2 > URL Generator, enable `bot` and `applications.commands` scopes. Assign administrator permissions and copy the link and add the bot to your server.
  6. Paste the token at the bottom of the `launch_bot.py` file.
### 6. Run the Bot
To start the bot, run the following command:
```
python launch_bot.py
```
### 7. Change the Constant Values.
Change the `guild_id` to your discord server in modals/constants.py.

## Contributing

🚀 **Dip your toes into contributing by looking at issues with the label [good first issue](https://github.com/themoeway/eventbot/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).**

Since this is a distributed effort, we **highly welcome new contributors**! Feel free to browse the [issue tracker](https://github.com/themoeway/eventbot/issues), and read our [contributing guidelines](contribute.md).

If you're looking to code, please let us know what you plan on working on before submitting a Pull Request. This gives the core maintainers an opportunity to provide feedback early on before you dive too deep. You can do this by opening a Github Issue with the proposal.

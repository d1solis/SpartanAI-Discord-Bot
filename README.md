# SpartanAI Discord Bot

## Overview
**SpartanAI** is a custom-built Discord bot for the *Spartan Army* — a Halo-inspired Twitch community hosted by **[Real Life Spartan (RLS)](https://reallifespartan.com/)**. SpartanAI helps with moderation, engagement, and hype — making your server feel like a real battlefield. 🔥

## 💡 Features
- **Custom Commands:** Includes both slash and prefix commands like `/ping`, `/help`, `/hype`, `/8ball`, and more.
- **Auto Greetings:** Sends welcome DMs and farewell messages to keep your server warm and active.
- **Message Filtering:** Automatically deletes NSFW, political, and religious content to enforce server rules.
- **Role Assignment:** Grants or removes the “Ghosts of Reach” role using `/assign` and `/remove`.
- **Secret Command Access:** Allows exclusive commands only for users with a specific role.
- **Direct Messaging:** Sends custom DMs to users via the `/dm` command.
- **Community Polls:** Creates quick polls with thumbs-up/thumbs-down reactions using `/poll`.
- **Motivational Commands:** Encourages hype and Halo-inspired energy with `/believe`, `/spartan`, and more.
- **Activity Logging:** Tracks bot activity and errors with a `discord.log` file.

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/SpartanAI.git
cd SpartanAI
```

### 2. Set up `.env`

Create a `.env` file in the root directory and add your Discord bot token:

```env
DISCORD_TOKEN=your-discord-bot-token
```

> ⚠️ **Never commit your real `.env` file. Always add it to `.gitignore` or keep it safely written down elsewhere.**

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the bot

```bash
python main.py
```

## 📁 Project Structure

```
SpartanAI/
├── main.py              # Main bot code
├── .env                 # Secret token file (ignored)
├── .gitignore           # Ignore .env, logs, etc. (optional)
├── discord.log          # Logs for monitoring
├── requirements.txt     # Python dependencies
├── README.md            # You're here!
└── screenshots/         # Folder for project images
```

## 🚀 Deployment with Discloud

You can deploy SpartanAI on [Discloud](https://docs.discloud.com/en/suport/host/bots/via-vscode) using this config for VSCode Extension:

```
ID=
TYPE=python
MAIN=main.py
NAME=SpartanAI
AVATAR=
RAM=100
AUTORESTART=true
VERSION=latest
```

## 📚 Dependencies

Add these to your `requirements.txt`:

```
discord.py
python-dotenv
```

## 🙌 Credits

- Developed by [Dalila Solis](https://github.com/d1solis)
- Built for the Spartan Army and Real Life Spartan (RLS)
- Powered by the amazing `discord.py` library

## 📜 License

This project is licensed under the MIT License.

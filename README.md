# Finite Clock
Created By:
[Dakota J Payne](https://github.com/DakotaJPayne)
&
[Abdul Aziz Oshinberu](https://github.com/Abdul-aziz9)

>"To measure your days is to own them. The truth is only painful until it becomes your strategy."

The Finite Clock is a life expectancy countdown engine. By synthesizing biological data (birth date, gender) with actuarial government statistics, it provides a high-fidelity visualization of the time remaining in a human life.

Currently in Version 1 (Python POC), this tool renders a terminal-based interface featuring a status image and a precise countdown of years, days, hours, and minutes.

# Purpose

For the user to objectively face the finality of existence and cherish every remaining second; the user is prompted to move with discipline and integrity.

V1 (Current): Terminal-based Python proof-of-concept.

V2 (Upcoming): Highly reliable Rust implementation.

Deployment: Optimized for the TRMNL e-ink dashboard.

# Prerequisites

Python 3.10 or higher

A terminal environment (Linux/macOS preferred; Windows compatible)

# Installation & Setup

To run the Finite Clock on your local machine, follow these steps to ensure a clean, isolated environment.

1. Clone the Repository

```
git clone "https://github.com/DakotaJPayne/finite-clock.git"
cd finite-clock/python
```

2. Initialize the Environment

We use a Virtual Environment (venv) to prevent library conflicts.

```
# Create the environment
python3 -m venv venv
```

```
# Activate the environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
```

3. Install Dependencies

`pip install -r requirements.txt`


# One-Command Execution (Alias)

To run the Finite Clock instantly from anywhere in your terminal without manual activation, you can create an alias.

## For Linux/macOS (zsh or bash)

Open your config file: `nano ~/.zshrc` (or `~/.bashrc`)

Add this line at the bottom (replace /path/to/ with your actual folder path):

`alias finite='cd /path/to/finite-clock/python && source venv/bin/activate && python3 main.py'`


Save and restart your terminal. Now, simply typing finite will launch the clock.

## For Windows (PowerShell)

Open your profile: notepad $PROFILE

Add this function:

`function finite { cd "C:\path\to\finite-clock\python"; .\venv\Scripts\activate; python main.py }`


# Usage

If not using an alias, launch the clock manually from the python directory:

`python3 main.py`


Upon launch, the program will prompt you for your birth details and gender to calculate your specific actuarial path.

# Roadmap

- [x] Python Terminal Prototype (v1)

- [ ] Requirements.txt optimization

- [ ] Conversion to Rust for server-side stability (v2)

- [ ] TRMNL Dashboard Integration API

- [ ] Web-based configuration portal

# License

MIT

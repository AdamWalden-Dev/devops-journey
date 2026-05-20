# System Report 
reads system information and logs it 

## Requirements
- Python3
- Bash

## Setup
clone repository:
```bash
git clone https://github.com/AdamWalden-Dev/devops-journey
```
create your virtual enviroment:
```bash
python3 -m venv venv
source venv/bin/activate
```
pip install Psutil
```bash
pip3 install -r requirements.txt
```

## How to Run
run run_report.sh in bash
```bash
./run_report.sh
```

## What it Does
- gathers system information
- logs them

## Security
logs hidden with .gitignore to exclude generated output from version control
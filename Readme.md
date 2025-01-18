# Selenium Automation Contract Creation

This project automates the process of logging into the website `https://outriskai.com/login`, creating a contract, generating it, and downloading or sharing the contract URL using Python and Selenium WebDriver.

## Features

- **Automated Login**: Logs into the website using the provided credentials.
- **Contract Creation**: Automatically fills out contract details such as title, parties involved (promisor and promisee), contract value, and more.
- **Dynamic Date Selection**: Allows for setting a custom contract date based on the configuration.
- **Contract Generation**: After filling in the details, it generates the contract.
- **Editing**: It adds customizable text to the contract.
- **Download & Share**: Downloads the generated contract and shares the URL via clipboard.

## Requirements

### Python 3.x
Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

### Python Packages
This project requires the following Python packages:

- **selenium==4.8.0**
- **pyperclip==1.8.2**

To install the required packages, you can use the following command:

```bash
pip install -r requirements.txt

### Run the script
python main.py


Setup Instructions

Step 1: Clone the Repository

To start working with this project, first clone the repository to your local machine. Open your terminal and run the following command:

git clone https://github.com/yourusername/repositoryname.git
Replace yourusername/repositoryname with the actual path to the repository if you're cloning from a remote source like GitHub.


Step 2: Install Dependencies
After cloning the repository, navigate to the project directory:

cd repositoryname


Now, install the necessary Python dependencies listed in requirements.txt:

pip install -r requirements.txt

Step 3: Configure the config.py File

In the config.py file, update the following fields:

USERNAME: Enter your login username for the website.
PASSWORD: Enter your login password for the website.
CONTRACT_DATE: Set the desired contract date in the format YYYY-MM-DD (e.g., 2024-12-01).
TITLE: Set the title for the contract (e.g., "Job offer").
PROMISOR: Set the name of the promisor (e.g., "Rishabh").
PROMISEE: Set the name of the promisee (e.g., "Faisal").



Step 4: Run the Script

Once you have cloned the repository, installed dependencies, and configured config.py, you can run the automation script:

python main.py
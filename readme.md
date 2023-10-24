# Prompt Tester

**Prompt Tester** is a Python script for testing the same prompt multiple times concurrently using the OpenAI GPT-3 model. It allows you to evaluate how the model responds to a specific prompt when tested multiple times.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Features

- Test the same prompt multiple times concurrently with the OpenAI GPT-3 model.
- Store and analyze the responses for further evaluation.
- Easily configure the project using environment variables.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

To run this project, you'll need the following prerequisites:

- Python
- An OpenAI API key

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/prompt-tester.git
   ```
2. Change to the project directory
   
   ```bash
   cd prompt-tester
   ```
  
3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Usage
To use Prompt Tester, follow these steps:

1. Create a .env file in the project directory.
2. Add your OpenAI API key to the .env file: 

   ```makefile
   OPENAI_API_KEY=your_api_key_here
   ```
3. Add the prompt you want to test inside the `prompt.txt` file.
4. Run the script:

   ```bash
   python main.py
   ```
   
The script will process the prompt(s) concurrently, and the results will be written to an output.txt file in the project directory.

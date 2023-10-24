import openai
from multiprocessing import Pool
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Define the function to process a single prompt
def process_prompt(_):
    # Initialize OpenAI API with the key from the environment
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key

    with open('prompt.txt', 'r') as prompt_file:
        prompt = prompt_file.read()  # Read the entire prompt as a single string

    # Process the prompt and return the result
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Choose the appropriate chat model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message['content']

if __name__ == "__main__":
    # Define the number of times you want to test the same prompt
    num_tests = 10  # You can change this to the desired number of tests

    # Create a list of dummy values to use as placeholders for concurrent processing
    prompt_list = [None] * num_tests

    # Create a pool of processes to process prompts concurrently
    with Pool(processes=4) as pool:  # Adjust the number of processes as needed
        results = pool.map(process_prompt, prompt_list)

    # Write the results to output.txt
    with open('output.txt', 'w') as output_file:
        for idx, result in enumerate(results, 1):
            output_file.write(f"Result {idx}:\n{result}\n\n")

    print("All prompts processed, and results written to output.txt.")

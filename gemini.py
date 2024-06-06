import json
import os
import subprocess
import difflib

def load_dataset(filename):
    dataset = []
    with open(filename, 'r') as file:
        for line in file:
            entry = json.loads(line)
            dataset.append(entry)
    return dataset

# Load your dataset containing prompts and corresponding Manim codes
dataset = load_dataset('dataset.jsonl')

def get_manim_code(prompt):
    # List to store tuples of (similarity, manim_code)
    matches = []

    # Search for matching prompts in the dataset
    for entry in dataset:
        input_text = entry['input_text']
        similarity = difflib.SequenceMatcher(None, prompt.lower(), input_text.lower()).ratio()
        matches.append((similarity, entry['output_text']))

    # Sort matches by similarity
    matches.sort(key=lambda x: x[0], reverse=True)

    # Check if there are any sufficiently similar matches
    if matches and matches[0][0] >= 0.7:  # Adjust threshold as needed
        return matches[0][1]  # Return the Manim code for the most similar prompt
    else:
        return None  # No sufficiently similar match found

def render_video(manim_code):
    # Write Manim code to a temporary file
    with open('temp_manim_code.py', 'w') as file:
        file.write(manim_code)

    # Execute Manim command to render the video
    subprocess.run(['manim', 'temp_manim_code.py'])

    # Remove temporary file
    os.remove('temp_manim_code.py')

def main():
    while True:
        # Prompt user for input
        user_prompt = input("Enter your prompt: ")

        # Get corresponding Manim code
        manim_code = get_manim_code(user_prompt)

        if manim_code:
            print("Manim Code:", manim_code)

            # Render the video
            render_video(manim_code)
        else:
            print("No matching Manim code found for the prompt.")

        # Ask user if they want to continue
        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

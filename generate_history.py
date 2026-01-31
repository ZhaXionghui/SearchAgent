import json

def generate_history(jsonlfile, outputfile):
    """
    Add history to each conversation in the JSONL, blank history for each line.

    Parameters:
    jsonlfile (str): Path to the input JSONL file containing conversation data.(each line is a JSON object, id, question, answer)

    outputfile (str): Path to the output JSONL file to save the conversation history.
    """
    with open(jsonlfile, 'r', encoding='utf-8') as infile, open(outputfile, 'w', encoding='utf-8') as outfile:
        for line in infile:
            conversation = json.loads(line)
            conversation['history'] = []  # Add blank history
            outfile.write(json.dumps(conversation, ensure_ascii=False) + '\n')

if __name__ == "__main__":
    input_jsonl = './question_with_answers.jsonl'  # Input file path
    output_jsonl = './question_with_history.jsonl'  # Output file path
    generate_history(input_jsonl, output_jsonl)
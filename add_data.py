import json
import argparse

# Function to add more data to the JSON file
def add_data(problem_name, solution_name, outcome):
    with open('solution_finder.json', 'r') as f:
        data = json.load(f)
    new_entry = {'name': problem_name, 'solutions': [{'name': solution_name, 'outcome': outcome}]}
    data['problems'].append(new_entry)
    with open('solution_finder.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add more data to Solution Finder.')
    parser.add_argument('--problem_name', required=True, help='Name of the problem')
    parser.add_argument('--solution_name', required=True, help='Name of the solution')
    parser.add_argument('--outcome', required=True, help='Outcome of the solution')
    args = parser.parse_args()
    add_data(args.problem_name, args.solution_name, args.outcome)
import json
import argparse

def add_problem(problem_name, solution_name, outcome):
    with open('solution_finder.json', 'r') as f:
        data = json.load(f)
    new_problem = {
        'id': len(data['problems']) + 1,
        'name': problem_name,
        'solutions': [
            {
                'id': len(data['problems']) + 1,
                'name': solution_name,
                'outcome': outcome
            }
        ]
    }
    data['problems'].append(new_problem)
    with open('solution_finder.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add a new problem to the JSON file.')
    parser.add_argument('--problem', required=True, help='Name of the problem')
    parser.add_argument('--solution', required=True, help='Name of the solution')
    parser.add_argument('--outcome', required=True, help='Outcome of the solution')
    args = parser.parse_args()
    add_problem(args.problem, args.solution, args.outcome)
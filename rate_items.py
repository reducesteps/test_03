import json
import argparse

# Function to handle rating of solutions, problems, and outcomes
def rate_items(search_type, query, rating):
    with open('solution_finder.json', 'r') as f:
        data = json.load(f)
    for problem in data['problems']:
        for solution in problem['solutions']:
            if query.lower() in str(solution.get(search_type, '')).lower():
                solution['rating'] = rating
    with open('solution_finder.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rating system for Solution Finder.')
    parser.add_argument('--search_type', required=True, help='Type of item to rate: problem, solution, or outcome')
    parser.add_argument('--query', required=True, help='Item to rate')
    parser.add_argument('--rating', type=int, required=True, help='Rating value')
    args = parser.parse_args()
    rate_items(args.search_type, args.query, args.rating)
import json
import argparse
from datetime import datetime

# Function to handle search history
def search_history(search_type, query, limit):
    with open('solution_finder.json', 'r') as f:
        data = json.load(f)
    with open('search_history.json', 'r') as f:
        history_data = json.load(f)
    results = []
    for problem in data['problems']:
        for solution in problem['solutions']:
            if query.lower() in solution[search_type].lower():
                results.append(solution[search_type])
    history_data.append({'search_type': search_type, 'query': query, 'timestamp': datetime.now().isoformat()})
    with open('search_history.json', 'w') as f:
        json.dump(history_data, f, indent=4)
    return results[:limit]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search history for Solution Finder.')
    parser.add_argument('--search_type', required=True, help='Type of search: problem, solution, or outcome')
    parser.add_argument('--query', required=True, help='Search query')
    parser.add_argument('--limit', type=int, default=10, help='Limit the number of search results')
    args = parser.parse_args()
    results = search_history(args.search_type, args.query, args.limit)
    print(results)
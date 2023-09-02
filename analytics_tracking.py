import json
import argparse
from collections import Counter

# Function to handle analytics and frequency tracking
def analytics_tracking(search_type, query, limit):
    with open('solution_finder.json', 'r') as f:
        data = json.load(f)
    with open('analytics.json', 'r') as f:
        analytics_data = json.load(f)
    results = []
    for problem in data['problems']:
        for solution in problem['solutions']:
            if query.lower() in solution[search_type].lower():
                results.append(solution[search_type])
    analytics_data[search_type] = Counter(analytics_data.get(search_type, {})) + Counter(results)
    with open('analytics.json', 'w') as f:
        json.dump(analytics_data, f, indent=4)
    return sorted(results, key=lambda x: analytics_data[search_type].get(x, 0), reverse=True)[:limit]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analytics tracking for Solution Finder.')
    parser.add_argument('--search_type', required=True, help='Type of search: problem, solution, or outcome')
    parser.add_argument('--query', required=True, help='Search query')
    parser.add_argument('--limit', type=int, default=10, help='Limit the number of search results')
    args = parser.parse_args()
    results = analytics_tracking(args.search_type, args.query, args.limit)
    print(results)
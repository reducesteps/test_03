import json
import argparse
from operator import itemgetter

# Function to handle multiple keyword sorting
def keyword_sorting(search_type, keywords, limit):
    with open('solution_finder.json', 'r') as f:
        data = json.load(f)
    results = []
    for problem in data['problems']:
        for solution in problem['solutions']:
            if any(keyword.lower() in str(solution.get(search_type, '')).lower() for keyword in keywords):
                results.append({'problem': problem['name'], 'solution': solution['name'], 'outcome': solution['outcome']})
    sorted_results = sorted(results, key=itemgetter('problem', 'solution'))
    return sorted_results[:limit]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Multiple keyword sorting for Solution Finder.')
    parser.add_argument('--search_type', required=True, help='Type of search: problem, solution, or outcome')
    parser.add_argument('--keywords', nargs='+', required=True, help='Keywords for sorting')
    parser.add_argument('--limit', type=int, default=10, help='Limit the number of search results')
    args = parser.parse_args()
    results = keyword_sorting(args.search_type, args.keywords, args.limit)
    print(results)
import json
import argparse

# Function to handle rating items
def rate_items(item_type, item_name, rating):
    with open('solution_finder.json', 'r') as f:
        data = json.load(f)
    for problem in data['problems']:
        for solution in problem['solutions']:
            if item_name.lower() == solution['name'].lower() and item_type.lower() == 'solution':
                solution['rating'] = rating
                print(f'Rated {item_name} with {rating} stars.')
    with open('solution_finder.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rating system for Solution Finder.')
    parser.add_argument('--item_type', required=True, help='Type of item: problem, solution, or outcome')
    parser.add_argument('--item_name', required=True, help='Name of the item to rate')
    parser.add_argument('--rating', type=int, required=True, help='Rating to be given')
    args = parser.parse_args()
    rate_items(args.item_type, args.item_name, args.rating)
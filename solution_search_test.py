import json

def main():
    with open('solution_finder.json', 'r') as f:
        data = json.load(f)
    print(search_solutions_by_problem('Problem A', data))
    print(search_solutions_by_outcome('Positive', data))
    print(search_problems_by_solution('Solution A1', data))

def search_solutions_by_problem(problem_name, json_data):
    results = []
    for problem in json_data['problems']:
        if problem['name'] == problem_name:
            results.extend(problem['solutions'])
    return results

def search_solutions_by_outcome(outcome, json_data):
    results = []
    for problem in json_data['problems']:
        for solution in problem['solutions']:
            if solution['outcome'] == outcome:
                results.append(solution)
    return results

def search_problems_by_solution(solution_name, json_data):
    results = []
    for problem in json_data['problems']:
        for solution in problem['solutions']:
            if solution['name'] == solution_name:
                results.append(problem)
    return results

if __name__ == '__main__':
    main()
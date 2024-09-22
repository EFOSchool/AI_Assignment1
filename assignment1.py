from collections import defaultdict
from bfs import bfs
from dfs import dfs
import time
import csv

adj_list = {
    'Oradea': { 'Sibiu': 151, 'Zerind': 71 },
    'Zerind': { 'Oradea': 71, 'Arad': 75 },
    'Arad': { 'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Timisoara': { 'Arad': 118, 'Lugoj': 111 },
    'Lugoj': { 'Mehadia': 70, 'Timisoara': 111},
    'Mehadia': { 'Lugoj': 70, 'Dobreta': 75 },
    'Dobreta': { 'Mehadia': 75, 'Craiova': 120 },
    'Craiova': { 'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138 },
    'Rimnicu Vilcea': { 'Craiova': 146, 'Sibiu': 80, 'Pitesti': 97 },
    'Sibiu': { 'Arad': 140, 'Oradea': 151, 'Rimnicu Vilcea': 80, 'Fagaras': 99 },
    'Fagaras': { 'Sibiu': 99, 'Bucharest': 211 },
    'Pitesti': { 'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101 },
    'Bucharest': { 'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85 },
    'Urziceni': { 'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98 },
    'Giurgiu': { 'Bucharest': 90 },
    'Vaslui': { 'Urziceni': 142, 'Iasi': 92 },
    'Iasi': { 'Vaslui': 92, 'Neamt': 87 },
    'Neamt': { 'Iasi': 87 },
    'Hirsova': { 'Urziceni': 98, 'Eforie': 86 },
    'Eforie': { 'Hirsova': 86 },
}

h_sld = {
    'Oradea': 380,
    'Zerind': 374,
    'Arad': 366,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Fagaras': 176,
    'Pitesti': 100,
    'Bucharest': 0,
    'Urziceni': 80,
    'Giurgiu': 77,
    'Vaslui': 199,
    'Iasi': 226,
    'Neamt': 234,
    'Hirsova': 151,
    'Eforie': 161
}

def run_search_to_csv(goal):
    """
    Runs all searches and exports to csv for comparison/analysis
    """
    
    # results list for printing data table
    results = []
    
    # iterating through all cities for performance testing
    for start_city in adj_list:
        if start_city == goal:
            continue
        
        # Run BFS and track time and nodes visited
        start_time = time.perf_counter()
        res_bfs, visited_bfs = bfs(adj_list, start_city, goal)
        time_bfs = time.perf_counter() - start_time
        
        # Run DFS and track time and nodes visited
        start_time = time.perf_counter()
        res_dfs, visited_dfs = dfs(adj_list, start_city, goal)
        time_dfs = time.perf_counter() - start_time
        
        # check that it is the right format before adding to results
        visited_bfs = visited_bfs if isinstance(visited_bfs, int) else len(visited_bfs)
        visited_dfs = visited_dfs if isinstance(visited_dfs, int) else len(visited_dfs)
            
        # list for table
        results.append([
            start_city,
            time_bfs, visited_bfs,
            time_dfs, visited_dfs,
        ])
    
    with open('execution_time_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow([
            "Start City",
            "BFS Time (s)", "BFS Nodes Visited",
            "DFS Time (s)", "DFS Nodes Visited",
        ])
        # Write the data
        writer.writerows(results)

def main():
    while True: 
        print('\n\n\nAssignment 1: SEARCH')
        print('-------------------------')
        print('How would you like to proceed: ')
        print('1) Run comprehensive test of all algorithms and start cities and export results to a csv file for analysis')
        print('2) Select individual search algorithms to view their results')
        print('Enter Q to exit')
        runType = input('\nEnter number of way you\'d like to run the program: ').lower()
        
        if runType == 'q':
            break
        elif runType == '1':
            goalCity = input('Select a goal city: ')
            run_search_to_csv(goalCity)
            print('\nResults have been printed to execution_time_results.csv\n')
            break        
        
        print('\n\n--------------------')
        print('1) Breadth-First Search')
        print('2) Depth-First Search')
        print('3) Best-First Search (Greedy)')
        print('4) A* Search')
        print('Enter Q to exit\n')
        choice = input('Enter number of search you\'d like to see: ').lower()
        
        results = []
        
        if choice == 'q':
            break
                
        start = input('\nSelect a start city (if you want to see all possible starts hit enter to continue): ')
        goal = input('Select a goal city: ')
        
        # only run for selected city
        if start:
            visited_count = 0
            # Perform the search only for the selected start city
            start_time = time.perf_counter()
            if choice == '1':
                res, visited_count = bfs(adj_list, start, goal)
            elif choice == '2':
                visited_count, res = dfs(adj_list, start, goal)
            duration = (time.perf_counter() - start_time)

            # Append the result for this search
            result = {
                'Start City': start,
                'Result': res,
                'Duration (s)': duration,
                'Total Cities Visited': visited_count
            }
            print('\n\n\nCHECK: ', res)
            
            print('\nResults below with final path and total cities visited: \n\n')
        
            # Print all results at the end
            print(f"From {result['Start City']}: {result['Result']}, "
                    f"Time Taken: {result['Duration (s)']:.6f}s, "
                    f"Total Cities Visited: {result['Total Cities Visited']}")
        else: 
            for start_city in adj_list:
                visited_count = 0
                if start_city == start:
                    continue
                
                # start timer and determine what search to do
                start = time.perf_counter()
                if choice == '1':
                    res, visited_count = bfs(adj_list, start_city, goal)
                elif choice == '2':
                    visited_count, res = dfs(adj_list, start_city, goal)
                
                duration = (time.perf_counter() - start)

                # Append results for this search
                results.append({
                    'Start City': start_city,
                    'Result': res,
                    'Duration (s)': duration,
                    'Total Cities Visited': len(visited_count) if isinstance(visited_count, list) else visited_count
                })
            
            print('\nResults below with final path and total cities visited: \n\n')
        
            # Print all results at the end
            for result in results:
                print(f"From {result['Start City']}: {result['Result']}, "
                    f"Time Taken: {result['Duration (s)']:.6f}s, "
                    f"Total Cities Visited: {result['Total Cities Visited']}")

if __name__ == '__main__':
    main()
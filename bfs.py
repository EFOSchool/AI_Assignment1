from collections import defaultdict
import time
import csv


def bfs(graph, start, goal="Bucharest"):
    """
    Explore all nodes level by level using a queue.
    
    Args:
        graph (dict): Adjacency list representation of Romania 
        start (str): Starting node
        goal (str): Target node, defaulting to Bucharest
        
    Returns:
        tuple: 
            - path (list): Path through object as a list of nodes
            - visited_count (int): The total number of nodes visited during search
    """
    visited = []
    queue = [[start]]
    
    if start == goal:
        return [start], 1
    
    while queue:
        # first path
        path = queue.pop(0)
        # last node
        node = path[-1]
        
        if node not in visited:
            neighbors = graph[node]
            
            # new path and push to queue
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
                # check if goal
                if neighbor == goal:
                    # return a path and count for performance analysis
                    return new_path, len(visited) + 1
        
        # mark visited so it isn't repeated
        visited.append(node)

    # if no path is found
    return [], len(visited)

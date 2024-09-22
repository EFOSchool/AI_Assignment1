def dfs(graph, start, goal="Bucharest", path=None, visited=None):
    """
    Uses recursion to explore each branch of a graph
    
    Args:
        graph (dict): Adjacency list representation of Romania 
        start (str): Starting node
        goal (str): Target node, defaulting to Bucharest
        visited (set, optional): Makes sure the same nodes aren't getting revisted
        path (list, optional): Current path search has followed
        
    Returns:
        tuple: 
            - path (list): Path through object as a list of nodes
            - visited_count (int): The total number of nodes visited during search
    """
    # initial run
    if visited is None:
        visited = set()
    if path is None:
        path = []
        
    # first node
    visited.add(start)
    path.append(start)
    
    # first case to check if it is goal
    if start == goal:
        return len(visited), path
    
    # go through each neighbor
    for neighbor in graph[start]:
        if neighbor not in visited:
            # use recursion for backtracking
            visited_count, result_path = dfs(graph, neighbor, goal, path, visited)
            if result_path:
                return visited_count, result_path
            
    # case that no path is found
    path.pop()
    return len(visited), []

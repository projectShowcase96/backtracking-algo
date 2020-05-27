# We need to find possible routes to reach goal nodes using backtracking concept
# Backtracking basic pseudocode Source: 6029879 - stackoverflow

# ￼
# ￼
# boolean backtrackDFS(v)  {
#    If  (SolutionFound(v))  return true;
#    Mark vertex v as reached.
#    for (each unreached vertex u adjacenct from v)
#         if (backtrakDFS(u)) return true;
#    Unmark vertex v; 
#    return false;
# }

from data import *
import time
import resource 


# # starting timer here
time_start = time.perf_counter()


# if solution found print the solution
def solution_found(visited):

    print(visited)
    return


# backtracking algorithm
def back_track(graph, vertex, goal_vertex, visited):

    # inserting visited vertex
    visited.append(vertex)

    # checking for goal vertex
    if vertex == goal_vertex:
        solution_found(visited)
        
    
    # print(visited)

    # iterating child nodes of visited vertex
    for neighbour in graph[vertex]:
        
        # print(neighbour)
        
        # checking wheather child vertex is visited or not
        if neighbour not in visited:

            # if not visited then visit and recursive call 
            back_track(graph, neighbour, goal_vertex, visited)
            
            
    # if visited vertex has no child node then pop it out
    visited.pop()
    
    # print("after pop - ", visited)
    
    return False

    
    
    
# back_track method calling
back_track(adjacency_matrix, 'A', 'G', [])



# all things need to print how much time code used
time_elapsed = (time.perf_counter() - time_start)

memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0

print ("%5.1f secs %5.1f MByte" % (time_elapsed,memMb))


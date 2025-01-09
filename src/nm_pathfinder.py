def find_path (source_point, destination_point, mesh):

    """
    Searches for a path from source_point to destination_point through the mesh

    Args:
        source_point: starting point of the pathfinder
        destination_point: the ultimate goal the pathfinder must reach
        mesh: pathway constraints the path adheres to

    Returns:

        A path (list of points) from source_point to destination_point if exists
        A list of boxes explored by the algorithm
    """

    path = []
    boxes = {}
    # find boxes that contain start and goal points
    for item in mesh["boxes"]: 
    # item returns coords for boxes
        if (within_bounds(item, source_point)):
            boxes.update({"source": item})
        if (within_bounds(item, destination_point)):
            boxes.update({"goal": item})
    path, boxes = BFS(boxes["source"], boxes["goal"], mesh)
    return path, boxes.keys()

def within_bounds (box, point):
    # check if point in range of box 
    # x1, x2, y1, y2
    # 0,  1.  2,  3
    # bias inclusive to bottom right so points exactly on edge of boxes won't be missed
    if (((box[0] < point[0]) and (box[2] < point[1])) 
    and (box[1] >= point[0] and box[3] >= point[1])):
        return True
    return False

def BFS (start, goal, mesh):
    # add start point to queue
    queue = [start]
    came_from = dict()
    came_from[start] = None

    # visit boxes
    while not len(queue) == 0:
        current = queue.pop()
        for box in mesh["adj"][current]:
            if box not in came_from:
                queue.append(box)
                came_from[box] = current

    # create path from goal
    current = goal
    path = []
    
    while current != start:
        if (came_from[current] == None):
            print("No path!")
            path = [(start[0],start[2]),(start[0],start[2])]
            break
        path.append(((current[0]+current[1])/2,(current[2]+current[3])/2))
        current = came_from[current]
    path.append(((start[0]+start[1])/2,(start[2]+start[3])/2))
    path.reverse()
    return path, came_from
            
    


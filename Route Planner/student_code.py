import math
import heapq

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def insert(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def remove(self):
        return heapq.heappop(self._queue)[-1]

    def isEmpty(self):
        return len(self._queue) == 0

    def getSize(self):
        return self._index


def get_heuristic(node, goal_node):
    # straight line distance from node to goal node will serve as heuristic
    return get_distance(node, goal_node)

def get_distance(src_node, dest_node):
    # apply two point distance formula to get the straight line distance between two points
    x1, y1 = src_node
    x2, y2 = dest_node
    distance = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    return distance


def shortest_path(M, start, goal):

    map = M

    if map is None or map.roads[start] is None or len(map.roads[start]) < 1:
        return None

    if start == goal:
        return [start]

    queue = PriorityQueue()

    shortest_dist = {}
    shortest_dist[start] = 0
    parents = {}

    goal_cord = map.intersections[goal]

    path_cost = 0
    h_cost = get_heuristic((map.intersections[start]), goal_cord)
    f_cost = h_cost + path_cost

    queue.insert((start, path_cost, h_cost), f_cost)

    while not queue.isEmpty():

        current_node, path_cost, h_cost = queue.remove()
        current_node_cord = map.intersections[current_node]

        if current_node == goal:
            break

        for neighbor in map.roads[current_node]:

            neighbor_cord = map.intersections[neighbor]

            neighbor_path_cost = path_cost + get_distance(current_node_cord, neighbor_cord)
            neighbor_h_cost = get_heuristic(neighbor_cord, goal_cord)
            neighbor_f_cost = neighbor_path_cost + neighbor_h_cost

            if neighbor in shortest_dist:
                if shortest_dist[neighbor] > neighbor_f_cost:
                    shortest_dist[neighbor] = neighbor_f_cost
                    parents[neighbor] = current_node
                    queue.insert((neighbor, neighbor_path_cost, neighbor_h_cost), neighbor_f_cost)

            else:
                shortest_dist[neighbor] = neighbor_f_cost
                parents[neighbor] = current_node
                queue.insert((neighbor, neighbor_path_cost, neighbor_h_cost), neighbor_f_cost)

    path = [goal]
    current_node = goal

    while current_node != start:
        parent = parents[current_node]
        path.append(parent)
        current_node = parent
    path.reverse()

    return path

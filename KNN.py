import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class QuadTreeNode:
    def __init__(self, point):
        self.point = point
        self.nw = None
        self.ne = None
        self.sw = None
        self.se = None

class QuadTree:
    def __init__(self):
        self.root = None

    def insert(self, point):
        if not self.root:
            self.root = QuadTreeNode(point)
        else:
            self._insert_recursive(self.root, point)

    def _insert_recursive(self, node, point):
        if point.x < node.point.x and point.y < node.point.y:
            if not node.nw:
                node.nw = QuadTreeNode(point)
            else:
                self._insert_recursive(node.nw, point)
        elif point.x >= node.point.x and point.y < node.point.y:
            if not node.ne:
                node.ne = QuadTreeNode(point)
            else:
                self._insert_recursive(node.ne, point)
        elif point.x < node.point.x and point.y >= node.point.y:
            if not node.sw:
                node.sw = QuadTreeNode(point)
            else:
                self._insert_recursive(node.sw, point)
        else:
            if not node.se:
                node.se = QuadTreeNode(point)
            else:
                self._insert_recursive(node.se, point)

    def knn_search(self, query_point, k):
        if not self.root:
            return []

        nearest_points = []
        self._knn_search_recursive(self.root, query_point, k, nearest_points)
        return nearest_points

    def _knn_search_recursive(self, node, query_point, k, nearest_points):
        if not node:
            return

        distance = math.sqrt((node.point.x - query_point.x) ** 2 + (node.point.y - query_point.y) ** 2)

        if len(nearest_points) < k:
            nearest_points.append((node.point, distance))
            nearest_points.sort(key=lambda x: x[1], reverse=True)
        elif distance < nearest_points[0][1]:
            nearest_points[0] = (node.point, distance)
            nearest_points.sort(key=lambda x: x[1], reverse=True)

        if query_point.x < node.point.x and query_point.y < node.point.y:
            self._knn_search_recursive(node.nw, query_point, k, nearest_points)
        elif query_point.x >= node.point.x and query_point.y < node.point.y:
            self._knn_search_recursive(node.ne, query_point, k, nearest_points)
        elif query_point.x < node.point.x and query_point.y >= node.point.y:
            self._knn_search_recursive(node.sw, query_point, k, nearest_points)
        else:
            self._knn_search_recursive(node.se, query_point, k, nearest_points)

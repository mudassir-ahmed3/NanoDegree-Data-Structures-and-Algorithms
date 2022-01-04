# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self,handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)


    def insert(self, path_list,handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        # sub_paths = path.split("/")
        for part in path_list:
            if part not in current_node.children:
                current_node.children[part] = RouteTrieNode()
            current_node = current_node.children[part]

        current_node.handler = handler


    def find(self,path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for part in path_list:
            if part not in current_node.children:
                return None
            current_node = current_node.children[part]

        return current_node.handler




# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self,handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, char, handler):
        # Insert the node as before
        if char not in self.children:
            self.children[char] = RouteTrieNode()


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        self.route_trie.insert(path_list,handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        return self.route_trie.find(path_list)


    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        path_list = [part for part in path.split("/") if part != ''] #I needed to do this to avoid having empty string as I was getting before as path's part when returning path.split("/")
        return path_list

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

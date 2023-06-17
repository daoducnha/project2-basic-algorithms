class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.is_handler = False
        self.children_path = {}
        self.handler = handler

    def insert(self, sub_path):
        if sub_path not in self.children_path:
            self.children_path[sub_path] = RouteTrieNode()
class RouteTrie:
    def __init__(self, path='/'):
        self.root = RouteTrieNode()
        self.root.insert(path)

    def insert(self, path, handler):
        current_node = self.root
        sub_paths = self.split_path(path)

        for sub_path in sub_paths:
            if sub_path not in current_node.children_path:
                return
            current_node = current_node.children_path[sub_path]

        current_node.is_handler = True
        current_node.handler = handler

    def find(self, path):
        current_sub_path = self.root
        sub_paths = self.split_path(path)

        for sub_path in sub_paths:
            if sub_path not in current_sub_path.children_path:
                return None
            current_sub_path = current_sub_path.children_path[sub_path]

        return current_sub_path.handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        sub_paths = path.split('/')
        if sub_paths[-1] == '':
            sub_paths = sub_paths[:-1]
        sub_paths[0] = '/'
        return sub_paths
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route = RouteTrie()
        self.handler = dict()

        self.handler[root_handler] = root_handler
        self.handler[not_found_handler] = not_found_handler

        self.route.insert("/", self.handler[root_handler])


    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        current_node = self.route.root
        self.handler[handler] = handler

        sub_paths = self.split_path(path)

        for sub_path in sub_paths:
            if sub_path not in current_node.children_path:
                current_node.children_path[sub_path] = RouteTrieNode(self.handler["not found handler"])
            current_node = current_node.children_path[sub_path]

        current_node.is_handler = True
        current_node.handler = self.handler[handler]

    def lookup(self, path):

        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        sub_paths = self.split_path(path)
        current_node = self.route.root

        for sub_path in sub_paths:
            if sub_path not in current_node.children_path:
                return self.handler["not found handler"]
            current_node = current_node.children_path[sub_path]


        return current_node.handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        sub_paths = path.split('/')
        if sub_paths[-1] == '':
            sub_paths = sub_paths[:-1]
        sub_paths[0] = '/'
        return sub_paths


if __name__ == '__main__':
    ## Here are some test cases and expected outputs you can use to test your implementation

    ## create the router and add a route
    router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    ## some lookups with the expected output
    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one

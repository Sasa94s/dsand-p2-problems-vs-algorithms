# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode('/', root_handler)

    def insert(self, path, handler):
        current_node = self.root
        for part in path:
            if part not in current_node.children:
                current_node.insert(part)
            current_node = current_node.children[part]
        current_node.handler = handler

    def find(self, path):
        current_node = self.root
        for part in path:
            if part not in current_node.children:
                return None
            current_node = current_node.children[part]
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, value='', handler=None, children={}):
        self.value = value
        self.handler = handler
        self.children = children

    def insert(self, path_part, value='',  handler=None):
        self.children[path_part] = RouteTrieNode(value, handler)

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler=None):
        self.root = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        self.root.insert(self.split_path(path), handler)

    def lookup(self, path):
        handler = self.root.find(self.split_path(path))
        return handler if handler else self.not_found_handler

    def split_path(self, path):
        res = []
        path_part = ''
        for char in path[1:]:
            if char == '/':
                if path_part != '':
                    res.append(path_part)
                    path_part = ''
            else:
                path_part += char

        if path_part != '':
            res.append(path_part)

        return res

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
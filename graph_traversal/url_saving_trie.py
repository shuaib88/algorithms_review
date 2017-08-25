# Trie structure that elminates redundant prefixes of strings

class Trie:


    def __init__(self):
        self.root_node = {}


    def check_present_and_add(self, url_string):

        current_node = self.root_node
        is_new_word = False

        for char in url_string:

            print char

            if char not in current_node:
                current_node[char] = {}
                is_new_word = True
                print "^ not in dict"
            current_node = current_node[char]

        if "End Of Word" not in current_node:
            current_node["End Of Word"] = {}

        return is_new_word


# test
visited = Trie()

# execute
visited.check_present_and_add("www.google.com")
visited.check_present_and_add("www.google.com/jobs")
visited.check_present_and_add("www.maps.com")
visited.check_present_and_add("maps.google.com")


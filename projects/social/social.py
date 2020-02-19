import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        friends=list()
        # Add users
        for user_num in range(self.last_id +1, num_users+1): #FOR EVERY USER FROM 1- NUM OF USERS
            # print("USER-->",user_num)
            for friend_num in range(self.last_id +1, num_users +1): #GET EVERY USERS FRIEND
                # print("FRIEND -->", friend_num)
                if user_num<friend_num: #IF THE USER NUM IS LESS THAN THE FRIEND NUM, ADD IT TO THE FRIENDS LIST, KEEP FROM REPEATING FRIENDSHIPS
                    friends.append((user_num, friend_num))
                    # print("friends -->", friends)
            self.add_user(user_num)# prepends the friends list so you see whos friends belong to who,,
        
        # print("random")
        random.shuffle(friends)

        for i in range(num_users):
            self.add_friendship(friends[i][0], friends[i][1])#takes friends id and user id and makes a two-way friendship.... send in pairs from friends list

        # Create friendships

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME



        q=Queue()#make a queue
        q.enqueue([user_id]) #add first user id
        while q.size()>0: #until empty
            # print("THE Q", q)
            curr_path=q.dequeue() #make current path the first item inline thats removed
            # print("current path",curr_path)
            curr_node=curr_path[-1]#current node is the last item into the q
            # print("current node", curr_node)
            if curr_node in visited and len(curr_path)<len(visited[curr_node]):
                #if current node has been visited and the current path is shorter than the path at the current node, reassign visited[node] path to current path
                visited[curr_node] = curr_path
            if curr_node not in visited:
                #if we haven't visited it yet, the path at the current node will be assigned below
                visited[curr_node]=curr_path

                edge=self.friendships[curr_node]
                #friendships at that node(person)
                for e in edge: #for every friend in the friendships
                    # print("E", e)
                    # print("path plus e", curr_path)
                    q.enqueue(curr_path + [e]) #adds e to end of path so it stops
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

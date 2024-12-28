import requests
class Post:
    def __init__(self):
        self.url = "https://api.npoint.io/c790b4d5cab58020d391"
        self.posts = []
        self.num = 0

    def get_data(self):
         self.posts = requests.get(self.url).json()
         return self.posts

    def get_exact_data(self):
        for i in range(len(self.posts)):
            if self.posts[i]['id'] == self.num:
                return self.posts[i]




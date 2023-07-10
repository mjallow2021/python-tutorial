class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author
      

    def create_post(self, message, author):
       self.message = message
       self.author = author
        
    def change_post(self, new_message, author):
        #print (f"Post: {self.new_message}, written by {self.author}")
        self.message = new_message
        self.author = author

    def get_post_info(self):
        print (f"Post: {self.message}, written by {self.author}")



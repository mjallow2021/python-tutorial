from nanafullcourse_07OOPUserClass import User
from nanafullcourse_07OOPPostClass import Post

app_user_one = User("mj@python.com", "Mo Jallow", "passwd", "IT Engineer")
app_user_one.get_user_info()
app_user_one.change_job_title("Devops Engineer")
app_user_one.get_user_info()
app_user_two = User("brandon@python.com", "Bigman Brandon", "passwd", "IT Engineer")
app_user_two.get_user_info()
new_post = Post("this is a post from Brandon", app_user_two.name)
new_post.get_post_info()
new_post.change_post = Post("this is a post CHANGED  from Brandon to BIGMAN BRANDON", app_user_two.name)
new_post.get_post_info()
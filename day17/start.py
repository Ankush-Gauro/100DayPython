class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        self.following  += 1
        user.follower += 1

user_1 = User("001", "aj")
user_2 = User("002", "ankush")

user_1.follow(user_2)

print("Followers: ", user_1.follower, "\nFollowing:", user_1.following)
print("Followers: ", user_2.follower, "\nFollowing:", user_2.following)
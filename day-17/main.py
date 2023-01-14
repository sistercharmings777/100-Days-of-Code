class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User('001', 'Prince')

print(user_1.id)
print(user_1.username)
print(user_1.follower)

user_2 = User('002', 'Daniella')
print(user_2.username)

user_1.follow(user_2)
user_2.follow(user_1)

print(user_1.follower, user_1.following)
print(user_2.follower, user_2.following)
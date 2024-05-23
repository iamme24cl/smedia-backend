import random
from faker import Faker
from flask import session

from models.like import Like
from models.post import Post
from models.user import User
from models.comment import Comment

fake = Faker()

def generate_fake_data(num_users=10, num_posts=30, num_comments=50, num_likes=100):
    users = []
    posts = []
    comments = []
    likes = []

    for _ in range(num_users):
        user = User(
            name=fake.name(),
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),  # Generate a fake password
            avatar=fake.image_url(),
            bio=fake.text(max_nb_chars=100),
            location=fake.city(),
            joined_at=fake.date_this_decade()
        )
        users.append(user)
        session.add(user)

    session.commit()

    for _ in range(num_posts):
        post = Post(
            user_id=random.choice(users).id,
            content=fake.text(max_nb_chars=200),
            image=fake.image_url(),
            likes=random.randint(0, 1000),
            comments=random.randint(0, 100),
            created_at=fake.date_time_this_year()
        )
        posts.append(post)
        session.add(post)

    session.commit()

    for _ in range(num_comments):
        comment = Comment(
            post_id=random.choice(posts).id,
            user_id=random.choice(users).id,
            content=fake.text(max_nb_chars=100),
            created_at=fake.date_time_this_year()
        )
        comments.append(comment)
        session.add(comment)

    session.commit()

    for _ in range(num_likes):
        like = Like(
            post_id=random.choice(posts).id,
            user_id=random.choice(users).id,
            created_at=fake.date_time_this_year()
        )
        likes.append(like)
        session.add(like)

    session.commit()
    
if __name__ == '__main__':
    generate_fake_data()
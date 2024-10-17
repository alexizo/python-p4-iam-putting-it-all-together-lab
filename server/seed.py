from random import randint, choice as rc
from faker import Faker
from app import app
from models import db, Recipe, User

fake = Faker()

with app.app_context():
    Recipe.query.delete()
    User.query.delete()

    users = []
    usernames = set()

    for _ in range(20):
        username = fake.first_name()
        while username in usernames:
            username = fake.first_name()
        usernames.add(username)

        user = User(
            username=username,
            bio=fake.paragraph(nb_sentences=3),
            image_url=fake.image_url(),  # Use faker's image_url for random images
        )
        user.password_hash = user.username + 'password'  # Consider using hashing

        users.append(user)

    db.session.add_all(users)

    recipes = []
    for _ in range(100):
        instructions = fake.paragraph(nb_sentences=8)
        
        recipe = Recipe(
            title=fake.sentence(),
            instructions=instructions,
            minutes_to_complete=randint(15, 90),
        )

        recipe.user = rc(users)

        recipes.append(recipe)

    db.session.add_all(recipes)
    
    db.session.commit()
    print("Database seeded successfully.")

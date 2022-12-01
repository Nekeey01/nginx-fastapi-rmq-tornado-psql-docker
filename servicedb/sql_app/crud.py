
from .db import db
from .models import problem_table

async def create_user(user):
    query = problem_table.insert().values(
        Name=user['Name'], Surname=user['Surname'], Midname=user['Midname'], Phone=user['Phone'], Problem=user['Problem']
    )
    user_id = await db.execute(query)
    return user_id

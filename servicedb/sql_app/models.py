import sqlalchemy
from sql_app.db import db

metadata = sqlalchemy.MetaData()

problem_table = sqlalchemy.Table(
    "Problems",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("Name", sqlalchemy.String),
    sqlalchemy.Column("Surname", sqlalchemy.String),
    sqlalchemy.Column("Midname", sqlalchemy.String),
    sqlalchemy.Column("Phone", sqlalchemy.String),
    sqlalchemy.Column("Problem", sqlalchemy.String),

)

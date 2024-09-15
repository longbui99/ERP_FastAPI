from pydantic import BaseModel
from tortoise import fields, models

class User(BaseModel):
    id: int
    login: str
    password: str
    email: str

class _User(models.Model):
    id: str = fields.IntField(primary_key=True)
    login: str = fields.TextField()
    password: str = fields.TextField()
    email: str = fields.TextField()

    def __str__(self):
        return f"User({self.id})"
    class Meta:
        table = "res_users"
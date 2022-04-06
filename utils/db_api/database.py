from gino import Gino
from data.config import DB_HOST, DB_NAME, DB_PASS,DB_USER
db = Gino()
from aiogram import types



class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key = True)
    tg_id = db.Column(db.String)
    username = db.Column(db.String)
class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String)
class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer,primary_key = True)
    cat_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    name = db.Column(db.String)
    price = db.Column(db.Float)
    date_time = db.Column(db.String)



class DB_Commands:
    
    async def add_user(self, tg_id, username):
        users = await self.get_users()
        for i in users:
            if i.tg_id == str(tg_id):
                return True
        await Users.create(tg_id=str(tg_id),username=username)
        return ''

    async def add_category(self, name):
        cats = await self.get_categories()
        for i in cats:
            print(i==name)
            if i.name==name:
                return ''
        await Category.create(name=str(name))
        return ''

    async def delete_category(self,id):
        try:
            a = await Category.query.where(Category.id == int(id)).gino.first()
            await a.delete()
        except:
            return ''

    async def get_categories(self):
        categories = await Category.query.gino.all()
        return categories

    async def get_users(self):
        users = await Users.query.gino.all()
        return users




async def create_db():
    await db.set_bind(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")
    # await db.gino.create_all()
    # await db.gino.drop_all()
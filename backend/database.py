from model import Todo
# MongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.TodoList
collection = database.todo


async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document
    

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return result


async def update_todo(title, desc):
    await collection.update_one({"title":title}, {"$set":{"description": desc}})
    document = await collection.find_one({"title":title})
    return document


async def remove_todo(title):
    await collection.delete_one({"title":title})
    return True

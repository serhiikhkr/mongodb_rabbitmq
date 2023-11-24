from mongoengine import connect


connect(host="mongodb+srv://helloworld:goitserhii@serhii.n5tsqhh.mongodb.net/?retryWrites=true&w=majority", ssl=True)

# available_databases = conn.list_database_names()


from app.data.mongodb.connection import Connection

class CreateDatabase:
    def __init__(self):
        self.DATABASE_NAME = "monitoring"
        self.connection = Connection().connection
        self.init_database()

    def init_database(self):
        try:
            self.create_collections()
            self.connection.close()
        except Exception as err:
            print(err)

    def create_collections(self):
        db = self.connection[self.DATABASE_NAME]

        # Creation of the users collection
        users_collection = db['users']
        users_collection.create_index('username', unique=True)

        # Creation of the devices collection
        devices_collection = db['devices']
        devices_collection.create_index('device_name', unique=True)

        # Creation of the device_informations collection
        device_informations_collection = db['device_informations']
        device_informations_collection.create_index('device_id', unique=True)

if __name__ == "__main__":
    cr = CreateDatabase()

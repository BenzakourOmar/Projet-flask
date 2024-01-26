from app import mongo

class SNMPData:
    def __init__(self, device_name, memory_usage, cpu_usage, disk_usage):
        self.device_name = device_name
        self.memory_usage = memory_usage
        self.cpu_usage = cpu_usage
        self.disk_usage = disk_usage

    def save_to_mongo(self):
        mongo.db.snmp_data.insert_one({
            'device_name': self.device_name,
            'memory_usage': self.memory_usage,
            'cpu_usage': self.cpu_usage,
            'disk_usage': self.disk_usage
        })

    @staticmethod
    def get_all():
        return list(mongo.db.snmp_data.find())

from flask import jsonify, request
from app import app
from app.models import SNMPData

@app.route('/snmp_data', methods=['GET'])
def get_snmp_data():
    snmp_data = SNMPData.get_all()
    return jsonify(snmp_data)

@app.route('/snmp_data', methods=['POST'])
def add_snmp_data():
    data = request.json
    new_snmp_data = SNMPData(
        device_name=data['device_name'],
        memory_usage=data['memory_usage'],
        cpu_usage=data['cpu_usage'],
        disk_usage=data['disk_usage']
    )
    new_snmp_data.save_to_mongo()
    return jsonify({'message': 'Data added successfully'})

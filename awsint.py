from flask import Flask,render_template,request,jsonify
import boto3
import uuid
from datetime import datetime

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', region_name = "ap-south-1")
Photographers_id_table=dynamodb.Table('Photographers_id')

@app.route('/photographers', methods = ['GET'])
def get_photographers():
    try:
        response = Photographers_id_table.scan()
        return jsonify(response['Items'])
    except Exception as e:
        return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
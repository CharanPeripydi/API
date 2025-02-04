from flask import Flask, request, jsonify
from db import init_db, mysql
from models import Employee

app = Flask(__name__)
init_db(app)

@app.route('/employees', methods=['GET'])
def get_employees():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchall()
    
    employees = []
    for row in result:
        employees.append({
            'id': row[0],
            'name': row[1],
            'position': row[2],
            'salary': row[3]
        })
    
    return jsonify({'employees': employees})

@app.route('/employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    name = data.get('name')
    position = data.get('position')
    salary = data.get('salary')
    
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)", (name, position, salary))
    mysql.connection.commit()
    
    return jsonify({'message': 'Employee added successfully'}), 201

@app.route('/employee/<int:id>', methods=['GET'])
def get_employee(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM employees WHERE id = %s", (id,))
    result = cursor.fetchone()
    
    if result:
        employee = {
            'id': result[0],
            'name': result[1],
            'position': result[2],
            'salary': result[3]
        }
        return jsonify({'employee': employee})
    
    return jsonify({'message': 'Employee not found'}), 404

@app.route('/employee/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()
    name = data.get('name')
    position = data.get('position')
    salary = data.get('salary')
    
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE employees SET name = %s, position = %s, salary = %s WHERE id = %s", (name, position, salary, id))
    mysql.connection.commit()
    
    return jsonify({'message': 'Employee updated successfully'})

@app.route('/employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM employees WHERE id = %s", (id,))
    mysql.connection.commit()
    
    return jsonify({'message': 'Employee deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)

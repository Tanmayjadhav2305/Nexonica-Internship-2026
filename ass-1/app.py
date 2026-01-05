from flask import Flask, request, jsonify

app = Flask(__name__)

# temporary storage of employees
employees = []
auto_id = 1


# add employee
@app.route('/add_emp', methods=['POST'])
def add_emp():
    global auto_id
    data = request.get_json()

    emp = {
        "id": auto_id,
        "name": data.get("name"),
        "email": data.get("email"),
        "salary": data.get("salary")
    }

    employees.append(emp)
    auto_id += 1

    return jsonify({"message": "Employee added successfully", "employee": emp}), 201


# get all employees
@app.route('/get_emp', methods=['GET'])
def get_emp():
    return jsonify(employees), 200


if __name__ == '__main__':
    app.run(debug=True)

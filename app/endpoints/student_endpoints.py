from flask import Blueprint, request, jsonify
from app.services.student_service import create_student, get_student, update_student, delete_student, get_all_students

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('', methods=['POST'])
def create():
    data = request.get_json()
    name = data.get('name')
    contact_info = data.get('contact_info')
    student = create_student(name, contact_info)
    return jsonify(student.to_dict()), 201

@student_bp.route('/<student_id>', methods=['GET'])
def get(student_id):
    student = get_student(student_id)
    if student:
        return jsonify(student.to_dict())
    return jsonify({'error': 'Student not found'}), 404

@student_bp.route('/', methods=['GET'])
def get_all():
    students = get_all_students()  # This returns a list of student dictionaries
    if students:
        return jsonify(students)  # Return list of student data
    return jsonify({'error': 'No students found'}), 404

@student_bp.route('/<student_id>', methods=['PUT'])
def update(student_id):
    data = request.get_json()
    name = data.get('name')
    contact_info = data.get('contact_info')
    student = update_student(student_id, name, contact_info)
    if student:
        return jsonify(student.to_dict())
    return jsonify({'error': 'Student not found'}), 404

@student_bp.route('/<student_id>', methods=['DELETE'])
def delete(student_id):
    result = delete_student(student_id)
    if result:
        return jsonify({'message': 'Student deleted'})
    return jsonify({'error': 'Student not found'}), 404

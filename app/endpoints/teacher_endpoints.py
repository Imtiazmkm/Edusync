from flask import Blueprint, request, jsonify
from app.services.teacher_service import create_teacher, get_teacher, update_teacher, delete_teacher

teacher_bp = Blueprint('teacher_bp', __name__)

@teacher_bp.route('', methods=['POST'])
def create():
    data = request.get_json()
    name = data.get('name')
    contact_info = data.get('contact_info')
    specializations = data.get('specializations')
    teacher = create_teacher(name, contact_info, specializations)
    return jsonify(teacher.to_dict()), 201

@teacher_bp.route('/<teacher_id>', methods=['GET'])
def get(teacher_id):
    teacher = get_teacher(teacher_id)
    if teacher:
        return jsonify(teacher.to_dict())
    return jsonify({'error': 'Teacher not found'}), 404

@teacher_bp.route('/<teacher_id>', methods=['PUT'])
def update(teacher_id):
    data = request.get_json()
    name = data.get('name')
    contact_info = data.get('contact_info')
    specializations = data.get('specializations')
    teacher = update_teacher(teacher_id, name, contact_info, specializations)
    if teacher:
        return jsonify(teacher.to_dict())
    return jsonify({'error': 'Teacher not found'}), 404

@teacher_bp.route('/<teacher_id>', methods=['DELETE'])
def delete(teacher_id):
    result = delete_teacher(teacher_id)
    if result:
        return jsonify({'message': 'Teacher deleted'})
    return jsonify({'error': 'Teacher not found'}), 404

import http

from flask import Blueprint, Response, request, jsonify
from marshmallow import ValidationError

from database import db
from models.pupil import PupilHomeTask
from serializers.pupil import PupilSchema

pupil_router = Blueprint('pupil', __name__, url_prefix='/pupil')


@pupil_router.route('')
def get():
    pupil_schema = PupilSchema()

    pupils = PupilHomeTask.query.order_by(PupilHomeTask.email)
    pupils_json = pupil_schema.dump(pupils, many=True)
    return jsonify(pupils_json)


@pupil_router.route('/<int:id_>')
def retrieve(id_):
    pupil_schema = PupilSchema()
    
    pupil = PupilHomeTask.query.filter_by(id=id_).first()
    pupils_json = pupil_schema.dump(pupil)
    return jsonify(pupils_json)


@pupil_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)

    schema = PupilSchema()
    try:
        pupil_data = schema.load(data)
        new_pupil = PupilHomeTask(
            email=pupil_data['email'],
            name=pupil_data['name'],
            last_name=pupil_data['last_name'],
            home_tasks=pupil_data['home_tasks'])
        db.session.add(new_pupil)
        db.session.commit()

        new_pupil_json = schema.dump(new_pupil)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_pupil_json


@pupil_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    schema = PupilSchema()
    try:
        pupil_data = schema.load(data)
        pupil = PupilHomeTask.query.filter_by(id=id_).first()
        pupil.email = pupil_data['email']
        pupil.name = pupil_data['name']
        pupil.last_name = pupil_data['last_name']
        pupil.home_tasks = pupil_data['home_tasks']
        db.session.add(pupil)
        db.session.commit()

        new_pupil_json = schema.dump(pupil)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_pupil_json


@pupil_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    PupilHomeTask.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT

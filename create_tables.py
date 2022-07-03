from main import db
from models.pupil import PupilHomeTask

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    db.session.add(PupilHomeTask(email="andrii@gmail.com"))
    db.session.commit()
    print("created tables")

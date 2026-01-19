from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

class SubjectTable:
    def __init__(self, db_url: str):
        """Подключение к базе данных"""
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def add_subject(self, title: str, description: str):
        session = self.Session()
        new_subject = Subject(title=title, description=description)
        session.add(new_subject)
        session.commit()
        subject_id = new_subject.id
        session.close()
        return subject_id

    def get_subject_by_id(self, subject_id: int):
        session = self.Session()
        subject = session.query(Subject).filter_by(id=subject_id).first()
        session.close()
        if subject:
            return {"id": subject.id, "title": subject.title, "description": subject.description}
        return None

    def update_subject(self, subject_id: int, new_title: str, new_description: str):
        session = self.Session()
        subject = session.query(Subject).filter_by(id=subject_id).first()
        if subject:
            subject.title = new_title
            subject.description = new_description
            session.commit()
            updated = True
        else:
            updated = False
        session.close()
        return updated

    def delete_subject(self, subject_id: int):
        session = self.Session()
        subject = session.query(Subject).filter_by(id=subject_id).first()
        if subject:
            session.delete(subject)
            session.commit()
            deleted = True
        else:
            deleted = False
        session.close()
        return deleted

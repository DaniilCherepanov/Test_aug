import pytest
from subject_table import SubjectTable, Subject
import logging

logging.basicConfig(level=logging.INFO)

DB_URL = "postgresql://postgres:12345@localhost:5432/mydb"

@pytest.fixture(scope="module")
def subjects():
    table = SubjectTable(DB_URL)
    yield table
    try:
        with table.Session() as session:
            session.query(Subject).delete()
            session.commit()
            logging.info("Данные успешно очищены после тестов")
    except Exception as e:
        logging.error(f"Ошибка при очистке данных: {str(e)}")

def test_add_subject(subjects):
    logging.info("Запуск теста добавления предмета")
    subject_id = subjects.add_subject("Математика", "Описание для теста")
    assert subject_id is not None
    subject = subjects.get_subject_by_id(subject_id)
    assert subject["title"] == "Математика"

def test_update_subject(subjects):
    logging.info("Запуск теста обновления предмета")
    subject_id = subjects.add_subject("Физика", "До обновления")
    updated = subjects.update_subject(subject_id, "Физика", "После обновления")
    assert updated is True
    subject = subjects.get_subject_by_id(subject_id)
    assert subject["description"] == "После обновления"

def test_delete_subject(subjects):
    logging.info("Запуск теста удаления предмета")
    subject_id = subjects.add_subject("История", "На удаление")
    deleted = subjects.delete_subject(subject_id)
    assert deleted is True
    subject = subjects.get_subject_by_id(subject_id)
    assert subject is None

def test_update_invalid_id(subjects):
    logging.info("Запуск теста обновления несуществующего ID")
    result = subjects.update_subject(9999, "Test", "Invalid ID")
    assert result is False

def test_delete_invalid_id(subjects):
    logging.info("Запуск теста удаления несуществующего ID")
    result = subjects.delete_subject(9999)
    assert result is False

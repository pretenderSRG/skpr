import pytest
from unittest.mock import MagicMock

from dao.model.user import User
from dao.user import UserDAO
from service.user import UserService


@pytest.fixture()
def user_dao():
    user_dao = UserDAO(None)

    john = User(id=1, username='John', password=123, role='user')
    kate = User(id=2, username='Kate', password=123, role='user')
    leo = User(id=3, username='Leo', password=123, role='user')

    user_dao.get_one = MagicMock(return_value=john)
    user_dao.get_all = MagicMock(return_value=[john, kate, leo])
    user_dao.create = MagicMock(return_value=User(id=1, username='John', password=123, role='user'))
    user_dao.delete = MagicMock()
    user_dao.update = MagicMock()
    user_dao.get_by_username = MagicMock(return_value=john)

    return user_dao


class TestUserService:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.user_service = UserService(dao=user_dao)

    def test_get_one(self):
        user = self.user_service.get_one(1)

        assert user is not None
        assert user.id is not None
        assert user.username is not None
        assert user.password is not None
        assert user.role is not None

    def test_get_all(self):
        users = self.user_service.get_all()

        assert len(users) > 0

    def test_create(self):
        user_data = {
            "username": "Ivan",
            "password": 000,
            "role": "user"
        }

        user = self.user_service.create(user_data)

        assert user.id is not None

    def test_delete(self):
        self.user_service.delete(1)

    def test_get_by_username(self):
        user = self.user_service.get_by_username("John")

        assert user is not None
        assert user.username == "John"

    def test_update(self):
        user_data = {
            "username": "Ivan",
            "password": 000,
            "role": "user"
        }

        user = self.user_service.update(user_data)

        assert user is not None




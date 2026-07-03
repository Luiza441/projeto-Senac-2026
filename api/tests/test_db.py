from sqlalchemy import select

from viajei_api.models import User

from dataclasses import asdict


def test_create_user(session):
    new_user = User("Luiza@test.test", "senha123")

    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.email == "joao@test.test"))

    breakpoint()

    assert user.email == "Luiza@test.test"

    assert asdict(user) == {
        "id": 1,
        "password": "senha123",
        "email": "Luiza@test.test",
        "created_at": time,
    }
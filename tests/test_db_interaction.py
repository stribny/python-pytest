from python_pytest.db_interaction import User, save_user


def test_user_can_be_saved(session):
    # given
    user_id = 1
    user_email = "example@example.com"
    user = User(id=user_id, email=user_email)

    # when
    save_user(session, user)

    # then
    saved_user = session.query(User).filter(User.id == user_id).first()
    assert saved_user.email == user_email
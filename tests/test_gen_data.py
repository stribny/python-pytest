from faker import Faker
from python_pytest import gen_data


fake = Faker()


def test_is_color_accepts_valid_color_codes():
    # given
    color_code = fake.color()

    # when
    result = gen_data.is_color(color_code)

    # then
    assert result == True
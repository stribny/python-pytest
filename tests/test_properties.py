import pytest
from hypothesis import given, assume
from hypothesis.strategies import integers, text, datetimes, from_regex, builds, composite
from python_pytest.properties import is_first_name, is_before_datetime, Person


@given(integers(1, 100))
def test_person_can_grow_older(age):
    # given
    person = Person(age=age)

    # when
    person.grow_older()

    # then
    person.age == age + 1


@given(builds(Person, age=integers(1, 100)))
def test_person_can_grow_older_2(person):
    current_age = person.age
    person.grow_older()
    person.age == current_age + 1


@given(builds(Person, age=integers(min_value=101)))
def test_person_cannot_grow_older(person):
    with pytest.raises(ValueError):
        person.grow_older()


@composite
def first_names(draw):
    allowed_first_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    lower_letters_strategy = from_regex(regex=r"^[a-z]$", fullmatch=True)
    first_letter = draw(text(alphabet=allowed_first_letters, min_size=1, max_size=1))
    rest = draw(text(alphabet=lower_letters_strategy, min_size=2, max_size=10))
    return first_letter + rest


@given(first_names())
def test_is_first_name(first_name):
    assert is_first_name(first_name)


@composite
def from_to_datetimes(draw):
    from_datetime = draw(datetimes())
    to_datetime = draw(datetimes())
    assume(from_datetime < to_datetime)
    return (from_datetime, to_datetime)


@given(from_to_datetimes())
def test_is_before_datetime(datetimes):
    assert is_before_datetime(datetimes[0], datetimes[1])



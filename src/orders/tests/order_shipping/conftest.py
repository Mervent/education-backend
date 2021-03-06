import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def user(mixer):
    return mixer.blend('users.User', first_name='Kamaz', last_name='Otkhodov')


@pytest.fixture(autouse=True)
def ship(mocker):
    return mocker.patch('shipping.factory.ship')


@pytest.fixture
def record(mixer):
    return mixer.blend('courses.Record', course__name_genitive='курсов катанья и мытья')


@pytest.fixture
def order(mixer, record, user):
    order = mixer.blend('orders.Order', user=user, price=1500)
    order.set_item(record)

    return order

import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def ship(mocker):
    return mocker.patch('shipping.shipments.RecordShipment.ship')


def test_record(record, ship, user):
    record.ship(to=user)

    ship.assert_called_once()

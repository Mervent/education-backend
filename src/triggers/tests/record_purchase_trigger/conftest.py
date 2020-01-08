from datetime import datetime

import pytest

from triggers.record_purchase import RecordPurchaseTrigger

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def order(order, record):
    order.set_item(record)
    order.setattr_and_save('paid', datetime(2032, 12, 1, 15, 13))

    return order


@pytest.fixture
def trigger(order):
    return RecordPurchaseTrigger(order)

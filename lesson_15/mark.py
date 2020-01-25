from functools import partial

import allure
import pytest

# severity
blocker = partial(allure.severity, allure.severity_level.BLOCKER)
critical = partial(allure.severity, allure.severity_level.CRITICAL)
normal = partial(allure.severity, allure.severity_level.NORMAL)
minor = partial(allure.severity, allure.severity_level.MINOR)

# tags
catalog = pytest.mark.catalog
cart = pytest.mark.cart
admin = pytest.mark.admin
product = pytest.mark.product

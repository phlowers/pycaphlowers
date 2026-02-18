# Copyright (c) 2026, RTE (http://www.rte-france.com)
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# SPDX-License-Identifier: MPL-2.0

import logging
from importlib.metadata import version

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

__version__ = version('Pycaphlowers')

logger.info("Pycaphlowers package initialized.")
logger.info(f"Pycaphlowers version: {__version__}")

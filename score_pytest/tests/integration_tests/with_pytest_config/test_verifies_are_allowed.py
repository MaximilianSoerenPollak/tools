# *******************************************************************************
# Copyright (c) 2026 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0
#
# SPDX-License-Identifier: Apache-2.0
# *******************************************************************************
import pytest
from attribute_plugin import add_test_properties

SCORE_MARKERS = [
    "test_properties(dict): Add custom properties to test XML output",
    "metadata",
]


def test_score_markers_are_registered(pytestconfig: pytest.Config):
    markers = pytestconfig.getini("markers")
    for marker in SCORE_MARKERS:
        assert marker in markers


# With '--strict-markers' (see BUILD) this fails at collection time
# if the score markers are not registered.
@add_test_properties(
    fully_verifies=["TREQ_ID_2"],
    partially_verifies=["TREQ_ID_1"],
    test_type="interface-test",
    derivation_technique="design-analysis",
)
@pytest.mark.metadata
def test_fully_and_paritall_verifies_allowed():
    """Both partial & fully verifies are allowed"""


# Test that only fully is allowed
@add_test_properties(
    fully_verifies=["TREQ_ID_2"],
    test_type="interface-test",
    derivation_technique="design-analysis",
)
@pytest.mark.metadata
def test_fully_verifies_allowed():
    """Fully verifies only is allowed"""


# Test that only partially is allowed
@add_test_properties(
    partially_verifies=["TREQ_ID_1"],
    test_type="interface-test",
    derivation_technique="design-analysis",
)
@pytest.mark.metadata
def test_partially_verifies_allowed():
    """Partially verifies only is allowed"""

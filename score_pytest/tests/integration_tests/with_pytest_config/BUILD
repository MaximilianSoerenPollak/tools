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

load("@score_tools//score_pytest:pytest.bzl", "score_pytest")

# The consumer brings its own config, which replaces the default pytest.ini
# shipped with score_pytest (and with it, the markers defined there).
score_pytest(
    name = "test_with_pytest_config",
    srcs = ["test_markers_with_pytest_config.py"],
    pytest_config = "pyproject.toml",
)

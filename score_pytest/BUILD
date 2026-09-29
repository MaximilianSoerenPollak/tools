# *******************************************************************************
# Copyright (c) 2025 Contributors to the Eclipse Foundation
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

load("@aspect_rules_py//py:defs.bzl", "py_library")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("//score_pytest:pytest.bzl", "score_pytest")

exports_files([
    "pytest.ini",
    "py_pytest.bzl",
    "requirements_py314.txt",
    "requirements_py312.txt",
])

score_pytest(
    name = "test_rules_are_working_correctly",
    srcs = glob(
        [
            "tests/*.py",
        ],
        allow_empty = True,
    ),
)

py_library(
    name = "attribute_plugin",
    srcs = ["attribute_plugin.py"],
    imports = ["."],
    visibility = ["//visibility:public"],
)

compile_pip_requirements(
    name = "requirements",
    srcs = [
        "requirements.in",
    ],
    requirements_txt = "requirements_py312.txt",
    tags = [
        "manual",
    ],
)


compile_pip_requirements(
    name = "requirements_py314",
    # Keep the Python version selector in pip-compile's generated header so
    # developers regenerate this lock with its matching toolchain.
    env = {
        "CUSTOM_COMPILE_COMMAND": "bazel run --@rules_python//python/config_settings:python_version=3.14 //score_pytest:requirements_py314.update",
    },
    srcs = [
        "requirements.in",
    ],
    requirements_txt = "requirements_py314.txt",
    tags = [
        "manual",
    ],
)



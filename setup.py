#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
    "requests>=2.31.0",
    "langchain==0.0.232",
    "llama-hub==0.0.10",
    "llama-index==0.7.8",
    "uvicorn==0.23.0",
    "fastapi==0.100.0",
]

test_requirements = []

setup(
    author="AIM by DPhi",
    author_email="support@aiplanet.com",
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="An end to end LLM framework",
    entry_points={
        "console_scripts": [
            "llmstack=llm_stack.cli:main",
            "llm-stack=llm_stack.cli:main",
            "llmstk=llm_stack.cli:main",
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="llm_stack",
    name="llm_stack",
    packages=find_packages(include=["llm_stack", "llm_stack.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/aiplanethub/llmstack",
    version="0.1.0",
    zip_safe=False,
)

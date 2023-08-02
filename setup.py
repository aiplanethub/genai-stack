#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="AIM by DPhi",
    author_email='support@aiplanet.com',
    python_requires='>=3.8',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    description="An end to end LLM framework",
    entry_points={
        'console_scripts': [
            'llaim=llaim.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='llaim',
    name='llaim',
    packages=find_packages(include=['llaim', 'llaim.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/dphi-official/llaim',
    version='0.1.0',
    zip_safe=False,
)

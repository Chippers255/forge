#!/usr/bin/env python
"""cookiecutter distutils configuration."""
from setuptools import setup

version = "0.1.0"

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirements = [
    "Jinja2<3.0.0",
]

setup(
    name='forge',
    version=version,
    description=(
        'A command-line tool to create prebuilt data science repositories from a template.'
    ),
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Tom Nelson',
    author_email='tn90ca@gmail.com',
    url='https://github.com/Chippers255/forge',
    packages=['forge'],
    package_dir={'forge': 'forge'},
    entry_points={'console_scripts': ['forge = forge.__main__:main']},
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=requirements,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
)
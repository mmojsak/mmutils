# coding: utf-8
from setuptools import setup

setup(
    name="mmutils",
    version="1.0",
    description="A set of functions commonly used in my scripts.",
    keywords="utilities",
    url="https://github.com/mmojsak/mmutils",
    author="Mateusz Mojsak",
    author_email="",
    classifiers=[
        "Environment :: Console",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
    py_modules=[
        "mmutils",
    ],
    entry_points={
        "console_scripts": [
            "mmutils = mmutils:main",
        ],
    },
    install_requires=[
        "numpy>=1.12.0",
        "pickle>=3.0.0"
    ]
)

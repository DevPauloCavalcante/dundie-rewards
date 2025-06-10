from turtle import setup

from setuptools import find_packages


def read_requirements(file_path):
    """Read requirements from a file and return a list of packages."""
    return [
        line.strip()
          for line in open(file_path).split("\n")
          if not line.startswith("#","git+",'"','-')
    ]

setup(
    name="dundie",
    version="0.1.0",
    description="Reward Point System for Dunder Mifflin Employees",
    author="Paulo Cavalcante",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dundie = dundie.__main__:main",
        ],
    },
    install_requires=read_requirements("requirements.txt"),
    extras_requires={
        "test": read_requirements("requirements-test.txt"),
        "dev": [
            "ipdb",
            "pudb",
            "ipython"        
        ]

    }
)
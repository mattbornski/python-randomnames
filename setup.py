from setuptools import setup, find_packages
import os

import randomnames.version

setup(
    name='python-randomnames',
    version=".".join(map(str, randomnames.version.VERSION)),
    packages = find_packages(),

    author = 'Concentric Sky',
    author_email = 'django@concentricsky.com',
    description = 'Generate random adjective/noun pairs',
    license = 'Apache2'
)

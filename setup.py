import os
from setuptools import setup
from os.path import dirname, realpath

scripts = []
# for path in ['rapid_ocean/scripts/ologs']:
#     if os.path.exists(os.path.join(os.path.dirname(__file__), path)):
#         scripts.append(path)

setup(
    name='pycfr',
    packages=['pycfr'],
    install_requires=[],
    scripts=scripts,
    dependency_links=[],
)

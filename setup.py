from io import open
from setuptools import setup

"""
:authors: Kvas Andrey, Belkova Ksenia, Nekrasova Anna
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2023 kvasik3000
"""

version = '0.1'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open("requirements.txt", "r") as file:
    requirements = file.read().splitlines()

setup(
    name='Droplet-Detector',
    version=version,

    author='Kvas Andrey, Belkova Ksenia, Nekrasova Anna',
    author_email='superadrenoline3000@gmail.com',

    description='Telegram bot that draws the outlines of drips on a photo ',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/kvasik3000/Droplet-Detector',

    license='Apache License, Version 2.0, see LICENSE file',

    packages=['Droplet-Detector'],
    install_requires=requirements,

    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires='==3.9.*',
)

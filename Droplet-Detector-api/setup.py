from io import open
from setuptools import setup

"""
:authors: Kvas Andrey, Belkova Ksenia, Nekrasova Anna
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2021 Peopl3s
"""

version = '0.0.1'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open("requirements.txt", "r") as file:
    requirements = file.read().splitlines()

setup(
    name='Droplet-Detector-api',
    version=version,

    author='Kvas Andrey, Belkova Ksenia, Nekrasova Anna',
    author_email='a.kvas@g.nsu.ru, k.belkova@g.nsu.ru, a.nekrasova@g.nsu.ru',

    description='Telegram bot that draws the outlines of drips on a photo ',
    long_description=long_description,
    # long_description_content_type='text/markdown',

    url='https://github.com/Peopl3s/club_house_api',
    download_url='https://github.com/Peopl3s/club-house-api/archive/main.zip'

    license='Apache License, Version 2.0, see LICENSE file',

    packages=['club_house_api'],
    install_requires=['aiohttp', 'aiofiles'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
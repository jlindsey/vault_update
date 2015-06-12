from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vault_update',
    version='1.0.0',
    description='Update entries in Vault instead of overwriting',
    long_description=long_description,
    url='https://github.com/jlindsey/vault_update',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    keywords='vault util cli',
    packages=['vault_update'],
    entry_points={
        'console_scripts': [
            'vault_update=vault_update.cli:main'
        ]
    },
)

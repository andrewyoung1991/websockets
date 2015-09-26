import os
import sys

import setuptools
from websockets.version import version


# Avoid polluting the .tar.gz with ._* files under Mac OS X
os.putenv('COPYFILE_DISABLE', 'true')

root = os.path.dirname(os.path.abspath(__file__))

# Prevent distutils from complaining that a standard file wasn't found
README = os.path.join(root, 'README')
if not os.path.exists(README):
    os.symlink(README + '.rst', README)

with open(README, encoding='utf-8') as f:
    long_description = '\n\n'.join(f.read().split('\n\n')[1:])

py_version = sys.version_info[:2]

if py_version < (3, 3):
    raise Exception("websockets requires Python >= 3.3.")

setuptools.setup(
    name='websockets',
    version=version,
    author='Aymeric Augustin',
    author_email='aymeric.augustin@m4x.org',
    url='https://github.com/aaugustin/websockets',
    description="An implementation of the WebSocket Protocol (RFC 6455)",
    long_description=long_description,
    download_url='https://pypi.python.org/pypi/websockets',
    packages=[
        'websockets',
        ],
    extras_require={
        ':python_version=="3.3"': ['asyncio'],
        },
    tests_require={
        },
    entry_points={
        'console_scripts': [
            'run-example-server=example.server:main',
            'run-example-client=example.client:main',
            ]
        },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        ],
    platforms='all',
    license='BSD'
)

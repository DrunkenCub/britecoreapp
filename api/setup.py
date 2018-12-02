"""Setup module of the package."""
import uuid

__author__ = 'Chathuranga Bandara <contact@chathuranga.com>'
from setuptools import setup, find_packages
from pip.req import parse_requirements


INSTALL_REQS = parse_requirements('requirements.txt', session=uuid.uuid1())
REQS = [str(ir.req) for ir in INSTALL_REQS]

setup(
    name="api",
    version="0.0.1",
    packages=find_packages(),
    author="Chathuranga Bandara",
    author_email="contact@chathuranga.com",
    description="API for britecore",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="",
    include_package_data=True,
    install_requires=REQS
)
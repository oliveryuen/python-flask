from setuptools import setup, find_packages
from os import path

CURR_DIR = path.abspath(path.dirname(__file__))
with open(path.join(CURR_DIR, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

INSTALL_DEPENDENCIES = [
    'dynaconf',
    'flask',
    'flask-restplus',
    'healthcheck'
]

TEST_DEPENDENCIES = [
    'pytest'
]

setup(
    name='myflaskapp',
    version='0.0.1',
    description='A sample Python Flask project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/oliveryuen/python-flask',
    author='Oliver Yuen',
    install_requires=INSTALL_DEPENDENCIES,
    tests_require=TEST_DEPENDENCIES,
    test_suite='tests',
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        # How mature is this project?
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'License :: Apache',
        'Operating System :: OS Independent'
    ]
)

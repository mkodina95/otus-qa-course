from setuptools import setup, find_packages

setup(
    name='otus-qa-course',
    version='0.1',
    url='https://github.com/mkodina95/otus-qa-course',
    license='MIT',
    author='Marina Kodina',
    author_email='marusya-k95@yandex.ru',
    description='Otus-qa-course tests',
    packages=find_packages(exclude=['tests']),
    setup_requires=[
        'allure-pytest==2.8.6',
        'pytest==4.6.0',
        'requests==2.20.0',
        'selenium==3.141.0',
        'PyMySQL==0.9.3'
    ],
    zip_safe=False)

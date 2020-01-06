from setuptools import setup

setup(
    name='fakeemail',
    version='0.10.1',
    author='Tom Wardill',
    author_email='tom@howrandom.net',
    description='A fake Email Server with a Web Front End',
    url='https://github.com/tomwardill/FakeEmail',
    zip_safe=True,
    packages=['fakeemail', 'twisted.plugins'],
    install_requires=[
        'Twisted',
        'jinja2',
        'zope.interface',
    ],
    package_data={
        'twisted': ['plugins/fakeemail.py'],
        'fakeemail': ['templates/*']
        },
    entry_points={
        'console_scripts': [
            'fakeemail=fakeemail.server:start'
        ]
    }
)

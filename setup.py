from setuptools import setup

setup(
    name='cron_parser',
    packages=['cron_parser'],
    entry_points = {
        'console_scripts': ['cron_parser=cron_parser.cli:main'],
    },
)

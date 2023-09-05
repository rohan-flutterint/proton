from setuptools import setup, find_packages
from setuptools.command.install_scripts import install_scripts
import subprocess
import os

setup(
    name='proton_smoke_test',
    version='0.1',
    author='timeplus',
    description='Smoke Test for Proton',
    # packages=find_packages(),
    package_dir={
        'ci_runner': '',
        'helpers': 'helpers'
    },
    package_data={'': ['*.json', '*.yml', '*.env', '*.sh']},
    data_files=[
        ('deps', ['dep/clickhouse-driver-0.2.4.tar'])
    ],
    install_requires=['pytest==6.2.5', 'requests>=2.26.0', 'pyOpenSSL==23.0.0', 'pytest-cases==3.6.5', 'unidiff==0.7.0',
                      'docker-compose==1.29.2', 'boto3==1.20.4', 'urllib3==1.26.7', 'pytest-html==3.1.1',
                      'psycopg2-binary==2.9.3', 'kafka-python==2.0.2', 'timeplus==1.1.2', 'sseclient-py>=1.7.2',
                      'clickhouse-driver'],
    dependency_links=[os.path.join(os.getcwd(), 'deps', 'clickhouse-driver-0.2.4.tar')],
    entry_points={
        'console_scripts': [
            'proton_smoke_test = ci_runner.ci_runner:main'
        ]
    },
)

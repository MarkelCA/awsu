from setuptools import setup, find_packages

setup(
    name='awsu',
    version='0.1',
    description='AWS Utilities.',
    author='Markel Cuesta',
    author_email='cuestaarribas.markel@proton.me',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'awsu=aws_utils.__main__:main',  # Points to the main function in `__main__.py`
        ],
    },
)


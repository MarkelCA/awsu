from setuptools import setup, find_packages

setup(
    name='awsu',
    version='0.1',
    description='AWS Utilities. An extensible aws wrapper built for custom features.',
    author='Markel Cuesta',
    author_email='cuestaarribas.markel@proton.me',
    packages=find_packages(),
    install_requires=[
        'argcomplete',  
    ],
    entry_points={
        'console_scripts': [
            'awsu=aws_utils.__main__:main',  # Points to the main function in `__main__.py`
        ],
    },
)


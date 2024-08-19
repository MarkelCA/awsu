from setuptools import setup, find_packages

setup(
    name='awsu',
    version='0.1',
    description='AWS Utilities. An extensible aws wrapper built for custom features.',
    author='Markel Cuesta',
    author_email='cuestaarribas.markel@proton.me',
    packages=find_packages(),
    install_requires=[
        'argcomplete==3.5.0',  
        'PyYAML==6.0.2',
        'boto3==1.34.161'
    ],
    entry_points={
        'console_scripts': [
            'awsu=aws_utils.main:main',
        ],
    },
)

print("To enable autocompletion run this after the installation has been completed. You can add this line to your .bashrc or .bash_profile to enable autocompletion permanently:\neval \"$(register-python-argcomplete awsu)\"")

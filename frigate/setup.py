from setuptools import setup, find_packages

setup(
    name="frigate",
    version="0.0.1",
    description="Start Shipping Your Tensorflow Models! Turn your ML projects into a useable no-code demo and scalable and monetizable API. All faster than you can write a README.",
    author="Armaan Goel",
    author_email="armaangoel78@gmail.com",
    url="https://github.com/armaangoel78/Frigate-AI",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'frigate=cli.main:main'
        ]
    },
    install_requires=[
        'boto3',
        'aws_cdk.core',
        'aws_cdk.aws_s3',
        'docopt',
        'rich'
    ],
)
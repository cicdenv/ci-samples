from setuptools import setup, find_packages

setup(
    name='sample',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points='''
        [console_scripts]
        sample=main:main
    ''',
)

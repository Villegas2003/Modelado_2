from setuptools import setup, find_packages

setup(
    name='calistenia_simulacion',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'tkinter'
    ],
    entry_points={
        'console_scripts': [
            'calistenia_simulacion=src.main:main'
        ]
    }
)
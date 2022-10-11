from setuptools import setup, find_packages

setup(
    name='Space Attack',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pygame==2.1.2'
    ],
    entry_points={
        'console_scripts': ['space-attack=run_game']
    }
)

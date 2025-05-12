from setuptools import setup, find_packages

setup(
    name="botscan",
    version="1.0.0",
    description="Linter e formatação para automações RPA em Python",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Ruan Chaves Machado",
    author_email="whiterun092@gmail.com",
    url="https://github.com/usuario/botscan",
    packages=find_packages(),
    install_requires=[
        "pylint",
        "black",
    ],
    entry_points={
        'console_scripts': [
            'botscan-cli=botscan.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

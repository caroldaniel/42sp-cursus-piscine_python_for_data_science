from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="cado-car",
    author_email="cado-car@student.42sp.org.br",
    url="https://github.com/caroldaniel/42sp-cursus-piscine_python_for_data_science/tree/main/python-0-starting/ex09",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

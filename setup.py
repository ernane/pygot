import setuptools


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pygot",
    version="0.1.0",
    author="Ernane Sena",
    author_email="ernane.sena@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ernane/pygot",
    packages=setuptools.find_packages(exclude="tests"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    extras_require={"dev": read("requirements-dev.txt")},
    tests_require=["pytest", "pytest-cov"],
    setup_requires=["pytest-runner"],
)

import setuptools
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(current_directory, "README.md"), "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pal",
    version="0.0.1",
    author="Assured Information Security, Inc",
    author_email="wrightj@ainfosec.com",
    description="Generate C/C++ register access intrinsics for ARMv8-A",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bareflank/pal",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

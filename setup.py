from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ozzy_image_processing",
    version="0.0.2",
    author="Ozzy Azevedo",
    author_email="ozzysp@icloud.com",
    description="Package to process images using Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ozzysp/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
    ],
)

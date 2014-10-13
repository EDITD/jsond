import setuptools


REQUIREMENTS = [
    "nose==1.3.0",
    "python-dateutil==1.5",
]


if __name__ == "__main__":
    setuptools.setup(
        name="jsond",
        version="0.0.1",
        author="EDITD",
        author_email="engineering@editd.com",
        packages=setuptools.find_packages(),
        scripts=[],
        url="https://github.com/EDITD/jsond",
        license="LICENSE.txt",
        description="JSON (with dates)",
        long_description="View the github page (https://github.com/EDITD/jsond) for more details.",
        install_requires=REQUIREMENTS
    )

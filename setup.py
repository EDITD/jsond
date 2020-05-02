import setuptools
import sys


REQUIREMENTS = [
    "python-dateutil>=2.0.0,<3.0.0",
    "six>=1.10.0,<2",
]

DEV_REQUIREMENTS = [
    "nose>=1.3,<1.4",
]


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "requirements":
        for req in REQUIREMENTS:
            print(req)
        sys.exit(0)

    setuptools.setup(
        name="jsond",
        version="1.3.0.1",
        author="EDITD",
        author_email="engineering@editd.com",
        packages=setuptools.find_packages(),
        scripts=[],
        url="https://github.com/EDITD/jsond",
        license="LICENSE.txt",
        description="JSON (with dates)",
        long_description="View the github page (https://github.com/EDITD/jsond) for more details.",
        install_requires=REQUIREMENTS,
        extras_require={
            "dev": DEV_REQUIREMENTS,
        }

    )

import setuptools


# How do we keep this in sync with requirements.pip?
#
REQUIREMENTS = [
    "nose==1.3.0",
    "python-dateutil==1.5",
]


if __name__ == "__main__":
    setuptools.setup(
        name="jsond",
        version="0.0.1",
        author="Sujay Mansingh",
        author_email="sujay.mansingh@gmail.com",
        packages=setuptools.find_packages(),
        scripts=[],
        url="https://github.com/sujaymansingh/jsond",
        license="LICENSE.txt",
        description="JSON (with dates)",
        long_description="View the github page (https://github.com/sujaymansingh/jsond) for more details.",
        install_requires=REQUIREMENTS
    )

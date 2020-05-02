import re
import setuptools
import sys


REQUIREMENTS = [
    "python-dateutil>=2.0.0,<3.0.0",
    "six>=1.10.0,<2",
]

DEV_REQUIREMENTS = [
    "nose>=1.3,<1.4",
]


def get_version():
    # Regex matching version pattern
    version_pattern = re.compile(r"(?P<version>\d+(\.\d+){1,3}([.-][\w-]+)?)")
    changelog_file = "CHANGELOG.md"

    with open(changelog_file, "r") as changelog:
        for changelog_line in changelog:
            version = version_pattern.search(changelog_line)
            if version is not None:
                return "".join(version.group("version"))
        raise RuntimeError("Couldn't find a valid version in {}".format(changelog_file))


def get_long_description():
    with open('README.md') as f:
        return f.read()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "requirements":
        for req in REQUIREMENTS:
            print(req)
        sys.exit(0)

    setuptools.setup(
        name="jsond",
        version=get_version(),
        author="EDITED devs",
        author_email="dev@edited.com",
        packages=setuptools.find_packages(),
        scripts=[],
        url="https://github.com/EDITD/jsond",
        license="MIT",
        license_file="LICENSE.txt",
        description="JSON (with dates)",
        long_description=get_long_description(),
        long_description_content_type="text/markdown",
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Development Status :: 5 - Production/Stable",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
        install_requires=REQUIREMENTS,
        extras_require={
            "dev": DEV_REQUIREMENTS,
        }

    )

from pathlib import Path

from setuptools import setup


def read(name):
    return open(Path(Path(__file__).parent, name)).read()


setup(
    name="gdbm-viewer",
    version="0.0.0",
    packages=["gdbm_viewer"],
    install_requires=["pyinotify"],
    entry_points={
        "console_scripts": [
            "gdbm-viewer = gdbm_viewer.__main__:main",
        ],
    },
    description="Live gdbm database viewer",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/jcrd/gdbm-viewer",
    license="MIT",
    author="James Reed",
    author_email="james@twiddlingbits.net",
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
)

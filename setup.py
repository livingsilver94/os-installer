from setuptools import find_packages, setup

setup(
    name="os-installer",
    version="16.0",
    author="Solus",
    author_email="copyright@getsol.us",
    description=("Operating System Installer"),
    license="GPL-2.0-or-later",
    url="https://github.com/getsolus/os-installer",
    packages=find_packages(),
    scripts=["os-installer-gtk"],
    classifiers=["License :: OSI Approved :: GPL-2.0 License"],
    package_data={"os_installer2": ["data/*.png", "data/*.svg", "data/*.css"]},
)

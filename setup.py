from setuptools import setup, find_packages

setup(
    name="guid-rename",
    version="0.1",
    packages=find_packages(),
    install_requires=["click"],
    entry_points={"console_scripts": {"guid_rename = guid_rename.__main__:run"}},
)

from setuptools import find_packages, setup

setup(
    name="guid-rename",
    version="0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["click"],
    entry_points={"console_scripts": {"guid-rename = guid_rename.__main__:run"}},
)

from setuptools import setup, find_packages

setup(
    name="quicksight-backup-tool",
    version="0.1.0",
    description="A tool for backing up AWS QuickSight assets",
    author="marvelmaniac",
    author_email="marvelmaniac@wearehackerone.com",
    packages=find_packages(),
    install_requires=[
        "requests>=0.0.1"
    ],
    entry_points={
        "console_scripts": [
            "quicksight-backup=quicksight_backup.cli:main",
        ],
    },
    python_requires=">=3.8",
)

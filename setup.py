import os
import setuptools

# Safeguard against missing README.md
try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "A small Python package for ML app."

__version__ = "0.0.0"

REPO_NAME = "ml-end-end-proj"
AUTHOR_USER_NAME = "Mat-Project"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "mathan21092006@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for ML app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)

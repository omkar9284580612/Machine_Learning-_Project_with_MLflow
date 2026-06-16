import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1"

REPO_NAME = "Machine_Learning_Project_with-_MLflow"
AUTHOR_USER_NAME = "omkar"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "kaleomkar992@gmail.com"


setuptools.setup(
    name='mlProject',
    version=__version__,
    author='omkar',
    author_email='kaleomkar992@gmail.com',
    description="A small python package for ml app",
    long_description="A small python package for ml app",
    long_description_content="text/markdown",
    url=f"https://github.com/omkar9284580612/Machine_Learning-_Project_with_MLflow.git",
    project_urls={
        "Bug Tracker": f"https://github.com/omkar9284580612/Machine_Learning-_Project_with_MLflow.git/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()


__version__="0.0.0"
REPO_NAME="Text-Summarization-End-to-End"
Author_USER_NAME="Fasil Hameed"
SRC_REPO ="textSummarizer"
Author_Email="faisalhameed763@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=Author_USER_NAME,
    author_email=Author_Email,
    description="Python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{Author_USER_NAME}/{REPO_NAME}",
    project_urls={
        "bug Tracker":f"https://github.com/{Author_USER_NAME}/{REPO_NAME}",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)
import setuptools
  
with open("README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="scsmote-package",
    version="0.0.2",
    author="Hetul Mehta",
    author_email="hetulmehta08@gmail.com",
    packages=["scsmote_package"],
    description="A SMOTE variant called sematic-cosine SMOTE that generates textual synthetic data ",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/hetulmehta/SC-SMOTE.git",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)
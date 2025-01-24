from setuptools import setup, find_packages

setup(
    name="uzumseller",
    version="1.0.0",
    description="Python SDK of seller.uzum.uz API Gateway",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Sayfulla Mirkhalikov",
    author_email="mirxoliqov.sayfulla@gmail.com",
    url="https://github.com/thesayfulla/uzumseller-sdk",
    keywords="uzumseller, uzum, api, sdk",
    packages=find_packages(),
    install_requires=[
        "requests>=2.26.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
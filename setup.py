import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scrapeShivam",
    version="2.0.0",
    author="Shivam Vishwakarma",
    author_email="sv6375261073@gmail.com",
    description="Scrapping altnews|Google images|Instagram|facebook|Twitter|Tradingview chartImage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sv6375261073/scrapperSV",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["requests",
			"beautifulsoup4==4.9.2",
			"imageio==2.9.0",
			"lxml==4.5.2",
			"matplotlib",
			"numpy",
			"pandas",
			"Pillow==8.2.0",
			"selenium==3.141.0"]
)

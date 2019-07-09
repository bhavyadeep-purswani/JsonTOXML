import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="JsonToXML",
    version="0.0.1",
    author="Bhavyadeep Purswani",
    license = 'LICENCE.txt',
    author_email="bhavyadeep.purswani98@gmail.com",
    description="A Library to convert JSON into XML format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bhavyadeep-purswani/JsonTOXML",
    packages=setuptools.find_packages(),
    install_requires=[
        'xml.etree.cElementTree',
        'json',
        'xml.dom.minidom',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
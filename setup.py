import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylotus", # Replace with your own username
    version="1.0.0",
    author="Alex Claman",
    author_email="alexanderclaman@gmail.com",
    description="A simple Python wrapper for the WarFrame API",
    install_requires=['requests'],
    keywords='API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alex-claman/pylotus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    project_urls={
        'Bug Reports': 'https://github.com/alex-claman/pylotus/issues',
        'Source': 'https://github.com/alex-claman/pylotus/'
    },
)
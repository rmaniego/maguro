import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name = 'maguro',
    packages = ["maguro"],
    version = '0.0.2',
    license='MIT',
    description = 'Maguro is a lightweight python package that simplifies the management of C/TSV data and files.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Rodney Maniego Jr.',
    author_email = 'rod.maniego23@gmail.com',
    url = 'https://github.com/rmaniego/maguro',
    download_url = 'https://github.com/rmaniego/maguro/archive/v1.0.tar.gz',
    keywords = ['CSV', 'TSV', 'File', 'Storage'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers', 
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6'
)
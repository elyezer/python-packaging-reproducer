"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

with open('LICENSE', encoding='utf-8') as file:
    license = file.read()

with open('README.rst', encoding='utf-8') as file:
    long_description = file.read()

with open('VERSION', encoding='utf-8') as file:
    version = file.read().strip()

setup(
    name='sampleproject',  # Required
    version=version,
    description='A sample Python project',  # Optional
    license=license,
    long_description=long_description,  # Optional
    url='https://github.com/pypa/sampleproject',  # Optional
    author='The Python Packaging Authority',  # Optional
    author_email='pypa-dev@googlegroups.com',  # Optional

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(),  # Required
    install_requires=['requests'],  # Optional

    entry_points="""
        [console_scripts]
        sample=sample:main
    """,
)

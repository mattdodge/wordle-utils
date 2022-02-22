import re
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

with open('wordle/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)


setuptools.setup(
    name="wordle-utils",
    version=version,
    author="Matt Dodge",
    author_email="wordle@mattdodge.codes",
    description="Helper functions, word lists, and analysis tools for Wordle and other Wordle variants.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=reqs,
    url="https://github.com/mattdodge/wordle-utils",
    packages=setuptools.find_packages(),
    setup_requires=['setuptools_scm'],
    include_package_data=True,
    entry_points='''
        [console_scripts]
        solve_wordle=wordle.play:solve
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

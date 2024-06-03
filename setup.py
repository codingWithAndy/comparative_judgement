from setuptools import setup, find_packages

# setup(
#     name='comparative_judgement',
#     version='0.0.1',
#     packages=find_packages(),
#     install_requires=[
#         'numpy',
#         'scipy',
#         'matplotlib',
#         'ray',
#     ],
#     author='Andy Gray',
#     description='A package for conducting Comparative Judgement',
#     long_description=open('README.md').read(),
#     long_description_content_type='text/markdown',
# )

VERSION = "0.0.1"  # PEP-440

NAME = "comparative_judgement"

INSTALL_REQUIRES = [
    "pandas",
    "numpy",
    "ray",
    "scipy",
]


setup(
    name=NAME,
    version=VERSION,
    description="A package for conducting Comparative Judgement",
    url="https://github.com/codingWithAndy/comparative_judgement",
    project_urls={
        "Source Code": "https://github.com/codingWithAndy/comparative_judgement",
    },
    author="Andy Gray",
    author_email="",
    license="",
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ],
    # Snowpark requires Python 3.8
    python_requires=">=3.8",
    # Requirements
    install_requires=INSTALL_REQUIRES,
    packages=["comparative_judgement"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)

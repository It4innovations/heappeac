from setuptools import setup, find_packages


with open("requirements.txt") as reqs:
    requirements = [line for line in reqs.read().split("\n") if line]


setup(name="heappeac",
      version="4.0",
      description="HEAppE API Python client",
      long_description="",
      url="",
      author="IT4I",
      author_email="support.heappe@it4i.cz",
      license="MIT",
      packages=find_packages(),
      install_requires=requirements)

from setuptools import setup, find_packages


with open("requirements.txt") as reqs:
    requirements = [line for line in reqs.read().split("\n") if line]


setup(name="heappeac",
      version="0.1",
      description="HEAppE API Python client",
      long_description="",
      url="",
      author="Vojtech Cima",
      author_email="cima.vojtech@gmail.com",
      license="MIT",
      packages=find_packages(),
      install_requires=requirements)

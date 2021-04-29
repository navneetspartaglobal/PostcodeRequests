from setuptools import setup

setup(name="app",
      authors="Lewis Twelftree, Navneet Pandey, David Childs",
      description="Package to retrieve information linked to a postcode",
      install_requires=[
          "requests",
          "json",
          "pprint"])
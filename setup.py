from setuptools import setup

setup(
   name='kyber',
   version='1.0',
   description='A useful module',
   author='kyberman',
   author_email='kyber@mail.com',
   packages=['kyber'],  #same as name
   install_requires=['pycryptodome'], #external packages as dependencies
)
from setuptools import setup

setup(name='factbook',
      version='0.1',
      description='python package for interacting with the CIA World Factbook',
      url='http://github.com/rabbitsfeat/factbook',
      author='rabbitsfeat',
      author_email='rsabb24@gmail.com',
      license='MIT',
      packages=['factbook'],
      include_package_data=True,
      install_requires=[
          'requests',
      ],
      zip_safe=False)

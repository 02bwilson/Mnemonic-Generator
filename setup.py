from setuptools import setup, find_packages


setup(
    name='Mnemonic Generator',
    version='1.0',
    license='cc-by-4.0',
    author="Bryce Wilson",
    packages=find_packages(''),
    package_dir='',
    url='https://github.com/02bwilson/Mnemonic-Generator',
    keywords='Mnemonic Generator, Mnemonic Phrase, Timings',
    install_requires=[
          'json',
          'random',
      ],

)
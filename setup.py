from setuptools import setup, find_packages


def readfile(name):
    with open(name) as f:
        return f.read()


README = readfile('README.md')
CHANGES = readfile('CHANGES.txt')

install_requires = [
    'pyramid',
    'pymongo',
    'pyramid_mongodb_debugtoolbar'
]

testing_extras = [
    'WebTest',
    'nose',
    'coverage',
]

setup(name='pyramid_mongodb',
      version='1.0',
      description='An improved package that provides mongodb connectivity. Not compatible with pyramid_mongo',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP :: WSGI",
          "License :: MIT",
      ],
      keywords='wsgi pylons pyramid mongodb pymongo pyramid_mongo_debugtoolbar',
      author="Jonathan Mackenzie",
      author_email="pylons-discuss@googlegroups.com",
      url="https://github.com/jonnoftw/pyramid_mongodb",
      license="MIT",
      packages=find_packages('pyramid_mongodb', exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require={
          'testing': testing_extras,
      },
      test_suite="tests",
      )

from setuptools import setup, find_packages
import jfu

setup(
    name='django-dprog-%s' % jfu.__prog__,
    version=jfu.__version__,
    author=jfu.__author__,
    author_email="alem@cidola.com",
    maintainer='Philippe Docourt',
    description=jfu.__desc__,
    license=jfu.__licence__,
    keywords="django, jquery file upload, multi-upload",
    url="http://packages.python.org/jfu",
    packages=find_packages(),
    include_package_data=True,
    long_description=open('README.rst').read(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: %s" % jfu.__licence__,
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

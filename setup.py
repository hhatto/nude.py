try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import nude


setup(name='nudepy',
      version=nude.__version__,
      description="Nudity detection with Python. Port of nude.js to Python.",
      long_description=open('README.rst').read(),
      author='Hideo Hattori',
      author_email='hhatto.jp@gmail.com',
      url='https://github.com/hhatto/nude.py',
      license='MIT',
      platforms='Linux',
      packages=['nude'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3'],
      keywords="nude",
      zip_safe=False,
      )

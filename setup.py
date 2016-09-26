try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from Cython.Build import cythonize


setup(name='nudepy',
      version='0.3',
      description="Nudity detection with Python. Port of nude.js to Python.",
      long_description=open('README.rst').read(),
      author='Hideo Hattori',
      author_email='hhatto.jp@gmail.com',
      url='https://github.com/hhatto/nude.py',
      license='MIT',
      platforms='Linux',
      py_modules=['nude'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3'],
      keywords="nude",
      zip_safe=False,
      install_requires=['pillow', 'Cython'],
      entry_points={'console_scripts': ['nudepy = nude:main']},
      ext_modules=cythonize("skin_classifier.pyx"),
      )

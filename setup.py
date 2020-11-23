try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension
try:
    from Cython.Distutils import build_ext
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

if USE_CYTHON:
    ext = '.pyx'
    cmdclass = {'build_ext': build_ext}
else:
    ext = '.c'
    cmdclass = {}

ext_modules = [Extension(
    'skin_classifier',
    sources=['skin_classifier' + ext]
)]

setup(name='nudepy',
      version='0.5.1',
      description="Nudity detection with Python. Port of nude.js to Python.",
      long_description=open('README.rst').read(),
      author='Hideo Hattori',
      author_email='hhatto.jp@gmail.com',
      url='https://github.com/hhatto/nude.py',
      license='MIT',
      platforms='Linux',
      py_modules=['nude'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3'],
      keywords="nude",
      zip_safe=False,
      install_requires=['pillow'],
      entry_points={'console_scripts': ['nudepy = nude:main']},
      ext_modules=ext_modules,
      cmdclass=cmdclass,
      )

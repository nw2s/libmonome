from distutils.extension import Extension
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize([Extension("monome", ["monome.pyx"], libraries=["monome"])])
)

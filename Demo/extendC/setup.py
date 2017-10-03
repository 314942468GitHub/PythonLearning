from distutils.core import setup, Extension
MOD = 'cal'
setup(name=MOD, ext_modules=[Extension(MOD, sources=['cal.c'])])
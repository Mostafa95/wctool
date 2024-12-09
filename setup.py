from setuptools import setup

setup(
  name='FileStats',
  version='1.0.0',
  py_modules=['main','utils'],
  python_requires=">=3.6",
  install_requires=['setuptools'],
  entry_points={
    'console_scripts': [
      'ccwc=main:main'
    ]
  }
)
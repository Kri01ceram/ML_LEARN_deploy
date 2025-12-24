from setuptools import setup, find_packages

setup(
    name='ml_project',
    version='0.0.1',
    author='krish',
    author_email='0.krishna1120@gmail.com',
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'scikit-learn', 'flask','seaborn'],
)
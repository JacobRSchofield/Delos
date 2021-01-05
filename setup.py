from setuptools import setup, find_packages
from delos import __version__

setup(
    name='Delos',
    description='Delos AI',
    author='Jacob Schofield',
    version=str(__version__),
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.npy', '*.json', '*.h5', '*.pth', '*.pkl', '*.tar', '*.dat', '*.csv']
    },
    install_requires=[
        'numpy',
        'setuptools-git',
        'torch',
        'scipy',
        'dask',
        'distributed',
        'bokeh',
        'pathlib',
        'torchvision',
        'opencv-python',
        'scikit-image',
        'joblib',
        'scikit-learn',
        'msgpack',
        'numba',
    ],
    entry_points={
        'console_scripts': [],
    }
)

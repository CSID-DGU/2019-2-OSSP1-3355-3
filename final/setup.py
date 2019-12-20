from setuptools import setup, find_packages


setup(
    name='pytorch-stacked-hourglass',
    version='1.0.0a5',
    maintainer='Aiden Nibali',
    url='https://github.com/anibali/pytorch-stacked-hourglass',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'importlib_resources',
        'Pillow',
        'scipy',
        'tabulate',
        'torch',
    ],
    classifiers=[
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ]
)

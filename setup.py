from distutils.core import setup
setup(
    name='mpysa',
    packages=['mpysa'],
    version='0.1',
    description='mPesa API Python library.',
    author='Jimmy Kamau',
    author_email='jimmykambiz@gmail.com',
    url='https://github.com/jimmykamau/mpysa',
    download_url='https://github.com/jimmykamau/mpysa/tarball/0.1',
    keywords=['mpysa', 'python', 'python_mpesa'],
    classifiers=[],
    package_dir={'mpysa': 'lib'},
    license='MIT License',
    install_requires=[
        'requests',
    ],
)

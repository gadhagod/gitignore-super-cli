import setuptools

setuptools.setup(
    name='gitignore-super-cli',
    version='0.0',
    author='Aarav Borthakur',
    author_email='gadhaguy13@gmail.com',
    description='Create gitignore templates from your command line',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gadhagod/gitignore-cli',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'click',
        'requests'
    ],
    scripts=['./ignore'],
    python_requires='>=3.6'
)
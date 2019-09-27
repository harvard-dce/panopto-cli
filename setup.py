from setuptools import setup

install_requires = [
    "Click",
    "requests",
    "zeep"
]

setup(
    name="panopto-cli",
    version="0.7.1",
    py_modules=['panopto'],
    install_requires=install_requires,
    license='Apache 2.0',
    author='Jay Luker',
    author_email='jay_luker@harvard.edu',
    url='https://github.com/harvard-dce/panopto-cli',
    entry_points='''
        [console_scripts]
        panopto=panopto:cli 
    ''',
)

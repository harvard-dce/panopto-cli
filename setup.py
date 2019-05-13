from setuptools import setup

install_requires = [
    "Click",
    "requests",
    "zeep"
]

setup(
    name="panopto-cli",
    version="0.4.0",
    py_modules=['panopto'],
    install_requires=install_requires,
    licence='Apache 2.0',
    author='Jay Luker',
    url='https://github.com/harvard-dce/panopto-cli',
    entry_points='''
        [console_scripts]
        panopto=panopto:cli 
    ''',
)

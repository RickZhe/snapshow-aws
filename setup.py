from setuptools import setup

setup(
    name='snapshow',
    version='0.1',
    author="Rick Zheng",
    author_email="rick.zheng@gmail.com",
    description="snapshow snaps aws instances",
    license="GPLv3+",
    packages=['snapshow'],
    url="https://github.com/RickZhe/snapshow-aws",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_script]
        snapshow=shapshow.snapshow:cli
    ''',

)
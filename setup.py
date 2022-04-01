import setuptools
import sys, io

with open("README.md", "r", encoding="utf-8", errors="ignore") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nonebot-plugin-fire",
    version="1.0.2",
    author="moyusoldier",
    author_email="1433221642@qq.com",
    keywords=("pip", "nonebot2", "nonebot", "fire", "nonebot_plugin"),
    description="""nonebot2 plugin fire""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/25252www/nonebot_plugin_fire",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    platforms="any",
    install_requires=[
        'nonebot-plugin-apscheduler>=0.1.2',
        'nonebot2>=2.0.0-beta.2',
        'nonebot-adapter-onebot>=2.0.0b1'
    ]
)

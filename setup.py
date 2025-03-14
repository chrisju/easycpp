from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="easycpp",  # 模块的名称
    version="1.0.0",  # 版本号
    packages=find_packages(),  # 自动查找目录中的包
    description="Enjoyably using embedded C++ code or dynamic libraries",  # 简介
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Chris Ju",  # 作者信息
    author_email="zhuzhu101011@gmail.com",  # 邮箱
    url="http://blog2.moez.win/",  # 项目主页（可选）
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # 或其他许可证
    ],
    python_requires=">=3.6",  # Python 版本要求
)


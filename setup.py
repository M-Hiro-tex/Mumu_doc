from setuptools import setup, find_packages

setup(
    name='Project_dir',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # 依存するパッケージをここに指定
        'numpy',
        'vispy',
    ],
)

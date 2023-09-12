from setuptools import setup, find_packages

setup(
    name         = 'ePlot',
    version      = "0.0.1",
    description  = "A handy tool to ease the use of matplotlib",
    author       = "Yongchao He",
    author_email = "Yongchao-He@outlook.com",
    url          = "https://github.com/yongchaoHe/ePlot.git",

    packages     = find_packages(),

    python_requires='>=3.9',
    install_requires=['Cython>=0.29', 'numpy>=1.20', 'matplotlib>=3.3.4']
)

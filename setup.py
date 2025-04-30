from setuptools import setup, find_packages

setup(
    name="ipex_to_cuda",
    version="0.1.0",
    packages=find_packages(include=['.', 'ipex_to_cuda']),
    py_modules=["attention", "diffusers", "gradscaler", "hijacks"],
    description="Adapt IPEX to CUDA",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="wltechblog",
    url="https://github.com/wltechblog/ipex_to_cuda",
    install_requires=[
        "torch>=2.0.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
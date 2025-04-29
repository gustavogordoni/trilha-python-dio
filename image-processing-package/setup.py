from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
    
with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    

setup(
    name="image_processing_tools",
    version="0.0.1",
    author="gustavo_gordoni",
    author_email="gustavogordoni1@gmail.com",
    description="Pacote de processamento de imagens com funções de visualização, resize e histogramas",
    long_description=page_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
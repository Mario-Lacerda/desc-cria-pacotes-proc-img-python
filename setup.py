from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing",
    version="0.0.1",
    author="Jonatas de Siqueira bitencourt Cursino",
    author_email="jonatas.d.siqueira@gmail.com",
    description="Imagem usada pra desafio DIO.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jonny23Parker/processamento_Imagem_python.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
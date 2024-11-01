from setuptools import setup, find_packages

setup(
    name="openai-openapi",
    version="0.1.0",
    description="OpenAPI specification and API exploration engine for OpenAI API",
    author="Your Name",
    author_email="you@example.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "pyyaml==5.4.1",
        "requests==2.25.1",
        "flask==1.1.2",
        "flask-cors==3.0.10",
        "flask-restful==0.3.8",
        "flask-swagger-ui==3.36.0"
    ],
    include_package_data=True,
)

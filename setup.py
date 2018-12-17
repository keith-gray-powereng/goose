from setuptools import setup

requirements = []
test_requirements = []


setup(
    name="goose",
    version="0.1.0",
    description="Tools for creating GOOSE messages for use in testing",
    author="Keith Gray",
    author_email="keith.gray@powereng.com",
    url="https://github.com/keith-gray-powereng/goose",
    packages=["goose"],
    package_dir={"goose": "goose"},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    test_suite="tests",
    tests_require=test_requirements,
)

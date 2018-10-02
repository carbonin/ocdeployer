from setuptools import setup

setup(
    name="ocdeployer",
    use_scm_version=True,
    description="A tool which wraps the OpenShift command line tools to enable repeatable automated deployment of OpenShift templates",
    license="MIT",
    author="Brandon Squizzato",
    author_email="bsquizza@redhat.com",
    url="https://www.github.com/bsquizz/ocdeployer",
    packages=["ocdeployer"],
    keywords=["openshift", "kubernetes"],
    setup_requires=["setuptools_scm"],
    include_package_data=True,
    install_requires=["sh", "prompter", "pyyaml"],
    scripts=["scripts/ocdeployer"],
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires=">=3.4",
)
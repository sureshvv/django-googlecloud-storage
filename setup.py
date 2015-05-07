from setuptools import setup, find_packages

setup(
    name='django_google_cloud_storage',
    version='0.0.1',
    packages=find_packages(),
    #package_data={"": "*"},
    include_package_data=True,
    zip_safe=False,
    description= ".",
    long_description=open('README.md').read(),
    author="Christos Kopanos",
    author_email="ckopanos@redmob.gr",
    install_requires=['GoogleAppEngineCloudStorageClient==1.9.15.0']
)

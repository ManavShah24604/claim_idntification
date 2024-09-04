from setuptools import setup, find_packages

setup(
    name='claim_identification',           
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],            # Add dependencies here or use requirements.txt
    author='Manav',
    description='Identifies Claims from Text',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['google-generativeai','pandas','sklearn'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

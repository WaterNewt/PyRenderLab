from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='pyrenderlab',
        version='1.0.0',
        author='Yunus Ruzmetov',
        author_email='waternewtinfo@gmail.com',
        description='A simple 3D engine written in Python.',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=[
            'pygame',
            'numpy',
        ],
        python_requires='>=3.9.6',
    )
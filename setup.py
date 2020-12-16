from setuptools import setup

setup(
    name='xadmin-config',
    version='1.0',
    packages=['xplugin_config'],
    url='https://github.com/alexsilva/xadmin-config',
    license='MIT',
    author='alex',
    author_email='alex@fabricadigital.com.br',
    description='Xadmin plugin that allows to view component configurations.',
    include_package_data=True,
    classifiers=[
        'Framework :: Django :: 2',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7'
    ]
)

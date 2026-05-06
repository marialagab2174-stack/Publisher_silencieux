from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'publisher_silencieux'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Maria Lagab',
    description='Challenge Débogage : Correction du Publisher Silencieux',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'status_node = publisher_silencieux.publisher_node:main'
        ],
    },
)

from setuptools import setup

package_name = 'atturtle_vision'
scripts_locn = 'scripts'

setup(
    name=package_name,
    version='0.0.0',
    packages=[scripts_locn],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='acbuynak',
    maintainer_email='acbuynak@gmail.com',
    description='Vison Support for Camera',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'atturtle_vision = atturtle_vision.atturtle_vision:main'
        ],
    },
)

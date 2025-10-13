from setuptools import setup

package_name = 'random_threshold'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # 🔽 EZ a sor hiányzik nálad, ez másolja át a launch fájlt
        ('share/' + package_name + '/launch', ['launch/launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='balint',
    maintainer_email='balint@example.com',
    description='Random number publisher and threshold subscriber demo',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'random_publisher = random_threshold.random_publisher:main',
            'threshold_subscriber = random_threshold.threshold_subscriber:main',
        ],
    },
)

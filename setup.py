import platform
from setuptools import setup
from setuptools import find_packages
from setuptools import Extension


extra_compile_args = [
    '-std=c++11',
    '-O3',
    '-Wall',
    '-fno-strict-aliasing',
    '-fno-rtti',
]

if platform.system() == 'Darwin':
    extra_compile_args += ['-mmacosx-version-min=10.7', '-stdlib=libc++']


setup(
    name="python-rocksdb",
    version='0.7.0',
    description="Python bindings for RocksDB",
    keywords='rocksdb',
    author='Ming Hsuan Tu',
    author_email="qrnnis2623891@gmail.com",
    url="https://github.com/twmht/python-rocksdb",
    license='BSD License',
    setup_requires=['setuptools>=25', 'Cython>=0.20'],
    install_requires=['setuptools>=25'],
    package_dir={'rocksdb': 'rocksdb'},
    packages=find_packages('.'),
    ext_modules=[Extension(
        'rocksdb._rocksdb',
        ['rocksdb/_rocksdb.pyx'],
        include_dirs=[
            'C:/Program Files/rocksdb/include',
            'C:/Program Files/rocksdb/build/rocksdb-shared.dir/Release',
            'C:/Program Files/rocksdb/build/Release'
        ],
        extra_compile_args=extra_compile_args,
        language='c++',
        libraries=['rocksdb', 'Shlwapi', 'Rpcrt4'],
        library_dirs=[
            'C:/Program Files/rocksdb/build/Release'
        ]
    )],
    extras_require={
        "doc": ['sphinx_rtd_theme', 'sphinx'],
        "test": ['pytest'],
    },
    include_package_data=True,
    zip_safe=False,
)

from distutils.core import setup

setup(
    name="dosy",
    py_modules=["dosy"],
    entry_points={"console_scripts": ["dosy=dosy:main"]},
    version="0.2.3",
    description="DOS attack - Slow down Connection",
    author="Network Slutter and Gokberk Yaltirakli",
    author_email="netslutter@pm.me",
    url="https://github.com/netslutter/dosy",
    keywords=["dos", "http", "dosy"],
    license="MIT",
)

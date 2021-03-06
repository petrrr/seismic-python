import setuptools

def configure():
# Initialize the setup kwargs
    kwargs = {"name": "seismic-python",
            "version": "1.0a0",
            "author": "Malcolm White",
            "author_email": "malcolcw@usc.edu",
            "maintainer": "Malcolm White",
            "maintainer_email": "malcolcw@usc.edu",
            "url": "http://malcolmw.github.io/seismic-python",
            "description": "Seismic data analysis tools",
            "download_url": "https://github.com/malcolmw/seismic-python.git",
            "platforms": ["linux", "osx"],
            "requires": ["obspy", "sqlite3"],
            "packages": ["seispy"],
            "py_modules": ["seispy.constants",
                           "seispy.coords",
                           "seispy.faults",
                           "seispy.fmm3dio",
                           "seispy.geogrid",
                           "seispy.geometry",
                           "seispy.mapping",
                           "seispy.sqlschemas",
                           "seispy.surface",
                           "seispy.topography",
                           "seispy.ttgrid",
                           "seispy.velocity"]}
    return(kwargs)

if __name__ == "__main__":
    kwargs = configure()
    setuptools.setup(**kwargs)

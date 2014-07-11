
================
Package Metadata
================

- **author:** Eric Hendricks

- **author-email:** eric.hendricks@nasa.gov

- **classifier**:: 

    Intended Audience :: Science/Research
    Topic :: Scientific/Engineering

- **description-file:** README.txt

- **entry_points**:: 

    [openmdao.component]
    hsrnoise_wrapper.hsrnoise.HSRNOISE=hsrnoise_wrapper.hsrnoise:HSRNOISE
    [openmdao.container]
    hsrnoise_wrapper.geometry.Geometry=hsrnoise_wrapper.geometry:Geometry
    hsrnoise_wrapper.hsrnoise.HSRNOISE=hsrnoise_wrapper.hsrnoise:HSRNOISE
    hsrnoise_wrapper.MEflows.MEflows=hsrnoise_wrapper.MEflows:MEflows
    hsrnoise_wrapper.stream.Stream=hsrnoise_wrapper.stream:Stream

- **home-page:** https://github.com/OpenMDAO-Plugins/hsrnoise_wrapper

- **keywords:** openmdao

- **license:** Apache License, Version 2.0

- **maintainer:** Kenneth Moore

- **maintainer-email:** kenneth.t.moore-1@nasa.gov

- **name:** hsrnoise_wrapper

- **requires-dist:** openmdao.main

- **requires-python**:: 

    >=2.6
    <3.0

- **static_path:** [ '_static' ]

- **summary:** OpenMDAO component wrapper for HSR_Noise

- **version:** 0.2.1


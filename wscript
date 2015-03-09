def options(opt):
    opt.load('compiler_cxx')

def configure(conf):
    conf.load('compiler_cxx')

    if conf.env.CXX_NAME == 'msvc':
        conf.env.append_value('CXXFLAGS', ['/EHsc'])

    if conf.env.CXX_NAME == 'gcc':
        conf.env.append_value('CXXFLAGS', ['-std=c++11'])
        conf.env.append_value('LINKFLAGS', ['-pthread'])

def build(bld):
    bld.stlib(source=GTEST_SOURCE,
              includes=GTEST_INCLUDE,
              target='gtest')

GTEST_SOURCE = [
    'src/gtest-all.cc'
]

GTEST_INCLUDE = [
    './',
    'include/',
]

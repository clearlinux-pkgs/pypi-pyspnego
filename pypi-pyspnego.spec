#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-pyspnego
Version  : 0.9.1
Release  : 27
URL      : https://files.pythonhosted.org/packages/fb/38/46174701e2a2de8b72e79c980324b034203edafff3c543a4134b2c1ae9af/pyspnego-0.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/fb/38/46174701e2a2de8b72e79c980324b034203edafff3c543a4134b2c1ae9af/pyspnego-0.9.1.tar.gz
Summary  : Windows Negotiate Authentication Client and Server
Group    : Development/Tools
License  : MIT
Requires: pypi-pyspnego-bin = %{version}-%{release}
Requires: pypi-pyspnego-license = %{version}-%{release}
Requires: pypi-pyspnego-python = %{version}-%{release}
Requires: pypi-pyspnego-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cython)
BuildRequires : pypi(setuptools)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Python SPNEGO Library
[![Test workflow](https://github.com/jborean93/pyspnego/actions/workflows/ci.yml/badge.svg)](https://github.com/jborean93/pyspnego/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/jborean93/pyspnego/branch/main/graph/badge.svg)](https://codecov.io/gh/jborean93/pyspnego)
[![PyPI version](https://badge.fury.io/py/pyspnego.svg)](https://badge.fury.io/py/pyspnego)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/jborean93/pyspnego/blob/master/LICENSE)

%package bin
Summary: bin components for the pypi-pyspnego package.
Group: Binaries
Requires: pypi-pyspnego-license = %{version}-%{release}

%description bin
bin components for the pypi-pyspnego package.


%package license
Summary: license components for the pypi-pyspnego package.
Group: Default

%description license
license components for the pypi-pyspnego package.


%package python
Summary: python components for the pypi-pyspnego package.
Group: Default
Requires: pypi-pyspnego-python3 = %{version}-%{release}

%description python
python components for the pypi-pyspnego package.


%package python3
Summary: python3 components for the pypi-pyspnego package.
Group: Default
Requires: python3-core
Provides: pypi(pyspnego)
Requires: pypi(cryptography)
Requires: pypi(krb5)

%description python3
python3 components for the pypi-pyspnego package.


%prep
%setup -q -n pyspnego-0.9.1
cd %{_builddir}/pyspnego-0.9.1
pushd ..
cp -a pyspnego-0.9.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686755001
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyspnego
cp %{_builddir}/pyspnego-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyspnego/2b1b1a0652626080334be38bf79eba5da489acee || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyspnego-parse

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyspnego/2b1b1a0652626080334be38bf79eba5da489acee

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

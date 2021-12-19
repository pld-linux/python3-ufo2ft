#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-ufo2ft.spec, here tests fail with fonttools 4)

Summary:	A bridge between UFOs and FontTools
Summary(pl.UTF-8):	Pomost między UFO a FontTools
Name:		python-ufo2ft
# keep 2.10.x for python2 support
Version:	2.10.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ufo2ft/
Source0:	https://files.pythonhosted.org/packages/source/u/ufo2ft/ufo2ft-%{version}.zip
# Source0-md5:	8678156f5bcb25374ab567f674086cf7
URL:		https://pypi.org/project/ufo2ft/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-booleanOperations >= 0.8.2
BuildRequires:	python-compreffor >= 0.4.6
BuildRequires:	python-cu2qu >= 1.6.5
BuildRequires:	python-enum34 >= 1.1.6
# fonttools[ufo]
BuildRequires:	python-fonttools >= 3.43.0
BuildRequires:	python-fs >= 2.2.0
BuildRequires:	python-pytest >= 2.8
BuildRequires:	python-skia-pathops >= 0.2.0
BuildRequires:	python-ufoLib2 >= 0.3.2.post2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-booleanOperations >= 0.8.2
BuildRequires:	python3-compreffor >= 0.4.6
BuildRequires:	python3-cu2qu >= 1.6.5
BuildRequires:	python3-fonttools >= 3.43.0
BuildRequires:	python3-fs >= 2.2.0
BuildRequires:	python3-pytest >= 2.8
BuildRequires:	python3-skia-pathops >= 0.2.0
BuildRequires:	python3-ufoLib2 >= 0.3.2.post2
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ufo2ft ("UFO to FontTools") is a fork of ufo2fdk whose goal is to
generate OpenType font binaries from UFOs without the FDK dependency.

%description -l pl.UTF-8
ufo2ft ("UFO to FontTools") to odgałęzienie projektu ufo2fdk. Celem
odgałęzienia jest generowanie z UFO binariów fontów OpenType bez
zależności od FDK.

%package -n python3-ufo2ft
Summary:	A bridge between UFOs and FontTools
Summary(pl.UTF-8):	Pomost między UFO a FontTools
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-ufo2ft
ufo2ft ("UFO to FontTools") is a fork of ufo2fdk whose goal is to
generate OpenType font binaries from UFOs without the FDK dependency.

%description -n python3-ufo2ft -l pl.UTF-8
ufo2ft ("UFO to FontTools") to odgałęzienie projektu ufo2fdk. Celem
odgałęzienia jest generowanie z UFO binariów fontów OpenType bez
zależności od FDK.

%prep
%setup -q -n ufo2ft-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/Lib \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/Lib \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/ufo2ft
%{py_sitescriptdir}/ufo2ft-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-ufo2ft
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/ufo2ft
%{py3_sitescriptdir}/ufo2ft-%{version}-py*.egg-info
%endif

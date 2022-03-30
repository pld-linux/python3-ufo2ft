#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	A bridge between UFOs and FontTools
Summary(pl.UTF-8):	Pomost między UFO a FontTools
Name:		python3-ufo2ft
Version:	2.25.1
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ufo2ft/
Source0:	https://files.pythonhosted.org/packages/source/u/ufo2ft/ufo2ft-%{version}.zip
# Source0-md5:	5df6eaf6c35247d3e0fbcdf7c68165f4
URL:		https://pypi.org/project/ufo2ft/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-booleanOperations >= 0.9.0
BuildRequires:	python3-cffsubr >= 0.2.8
BuildRequires:	python3-compreffor >= 0.4.6
BuildRequires:	python3-cu2qu >= 1.6.7
BuildRequires:	python3-fonttools >= 4.26.1
BuildRequires:	python3-fs >= 2.2.0
BuildRequires:	python3-pytest >= 2.8
BuildRequires:	python3-skia-pathops >= 0.5.1
BuildRequires:	python3-ufoLib2 >= 0.7.1
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ufo2ft ("UFO to FontTools") is a fork of ufo2fdk whose goal is to
generate OpenType font binaries from UFOs without the FDK dependency.

%description -l pl.UTF-8
ufo2ft ("UFO to FontTools") to odgałęzienie projektu ufo2fdk. Celem
odgałęzienia jest generowanie z UFO binariów fontów OpenType bez
zależności od FDK.

%prep
%setup -q -n ufo2ft-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/Lib \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/ufo2ft
%{py3_sitescriptdir}/ufo2ft-%{version}-py*.egg-info

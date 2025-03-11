#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Exclude specific directories from nosetests runs
Summary(pl.UTF-8):	Wykluczanie określonych katalogów z zakresu nosetests
Name:		python-nose_exclude
Version:	0.5.0
Release:	8
License:	LGPL
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/nose-exclude/
Source0:	https://files.pythonhosted.org/packages/source/n/nose-exclude/nose-exclude-%{version}.tar.gz
# Source0-md5:	072f72e782f28a9c42356976f8ec22d9
URL:		https://pypi.org/project/nose-exclude/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nose_exclude is a Nose plugin that allows you to easily specify
directories to be excluded from testing.

%description -l pl.UTF-8
nose_exclude to wtyczka Nose pozwalająca łatwo określać katalogi
do wykluczenia z testowania.

%package -n python3-nose_exclude
Summary:	Exclude specific directories from nosetests runs
Summary(pl.UTF-8):	Wykluczanie określonych katalogów z zakresu nosetests
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-nose_exclude
nose_exclude is a Nose plugin that allows you to easily specify
directories to be excluded from testing.

%description -n python3-nose_exclude -l pl.UTF-8
nose_exclude to wtyczka Nose pozwalająca łatwo określać katalogi
do wykluczenia z testowania.

%prep
%setup -q -n nose-exclude-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
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
%doc README.rst
%{py_sitescriptdir}/nose_exclude.py[co]
%{py_sitescriptdir}/nose_exclude-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-nose_exclude
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/nose_exclude.py
%{py3_sitescriptdir}/__pycache__/nose_exclude.cpython-*.py[co]
%{py3_sitescriptdir}/nose_exclude-%{version}-py*.egg-info
%endif

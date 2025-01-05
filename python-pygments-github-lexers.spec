Name:		python-pygments-github-lexers
Version:	0.0.5
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/p/pygments-github-lexers/pygments-github-lexers-%{version}.tar.gz
Summary:	Pygments Github custom lexers.
URL:		https://pypi.org/project/pygments-github-lexers/
License:	BSD
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Pygments Github custom lexers.

%prep
%autosetup -p1 -n pygments-github-lexers-%{version}

%files
%{py_sitedir}/pygments_github_lexers
%{py_sitedir}/pygments_github_lexers-*.*-info

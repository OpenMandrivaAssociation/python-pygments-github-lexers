# Created by pyp2rpm-3.3.5
%global pypi_name pygments-github-lexers

Name:           python-%{pypi_name}
Version:        0.0.5
Release:        1
Summary:        Pygments Github custom lexers
Group:          Development/Python
License:        BSD
URL:            https://github.com/liluo/pygments-github-lexers
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%{python3_sitelib}/pygments_github_lexers
%{python3_sitelib}/pygments_github_lexers-%{version}-py%{python3_version}.egg-info


# Created by pyp2rpm-3.1.3
%global pypi_name networking-bagpipe

Name:           python-%{pypi_name}
Version:        4.0.0
Release:        1%{?dist}
Summary:        Mechanism driver for Neutron ML2 plugin using BGP E-VPNs/IP VPNs as a backend

License:        UNKNOWN
URL:            http://www.openstack.org/
Source0:        https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildConflicts: python-oslosphinx = 3.4.0
BuildConflicts: python-sphinx = 1.2.0
BuildConflicts: python-sphinx = 1.3b1
BuildRequires:  python-coverage >= 3.6
BuildRequires:  python-discover
BuildRequires:  python-hacking < 0.11
BuildRequires:  python-hacking >= 0.10.0
BuildRequires:  python-oslosphinx >= 2.5.0
BuildRequires:  python-oslotest >= 1.10.0
BuildRequires:  python-pbr >= 1.8
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx < 1.3
BuildRequires:  python-sphinx >= 1.1.2
BuildRequires:  python-subunit >= 0.0.18
BuildRequires:  python-testrepository >= 0.0.18
BuildRequires:  python-testscenarios >= 0.4
BuildRequires:  python-testtools >= 1.4.0
BuildRequires:  python2-devel
BuildRequires:  python-sphinx

%description
 networkingbagpipe Driver and agent code to use bagpipebgp lightweight
implementation of BGPbased VPNs as a backend, for NeutronBGPVPN Interconnection
or Neutron ML2.* Free software: Apache license * Source: * Bugs: This package
includes:* a Neutron ML2 mechanism driver ('bagpipe') * compute node agent code
for:: * the bagpipe ML2 driver * the bagpipe driver of
networkingbgpvpn_BGPbased VPNs ...

%package -n     python2-%{pypi_name}
Summary:        Mechanism driver for Neutron ML2 plugin using BGP E-VPNs/IP VPNs as a backend
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-pbr >= 1.6
Requires:       python-Babel >= 2.3.4
Requires:       python-neutron-lib >= 0.1.0
Requires:       python-oslo-db >= 4.1.0
Requires:       python-oslo-config >= 3.9.0
Requires:       python-oslo-concurrency >= 3.5.0
Requires:       python-oslo-log >= 1.14.0
Requires:       python-oslo-messaging >= 4.5.0
Requires:       python-oslo-service >= 1.0.0
Requires:       python-setuptools
%description -n python2-%{pypi_name}
 networkingbagpipe Driver and agent code to use bagpipebgp lightweight
implementation of BGPbased VPNs as a backend, for NeutronBGPVPN Interconnection
or Neutron ML2.* Free software: Apache license * Source: * Bugs: This package
includes:* a Neutron ML2 mechanism driver ('bagpipe') * compute node agent code
for:: * the bagpipe ML2 driver * the bagpipe driver of
networkingbgpvpn_BGPbased VPNs ...

%package -n python-%{pypi_name}-doc
Summary:        networking-bagpipe documentation
%description -n python-%{pypi_name}-doc
Documentation for networking-bagpipe

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py2_install


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst doc/source/readme.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/networking_bagpipe-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Fri Sep 30 2016 Luke Hinds <lhinds@redhat.com> - 4.0.0-1
- Initial package.

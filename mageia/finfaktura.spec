%define bname	faktura.py

Name:		finfaktura
Version:	2.0.7
Release:	%mkrel 1
Summary:	Create, review and administer norwegian invoices
License:	GPLv2
Group:		Office/Finance
URL:		http://sourceforge.net/projects/finfaktura/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	desktop-file-utils
Requires:	PyQt4
Requires:	sqlite3-tools

%description
Create, review and administer invoices for use in Norway
and print on the F60 faktura form or send by email as PDF.

This program is unfortunately in Norwegian only


%prep
%setup -q

%build

%install
python setup.py install --prefix /usr --root %{buildroot}

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
install -m644 %{name}.png -D %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%{_bindir}/%{bname}
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-*.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}


%changelog
* Wed Aug 05 2015 Johnny A. Solbu <johnny@solbu.net> 2.0.7-1.solbu5
- Initial Mageia package

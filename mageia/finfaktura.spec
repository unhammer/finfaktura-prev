%define bname	faktura

Name:		finfaktura
Version:	2.1.0
Release:	%mkrel 1
Summary:	Create, review and administer norwegian invoices
License:	GPLv2
Group:		Office/Finance
URL:		http://sourceforge.net/projects/finfaktura/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	desktop-file-utils
Requires:	PyQt4
Requires:	python-reportlab
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
install -m644 %{bname}.1 -D %{buildroot}%{_mandir}/man1/%{bname}.1

%files
%doc AUTHORS ChangeLog README
%{_bindir}/%{bname}
%{_mandir}/man1/%{bname}.1*
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-*.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}


%changelog
* Sat Oct 24 2015 Johnny A. Solbu <johnny@solbu.net> 2.1.0-1.solbu5
- New version: 2.1.0

* Wed Oct 17 2015 Johnny A. Solbu <johnny@solbu.net> 2.0.10-1.solbu5
- New version: 2.0.10

* Mon Aug 17 2015 Johnny A. Solbu <johnny@solbu.net> 2.0.9-1.solbu5
- New version: 2.0.9

* Wed Aug 12 2015 Johnny A. Solbu <johnny@solbu.net> 2.0.8-1.solbu5
- New version: 2.0.8

* Wed Aug 05 2015 Johnny A. Solbu <johnny@solbu.net> 2.0.7-1.solbu5
- Initial Mageia package

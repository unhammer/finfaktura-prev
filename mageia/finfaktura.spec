%define bname	faktura

Name:		finfaktura
Version:	2.2.1
Release:	%mkrel 1
Summary:	Create, review and administer norwegian invoices
License:	GPLv2
Group:		Office/Finance
URL:		https://sourceforge.net/projects/finfaktura/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	desktop-file-utils
Requires:	PyQt4
Requires:	python-reportlab
Requires:	sqlite3-tools

%description
Create, review and administer invoices for use in Norway
and print on the F60 faktura form or send by email as PDF.


%prep
%setup -q

%build

%install
python setup.py install --prefix /usr --root %{buildroot}

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
install -m644 %{name}.png -D %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -m644 %{name}-icon.png -D %{buildroot}%{_datadir}/pixmaps/%{name}-icon.png
install -m644 %{bname}.1 -D %{buildroot}%{_mandir}/man1/%{bname}.1

%files
%doc AUTHORS ChangeLog README
%{_bindir}/%{bname}
%{_mandir}/man1/%{bname}.1*
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-*.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}*.png
%{_datadir}/%{name}
%license LICENSE


%changelog
* Mon Jun 18 2018 Johnny A. Solbu <johnny@solbu.net> 2.2.1-1.solbu5
- New version: 2.2.1

* Sun Feb 25 2018 Johnny A. Solbu <johnny@solbu.net> 2.2.0-1.solbu5
- New version: 2.2.0

* Wed Jun 07 2017 Johnny A. Solbu <johnny@solbu.net> 2.1.4-1.solbu5
- New version: 2.1.4

* Thu Nov 05 2015 Johnny A. Solbu <johnny@solbu.net> 2.1.2-1.solbu5
- New version: 2.1.2

* Sat Oct 31 2015 Johnny A. Solbu <johnny@solbu.net> 2.1.1-1.solbu5
- New version: 2.1.1

* Sat Oct 24 2015 Johnny A. Solbu <johnny@solbu.net> 2.1.0-1.solbu5
- New version: 2.1.0

* Sat Oct 17 2015 Johnny A. Solbu <johnny@solbu.net> 2.0.10-1.solbu5
- New version: 2.0.10

* Mon Aug 17 2015 Johnny A. Solbu <johnny@solbu.net> 2.0.9-1.solbu5
- New version: 2.0.9

* Wed Aug 12 2015 Johnny A. Solbu <johnny@solbu.net> 2.0.8-1.solbu5
- New version: 2.0.8

* Wed Aug 05 2015 Johnny A. Solbu <johnny@solbu.net> 2.0.7-1.solbu5
- Initial Mageia package

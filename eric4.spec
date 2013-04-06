Summary:	Eric4 - a full featured Python IDE
Summary(pl.UTF-8):	Eric4 - pełnowartościowe IDE dla Pythona
Name:		eric4
Version:	4.5.10
Release:	1
License:	GPL v3+
Group:		X11/Development/Tools
# http://downloads.sourceforge.net/project/eric-ide/eric4/stable/4.4.19/eric4-4.4.19.tar.gz
# Source0:	http://downloads.sourceforge.net/eric-ide/%{name}-%{version}.tar.gz
Source0:	http://downloads.sourceforge.net/eric-ide/%{name}-%{version}.tar.gz
# Source0-md5:	9fe7a1889b28619f9e51b10f19c81bd7
Source1:	%{name}.desktop
URL:		http://eric-ide.python-projects.org/
BuildRequires:	python-PyQt4-devel-tools
BuildRequires:	python-qscintilla2-devel >= 2.4.4-3
BuildRequires:	python-sip-devel >= 2:4.5.10
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-devel-tools
Requires:	python-modules-sqlite
Requires:	python-qscintilla2 >= 2.4.4-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eric4 is a full featured Python IDE that is written in PyQt4 using the
QScintilla editor widget.

%description -l pl.UTF-8
Eric4 jest pełnowartościowym IDE dla Pythona napisanym w PyQt4 i
używającym edytora QScintilla.

%package doc
Summary:	Documentation for Eric4
Summary(pl.UTF-8):	Dodatkowa dokumentacja dla Eric4
Group:		X11/Development/Tools
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for Eric4.

%description doc -l pl.UTF-8
Dodatkowa dokumentacja dla Eric4.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

python install.py -z -c -b %{_bindir} -d %{py_sitescriptdir} -i $RPM_BUILD_ROOT
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/eric4.desktop
install -D eric/pixmaps/eric.png $RPM_BUILD_ROOT%{_pixmapsdir}/eric4.png

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}/*
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}/*

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/LICENSE.GPL3

%clean
rm -rf $RPM_BUILD_ROOT

# NOTE: eric4 uses *.py files for it's own purposes
# so do not remove them from package
%files
%defattr(644,root,root,755)
%doc README* THANKS
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/eric4config.py*
%{py_sitescriptdir}/%{name}
%dir %{py_sitescriptdir}/%{name}plugins
%{py_sitescriptdir}/%{name}plugins/*
%exclude %{py_sitescriptdir}/%{name}/Documentation
%{_desktopdir}/eric4.desktop
%{_pixmapsdir}/eric4.png
%{_datadir}/qt4/qsci/api/python/*
%{_datadir}/qt4/qsci/api/ruby

%files doc
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/%{name}/Documentation
%{py_sitescriptdir}/%{name}/Documentation/Source

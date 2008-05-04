Summary:	Eric4 - a full featured Python IDE
Summary(pl.UTF-8):	Eric4 - pełnowartościowe IDE dla Pythona
Name:		eric4
Version:	4.1.3
Release:	2
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/eric-ide/%{name}-%{version}.tar.gz
# Source0-md5:	9083903022bbdd2ad43e8bdb52837b13
Source1:	%{name}.desktop
URL:		http://www.die-offenbachs.de/eric/index.html
BuildRequires:	python-qscintilla2-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-qscintilla2 >= 2.1_1.73-2
Requires:	python-devel-tools
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

python install.py -c -b %{_bindir} -d %{py_sitescriptdir} -i $RPM_BUILD_ROOT
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/eric4.desktop
install -D eric/pixmaps/eric.png $RPM_BUILD_ROOT%{_pixmapsdir}/eric4.png

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}/*
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}/*

%clean
rm -rf $RPM_BUILD_ROOT

# NOTE: eric4 uses *.py files for it's own purposes
# so do not remove them from package
%files
%defattr(644,root,root,755)
%doc ChangeLog README* THANKS
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/eric4config.py*
%{py_sitescriptdir}/%{name}
%dir %{py_sitescriptdir}/%{name}plugins
%{py_sitescriptdir}/%{name}plugins/*
%exclude %{py_sitescriptdir}/%{name}/Documentation
%{_desktopdir}/eric4.desktop
%{_pixmapsdir}/eric4.png

%files doc
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/%{name}/Documentation
%{py_sitescriptdir}/%{name}/Documentation/Source

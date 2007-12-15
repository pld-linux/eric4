Summary:	Eric4 - a full featured Python IDE
Summary(pl.UTF-8):	Eric4 - pełnowartościowe IDE dla Pythona
Name:		eric4
Version:	4.0.4
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/eric-ide/%{name}-%{version}.tar.gz
# Source0-md5:	1886926945a95c92f2151d5135120c67
Source1:	%{name}.desktop
URL:		http://www.die-offenbachs.de/eric/index.html
BuildRequires:	python-qscintilla2-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-qscintilla2 >= 2.1_1.73-2
Requires:	python-devel-tools
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

python install.py -c -b %{_bindir} -d %{py_sitedir} -i $RPM_BUILD_ROOT
install -D eric/pixmaps/eric.png $RPM_BUILD_ROOT%{_pixmapsdir}/eric4.png

%py_comp $RPM_BUILD_ROOT%{py_sitedir}/*
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/*

%clean
rm -rf $RPM_BUILD_ROOT

# NOTE: eric4 uses *.py files for it's own purposes
# so do not remove them from package
%files
%defattr(644,root,root,755)
%doc ChangeLog README* THANKS
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/eric4config.py
%{py_sitedir}/%{name}
%exclude %{py_sitedir}/%{name}/Documentation
%{_pixmapsdir}/eric4.png

%files doc
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{name}/Documentation
%{py_sitedir}/%{name}/Documentation/Source

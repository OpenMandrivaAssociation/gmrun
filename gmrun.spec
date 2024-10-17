Name:			gmrun
Version:		0.9.2
Release:		%mkrel 6
Summary:		Lightweight "Run program" dialog box with search history and tab completion
Group:			Graphical desktop/Other
License:		GPL+
URL:			https://sourceforge.net/projects/gmrun
Source0:		http://heanet.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:			gmrun-gmrunrc.patch
Patch1:			gmrun-0.9.2-gcc43.patch
Patch2:			gmrun-0.9.2-mousewheel.patch
Patch3:			gmrun-0.9.2-mga.patch
BuildRequires:		popt-devel
BuildRequires:		pkgconfig(gtk+-2.0)
Requires:		xterm
Requires:		man
Requires:		info
Requires:		xdg-utils

%description
A simple GTK program which provides a "run program" window.
It features a bash-like TAB completion, Ctrl-R/Ctrl-S for 
searching through the history and URL handlers for any user defined
prefix.


%prep
%setup -q
%autopatch -p1

%build
%configure
%make

%install
%makeinstall_std

%files
%doc ChangeLog AUTHORS COPYING README NEWS
%{_datadir}/gmrun/
%{_bindir}/gmrun

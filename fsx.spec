%define name    fsx
%define version 1.3
%define release %mkrel 5

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:	General filesystem exerciser
URL:		http://www.freebsd.org/cgi/cvsweb.cgi/src/tools/regression/fsx
License:	GPL
Group:		System/Kernel and hardware
Source0:	%{name}.c
Source1:	README
Buildroot:	 %{_tmppath}/%{name}-%{version}-root

%description
General filesystem exerciser

%build
%__cc %{optflags} -o %{name} %SOURCE0

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%_bindir
cp fsx $RPM_BUILD_ROOT%_bindir

install -d $RPM_BUILD_ROOT%_defaultdocdir/%{name}-%{version}
cp %SOURCE1 $RPM_BUILD_ROOT%_defaultdocdir/%{name}-%{version}

%files
%attr(755,root,root)
%_bindir/fsx
%_defaultdocdir/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT



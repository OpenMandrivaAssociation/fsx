%define name    fsx
%define version 1.3
%define release %mkrel 6

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




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3-6mdv2011.0
+ Revision: 618364
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.3-5mdv2010.0
+ Revision: 428959
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.3-4mdv2009.0
+ Revision: 245441
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.3-2mdv2008.1
+ Revision: 140731
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Feb 25 2007 Anne Nicolas <anne.nicolas@mandriva.com> 1.3-2mdv2007.0
+ Revision: 125555
- rebuild
- Import fsx

* Sun May 07 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.3-1mdk
- initial release


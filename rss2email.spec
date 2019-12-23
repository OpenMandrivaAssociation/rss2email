Name:           rss2email
Version:	3.11
Release:	1
Summary:        Deliver news from RSS feeds to your smtp server as text or html mail
Group:          Networking/News
License:        GPLv3
URL:            http://rss2email.infogami.com/

# Fedora variant of http://lindsey.smith.googlepages.com/r2e
Source3:        rss2email-r2e
BuildArch:      noarch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:       python-feedparser
Requires:       python3dist(pyxdg)

BuildRequires:  python-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(feedparser)
BuildRequires:  python3dist(html2text)
BuildRequires:  python3dist(beautifulsoup4)

%description
rss2email lets you subscribe to a list of XML newsfeeds (RSS or Atom). It can
parse them regularly with the help of cron and send new items to you by email.

A HTML mail will be send in the default configuration to the local smtp server.
See the man page r2e for details how to set rss2email up.


%prep
%autosetup -p1

# drop bundled egg-info
rm -rf *.egg-info/

install -Dpm644 %{SOURCE3} README.urpmi.update

%build
%py3_build

%install
%py3_install

# man pages
install -D -m 644 -p r2e.1 %{buildroot}%{_mandir}/man1/r2e.1

# migrate scripts
install -D -m 755 -p %{SOURCE1} %{buildroot}%{_bindir}/r2e-migrate
install -D -m 644 -p %{SOURCE2} %{buildroot}%{_mandir}/man1/r2e-migrate.1

%files
%license COPYING
%doc AUTHORS CHANGELOG README*
%{_bindir}/r2e
%{_bindir}/r2e-migrate
%{_mandir}/man1/r2e.1*
%{_mandir}/man1/r2e-migrate.1*
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Sep 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.65-2mdv2010.0
+ Revision: 442763
- rebuild

* Fri Mar 06 2009 Michael Scherer <misc@mandriva.org> 2.65-1mdv2009.1
+ Revision: 349898
- update to new version 2.65

* Tue Jan 06 2009 Jérôme Soyer <saispo@mandriva.org> 2.64-1mdv2009.1
+ Revision: 325359
- update to new version 2.64

* Thu Sep 04 2008 Jérôme Soyer <saispo@mandriva.org> 2.63-1mdv2009.0
+ Revision: 280664
- Fix RPM Group
- New release

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.62-4mdv2009.0
+ Revision: 260343
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.62-3mdv2009.0
+ Revision: 251553
- rebuild

* Sat Mar 01 2008 Michael Scherer <misc@mandriva.org> 2.62-1mdv2008.1
+ Revision: 177251
- update to new version 2.62

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Jérôme Soyer <saispo@mandriva.org> 2.61-1mdv2008.1
+ Revision: 132041
- New release

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 23 2007 Jérôme Soyer <saispo@mandriva.org> 2.60-1mdv2008.1
+ Revision: 101444
- New release 2.60


* Wed Aug 09 2006 Michael Scherer <misc@mandriva.org> 2.57-2mdv2007.0
- Rebuild to keep src in sync

* Mon Apr 10 2006 Michael Scherer <misc@mandriva.org> 2.57-1mdk
- New release 2.57

* Thu Dec 22 2005 Michael Scherer <misc@mandriva.org> 2.55-1mdk
- New release 2.55

* Wed Dec 21 2005 Michael Scherer <misc@mandriva.org> 2.54-1mdk
- First mandriva release
- patch to have FeedUrl in the header of the mail, to ease filtering


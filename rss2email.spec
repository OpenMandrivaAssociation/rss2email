Name:           rss2email
Version:	3.14
Release:	1
Summary:        Deliver news from RSS feeds to your smtp server as text or html mail
Group:          Networking/News
License:        GPLv3
URL:            https://rss2email.infogami.com/
Source0:        https://files.pythonhosted.org/packages/source/r/rss2email/rss2email-%{version}.tar.gz
#Patch0:         feedparser-version.patch
BuildArch:      noarch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:       python-feedparser
Requires:       python3dist(pyxdg)

BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(poetry)
BuildRequires:  python-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(feedparser)
BuildRequires:  pythonegg(html2text)
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

%build
%py_build

%install
%py_install

%files
%license COPYING
%doc AUTHORS CHANGELOG README*
%{_bindir}/r2e
%{python_sitelib}/%{name}/
#{python_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/
%{python_sitelib}/rss2email-3.12.2.dist-info/

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


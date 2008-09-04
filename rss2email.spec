Name:           rss2email
Version:        2.63
Release:        %mkrel 1
Summary:        Deliver news from RSS feeds to your smtp server as text or html mail
Group:          Networking/News
License:        GPLv3
URL:            http://rss2email.infogami.com/
Source0:        http://rss2email.infogami.com/rss2email.py
Source1:        http://rss2email.infogami.com/CHANGELOG
# Fedora variant of http://lindsey.smith.googlepages.com/r2e
Source3:        rss2email-r2e
# man page taken from
# http://ftp.debian.org/debian/pool/main/r/rss2email/rss2email_2.60-3.diff.gz
Source4:        rss2email-r2e.1
Source5:        rss2email-config.py.template
Patch0:         rss2email-use-configpy-from-homedir.patch
# patch taken from
# http://ftp.debian.org/debian/pool/main/r/rss2email/rss2email_2.60-3.diff.gz
Patch1:         rss2email-warn-if-problems-with-local-mta.patch
BuildArch:      noarch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires:       python-feedparser
Requires:       python-html2text

%description
rss2email lets you subscribe to a list of XML newsfeeds (RSS or Atom). It can
parse them regularly with the help of cron and send new items to you by email.

A HTML mail will be send in the default configuration to the local smtp server.
See the man page r2e for details how to set rss2email up.


%prep
%setup -q -c -T
install -p -m 0644 %{SOURCE0} rss2email.py
install -p -m 0644 %{SOURCE1} CHANGELOG.html
# let rss2email use ${HOME}/.rss2email/config.py
%patch0 -b .patch0
%patch1 -b .patch1
sed -i -e 's/\r//' CHANGELOG.html rss2email.py


%build
echo nothing to build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p  \
   $RPM_BUILD_ROOT%{_bindir}/ \
   $RPM_BUILD_ROOT%{_datadir}/%{name}/  \
   $RPM_BUILD_ROOT%{_mandir}/man1/

install -p -m 0755 rss2email.py $RPM_BUILD_ROOT%{_datadir}/%{name}/
install -p -m 0755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/r2e
sed -i -e 's;/usr/share;%{_datadir};g' $RPM_BUILD_ROOT%{_bindir}/r2e
install -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/man1/r2e.1
install -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/%{name}/config.py.template


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGELOG.html
%{_bindir}/*
%{_datadir}/%{name}/
%{_mandir}/man1/*

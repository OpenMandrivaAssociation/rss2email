Name:           rss2email
Version:        2.62
Release:        %mkrel 4
Summary:        A script that send mail for rss feed news
Group:          Networking/News
License:        GPL
URL:            http://www.aaronsw.com/2002/rss2email/
Source0:        http://ftp.debian.org/debian/pool/main/r/%{name}/%{name}_%{version}.orig.tar.bz2
Patch:          rss2email-2.54-add_header_feed_url.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildArch:      noarch
Requires:       python-feedparser
%description
rss2email is a simple Python script that lets you subscribe to a list of XML
newsfeeds (RSS or Atom) and get new items sent to you by email.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p  $RPM_BUILD_ROOT/%_bindir/
cat << EOF > $RPM_BUILD_ROOT/%_bindir/r2e
#!/bin/sh
mkdir -p ~/.rss2email/
cd ~/.rss2email/
touch config.py
exec python %_datadir/%name/rss2email.py feeds.dat \$*
EOF
chmod 755 $RPM_BUILD_ROOT/%_bindir/r2e

mkdir -p $RPM_BUILD_ROOT/%_datadir/%name/
cp *.py $RPM_BUILD_ROOT/%_datadir/%name/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%_datadir/%name/
%_bindir/*


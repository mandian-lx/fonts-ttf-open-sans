%define fontname open-sans

%define fontdir		%{_datadir}/fonts/TTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	A sanserif type­face font fam­ily
Name:		fonts-ttf-%{fontname}
Version:	1.10
Release:	0
Url:		http://www.opensans.com/
License:	ASL 2.0
Group:		System/Fonts/True type
Source0:	http://www.opensans.com/download/%{fontname}.zip
BuildArch:	noarch

BuildRequires:	fontconfig
BuildRequires:	mkfontscale
BuildRequires:	mkfontdir

%description
Open Sans is a clean and modern sans-serif typeface designed by Steve
Matteson and commissioned by Google. It is especially designed for
legibility across print, web, and mobile interfaces.

Open Sans is excellent for any type of use. It's incredibly readable in
smallsizes and also works great when printed in huge letters. The best
thing of all, it's a free font! You are free to use and download it for
your next design project.

It's a well known and modern font that is being used more and more on
new websites. Because of it's simplicity it really makes your content
easily readable. The same thing goes for offline content. When printed
it will make your documents amazing.

%prep
%setup -q -c %{name}-%{version}

%build
# nothing to do here!

%install
install -dm 0755 %{buildroot}/%{fontdir}/
install -pm 0644 *.ttf %{buildroot}/%{fontdir}/

#ttmkfdir %{buildroot}%{buildroot}%{fontdir}/ > %{buildroot}%{buildroot}%{fontdir}/fonts.dir
#ln -s fonts.dir %{buildroot}%{buildroot}%{fontdir}//fonts.scale
#

mkfontscale %{buildroot}%{fontdir}/
mkfontdir %{buildroot}%{fontdir}/

mkdir -p %{buildroot}%{fontconfdir}/
ln -s ../../..%{buildroot}%{fontdir} %{buildroot}%{fontconfdir}/ttf-%{fontname}:pri=50

%files
%dir %{fontdir}
%{fontconfdir}/ttf-%{fontname}:pri=50
%{fontdir}/*.ttf
%verify(not mtime)%{fontdir}/fonts.dir
%{fontdir}/fonts.scale
%doc Apache\ License.txt


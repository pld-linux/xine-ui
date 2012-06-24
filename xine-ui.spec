# Conditional build:
# --without	aa
# --without	lirc

Summary:	A Free Video Player
Summary(pl):	Odtwarzacz video
Summary(ko):	���� ������ �÷��̾�
Name:		xine-ui
Version:	0.9.7
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://xine.sourceforge.net/files/%{name}-%{version}.tar.gz
Source1:	xine.desktop
Source2:	xine_logo.png
Patch0:		%{name}-DESTDIR.patch
URL:		http://xine.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	sed
BuildRequires:	xine-lib-devel >= %{version}
%{!?_without_aa:BuildRequires:		aalib-devel}
%{!?_without_aa:BuildRequires:		aalib-progs}
%{!?_without_aa:BuildRequires:		slang-devel}
%{!?_without_aa:BuildRequires:		gpm-devel}
%{!?_without_lirc:BuildRequires:	lirc-devel}
BuildRequires:	libpng-devel
Obsoletes:	xine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_abindir	/usr/bin

%description
xine is a free gpl-licensed video player for unix-like systems. We
support mpeg-2 and mpeg-1 system (audio + video multiplexed) streams,
eventually mpeg-4 and other formats might be added.

xine plays the video and audio data of mpeg-2 videos and synchronizes
the playback of both. Depending on the properties of the mpeg stream,
playback will need more or less processor power, 100% frame rate has
been seen on a 400 MHz P II system.

%description -l fr
xine est un lecteur vid�o libre sous license GPL pour les syst�mes de
type unix. Nous supportons les flux mpeg-2 et mpeg-1 (audio + vid�o
multiplex�s), �ventuellement le mpeg-4 et d'autres formats peuvent
�tres ajout�s.

xine joue les donn�es vid�o et audio de vid�o mpeg-2 et synchronise la
lecture des deux. En fonction des propri�tes du flux mpeg, la lecture
aura besoin de plus ou moins de puissance du processeur, 100% de
restitution de trame a �t� vus sur un syst�me PII 400MHz.

%description -l ko
xine �� GPL���̼����� ������ UNIX�� ���� ������ �÷��̾��Դϴ�. ��
�÷��̾�� mpeg-2 �� mpeg 1 ��Ʈ���� �����ϸ�, ����� �������� ������
���߿��� mpeg-4 �� �ٸ� ������ ������ ������ �����Դϴ�.

%description -l pl
xine jest wolnodost�pnym odtwarzaczem film�w dla system�w uniksowych.
Obs�uguje strumienie MPEG-2 i MPEG-1 (przeplatany d�wi�k i obraz),
mo�e by� dodana obs�uga MPEG-4 i innych format�w.

%package aa
Summary:	XINE - Ascii Art player
Summary(pl):	XINE - odtwarzacz Ascii Art
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Group(pt):	Aplica��es/Gr�ficos
Requires:	xine-lib-aa >= %{version}

%description aa
Video player using Ascii Art library.

%description aa -l pl
Odtwarzacz film�w u�ywaj�cy biblioteki Ascii Art.

%prep
%setup -q -n xine-ui-%{version}
%patch0 -p1

%build
aclocal
autoconf
automake -a -c
autoheader
%configure \
	--disable-orbit \
%{?_without_lirc:	--disable-lirc} \
%{!?_without_lirc:	--enable-lirc}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_applnkdir}/Multimedia,%{_datadir}/xine/skins}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=$RPM_BUILD_ROOT%{_datadir}/doc/xine

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/xine.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xine/skins

%{!?_without_aa:install -d $RPM_BUILD_ROOT%{_abindir}}
%{!?_without_aa:install $RPM_BUILD_ROOT%{_bindir}/aaxine $RPM_BUILD_ROOT%{_abindir}}

gzip -9nf doc/{FAQ,README}* ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{README,README.{dxr3,divx4,syncfb,xinerc},FAQ}.gz *.gz
%lang(pl) %doc doc/{README,README.dxr3,FAQ}_pl.gz
%lang(it) %doc doc/{README,FAQ}_it.gz
%lang(es) %doc doc/{README,FAQ}_es.gz
%lang(fr) %doc doc/FAQ_fr.gz
%attr(755,root,root) %{_bindir}/xine
%{_datadir}/idl/xine.idl
%{_datadir}/xine/skins
%{_mandir}/man1/xine.1*
%lang(fr) %{_mandir}/fr/man1/xine.1*
%{_applnkdir}/Multimedia/xine.desktop

%{!?_without_aa:%files aa}
%{!?_without_aa:%defattr(644,root,root,755)}
%{!?_without_aa:%attr(755,root,root) %{_abindir}/aaxine}

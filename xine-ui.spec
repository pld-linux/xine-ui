#
# Conditional build:
# _without_aa		- without aaxine UI
# _without_lirc		- without lirc support
# _with_directfb	- with dfbxine UI (doesn't work now)
#
%ifarch alpha sparc sparc64
%define		_without_lirc	1
%endif
Summary:	A Free Video Player
Summary(ko):	���� ������ �÷��̾�
Summary(pl):	Odtwarzacz video
Summary(pt_BR):	Xine, um player de video
Summary(zh_CN):	һ����ѵ���Ƶ������(����)
Name:		xine-ui
Version:	0.9.22
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/xine/%{name}-%{version}.tar.gz
# Source0-md5:	2a59480b11cb136862cafcbc56d3922e
Source1:	xine.desktop
Source2:	xine.png
Source3:	xine_logo.png
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-nolibs.patch
Patch2:		%{name}-opt.patch
Patch3:		%{name}-system-readline.patch
URL:		http://xine.sourceforge.net/
%{?_with_directfb:BuildRequires:	DirectFB-devel >= 0.9.10}
%{!?_without_aa:BuildRequires:		aalib-devel >= 1.2.0}
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
%{!?_without_lirc:BuildRequires:	lirc-devel}
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel >= 4.2a
BuildRequires:	xine-lib-devel >= %{version}
Requires:	xine-plugin-audio
Obsoletes:	xine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pt_BR
O xine � um video player GPL para sistemas unix. L� arquivos MPEG-2 e
MPEG-1, al�m de AVIs MS MPEG4 / OpenDivX.

O xine l� o conte�do v�deo e �udio e sincroniza-os em tempo-real. As
necessidades de processador dependem das propriedades de cada arquivo.

%package aa
Summary:	XINE - Ascii Art player
Summary(pl):	XINE - odtwarzacz Ascii Art
Summary(pt_BR):	XINE - Player em Ascii Art (aalib)
Group:		Applications/Multimedia
Requires:	xine-output-video-aa >= %{version}
Requires:	xine-plugin-audio

%description aa
Video player using Ascii Art library.

%description aa -l pl
Odtwarzacz film�w u�ywaj�cy biblioteki Ascii Art.

%description aa -l pt_BR
Interface para o xine utilizando aalib (Ascii Art Library).

%package dfb
Summary:	XINE - player for DirectFB
Summary(pl):	XINE - odtwarzacz dla DirectFB
Group:		Applications/Multimedia
Requires:	xine-lib-directfb >= %{version}
Requires:	xine-plugin-audio

%description dfb
Video player using DirectFB library.

%description dfb -l pl
Odtwarzacz film�w u�ywaj�cy biblioteki DirectFB.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%{__autoheader}
%configure \
	--disable-orbit \
	--disable-corba \
%{?_without_lirc:	--disable-lirc} \
%{!?_without_lirc:	--enable-lirc}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Multimedia,%{_pixmapsdir},%{_datadir}/xine/skins}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=$RPM_BUILD_ROOT%{_datadir}/doc/xine

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/xine.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/xine/skins

mv $RPM_BUILD_ROOT%{_datadir}/locale/{pl_PL,pl}

cp src/xitk/xine-toolkit/README doc/README.xitk

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/{README_en,README.*} ChangeLog
%lang(cs) %doc doc/README_cs
%lang(de) %doc doc/README_de
%lang(es) %doc doc/README_es
%lang(fi) %doc doc/README_fi
%lang(fr) %doc doc/README_fr
%lang(it) %doc doc/README_it
%lang(pl) %doc doc/README_pl
%lang(uk) %doc doc/README_uk
#%attr(755,root,root) %{_bindir}/fbxine		(doesn't work for me)
%attr(755,root,root) %{_bindir}/xine
%attr(755,root,root) %{_bindir}/xine-bugreport
%attr(755,root,root) %{_bindir}/xine-check
%attr(755,root,root) %{_bindir}/xine-remote
%{_datadir}/xine/skins
%{_datadir}/xine/desktop
%{_datadir}/xine/visuals
%{_mandir}/man1/*.1*
%lang(de) %{_mandir}/de/man1/*.1*
%lang(es) %{_mandir}/es/man1/*.1*
%lang(fr) %{_mandir}/fr/man1/*.1*
%lang(pl) %{_mandir}/pl/man1/*.1*
%{_applnkdir}/Multimedia/xine.desktop
%{_pixmapsdir}/*
# CORBA files 
#%%{_datadir}/idl/xine.idl
#%attr(755,root,root) %{_bindir}/xine-remote

%{!?_without_aa:%files aa}
%{!?_without_aa:%defattr(644,root,root,755)}
%{!?_without_aa:%attr(755,root,root) %{_bindir}/aaxine}

%{?_with_directfb:%files dfb}
%{?_with_directfb:%defattr(644,root,root,755)}
%{?_with_directfb:%attr(755,root,root) %{_bindir}/dfbxine}

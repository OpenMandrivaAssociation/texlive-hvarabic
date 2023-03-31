Name:		texlive-hvarabic
Version:	59423
Release:	2
Summary:	Macros for RTL typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hvarabic
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvarabic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvarabic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides some macros for right-to-left
typesetting. It uses by default the arabic fonts Scheherazade
and ALM fixed, the only monospaced arabic font. The package
works with LuaLaTeX or XeLaTeX, but not with pdfLaTeX or latex.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/hvarabic
%doc %{_texmfdistdir}/doc/latex/hvarabic

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

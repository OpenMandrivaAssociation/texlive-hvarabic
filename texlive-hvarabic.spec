%global tl_name hvarabic
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.02
Release:	%{tl_revision}.1
Summary:	Macros for RTL typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/hvarabic
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hvarabic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hvarabic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides some macros for right-to-left typesetting. It uses
by default the arabic fonts Scheherazade and ALM fixed, the only
monospaced arabic font. The package works with LuaLaTeX or XeLaTeX, but
not with pdfLaTeX or latex.


# revision 18651
# category Package
# catalog-ctan /fonts/antt
# catalog-date 2007-08-24 10:36:49 +0200
# catalog-license gfsl
# catalog-version 2.08
Name:		texlive-antt
Version:	2.08
Release:	2
Summary:	Antykwa Torunska: a Type 1 family of a Polish traditional type
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/antt
License:	GFSL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/antt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/antt.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Antykwa Torunska is a serif font designed by the late Polish
typographer Zygfryd Gardzielewski, reconstructed and digitized
as as Type 1.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/antt/anttb.afm
%{_texmfdistdir}/fonts/afm/public/antt/anttbi.afm
%{_texmfdistdir}/fonts/afm/public/antt/anttcb.afm
%{_texmfdistdir}/fonts/afm/public/antt/anttcbi.afm
%{_texmfdistdir}/fonts/afm/public/antt/anttcl.afm
%{_texmfdistdir}/fonts/afm/public/antt/anttcli.afm
%{_texmfdistdir}/fonts/afm/public/antt/anttcm.afm
%{_texmfdistdir}/fonts/afm/public/antt/anttcmi.afm
%{_texmfdistdir}/fonts/afm/public/antt/anttcr.afm
%{_texmfdistdir}/fonts/afm/public/antt/anttcri.afm
%{_texmfdistdir}/fonts/afm/public/antt/anttl.afm
%{_texmfdistdir}/fonts/afm/public/antt/anttli.afm
%{_texmfdistdir}/fonts/afm/public/antt/anttm.afm
%{_texmfdistdir}/fonts/afm/public/antt/anttmi.afm
%{_texmfdistdir}/fonts/afm/public/antt/anttr.afm
%{_texmfdistdir}/fonts/afm/public/antt/anttri.afm
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-cs.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-ec.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-el.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-ex.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-exp.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-greek.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-mi.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-qx.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-rm.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-sy.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-t2b.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-t2c.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-t5.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-texnansi.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-ts1.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/antt-wncy.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/anttcap-cs.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/anttcap-ec.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/anttcap-qx.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/anttcap-t5.enc
%{_texmfdistdir}/fonts/enc/dvips/antt/anttcap-texnansi.enc
%{_texmfdistdir}/fonts/map/dvips/antt/antt-cs.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt-ec.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt-el.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt-ex.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt-exp.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt-greek.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt-mi.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt-qx.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt-rm.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt-sy.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt-t2a.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt-t2b.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt-t2c.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt-t5.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt-texnansi.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt-ts1.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt-wncy.map
%{_texmfdistdir}/fonts/map/dvips/antt/antt.map
%{_texmfdistdir}/fonts/opentype/public/antt/AntykwaTorunska-Bold.otf
%{_texmfdistdir}/fonts/opentype/public/antt/AntykwaTorunska-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/public/antt/AntykwaTorunska-Italic.otf
%{_texmfdistdir}/fonts/opentype/public/antt/AntykwaTorunska-Regular.otf
%{_texmfdistdir}/fonts/opentype/public/antt/AntykwaTorunskaCond-Bold.otf
%{_texmfdistdir}/fonts/opentype/public/antt/AntykwaTorunskaCond-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/public/antt/AntykwaTorunskaCond-Italic.otf
%{_texmfdistdir}/fonts/opentype/public/antt/AntykwaTorunskaCond-Regular.otf
%{_texmfdistdir}/fonts/opentype/public/antt/AntykwaTorunskaCondLight-Italic.otf
%{_texmfdistdir}/fonts/opentype/public/antt/AntykwaTorunskaCondLight-Regular.otf
%{_texmfdistdir}/fonts/opentype/public/antt/AntykwaTorunskaCondMed-Italic.otf
%{_texmfdistdir}/fonts/opentype/public/antt/AntykwaTorunskaCondMed-Regular.otf
%{_texmfdistdir}/fonts/opentype/public/antt/AntykwaTorunskaLight-Italic.otf
%{_texmfdistdir}/fonts/opentype/public/antt/AntykwaTorunskaLight-Regular.otf
%{_texmfdistdir}/fonts/opentype/public/antt/AntykwaTorunskaMed-Italic.otf
%{_texmfdistdir}/fonts/opentype/public/antt/AntykwaTorunskaMed-Regular.otf
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttbcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttbicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttcb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttcbcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttcbicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttcl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttclcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttcli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttclicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttcm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttcmcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttcmicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttcr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttcrcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttcri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttcricap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttlcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttlicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttmcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttmicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttrcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/cs-anttricap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttbcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttbicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttcb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttcbcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttcbicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttcl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttclcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttcli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttclicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttcm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttcmcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttcmicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttcr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttcrcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttcri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttcricap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttlcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttlicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttmcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttmicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttrcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ec-anttricap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/el-anttb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/el-anttbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/el-anttcb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/el-anttcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/el-anttcl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/el-anttcli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/el-anttcm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/el-anttcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/el-anttcr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/el-anttcri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/el-anttl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/el-anttli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/el-anttm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/el-anttmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/el-anttr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/el-anttri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ex-anttb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ex-anttcb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ex-anttcl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ex-anttcm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ex-anttcr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ex-anttl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ex-anttm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ex-anttr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/exp-anttb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/exp-anttbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/exp-anttcb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/exp-anttcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/exp-anttcl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/exp-anttcli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/exp-anttcm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/exp-anttcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/exp-anttcr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/exp-anttcri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/exp-anttl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/exp-anttli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/exp-anttm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/exp-anttmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/exp-anttr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/exp-anttri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/greek-anttb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/greek-anttbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/greek-anttcb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/greek-anttcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/greek-anttcl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/greek-anttcli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/greek-anttcm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/greek-anttcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/greek-anttcr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/greek-anttcri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/greek-anttl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/greek-anttli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/greek-anttm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/greek-anttmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/greek-anttr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/greek-anttri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/mi-anttbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/mi-anttcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/mi-anttcli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/mi-anttcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/mi-anttcri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/mi-anttli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/mi-anttmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/mi-anttri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttbcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttbicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttcb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttcbcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttcbicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttcl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttclcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttcli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttclicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttcm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttcmcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttcmicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttcr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttcrcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttcri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttcricap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttlcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttlicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttmcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttmicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttrcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/qx-anttricap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/rm-anttb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/rm-anttbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/rm-anttcb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/rm-anttcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/rm-anttcl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/rm-anttcli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/rm-anttcm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/rm-anttcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/rm-anttcr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/rm-anttcri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/rm-anttl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/rm-anttli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/rm-anttm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/rm-anttmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/rm-anttr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/rm-anttri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/sy-anttbz.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/sy-anttcbz.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/sy-anttclz.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/sy-anttcmz.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/sy-anttcrz.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/sy-anttlz.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/sy-anttmz.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/sy-anttrz.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2a-anttb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2a-anttbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2a-anttcb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2a-anttcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2a-anttcl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2a-anttcli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2a-anttcm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2a-anttcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2a-anttcr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2a-anttcri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2a-anttl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2a-anttli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2a-anttm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2a-anttmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2a-anttr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2a-anttri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2b-anttb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2b-anttbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2b-anttcb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2b-anttcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2b-anttcl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2b-anttcli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2b-anttcm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2b-anttcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2b-anttcr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2b-anttcri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2b-anttl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2b-anttli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2b-anttm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2b-anttmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2b-anttr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2b-anttri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2c-anttb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2c-anttbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2c-anttcb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2c-anttcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2c-anttcl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2c-anttcli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2c-anttcm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2c-anttcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2c-anttcr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2c-anttcri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2c-anttl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2c-anttli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2c-anttm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2c-anttmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2c-anttr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t2c-anttri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttbcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttbicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttcb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttcbcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttcbicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttcl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttclcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttcli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttclicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttcm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttcmcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttcmicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttcr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttcrcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttcri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttcricap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttlcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttlicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttmcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttmicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttrcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/t5-anttricap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttbcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttbicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttcb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttcbcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttcbicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttcl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttclcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttcli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttclicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttcm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttcmcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttcmicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttcr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttcrcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttcri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttcricap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttlcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttlicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttmcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttmicap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttrcap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/texnansi-anttricap.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ts1-anttb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ts1-anttbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ts1-anttcb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ts1-anttcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ts1-anttcl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ts1-anttcli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ts1-anttcm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ts1-anttcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ts1-anttcr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ts1-anttcri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ts1-anttl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ts1-anttli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ts1-anttm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ts1-anttmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ts1-anttr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/ts1-anttri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/wncy-anttb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/wncy-anttbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/wncy-anttcb.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/wncy-anttcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/wncy-anttcl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/wncy-anttcli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/wncy-anttcm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/wncy-anttcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/wncy-anttcr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/wncy-anttcri.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/wncy-anttl.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/wncy-anttli.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/wncy-anttm.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/wncy-anttmi.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/wncy-anttr.tfm
%{_texmfdistdir}/fonts/tfm/public/antt/wncy-anttri.tfm
%{_texmfdistdir}/fonts/type1/public/antt/anttb.pfb
%{_texmfdistdir}/fonts/type1/public/antt/anttbi.pfb
%{_texmfdistdir}/fonts/type1/public/antt/anttcb.pfb
%{_texmfdistdir}/fonts/type1/public/antt/anttcbi.pfb
%{_texmfdistdir}/fonts/type1/public/antt/anttcl.pfb
%{_texmfdistdir}/fonts/type1/public/antt/anttcli.pfb
%{_texmfdistdir}/fonts/type1/public/antt/anttcm.pfb
%{_texmfdistdir}/fonts/type1/public/antt/anttcmi.pfb
%{_texmfdistdir}/fonts/type1/public/antt/anttcr.pfb
%{_texmfdistdir}/fonts/type1/public/antt/anttcri.pfb
%{_texmfdistdir}/fonts/type1/public/antt/anttl.pfb
%{_texmfdistdir}/fonts/type1/public/antt/anttli.pfb
%{_texmfdistdir}/fonts/type1/public/antt/anttm.pfb
%{_texmfdistdir}/fonts/type1/public/antt/anttmi.pfb
%{_texmfdistdir}/fonts/type1/public/antt/anttr.pfb
%{_texmfdistdir}/fonts/type1/public/antt/anttri.pfb
%{_texmfdistdir}/tex/latex/antt/anttor.sty
%{_texmfdistdir}/tex/latex/antt/antyktor.sty
%{_texmfdistdir}/tex/latex/antt/il2antt.fd
%{_texmfdistdir}/tex/latex/antt/il2anttc.fd
%{_texmfdistdir}/tex/latex/antt/il2anttl.fd
%{_texmfdistdir}/tex/latex/antt/il2anttlc.fd
%{_texmfdistdir}/tex/latex/antt/ly1antt.fd
%{_texmfdistdir}/tex/latex/antt/ly1anttc.fd
%{_texmfdistdir}/tex/latex/antt/ly1anttl.fd
%{_texmfdistdir}/tex/latex/antt/ly1anttlc.fd
%{_texmfdistdir}/tex/latex/antt/omlantt.fd
%{_texmfdistdir}/tex/latex/antt/omlanttc.fd
%{_texmfdistdir}/tex/latex/antt/omlanttl.fd
%{_texmfdistdir}/tex/latex/antt/omlanttlc.fd
%{_texmfdistdir}/tex/latex/antt/omsantt.fd
%{_texmfdistdir}/tex/latex/antt/omsanttc.fd
%{_texmfdistdir}/tex/latex/antt/omsanttl.fd
%{_texmfdistdir}/tex/latex/antt/omsanttlc.fd
%{_texmfdistdir}/tex/latex/antt/omxantt.fd
%{_texmfdistdir}/tex/latex/antt/omxanttc.fd
%{_texmfdistdir}/tex/latex/antt/omxanttl.fd
%{_texmfdistdir}/tex/latex/antt/omxanttlc.fd
%{_texmfdistdir}/tex/latex/antt/ot1antt.fd
%{_texmfdistdir}/tex/latex/antt/ot1anttc.fd
%{_texmfdistdir}/tex/latex/antt/ot1anttcm.fd
%{_texmfdistdir}/tex/latex/antt/ot1anttl.fd
%{_texmfdistdir}/tex/latex/antt/ot1anttlc.fd
%{_texmfdistdir}/tex/latex/antt/ot1anttlcm.fd
%{_texmfdistdir}/tex/latex/antt/ot1anttlm.fd
%{_texmfdistdir}/tex/latex/antt/ot1anttm.fd
%{_texmfdistdir}/tex/latex/antt/ot2antt.fd
%{_texmfdistdir}/tex/latex/antt/ot2anttc.fd
%{_texmfdistdir}/tex/latex/antt/ot2anttl.fd
%{_texmfdistdir}/tex/latex/antt/ot2anttlc.fd
%{_texmfdistdir}/tex/latex/antt/ot4antt.fd
%{_texmfdistdir}/tex/latex/antt/ot4anttc.fd
%{_texmfdistdir}/tex/latex/antt/ot4anttl.fd
%{_texmfdistdir}/tex/latex/antt/ot4anttlc.fd
%{_texmfdistdir}/tex/latex/antt/qxantt.fd
%{_texmfdistdir}/tex/latex/antt/qxanttc.fd
%{_texmfdistdir}/tex/latex/antt/qxanttl.fd
%{_texmfdistdir}/tex/latex/antt/qxanttlc.fd
%{_texmfdistdir}/tex/latex/antt/t1antt.fd
%{_texmfdistdir}/tex/latex/antt/t1anttc.fd
%{_texmfdistdir}/tex/latex/antt/t1anttl.fd
%{_texmfdistdir}/tex/latex/antt/t1anttlc.fd
%{_texmfdistdir}/tex/latex/antt/t2aantt.fd
%{_texmfdistdir}/tex/latex/antt/t2aanttc.fd
%{_texmfdistdir}/tex/latex/antt/t2aanttl.fd
%{_texmfdistdir}/tex/latex/antt/t2aanttlc.fd
%{_texmfdistdir}/tex/latex/antt/t2bantt.fd
%{_texmfdistdir}/tex/latex/antt/t2banttc.fd
%{_texmfdistdir}/tex/latex/antt/t2banttl.fd
%{_texmfdistdir}/tex/latex/antt/t2banttlc.fd
%{_texmfdistdir}/tex/latex/antt/t2cantt.fd
%{_texmfdistdir}/tex/latex/antt/t2canttc.fd
%{_texmfdistdir}/tex/latex/antt/t2canttl.fd
%{_texmfdistdir}/tex/latex/antt/t2canttlc.fd
%{_texmfdistdir}/tex/latex/antt/t5antt.fd
%{_texmfdistdir}/tex/latex/antt/t5anttc.fd
%{_texmfdistdir}/tex/latex/antt/t5anttl.fd
%{_texmfdistdir}/tex/latex/antt/t5anttlc.fd
%{_texmfdistdir}/tex/latex/antt/ts1antt.fd
%{_texmfdistdir}/tex/latex/antt/ts1anttc.fd
%{_texmfdistdir}/tex/latex/antt/ts1anttl.fd
%{_texmfdistdir}/tex/latex/antt/ts1anttlc.fd
%{_texmfdistdir}/tex/plain/antt/antt-math.tex
%doc %{_texmfdistdir}/doc/fonts/antt/AntykwaTorunska-doc-en-2_03.pdf
%doc %{_texmfdistdir}/doc/fonts/antt/AntykwaTorunska-doc-pl-2_03.pdf
%doc %{_texmfdistdir}/doc/fonts/antt/AntykwaTorunska-doc-src-2_03.zip
%doc %{_texmfdistdir}/doc/fonts/antt/GUST-FONT-NOSOURCE-LICENSE.txt
%doc %{_texmfdistdir}/doc/fonts/antt/MANIFEST.txt
%doc %{_texmfdistdir}/doc/fonts/antt/README
%doc %{_texmfdistdir}/doc/fonts/antt/antt-latex-cyr.tex
%doc %{_texmfdistdir}/doc/fonts/antt/antt-latex-math.tex
%doc %{_texmfdistdir}/doc/fonts/antt/antt-latex-pl.tex
%doc %{_texmfdistdir}/doc/fonts/antt/antt-latex-t2a.tex
%doc %{_texmfdistdir}/doc/fonts/antt/antt-latex-t5.tex
%doc %{_texmfdistdir}/doc/fonts/antt/antt-mathtest.tex
%doc %{_texmfdistdir}/doc/fonts/antt/antt-table.tex
%doc %{_texmfdistdir}/doc/latex/antt/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.08-2
+ Revision: 749254
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.08-1
+ Revision: 717835
- texlive-antt
- texlive-antt
- texlive-antt
- texlive-antt
- texlive-antt


Name: {{{ git_cwd_name name="gdbm-viewer" }}}
Version: {{{ git_cwd_version lead="$(git tag | sed -n 's/^v//p' | sort --version-sort -r | head -n1)" }}}
Release: 1%{?dist}
Summary: Live gdbm database viewer

License: MIT
URL: https://github.com/jcrd/gdbm-viewer
VCS: {{{ git_cwd_vcs }}}
Source0: {{{ git_cwd_pack }}}

Requires: gdbm
Requires: python3-inotify
Requires: python3-tkinter

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%global debug_package %{nil}

%description
Live gdbm database viewer.

%prep
{{{ git_cwd_setup_macro }}}

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/gdbm_viewer
%{python3_sitelib}/gdbm_viewer-*.egg-info/
%{_bindir}/%{name}

%changelog
{{{ git_cwd_changelog }}}

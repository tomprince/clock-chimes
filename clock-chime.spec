Name:           clock-chime
Version:        0.1.2
Release:        1%{?dist}
Summary:        Hourly clock chime.

License:        MIT
URL:            https://github.com/tomprince/clock-chimes
Source0:        clock-chime-%{version}.tar.gz

BuildRequires: systemd flac
Requires:      systemd sound-theme-freedesktop

%description


%prep
%setup -q


%build
cargo build --release
flac -d sounds/*.flac

%install
install -d %{buildroot}%{_bindir}
install -t %{buildroot}%{_bindir} target/release/clock-chime
install -d %{buildroot}%{_userunitdir}
install -t %{buildroot}%{_userunitdir} clock-chime.timer clock-chime.service
install -d %{buildroot}%{_datadir}/sounds/freedesktop/stereo/
install -t %{buildroot}%{_datadir}/sounds/freedesktop/stereo/ sounds/*.wav

%files
%{_bindir}/clock-chime
%{_userunitdir}/clock-chime.*
%{_datadir}/sounds/freedesktop/stereo/*.wav
%doc
%license sounds/_readme_and_license.txt



%changelog
* Wed Feb 15 2017 Tom Prince <tom.prince@ualberta.net>
- Fix processing volume-configuration from command-line.

* Wed Jan 25 2017 Tom Prince <tom.prince@ualberta.net>
- Add volume configuration

* Wed Jan 18 2017 Tom Prince <tom.prince@ualberta.net>
- Add rust implementation.

* Mon Dec  7 2015 Tom Prince <tom.prince@ualberta.net>
- Initial packaging.

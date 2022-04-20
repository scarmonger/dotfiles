# Autogenerated config.py
#
# NOTE: config.py is intended for advanced users who are comfortable
# with manually migrating the config file on qutebrowser upgrades. If
# you prefer, you can also configure qutebrowser using the
# :set/:bind/:config-* commands without having to write a config.py
# file.
#
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Change the argument to True to still load settings configured via autoconfig.yml
# config.load_autoconfig(False)
config.load_autoconfig()

# Always restore open sites when qutebrowser is reopened. Without this
# option set, `:wq` (`:quit --save`) needs to be used to save open tabs
# (and restore them), while quitting qutebrowser in any other way will
# not save/restore the session. By default, this will save to the
# session which was last loaded. This behavior can be customized via the
# `session.default_name` setting.
# Type: Bool
c.auto_save.session = True

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0', 'https://accounts.google.com/*')

# Padding (in pixels) for the statusbar.
# Type: Padding
c.statusbar.padding = {'bottom': 1, 'left': 0, 'right': 0, 'top': 1}

# Search engines which can be used via the address bar.  Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` braces.  The following further
# placeholds are defined to configure how special characters in the
# search terms are replaced by safe characters (called 'quoting'):  *
# `{}` and `{semiquoted}` quote everything except slashes; this is the
# most   sensible choice for almost all search engines (for the search
# term   `slash/and&amp` this placeholder expands to `slash/and%26amp`).
# * `{quoted}` quotes all characters (for `slash/and&amp` this
# placeholder   expands to `slash%2Fand%26amp`). * `{unquoted}` quotes
# nothing (for `slash/and&amp` this placeholder   expands to
# `slash/and&amp`). * `{0}` means the same as `{}`, but can be used
# multiple times.  The search engine named `DEFAULT` is used when
# `url.auto_search` is turned on and something else than a URL was
# entered to be opened. Other search engines can be used by prepending
# the search engine name to the search term, e.g. `:open google
# qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}', 'cf': 'https://cfdocs.org/{}', 'sf': 'https://sfsupport.dataon.com/app/ticket/forms/{}', 'aw': 'https://wiki.archlinux.org/?search={}', 'mdb': 'https://mariadb.com/kb/en/+search/?q={}', 'yts': 'https://www.youtube.com/results?search_query={}','yu':'https://yufid.com/result_yufid.html?search={}'}

# Background color of the tab bar.
# Type: QssColor
c.colors.tabs.bar.bg = '#af6324'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = 'darkgrey'

# Bindings for normal mode
config.bind(',do', 'jseval javascript:/* FormFiller v0.1.12 */var d=document;function i(a){return d.getElementById(a)}function n(a){return d.getElementsByName(a)[0]}function e(a){t=\'change\';if(window.navigator.userAgent.match(/Trident|MSIEs/g)!=null){x=d.createEvent(\'Events\');x.initEvent(t,1,0);}else{x=new Event(t);}a.dispatchEvent(x);}function v(a,v){a.value=v;e(a)}function c(a){a.checked=true;e(a)}v(i("txtAccount"),"indodevniaga");v(i("txtUserName"),"marctinius");v(i("txtPassword"),"4.Spejize");void(0);')
config.bind(',ts', "jseval javascript:function prev() {    var dateObj = document.getElementById('cal_start_date');    var d = new Date(dateObj.value);    do {        d.setDate(d.getDate() - 1);        var i = d.getDay();    }    while (i < 1 || i == 6);    /* 0 = Sun, 1 = Mon, 6 = Sat */    dt = d.getDate() < 10 ?%20%270%27%20+%20d.getDate()%20:%20d.getDate();%20%20%20%20var%20mth%20=%20d.getMonth()%20+%201%20%3C%2010%20?%20%270%27%20+%20(d.getMonth()%20+%201)%20:%20d.getMonth()%20+%201;%20%20%20%20var%20tmp%20=%20mth%20+%20%27/%27%20+%20dt%20+%20%27/%27%20+%20d.getFullYear();%20%20%20%20console.log(tmp);%20%20%20%20dateObj.value%20=%20tmp;%20%20%20%20rubTanggal();}function%20next()%20{%20%20%20%20var%20dateObj%20=%20document.getElementById(%27cal_start_date%27);%20%20%20%20var%20d%20=%20new%20Date(dateObj.value);%20%20%20%20do%20{%20%20%20%20%20%20%20%20d.setDate(d.getDate()%20+%201);%20%20%20%20%20%20%20%20var%20i%20=%20d.getDay();%20%20%20%20}%20%20%20%20while%20(i%20%3C%201%20||%20i%20==%206);%20%20%20%20dt%20=%20d.getDate()%20%3C%2010%20?%20%270%27%20+%20d.getDate()%20:%20d.getDate();%20%20%20%20var%20mth%20=%20d.getMonth()%20+%201%20%3C%2010%20?%20%270%27%20+%20(d.getMonth()%20+%201)%20:%20d.getMonth()%20+%201;%20%20%20%20var%20tmp%20=%20mth%20+%20%27/%27%20+%20dt%20+%20%27/%27%20+%20d.getFullYear();%20%20%20%20console.log(tmp);%20%20%20%20dateObj.value%20=%20tmp;%20%20%20%20rubTanggal();}function%20setDuration()%20{%20%20%20%20/*%20dikurangi%202%20karena%20dipakai%20utk%20%22add%20row%22%20dan%20informasi%20*/%20%20%20%20var%20targetTbl%20=%20document.getElementsByTagName(%27table%27)[8].getElementsByTagName(%27tr%27).length%20-%202;%20%20%20%20/*%20dibagi%202%20karena%20ada%20tr%20lain%20yg%20tidak%20terlihat%20milik%20task%20*/%20%20%20%20rowCount%20=%20targetTbl%20/%202;%20%20%20%20var%20filledRow;%20%20%20%20/*%20Check%20row%20yang%20terisi%20oleh%20task%20*/%20%20%20%20for%20(var%20i%20=%201;%20i%20%3C=%20rowCount;%20i++)%20{%20%20%20%20%20%20%20%20var%20test%20=%20document.getElementById(%27selTest%27%20+%20i).value;%20%20%20%20%20%20%20%20if%20(test%20==%20%27%27)%20{%20%20%20%20%20%20%20%20%20%20%20%20filledRow%20=%20i%20-%201;%20%20%20%20%20%20%20%20%20%20%20%20break;%20%20%20%20%20%20%20%20}%20%20%20%20}%20%20%20%20console.log({%20%20%20%20%20%20%20%20filledRow%20%20%20%20});%20%20%20%20if%20(filledRow%20%3E%200)%20{%20%20%20%20%20%20%20%20/***%20Start%20Time%20-%20End%20Time%20***/%20%20%20%20%20%20%20%20var%20startTime%20=%20document.getElementsByName(%27hidStart_Time2%27)[0].value;%20%20%20%20%20%20%20%20var%20sTime%20=%20startTime.split(%27:%27);%20%20%20%20%20%20%20%20var%20attendTime%20=%20parseInt(sTime[0]);%20%20%20%20%20%20%20%20var%20durationPerTask%20=%20Math.ceil(8%20/%20filledRow);%20%20%20%20%20%20%20%20/*%20Kalau%20EAI,%20belum%20sampai%20jam%208%20*/%20%20%20%20%20%20%20%20if%20(attendTime%20%3C%208)%20{%20%20%20%20%20%20%20%20%20%20%20%20console.log(%27EAI%27);%20%20%20%20%20%20%20%20%20%20%20%20/*%20Kalau%20yang%20di%20isi%20hanya%201%20task%20*/%20%20%20%20%20%20%20%20%20%20%20%20if%20(durationPerTask%20==%208)%20{%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20console.log(%27duration=8%27);%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtStartTask1%27)[0].value%20=%20%2708:00%27;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtEndTask1%27)[0].value%20=%20%2712:00%27;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20/*%20Copy%20Task%20dari%20selTest%201*/%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27cboProject2%27)[0].selectedIndex%20=%20document.getElementsByName(%27cboProject1%27)[0].selectedIndex;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27selStage2%27)[0].selectedIndex%20=%20document.getElementsByName(%27selStage1%27)[0].selectedIndex;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementById(%27selTest%27%20+%202).value%20=%20document.getElementById(%27selTest%27%20+%201).value;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtRemark2%27)[0].value%20=%20document.getElementsByName(%27txtRemark1%27)[0].value;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtStartTask2%27)[0].value%20=%20%2713:00%27;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtEndTask2%27)[0].value%20=%20%2717:00%27;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20/*%20validateForm(document.frmttimesheet);%20*/%20%20%20%20%20%20%20%20%20%20%20%20}%20%20%20%20%20%20%20%20%20%20%20%20/*%20Kalau%20task%20yang%20di%20isi%20lebih%20dari%201%20*/%20%20%20%20%20%20%20%20%20%20%20%20else%20{%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20console.log(%27task%3E1%27);%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20sTask%20=%208;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20for%20(i%20=%201;%20i%20%3C=%20filledRow;%20i++)%20{%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20eTask%20=%20sTask%20+%20durationPerTask;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20(sTask%20%3C%2010)%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtStartTask%27%20+%20i)[0].value%20=%20%270%27%20+%20sTask%20+%20%27:00%27;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtStartTask%27%20+%20i)[0].value%20=%20sTask%20+%20%27:00%27;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20(eTask%20%3C%2010)%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtEndTask%27%20+%20i)[0].value%20=%20%270%27%20+%20eTask%20+%20%27:00%27;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtEndTask%27%20+%20i)[0].value%20=%20eTask%20+%20%27:00%27;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20sTask%20=%20eTask;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20}%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtEndTask%27%20+%20filledRow)[0].value%20=%20eTask%20+%20%27:00%27;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20/*%20validateForm(document.frmttimesheet);%20*/%20%20%20%20%20%20%20%20%20%20%20%20}%20%20%20%20%20%20%20%20}%20%20%20%20%20%20%20%20/*%20Kalau%20LTI%20*/%20%20%20%20%20%20%20%20else%20{%20%20%20%20%20%20%20%20%20%20%20%20console.log(%27LTI%27);%20%20%20%20%20%20%20%20%20%20%20%20if%20(durationPerTask%20==%208)%20{%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20console.log(%27duration=8%27);%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20/*%20jam%20TS%20awal%20ambil%20dari%20jam%20kehadiran%20*/%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtStartTask1%27)[0].value%20=%20document.getElementsByName(%27hidStart_Time2%27)[0].value;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtEndTask1%27)[0].value%20=%20%2712:00%27;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27cboProject2%27)[0].selectedIndex%20=%20document.getElementsByName(%27cboProject1%27)[0].selectedIndex;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27selStage2%27)[0].selectedIndex%20=%20document.getElementsByName(%27selStage1%27)[0].selectedIndex;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementById(%27selTest%27%20+%202).value%20=%20document.getElementById(%27selTest%27%20+%201).value;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtRemark2%27)[0].value%20=%20document.getElementsByName(%27txtRemark1%27)[0].value;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20ketelatan%20=%20attendTime%20-%208;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20endTime%20=%2017%20+%20ketelatan;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20endTime%20=%20endTime%20+%20%27:%27%20+%20sTime[1];%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtStartTask2%27)[0].value%20=%20%2713:00%27;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtEndTask2%27)[0].value%20=%20endTime;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20console.log(endTime);%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20/*%20validateForm(document.frmttimesheet);%20*/%20%20%20%20%20%20%20%20%20%20%20%20}%20else%20{%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20console.log(%27task%3E1%27);%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20sTaskH%20=%20attendTime;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20sTaskM%20=%20parseInt(sTime[1]);%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20(sTaskM%20%3C%2010)%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20sTaskM%20=%20%270%27%20+%20sTaskM;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20for%20(i%20=%201;%20i%20%3C=%20filledRow;%20i++)%20{%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20eTask%20=%20sTaskH%20+%20durationPerTask;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20(sTaskH%20%3C%2010)%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtStartTask%27%20+%20i)[0].value%20=%20%270%27%20+%20sTaskH%20+%20%27:%27%20+%20sTaskM;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtStartTask%27%20+%20i)[0].value%20=%20sTaskH%20+%20%27:%27%20+%20sTaskM;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20(eTask%20%3C%2010)%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtEndTask%27%20+%20i)[0].value%20=%20%270%27%20+%20eTask%20+%20%27:%27%20+%20sTaskM;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtEndTask%27%20+%20i)[0].value%20=%20eTask%20+%20%27:%27%20+%20sTaskM;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20sTaskH%20=%20eTask;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20}%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20remain%20=%208%20-%20durationPerTask%20*%20filledRow;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20eTask%20=%20eTask%20+%20remain;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%27txtEndTask%27%20+%20filledRow)[0].value%20=%20eTask%20+%20%27:%27%20+%20sTaskM;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20/*%20validateForm(document.frmttimesheet);%20*/%20%20%20%20%20%20%20%20%20%20%20%20}%20%20%20%20%20%20%20%20}%20%20%20%20%20%20%20%20%20%20%20%20tlength%20=%20document.getElementById(%22time%22).rows.length%20-%202;%20%20%20%20%20%20%20%20for%20(i%20=%201;%20i%20%3C=%20tlength;%20i++)%20{%20%20%20%20%20%20%20%20%20%20%20%20document.getElementsByName(%22txtRemark%22%20+%20i)[0].value%20=%20document.getElementById(%22selTest%22%20+%20i).value;%20%20%20%20%20%20%20%20}%20%20%20%20%20%20%20%20validateForm(document.frmttimesheet);%20%20%20%20}}/*%20Menambahkan%20tombol%20prev%20dan%20next%20*/var%20node%20=%20document.createElement(%22link%22);node.setAttribute(%27rel%27,%20%27stylesheet%27);node.setAttribute(%27href%27,%20%27https://www.w3schools.com/w3css/4/w3.css%27);document.getElementsByTagName(%27head%27)[0].appendChild(node);var%20node%20=%20document.createElement(%22div%22);node.setAttribute(%27class%27,%20%27w3-clear%20nextprev%27);node.innerHTML%20=%20%27%3Ca%20class=%22w3-btn%22%20href=%22javascript:prev()%22%20id=%22prev%22%20accesskey=%22p%22%3E%E2%9D%AE%3Cspan%20class=%22w3-hide-small%22%3E%20Previous%3C/span%3E%3C/a%3E%3Ca%20class=%22w3-btn%22%20href=%22javascript:next()%22%20id=%22next%22%20accesskey=%22n%22%3E%3Cspan%20class=%22w3-hide-small%22%3ENext%3C/span%3E%E2%9D%AF%3C/a%3E%3Ca%20class=%22w3-btn%22%20href=%22javascript:setDuration()%22%20accesskey=%22s%22%3E%3Cspan%20class=%22w3-hide-small%22%3ESet%20Timesheet%3C/span%3E%3C/a%3E%27;var%20tmpEl%20=%20document.getElementsByTagName(%27fieldset%27)[0].getElementsByTagName(%27div%27);if%20(tmpEl.length%20==%200)%20%20%20%20document.getElementsByTagName(%27fieldset%27)[0].appendChild(node);var%20tRow%20=%20document.getElementById(%22time%22).getElementsByTagName(%22tr%22),%20%20%20%20rowCount%20=%20(tRow.length%20-%202)%20/%202;for%20(i%20=%201;%20i%20%3C=%20rowCount;%20i++)%20{%20%20%20%20var%20j%20=%20i%20+%201;%20%20%20%20document.getElementsByName(%22txtStartTask%22%20+%20i)[0].setAttribute(%22tabindex%22,%20i);%20%20%20%20document.getElementsByName(%22txtEndTask%22%20+%20i)[0].setAttribute(%22tabindex%22,%20j);%20%20%20%20var%20st%20=%20document.getElementsByName(%22txtStartTask%22%20+%20i)[0],%20%20%20%20%20%20%20%20en%20=%20document.getElementsByName(%22txtEndTask%22%20+%20i)[0];%20%20%20%20st.onkeydown%20=%20function%20()%20{%20%20%20%20%20%20%20%20switch%20(window.event.keyCode)%20{%20%20%20%20%20%20%20%20%20%20%20%20case%2038:%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20a%20=%20parseInt(this.value.substring(0,%202));%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20tmp1%20=%20a%20+%201%20+%20this.value.substring(2);%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%204%20%3E%20tmp1.length%20&&%20(tmp1%20=%20%220%22%20+%20tmp1);%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20this.value%20=%20tmp1;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20tmp2%20=%20this.name.replace(%22txtStartTask%22,%20%22%22);%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20b%20=%20document.getElementsByName(%22txtEndTask%22%20+%20tmp2)[0],%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20c%20=%20parseInt(b.value.substring(0,%202));%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20c%20%3C=%20a%20&&%20(b.value%20=%20this.value);%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20break;%20%20%20%20%20%20%20%20%20%20%20%20case%2040:%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20a%20=%20parseInt(this.value.substring(0,%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%202)),%20tmp1%20=%20a%20-%201%20+%20this.value.substring(2),%204%20%3E%20tmp1.length%20&&%20(tmp1%20=%20%220%22%20+%20tmp1),%20this.value%20=%20tmp1,%20tmp2%20=%20this.name.replace(%22txtStartTask%22,%20%22%22),%20b%20=%20document.getElementsByName(%22txtEndTask%22%20+%20tmp2)[0],%20c%20=%20parseInt(b.value.substring(0,%202)),%20c%20%3C%20a%20&&%20(b.value%20=%20this.value);%20%20%20%20%20%20%20%20}%20%20%20%20};%20%20%20%20en.onkeydown%20=%20function%20()%20{%20%20%20%20%20%20%20%20switch%20(window.event.keyCode)%20{%20%20%20%20%20%20%20%20%20%20%20%20case%2038:%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20a%20=%20parseInt(this.value.substring(0,%202));%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20tmp1%20=%20a%20+%201%20+%20this.value.substring(2);%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%204%20%3E%20tmp1.length%20&&%20(tmp1%20=%20%220%22%20+%20tmp1);%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20this.value%20=%20tmp1;%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20tmp2%20=%20this.name.replace(%22txtEndTask%22,%20%22%22);%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20b%20=%20document.getElementsByName(%22txtStartTask%22%20+%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20tmp2)[0],%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20c%20=%20parseInt(b.value.substring(0,%202));%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20c%20%3E%20a%20&&%20(b.value%20=%20this.value);%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20break;%20%20%20%20%20%20%20%20%20%20%20%20case%2040:%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20a%20=%20parseInt(this.value.substring(0,%202)),%20tmp1%20=%20a%20-%201%20+%20this.value.substring(2),%204%20%3E%20tmp1.length%20&&%20(tmp1%20=%20%220%22%20+%20tmp1),%20this.value%20=%20tmp1,%20tmp2%20=%20this.name.replace(%22txtEndTask%22,%20%22%22),%20b%20=%20document.getElementsByName(%22txtStartTask%22%20+%20tmp2)[0],%20c%20=%20parseInt(b.value.substring(0,%202)),%20c%20%3E=%20a%20&&%20(b.value%20=%20this.value);%20%20%20%20%20%20%20%20}%20%20%20%20};%20%20%20%20st.onfocus%20=%20function%20()%20{%20%20%20%20%20%20%20%20this.value%20=%20this.value.replaceAll(%22:%22,%20%22%22);%20%20%20%20};%20%20%20%20en.onfocus%20=%20function%20()%20{%20%20%20%20%20%20%20%20this.value%20=%20this.value.replaceAll(%22:%22,%20%22%22);%20%20%20%20};%20%20%20%20st.onblur%20=%20function%20()%20{%20%20%20%20%20%20%20%20var%20a%20=%20this.value.substring(0,%202),%20%20%20%20%20%20%20%20%20%20%20%20b%20=%20this.value.substring(2);%20%20%20%20%20%20%20%200%20%3C%20a.length%20&&%20(this.value%20=%20%20%20%20%20%20%20%20%20%20%20%20a%20+%20%22:%22%20+%20b);%20%20%20%20};%20%20%20%20en.onblur%20=%20function%20()%20{%20%20%20%20%20%20%20%20var%20a%20=%20this.value.substring(0,%202),%20%20%20%20%20%20%20%20%20%20%20%20b%20=%20this.value.substring(2);%20%20%20%20%20%20%20%200%20%3C%20a.length%20&&%20(this.value%20=%20a%20+%20%22:%22%20+%20b);%20%20%20%20};};")
# config.bind('xs', 'config-cycle statusbar.show in-mode always')
config.bind('xs', 'config-cycle statusbar.hide false true')
config.bind('xt', 'config-cycle tabs.show always switching')
# config.bind('xx', 'config-cycle statusbar.show in-mode always;; config-cycle tabs.show always switching')
config.bind('xx', 'config-cycle statusbar.hide false true; config-cycle tabs.show always switching')

config.bind('K', 'tab-next')
config.bind('J', 'tab-prev')


# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['tkinter_ui.py', 'about.py', 'default.py', 'multicast.py', 'hotel.py', 'subscribe.py', 'online_search.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('../config/config.ini', 'config'),
        ('../config/demo.txt', 'config'),
        ('../config/rtp', 'config/rtp'),
        ('../updates/multicast/multicast_map.json', 'updates/multicast'),
        ('../updates/multicast/multicast_region_result.json', 'updates/multicast'),
        ('../static/images/favicon.ico', 'static/images'),
        ('../static/images/appreciate.jpg', 'static/images'),
        ('../static/images/settings_icon.png', 'static/images'),
        ('../static/images/hotel_icon.png', 'static/images'),
        ('../static/images/multicast_icon.png', 'static/images'),
        ('../static/images/subscribe_icon.png', 'static/images'),
        ('../static/images/online_search_icon.png', 'static/images'),
        ('about.py', '.'),
        ('default.py', '.'),
        ('multicast.py', '.'),
        ('hotel.py', '.'),
        ('subscribe.py', '.'),
        ('online_search.py', '.'),
        ('select_combobox.py', '.'),
        ('../version.json', '.')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='update-tool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='../static/images/favicon.ico'
)
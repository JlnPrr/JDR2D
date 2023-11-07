# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=[('D:/Formations_2021_2022/GameProjects/RPG2D_V1.6/RPG2D/map *.tmx', '.'), ('D:/Formations_2021_2022/GameProjects/RPG2D_V1.6/RPG2D/map *.tsx', '.'), ('D:/Formations_2021_2022/GameProjects/RPG2D_V1.6/RPG2D/map *.png', '.'), ('D:/Formations_2021_2022/GameProjects/RPG2D_V1.6/RPG2D/sprites *.png', '.'), ('D:/Formations_2021_2022/GameProjects/RPG2D_V1.6/RPG2D/dialogs *.png', '.'), ('D:/Formations_2021_2022/GameProjects/RPG2D_V1.6/RPG2D/dialogs *.ttf', '.'), ('D:/Formations_2021_2022/GameProjects/RPG2D_V1.6/RPG2D/sound *.mp3', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

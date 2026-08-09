#define MyAppName "Utility Manager"
#define MyAppVersion "0.1.1"
#define MyAppExeName "um.exe"

[Setup]
AppId={{11AA8720-8637-4480-930E-170B488373ED}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={autopf}\{#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName}
; "ArchitecturesAllowed=x64compatible" specifies that Setup cannot run
; on anything but x64 and Windows 11 on Arm.
ArchitecturesAllowed=x64compatible
; "ArchitecturesInstallIn64BitMode=x64compatible" requests that the
; install be done in "64-bit mode" on x64 or Windows 11 on Arm,
; meaning it should use the native 64-bit Program Files directory and
; the 64-bit view of the registry.
ArchitecturesInstallIn64BitMode=x64compatible
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
; Remove the following line to run in administrative install mode (install for all users).
PrivilegesRequired=lowest
OutputDir=dist
OutputBaseFilename=Utility Manager Setup
SetupIconFile=.\assets\icon.ico
SolidCompression=yes
WizardStyle=modern dynamic

[Registry]
Root: HKCU; Subkey: "Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app};{app}\tools"; Flags: preservestringtype

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: ".\dist\um\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: ".\dist\um\_internal\*"; DestDir: "{app}\_internal"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"

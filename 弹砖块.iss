;汉化:MonKeyDu 
;由 Inno Setup 脚本向导 生成的脚本,有关创建 INNO SETUP 脚本文件的详细信息，请参阅文档！!

#define MyAppName "弹砖块"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "纸盒工作室"
#define MyAppExeName "弹砖块.exe"

[Setup]
;注意:AppId 的值唯一标识此应用程序。请勿在安装程序中对其他应用程序使用相同的 AppId 值。
;（若要生成新的 GUID，请单击“工具”|”在 IDE 中生成 GUID）。
AppId={{65F98E07-4263-4476-AEB5-8C184CBEFFF4}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName}
DisableWelcomePage=no
DisableReadypage=yes
;下行注释，指定安装程序无法运行，除 Arm 上的 x64 和 Windows 11 之外的任何平台上.
ArchitecturesAllowed=x64compatible
;WizardImageFile=侧图186x356.bmp
;WizardSmallImageFile=顶图165x54.bmp,
;WizardSmallImageFile=顶图54x54.bmp
;下行注释，强制安装程序在 64 位系统上，但不强制以 64 位模式运行.
ArchitecturesInstallIn64BitMode=x64compatible
DisableProgramGroupPage=yes
;取消下行前面 ; 符号，在非管理安装模式下运行（仅为当前用户安装）.
;PrivilegesRequired=lowest
OutputDir=D:\桌面
OutputBaseFilename=弹砖块setup
SolidCompression=yes
WizardStyle=modern
WizardImageFile=D:\Temp\logo.bmp
WizardSmallImageFile=D:\Temp\logo.bmp
[Languages]
Name: "chs"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: checkablealone

[Files]
Source: "D:\桌面\弹砖块\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion

[code]
procedure InitializeWizard();
begin
WizardForm.LICENSEACCEPTEDRADIO.checked:= true;
end;

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent


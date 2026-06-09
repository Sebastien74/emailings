param([string]$HtmlPath,[string]$ImagesDir,[string]$OutOft,[string]$SubjectEnc)
$ErrorActionPreference='Stop'
$subject=[System.Net.WebUtility]::HtmlDecode($SubjectEnc)
$html=Get-Content -LiteralPath $HtmlPath -Raw -Encoding UTF8
$html=$html -replace 'src="images/','src="cid:'
$o=New-Object -ComObject Outlook.Application
$m=$o.CreateItem(0); $m.Subject=$subject; $m.BodyFormat=2; $m.HTMLBody=$html
# Forcer le codepage UTF-8 du corps (evite l'auto-detection CJK -> caracteres chinois)
$CPID="http://schemas.microsoft.com/mapi/proptag/0x3FDE0003"
try{ $m.PropertyAccessor.SetProperty($CPID,65001) }catch{ Write-Output ("WARN cpid: "+$_.Exception.Message) }
$CID="http://schemas.microsoft.com/mapi/proptag/0x3712001F"; $HID="http://schemas.microsoft.com/mapi/proptag/0x7FFE000B"
foreach($img in (Get-ChildItem -LiteralPath $ImagesDir -File | ?{$_.Extension -match '\.(jpg|jpeg|png|gif)$'})){
 $a=$m.Attachments.Add($img.FullName,1,$null,$img.Name)
 try{$p=$a.PropertyAccessor;$p.SetProperty($CID,$img.Name);$p.SetProperty($HID,$true)}catch{}
}
$m.SaveAs($OutOft,2); Write-Output ("OFT "+$OutOft+" subj="+$subject)
$m.Close(1)|Out-Null

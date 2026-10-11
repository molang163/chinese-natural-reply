# 110 · 电脑或软件问题

> 用户：Win11 的 C 盘只剩 6G 了，但我也没装啥大东西啊。有没有比较稳的清理办法，别让我一顿删完电脑起不来了。

出题人：GPT（不知道评分标准）

## 本仓库（发布版）

有。**先用 Win11 自带清理，再处理自己的大文件，这个顺序比较稳。** 软件装得少，更新残留、缓存和下载文件也会慢慢占满 C 盘。

按下面做：

1. **先清临时文件**  
   按 `Win + I` → **系统 → 存储 → 临时文件**，等扫描结束。先选“临时文件”“缩略图”“传递优化文件”这些缓存，再点“删除文件”。这是微软提供的清理方式。[微软操作说明](https://support.microsoft.com/zh-cn/windows/experience/performance-optimization/tips-to-improve-pc-performance-in-windows)

2. **这几项要单独看，别全部勾选**  
   **“下载”**里面是你下载的真实文件，先别选；**“回收站”**先打开检查；**“以前的 Windows 安装”**先留着，删掉就无法回退到上一个 Windows 版本了。[微软说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

3. **再找占空间的大头**  
   回到“存储”，看看“已安装的应用”“临时文件”“其他”“系统和保留”各占多少。自己的视频、压缩包、旧安装包可以移到 D 盘或移动硬盘，确认能打开后再删 C 盘那份。应用要通过“设置 → 应用 → 已安装的应用”卸载。

**别手动清空 `Windows`、`ProgramData`、`AppData`，尤其别碰 `WinSxS`、`Installer`；虚拟内存、休眠文件和还原点也先留着。** 微信、QQ 占得多，就从软件自己的存储管理里清缓存，聊天记录和附件逐项看。

你可以先发一张 **“设置 → 系统 → 存储”** 的截图，我帮你看该从哪一项下手，通常比到处找文件删更省事。

## 测试版（发布前的同一份规则，例子里还有个人信息）

有。**先用 Windows 自带清理，再处理自己的大文件，最稳妥。** 没装大软件，更新缓存、下载文件和聊天软件里的图片视频也会慢慢占满 C 盘。

按这个顺序来：

1. **先看谁占空间。** 按 `Win + I` → **系统 → 存储**，等统计完成，看“临时文件”“已安装的应用”“其他”分别占多少。

2. **清系统列出的缓存。** 进入 **临时文件**，先勾选“临时文件”“缩略图”“传递优化文件”等缓存项，再点“删除文件”。**不要全选**：“下载”是你下载的真实文件；“回收站”先检查内容；“以前的 Windows 安装”先留着，删掉会失去回退到上一版本的机会。[微软清理说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

3. **处理自己的大文件。** 在“下载”、桌面、视频文件夹里按大小排序。需要保留的可以先复制到 D 盘或移动硬盘，确认能打开后，再删除 C 盘原件。微信、QQ、浏览器的缓存，从软件自己的设置里清；聊天记录和接收的文件先看清楚。

4. **以后自动清临时文件。** 在“存储”里打开 **存储感知**，把自动清理“下载”设为 **从不**；如果你习惯从回收站找回东西，回收站也设为“从不”，自己检查后清空。[微软设置说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense)

**别手动删 `C:\Windows` 里的文件，尤其是 `WinSxS`、`Installer`；也别整文件夹删 `Program Files` 或 `AppData`。** 软件要卸载就走“设置 → 应用”，系统还原点也先保留。

我建议先争取留出 **20GB 以上**。如果清完还是很挤，把“存储”页各项占用的截图发来，我帮你找大头。

## 原版（不加 skill）

有，**先用 Win11 自带的清理功能，逐项确认，比按网上教程手删系统文件稳得多。** 没装大软件也可能积累更新文件、缓存和下载文件，先看占用再清。

**1. 先清系统认可的临时文件**

按 **Win＋I → 系统 → 存储 → 临时文件**，等扫描完成，别直接全选：

| 项目 | 建议 |
|---|---|
| 临时文件、缩略图、传递优化文件 | 可以优先清理 |
| Windows 更新清理 | 更新完成、重启后使用正常，再清 |
| 下载 | **先不勾**，这里可能是你保存的文件 |
| 回收站 | 打开检查，确认没有需要恢复的东西再清 |
| 以前的 Windows 安装 | 先保留，删后会失去回退旧版本的机会 |

确认勾选后点“删除文件”；清理过程中如果系统要求重启，就正常重启。这些自带入口和回退限制可参考[微软清理指南](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)。

**2. 再处理你认识的大文件**

检查“下载”和“视频”文件夹里的安装包、压缩包、视频。需要保留的，可以先复制到有空间的 D 盘或移动硬盘，**确认能打开后，再删 C 盘原件并清空回收站**。[微软说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

软件要通过“设置 → 应用 → 已安装的应用”卸载；不要把软件安装目录直接拖到 D 盘。

**3. 设置自动清理，避免又满**

进入 **存储 → 存储感知**，启用临时文件清理。为了保守，“下载文件夹自动删除”和“回收站自动删除”都可以设为“从不”，自己检查后手动处理。[微软存储感知说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense)

**几个地方别靠手删来腾空间：**`Windows`、`WinSxS`、`Windows\Installer`、`Program Files`，以及整个 `AppData`。尤其微软明确警告，手删 WinSxS 可能导致无法启动或更新。[微软说明](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)

先做第一步。如果释放得很少，把“存储”和“临时文件”页面截图发来，我帮你判断具体是哪一项占空间、哪些能动。

## talk-normal

有。**先用 Win11 自带的“存储”清理，再处理确认过的个人大文件**，这条路线比较稳。更新文件、缓存和下载内容也会逐渐占空间。

按这个顺序来，每做完一步看一下剩余空间：

1. **先看空间花在哪儿。**  
   按 `Win + I` → **系统 → 存储**，等统计完成，查看“临时文件”“应用”“其他”“系统和保留”各占多少。[微软操作说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

2. **清一轮低风险的临时文件。**  
   点进“临时文件”，优先选择**临时文件、缩略图、传递优化文件、DirectX 着色器缓存**，页面出现哪些就处理哪些。**“下载”保持取消勾选**；回收站先核对内容；**“以前的 Windows 安装”先保留**，它保存着回退旧版系统需要的文件。[微软关于旧版安装的说明](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/delete-your-previous-version-of-windows)

3. **搬走确认过的大文件。**  
   查看“清理建议”，重点检查下载里的安装包、压缩包、视频。需要留存的文件先复制到 D 盘或移动硬盘，确认复制完整、能够打开，再删除 C 盘原件并清空对应回收站内容。软件缓存优先通过软件自身的“缓存／存储管理”处理。[微软清理建议](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

4. **设置后续自动清理。**  
   开启“存储感知”，让它处理临时文件；下载文件夹的清理周期设为**“从不”**。为了保留人工核对的机会，回收站也可以设为“从不”，以后手动清理。[微软存储感知说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense)

**系统目录统一交给 Windows 管理。** `C:\Windows`，尤其其中的 `WinSxS`、`Installer`，以及 `Program Files`、`ProgramData`、整个 `AppData` 都保留原样。微软明确提示，手动删 WinSxS 可能损坏启动和更新，删 Installer 会影响软件维修、更新和卸载。[WinSxS 说明](https://learn.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)、[Installer 说明](https://learn.microsoft.com/en-us/troubleshoot/windows-client/application-management/missing-windows-installer-cache)

先完成前两步；建议把可用空间提高到 **20GB 左右**，给日常使用和更新留些余量。

## 好好说话 haohao-shuohua

有。**先用 Windows 自带工具清理，再处理自己的大文件，风险比较低。**没装大软件，更新残留、缓存和下载文件也可能占掉不少空间。

按这个顺序来：

1. **先看是谁占了空间。**按 `Win + I` →「系统」→「存储」，等统计完成，看“临时文件”“安装的应用”“系统和保留”分别多大。

2. **清理临时文件，但别全选。**进入「临时文件」，第一轮只选“临时文件”“缩略图”和缓存类项目，再点「删除文件」。**“下载”和“回收站”先取消勾选**，里面可能有你要留的东西。“以前的 Windows 安装”也先留着，删除后就不能通过它回退到升级前的系统了。[微软清理说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

3. **处理确定认识的大文件。**看看“下载”、桌面和视频文件夹里的安装包、压缩包、视频。有 D 盘或移动硬盘的话，先复制过去，确认能打开，再删除 C 盘原件。回收站也先检查，再清空。软件要从「设置 → 应用 → 安装的应用」卸载，别直接删安装目录。

4. **设置自动清理。**在「存储感知」里开启临时文件清理，把“下载文件夹”和“回收站”的自动删除都设为“从不”，继续自己检查后清理。[存储感知设置](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense)

**先别手动删 `C:\Windows` 下的东西，尤其是 `WinSxS` 和 `Installer`，也别把整个 `AppData` 当缓存清空。**微软明确提醒，手动删除 WinSxS 文件可能导致无法启动。[微软说明](https://learn.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)

如果第一轮只清出一点，把 **C 盘总容量，以及“临时文件／安装的应用／系统和保留”的大小**发我，就能继续判断该从哪里下手。

## Humanizer-zh

有。**先用 Windows 自带清理，再处理自己的大文件，是比较稳的顺序。**没装大软件也可能占满：系统更新残留、聊天软件缓存、休眠和虚拟内存文件都可能占空间，具体要看分类。

按下面顺序来：

1. **先看占用，再清临时文件**

   按 **Win＋I → 系统 → 存储**，等统计完成，看看哪一类最大，再进入 **“临时文件”**。

   可优先选：**临时文件、缩略图、传递优化文件、错误报告**。Windows 更新清理也交给这里处理；如果刚更新后电脑有异常，先留着。

   **不要直接全选：**
   - **下载**：里面可能是你保存的资料。
   - **回收站**：先打开确认没有需要恢复的文件。
   - **以前的 Windows 安装**：第一轮先留着，删除后就失去回退到上一版 Windows 的机会。[微软清理说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

2. **检查自己的文件和软件缓存**

   到“下载”、桌面、视频文件夹，按大小排序。大视频、压缩包、旧安装包可以移到 D 盘或移动硬盘；重要资料先复制，确认能打开，再删 C 盘原件。

   微信、QQ、浏览器等，**从软件自己的设置里清缓存**，看清“缓存”和“聊天记录／文件”的区别。卸载软件也走“设置 → 应用 → 已安装的应用”，不要直接删安装目录。

3. **设置自动清理**

   在“存储 → 存储感知”里开启临时文件清理；**下载文件夹的自动删除设为“从不”**。回收站也可先设为“从不”，由你手动检查清空。[微软设置说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense)

**别手动清空 `C:\Windows`、`ProgramData`、`AppData`，也别直接删 `pagefile.sys`、`hiberfil.sys`。**尤其 `WinSxS`，微软明确说明乱删可能导致无法启动或更新。[微软说明](https://learn.microsoft.com/en-au/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)

建议第一轮先争取留出 **15～20 GB**。如果清完还是很少，把**“存储”页面截图和 C 盘总容量**发来，就能根据实际占用判断下一步。

## humanizer（英文原版）

有。**先用 Windows 自带清理工具，逐项看清楚再删，比较稳。** 没装大软件，也可能被更新文件、缓存、聊天附件占满，先看占用统计。

按这个顺序来：

1. **清理系统识别的临时文件**  
   按 `Win + I` → **系统 → 存储 → 临时文件**，等扫描结束。第一轮这样选：

   | 项目 | 建议 |
   |---|---|
   | 临时文件、缩略图、DirectX 着色器缓存 | 可以先清 |
   | 下载 | **先别勾**，这里可能是你保存的资料 |
   | 回收站 | 打开检查，确认没有要恢复的再清 |
   | Windows 更新清理 | 最近更新后有异常就先留着 |
   | 以前的 Windows 安装／Windows.old | 第一轮先留着，删除后无法回退到此前版本 |

   确认勾选项后点“删除文件”，不要全选。也可以在开始菜单搜索“磁盘清理”，选 C 盘 →“清理系统文件”，按同样原则检查。[微软清理指南](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

2. **空间仍少，就查占用大头**  
   回到“存储”，看“已安装的应用”“临时文件”“其他”“系统和保留”各占多少。微信、QQ、浏览器、网盘的缓存，优先在对应软件的设置里清理；注意区分缓存和聊天记录、已下载文件。自己认识的视频、安装包等可以移到 D 盘或外置盘，先复制并确认能打开，再删原件。

3. **设置后续自动清理**  
   在“存储感知”里开启临时文件清理，把**下载文件夹自动删除设为“从不”**；回收站如果经常用来找回文件，也设为“从不”。[微软存储感知说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense)

**别手动删 `C:\Windows` 里的大文件，尤其是 `WinSxS` 和 `Installer`；也别整目录清空 `AppData`。** 微软明确提醒，误删 WinSxS 可能导致无法启动；删 Installer 缓存可能让软件无法更新、修复或卸载。[WinSxS 说明](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)、[Installer 说明](https://learn.microsoft.com/en-us/troubleshoot/windows-client/application-management/missing-windows-installer-cache)

先做第 1 步，看看能释放多少。清完仍紧张的话，把“存储”页面的分类容量或截图发来，我可以继续帮你判断哪些值得清。

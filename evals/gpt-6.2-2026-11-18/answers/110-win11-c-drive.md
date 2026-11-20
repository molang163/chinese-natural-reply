# 110 · 电脑或软件问题

> 用户：Win11 的 C 盘只剩 6G 了，但我也没装啥大东西啊。有没有比较稳的清理办法，别让我一顿删完电脑起不来了。

## GPT-6.2 Sol

### 本仓库 + AGENTS.md

有。先用 Win11 自带的「存储」清理，`C:\Windows` 和 `C:\Program Files` 里的文件别手动删。

1. 按 **Win + I**，打开 **系统 → 存储 → 临时文件**，等它算完。先勾「临时文件」「缩略图」「传递优化文件」。最近更新后电脑用着正常的话，也可以勾「Windows 更新清理」。[微软清理步骤](https://support.microsoft.com/zh-cn/windows/experience/performance-optimization/tips-to-improve-pc-performance-in-windows#bkmk_freediskspace)
2. 点 **删除文件**前，确认「下载」没勾上，里面是你自己的文件。回收站先打开看一眼再清。「以前的 Windows 安装」先留着，删掉就不能回退到升级前的版本了。[微软的回退说明](https://support.microsoft.com/zh-cn/windows/deployment/install-upgrade/delete-your-previous-version-of-windows)
3. 清完还缺空间，就回到 **存储** 看哪一项占得最多。要是下载或视频里有几个大文件，可以搬到 D 盘或移动硬盘。也可以把占用最大的两三项和大小发我，我帮你看看从哪项下手。[微软存储设置说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/storage-settings-in-windows)

### 本仓库（只装 skill）

有。先用 Win11 自带的清理工具，挑几项缓存清掉，再看 C 盘还剩多少。

1. **先清临时文件。** 按 **Win + I**，进 **系统 → 存储 → 临时文件**。等它算完，第一轮只勾「临时文件」「缩略图」「传递优化文件」里有的项，再点「删除文件」。 [微软的清理说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)
2. **「下载」和「回收站」先留着。** 翻一遍里面的文件再决定。看到「以前的 Windows 安装」也先跳过，刚升级后想退回旧版本会用到它。
3. **清完还紧，就找占空间的大文件。** 回到 **存储 → 清理建议 → 大型或未使用的文件**。没装多少软件，旧安装包、视频、聊天软件存下来的文件也能攒不少。要留的可以先复制到 D 盘或移动硬盘，确认能打开，再删 C 盘那份。

系统文件交给 Windows 的清理工具。尤其是 `C:\Windows\WinSxS`，看着再大也别进去手动删。 [微软的 WinSxS 说明](https://learn.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)

### talk-normal

用 **Win11 自带的存储设置**最稳。先清能重新生成的缓存，再看 C 盘到底是哪一类文件占得多。

1. **先清缓存。** 按 `Win + I` → **系统 → 存储 → 临时文件**。等扫描完，第一轮只勾选**临时文件、缩略图、传递优化文件**，再点「删除文件」。 [微软的清理步骤](https://support.microsoft.com/zh-cn/windows/experience/performance-optimization/tips-to-improve-pc-performance-in-windows)
2. **核对勾选项。** 「下载」里是你自己下载的文件，先取消勾选。回收站打开看一遍，确认里面的文件都可以丢再清空。「以前的 Windows 安装（`Windows.old`）」先留着，它用于升级后回退。 [微软的磁盘清理说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)
3. **找占空间的大文件。** 回到「存储」看哪一类最大，再点 **清理建议 → 大型或未使用的文件**。优先看旧安装包、压缩包和录屏，要留的可以移到 D 盘或移动硬盘。聊天软件占得多，就用软件里的存储管理清缓存。 [微软的存储设置说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/storage-settings-in-windows)

**系统目录交给 Windows 管理。** 手动删 `C:\Windows\WinSxS` 里的文件可能导致系统无法启动，`C:\Windows\Installer` 里的文件则用于软件更新、修复和卸载。 [WinSxS 说明](https://learn.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11) · [Installer 说明](https://learn.microsoft.com/zh-cn/troubleshoot/windows-client/application-management/missing-windows-installer-cache)

### 原版（不加 skill）

C 盘只剩 6 GB，先用 Win11 自带的「存储」清理。就算没装大软件，Windows 更新文件、下载的东西和聊天软件存下来的图片视频也可能占不少空间。

1. **先清能重新生成的缓存。** 按 `Win + I` → **系统 → 存储 → 临时文件**，等扫描完成。第一轮只勾选「临时文件」「缩略图」「传递优化文件」这几项，看到哪项就选哪项，再点「删除文件」。 [微软清理说明](https://support.microsoft.com/zh-cn/windows/experience/performance-optimization/tips-to-improve-pc-performance-in-windows)

2. **这几项先留着。** 「下载」里是你自己下载的文件，回收站也先打开确认一遍。「以前的 Windows 安装」删掉后，就无法用系统自带的功能退回升级前的版本。刚更新完的话，「Windows 更新清理」也可以等系统用着稳定了再考虑。 [微软关于释放空间和版本回退的说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

3. **清完还不够，就找最大的文件。** 回到 **系统 → 存储 → 清理建议**，看「大型或未使用的文件」。优先把自己认识的大视频、压缩包或旧安装包移到 D 盘或移动硬盘。重要文件先复制过去，确认能打开，再删 C 盘原件。 [微软清理建议](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

**别在资源管理器里手动删 `C:\Windows` 里的东西**，尤其是 `WinSxS` 和 `Installer`。前者误删可能导致系统无法启动，后者误删可能让软件无法更新、修复或卸载。 [WinSxS 说明](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11) · [Installer 缓存说明](https://learn.microsoft.com/zh-cn/troubleshoot/windows-client/application-management/missing-windows-installer-cache)

如果第一轮只腾出一点空间，把「存储」页占用最大的三项和各自的大小发我，我可以帮你判断下一步该查哪里。

## GPT-6.2 Astra

### 本仓库 + AGENTS.md

有。按 **Win + I** 打开设置，进 **系统 → 存储**，先看 C 盘哪一类占得最多。就算没装大软件，更新缓存、下载的视频和压缩包也会慢慢占满 C 盘。

1. 点 **临时文件**，等它算完。这一轮只勾列表里的 **临时文件、缩略图、传递优化文件**，这几项可以放心让 Windows 清理。[微软的缓存清理说明](https://support.microsoft.com/zh-cn/windows/deployment/updates-lifecycle/delivery-optimization-in-windows)
2. 点 **删除文件** 前再看一眼，**下载、回收站、以前的 Windows 安装** 先别勾。“下载”里是你自己存的文件，回收站里还能找回误删的东西，旧安装则是升级后回退系统用的。[微软的磁盘清理说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)
3. 如果清完还只剩几个 G，就打开 **下载** 文件夹，按 **大小** 排序，把认得的大视频、压缩包移到 D 盘或移动硬盘。像 `C:\Windows`、`Program Files` 这样的目录，留给系统和软件自己管理就好。

### 本仓库（只装 skill）

有。先按 **Win + I** 打开设置，进 **系统 → 存储**，看看 C 盘哪一项占得最多。就算没装大软件，更新缓存、下载的安装包和视频也会慢慢占地方。[微软的存储设置说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/storage-settings-in-windows)

1. **先清缓存。** 点进“临时文件”，等它算完。这次只勾列表里的 **“临时文件”“缩略图”“传递优化文件”**。从这里清这几项，不影响正常开机。
2. **点“删除文件”前，再看一眼勾选项。** “下载”和“回收站”先留空，里面可能有你还要的文件。如果看到“以前的 Windows 安装”，也先留着，刚升级后想退回上一版要用到它。[微软的清理说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)
3. **如果只清出几百 MB，** 打开自己的“下载”和“视频”文件夹，按大小排序。想留的大文件可以先复制到 D 盘或移动硬盘，确认副本能打开，再删 C 盘原件。最后去回收站只删对应的那几项，空间就腾出来了。

`C:\Windows`、`Program Files`、`AppData` 这些文件夹别手动整夹删。如果清完还是只剩几 GB，把“存储”里最大的三项和各自的大小发来，我帮你看下一步清哪里。

### talk-normal

有。**先用 Win11 自带的「存储」清缓存，`C:\Windows` 和 `Program Files` 交给系统管理。**

1. 按 `Win + I` 打开 **系统 → 存储**，等 C 盘统计完成，点「显示更多类别」看哪项占得最多。软件装得少，更新缓存、下载的压缩包和视频也可能占不少空间。[微软存储设置说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/storage-settings-in-windows)
2. 点开「临时文件」，第一轮只勾列表里出现的「临时文件」「缩略图」和「传递优化文件」。**确认「下载」「回收站」「以前的 Windows 安装」都留空**，再点「删除文件」。「下载」里是你自己存的文件，回收站里的东西还能找回，旧版安装则留给升级后回退用。[微软版本回退说明](https://support.microsoft.com/zh-cn/windows/deployment/install-upgrade/delete-your-previous-version-of-windows)
3. 清完再看 C 盘剩余空间。要是还只剩几个 GB，打开「下载」和「视频」，按大小排序。把认得的大文件先复制到 D 盘或移动硬盘，**从新位置打开，确认正常后**，再删 C 盘原件，最后到回收站只清掉刚确认的那几项。[微软释放空间指南](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

### 原版（不加 skill）

比较稳的做法是**先看 C 盘被什么占了，再用 Windows 自带的工具清缓存**。即使没装大软件，更新缓存、下载的文件和回收站也可能攒出不少空间。

1. **先看占用。** 按 `Win + I` 打开「设置 → 系统 → 存储」，等 C 盘统计完成。点「显示更多类别」，看哪几项最大。如果「临时文件」只有几百 MB，就直接看第 3 步。[微软的存储设置说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/storage-settings-in-windows)
2. **清缓存时别全选。** 点进「临时文件」，第一轮只勾「临时文件」「缩略图」「传递优化文件」这几项，再点「删除文件」。**让「下载」「回收站」「以前的 Windows 安装」保持未勾选**。「下载」里是你自己存的文件，回收站里可能还有想找回的东西，删掉「以前的 Windows 安装」会失去这次升级的回退选项。[微软的磁盘清理说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)
3. **还缺空间，就找自己认得的大文件。** 在资源管理器里打开「下载」或「视频」，按大小排序。要保留的视频、压缩包，可以先复制到 D 盘或移动硬盘，确认新位置的文件能打开，再删 C 盘原件。最后只从回收站删掉刚搬走的那几项，空间就腾出来了。[微软的文件迁移说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

如果最大的一项是「系统和保留空间」，先停在这里，别进 `C:\Windows`、`Program Files` 或 `AppData` 挑大文件硬删。把「存储」页**最大的三项名称和各自占多少 GB** 发来，我可以帮你判断下一步查哪里。

# 110 · 电脑或软件问题

> 用户：Win11 的 C 盘只剩 6G 了，但我也没装啥大东西啊。有没有比较稳的清理办法，别让我一顿删完电脑起不来了。

## 第 1 遍

### 本仓库 + AGENTS.md

有，**先用 Win11 自带清理，再处理自己的大文件**，比较稳。更新备份、缓存也会占地方，装的软件少，C 盘照样可能满。

按这个顺序来：

1. **先看空间花在哪儿。** 按 `Win + I` → **系统 → 存储**，等它统计完，看“临时文件”“已安装的应用”“系统和保留”各占多少。[微软说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/storage-settings-in-windows)

2. **点“临时文件”，手动挑选。** 先清“临时文件、缩略图、传递优化文件”等缓存，再点“删除文件”。这里有三个要留意：
   - **“下载”别直接勾**，里面是你自己下载的东西。
   - **回收站先打开检查**，再决定清不清。
   - **“以前的 Windows 安装”先留着**，删了就失去回退上个系统版本的机会。[微软清理说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

3. **再处理自己的大文件。** 到“下载、桌面、视频”里找安装包、压缩包、视频；要保留的先复制到 D 盘或移动硬盘，打开确认后再删 C 盘原件。软件通过 **设置 → 应用 → 已安装的应用 → 卸载** 来处理。

**别按网上教程手动删 `C:\Windows`、`WinSxS`、`Installer`，也别整包删 `AppData`。** 系统文件交给自带工具处理；手动删 WinSxS 确实可能导致无法启动。[微软提醒](https://learn.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)

你可以把“系统 → 存储”那页截图发来，我帮你看下一步清哪里最划算。

### 本仓库（只装 skill）

有，**先用 Win11 自带的清理功能，逐项勾选，别直接去 C 盘删大文件夹。** 没装大软件也会满，系统更新残留、聊天软件缓存和下载文件都会慢慢堆起来。

按这个顺序来：

1. **先看空间被谁占了。** 按 `Win + I` →「系统」→「存储」，等统计完成，看看最大的几项是什么。

2. **进「临时文件」，别全选。** 优先清临时文件、缩略图等缓存；**「下载」先别勾**，里面是你的真实文件；「回收站」先打开检查。「以前的 Windows 安装」也先留着，删掉后就不能靠它回退到升级前的系统了。[微软清理说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

3. **再处理应用缓存和个人大文件。** 微信、QQ 用软件里面的存储管理清缓存，聊天记录和附件逐项确认。下载目录里的视频、压缩包、旧安装包，可以先复制到 D 盘或移动硬盘，确认能打开后再删 C 盘原件。

4. **以后用「存储感知」清临时文件。** 把「下载」和「回收站」的自动删除设成「从不」，这些由你自己检查后处理。[微软设置说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense)

**`C:\Windows`、`WinSxS`、`Installer`、`Program Files` 和整个 `AppData`，都别手动整包删。** 软件通过「设置 → 应用 → 已安装的应用」卸载。

我建议先争取腾到 **20GB 以上**，给更新和日常使用留点余地。你把 **C 盘总容量、存储页面最大的三项及大小**发我，我帮你挑下一步清哪里。

### 原版（不加 skill）

有。**先用 Windows 自带清理，再查空间被谁占了**，这是比较稳的顺序。没装大软件，也可能积累不少更新文件和缓存。

**1．先清一轮系统缓存**

按 `Win + I` → **系统 → 存储 → 临时文件**，等扫描完成，逐项看清楚，别直接全选。

| 项目 | 这一轮怎么处理 |
|---|---|
| 临时文件、缩略图、DirectX 着色器缓存、传递优化文件 | 可以优先清理；缓存以后可能重新生成 |
| 下载 | **先不勾**，这里可能是你下载的文档、安装包 |
| 回收站 | 打开检查，确认没有要找回的文件再清 |
| 以前的 Windows 安装／Windows.old | **先保留**，删后会失去回退到上一版本的能力 |

选好后点“删除文件”。这是微软提供的清理入口；保留旧系统是为了留下回退余地。[微软清理说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

**2．还不够，就看存储分类，处理最大的那项**

- **文档、视频等大文件**：把认识的文件移到 D 盘或移动硬盘，确认能打开后再删除原件。
- **已安装的应用**：通过“设置 → 应用 → 已安装的应用”卸载不用的程序。
- **微信、QQ 等应用数据**：优先用应用自己的存储管理，仔细区分缓存与聊天文件。

**3．这些地方别手动硬删**

不要整夹删除 `C:\Windows`、`Program Files`、`ProgramData`、`AppData`，也不要手动删 `pagefile.sys`、`hiberfil.sys`。尤其是 Windows 下的 **WinSxS 和 Installer**：前者乱删可能导致无法启动，后者会影响软件更新、修复和卸载。[WinSxS 说明](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)、[Installer 说明](https://learn.microsoft.com/en-us/troubleshoot/windows-client/application-management/missing-windows-installer-cache)

建议先争取腾到 **15–20 GB 可用空间**，不用追求一次清干净。你可以把“系统 → 存储”的分类占用截图发来，带上 C 盘总容量；我帮你判断下一步清哪里最划算、风险最低。

### talk-normal

有。**优先用 Windows 自带清理工具，再处理软件缓存和个人大文件，风险比较低。** 更新残留、聊天附件等也会慢慢占空间。

按这个顺序做：

1. **清理系统列出的临时文件。**  
   按 `Win + I` →「系统」→「存储」→「临时文件」，等扫描完成。优先选「临时文件」「缩略图」「传递优化文件」等缓存项目，核对后点「删除文件」。这是微软推荐的清理入口。[微软说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

2. **把容易误删的项目留住。**  
   「下载」取消勾选，里面可能有你的资料；回收站先打开检查，再清空。「以前的 Windows 安装」先保留，它用于回退系统版本，删除会失去这条恢复途径。[微软说明](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/delete-your-previous-version-of-windows)

3. **通过软件自己的设置清缓存。**  
   微信、QQ、浏览器、网盘都可能积累大量文件。进入各自的「存储管理／清理缓存」，先看分类和大小；聊天记录、附件和离线下载逐项确认用途。

4. **把个人大文件移到 D 盘或移动硬盘。**  
   重点看「下载」「桌面」「视频」里的安装包、压缩包和视频。重要文件先复制到目标盘，确认能打开，再删除 C 盘原件。软件通过「设置 → 应用 → 已安装的应用」卸载。

**系统目录保持原样：**`C:\Windows`（尤其 `WinSxS`、`Installer`）、`Program Files`、整份 `AppData`，以及 `pagefile.sys`、`hiberfil.sys` 都交给系统或对应软件管理。

先做前两步，查看释放了多少；建议争取留出 **20～30GB**，给更新和日常临时文件留余量。

### 试验版 + AGENTS.md（没有发布）

有，**先用 Windows 自带的清理功能，再搬走自己的大文件**，比较稳。更新备份、应用缓存、桌面和下载文件都会占 C 盘，软件装得少也会满。

按这个顺序来：

1. **先清临时文件。**  
   按 `Win + I` → **系统 → 存储 → 临时文件**，等扫描结束。先选“临时文件”“缩略图”，再点“删除文件”。这是 Windows 自带的清理办法。[微软清理说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

2. **这几个选项先留着。**  
   **“下载”别直接勾**，里面可能有你要用的资料；“回收站”先打开检查；“以前的 Windows 安装”先保留，删掉后就不能退回上一个 Windows 版本。[微软说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

3. **清完还不够，就看谁占得最多。**  
   回到“存储”页面，看“已安装的应用”“其他”等分类。自己的大视频、压缩包可以复制到 D 盘或移动硬盘，确认能打开后再删 C 盘原件；软件通过“卸载”移除。[微软文件整理步骤](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

**别手动清空 `Windows`、`Program Files` 或整个 `AppData` 文件夹。** 尤其 `Windows` 里的 `WinSxS`，手删确实可能导致开不了机，交给系统清理工具处理。[微软提醒](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)

我建议先争取腾到 **20GB 左右**。你把“存储”页面的各项占用截图发来，我可以帮你挑最值得清的那一项。

### 试验版（没有发布）

有。**先用 Win11 自带清理，再处理自己的大文件，这样比较稳。** 更新残留、下载文件和软件缓存，也可能把 C 盘塞满。

按这个顺序来：

1. **先看谁占地方。** 按 `Win + I` →「系统」→「存储」，等它统计完，看看“临时文件”“已安装的应用”“其他”分别占多少。

2. **清“临时文件”，不要全选。** 先选“临时文件、缩略图、传递优化文件”。**“下载”取消勾选**，那里面是你自己保存的文件；回收站先检查再清。系统更新后用着正常、已经重启过，再考虑“Windows 更新清理”。这是微软提供的清理入口。[微软清理说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

3. **“以前的 Windows 安装”先留着。** 这项通常对应 `Windows.old`，清掉会失去回到上一个 Windows 版本的选项；刚升级过、还在观察有没有问题，就先别选。[微软说明](https://support.microsoft.com/zh-cn/windows/deployment/install-upgrade/delete-your-previous-version-of-windows)

4. **再处理自己的大文件。** 下载、桌面里的旧安装包和压缩包，确认不用再删；视频、照片可以先复制到 D 盘或移动硬盘，确认能打开后再删原件。微信、QQ 等从软件自己的“存储管理”里清，先看清选中的是缓存还是聊天文件。

**别手动删 `Windows`、`WinSxS`、`Installer`、`Program Files`，也别把整个 `AppData` 清空。** 尤其是 `WinSxS`，乱删确实可能导致电脑无法启动。[微软警告](https://learn.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)

先做前两步。你把“存储”页面各项占用的截图发来，再告诉我 C 盘总共多大，我帮你找下一块最值得清的地方。

## 第 2 遍

### 本仓库 + AGENTS.md

有，**先用 Win11 自带的清理工具，按项目挑着删，比较稳。** 更新残留、缓存、安装包都会慢慢占空间，软件装得少也会把 C 盘塞满。[微软说明](https://www.microsoft.com/en-us/windows/learning-center/how-to-delete-temporary-files)

按这个顺序来：

1. **清临时文件。** 按 `Win + I` → **系统 → 存储 → 临时文件**，等扫描完成。先勾“临时文件”“缩略图”“传递优化文件”，再点“删除文件”。

2. **有三项先留着。** “下载”和“回收站”先取消勾选，打开看看里面有没有要留的东西；“以前的 Windows 安装”也先留着，删掉会失去回退到上一版 Windows 的机会。[微软说明](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/delete-your-previous-version-of-windows)

3. **找个人大文件。** 回到“存储 → 清理建议”，看看哪些文件占地方。自己的视频、压缩包、安装包可以移到 D 盘或移动硬盘；软件缓存从软件自己的设置里清。[微软说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/storage-settings-in-windows)

**别直接删 `C:\Windows`、`Program Files`、`ProgramData`，也别整包清空 `AppData`。** 不用的软件通过“设置 → 应用 → 安装的应用”卸载。

清完还是很挤，就把“存储”页面各分类占用的截图发来，我帮你看下一步该清哪块。

### 本仓库（只装 skill）

有。**先用 Windows 自带的清理功能，再挪自己的大文件，别手动删系统目录。** 没装大软件，系统更新留下的文件和各种缓存也会占空间。

按这个顺序来：

1. **先看空间花在哪儿。** 按 `Win + I` →「系统」→「存储」，等它算完，看看是“临时文件”“已安装的应用”还是其他类别最大。

2. **打开“临时文件”，不要全选。**
   - 可以先清：临时文件、缩略图、传递优化文件。
   - **“下载”先别勾**，那是你下载的资料、安装包等自己的文件。
   - **回收站先打开检查**，确定里面都不要了再清。
   - **“以前的 Windows 安装”先留着**，删掉后就失去回退到升级前版本的功能。[微软清理说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)、[传递优化缓存说明](https://support.microsoft.com/zh-cn/windows/deployment/updates-lifecycle/delivery-optimization-in-windows)

3. **还不够，就处理自己的大文件。** 看看“下载、桌面、视频”里的视频、压缩包，能留到 D 盘或移动硬盘的就挪过去；不用的软件通过「设置 → 应用 → 已安装的应用」卸载。

**别把 `Windows`、`Program Files`、`AppData` 当垃圾文件夹清空。** 尤其 `Windows` 里的 `WinSxS` 和 `Installer`，交给系统工具处理；手动删 `WinSxS` 确实可能导致系统无法启动。[微软提醒](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)

你可以把**“存储”页面和“临时文件”列表**截个图发来，我帮你逐项挑哪些能清。

### 原版（不加 skill）

有。**先用 Win11 自带的清理功能，再处理你认识的个人文件，这样比较稳。** 没装大软件也可能被更新残留、下载文件和软件缓存慢慢占满。

建议按这个顺序来：

1. **先看空间花在哪儿。**  
   按 `Win + I` → **系统 → 存储**，等统计完成，看看“临时文件”“安装的应用”“系统和保留”分别多大。

2. **清理“临时文件”，不要全选。**  
   优先选：**缩略图、传递优化文件、临时 Internet 文件、临时文件**。清之前保存工作、关闭正在运行的软件。  
   **“下载”先不选**，它可能就是你的下载文件夹；回收站先打开检查。**“以前的 Windows 安装”也先留着**，删除后会失去返回上一 Windows 版本的功能。最近更新后如果电脑有异常，“Windows 更新清理”暂时也留着。[微软清理说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

3. **再处理自己的大文件和软件缓存。**  
   下载、桌面、视频里的旧安装包、压缩包、录像，可以逐个确认。需要保留的文件先复制到 D 盘或移动硬盘，确认能打开后再删 C 盘原件。微信、浏览器等缓存从软件自己的设置里清，留意别把聊天记录或重要附件一起删掉。不用的软件通过“设置 → 应用 → 安装的应用”卸载。

4. **清完再设置“存储感知”。**  
   在“系统 → 存储”里打开它，把自动删除下载文件设为**“从不”**；回收站也可以先设为“从不”，由你自己检查后清空。[微软设置说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense)

**别手动掏系统目录：**尤其是 `C:\Windows\WinSxS`、`C:\Windows\Installer`。删这些可能破坏系统维护，或导致软件无法更新、修复和卸载。[WinSxS 官方说明](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)、[Installer 官方说明](https://learn.microsoft.com/en-us/troubleshoot/windows-client/application-management/missing-windows-installer-cache)  
`AppData`、`ProgramData` 也别整包删；虚拟内存、休眠文件和还原点这轮先别碰。

先争取腾到 **20GB 左右**，给更新和日常使用留点余量。如果清完还是紧张，你可以发“存储”页面和“临时文件”列表的截图，我帮你逐项判断。

### talk-normal

有。**先用 Win11 自带清理，再处理自己的大文件，分批操作比较稳。** 更新残留、临时文件也会占空间，软件装得少照样可能把 C 盘撑满。

1. **先清临时文件**
   
   按 `Win + I` → **系统 → 存储 → 临时文件**，等扫描完成。
   优先勾选“临时文件、缩略图、DirectX 着色器缓存、传递优化文件”，再点“删除文件”。
   
   **“下载”和“回收站”先取消勾选**，里面可能有你的资料。“以前的 Windows 安装”也先保留，它用于回退到升级前的版本。[微软清理说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

2. **搬走个人大文件**
   
   打开“下载、桌面、视频”，按大小排序。把要留的视频、压缩包等复制到有空间的 D 盘或移动硬盘，确认能打开后，再删除 C 盘原件，并检查回收站。[微软操作说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)
   
   微信、QQ 等软件的缓存，通过软件里的“存储管理”清理；聊天记录和接收文件逐项确认。

3. **把自动清理设得保守些**
   
   在 **系统 → 存储 → 存储感知** 中开启临时文件清理，把自动清理“下载”和“回收站”的周期设为“从不”，这两处由你手动检查。[微软存储感知说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense)

**系统目录交给系统和对应软件管理**：`Windows`、`Program Files`、`ProgramData`、`AppData` 都先保留。尤其 `Windows\WinSxS`，手动删除其中的文件可能造成启动和更新故障。[微软提醒](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)

先做第 1 步，再检查剩余空间；建议先争取留出 **20GB 左右**作为日常缓冲。

### 试验版 + AGENTS.md（没有发布）

有。**先用 Windows 自带清理，再处理自己的大文件，比较稳。** 即使没装大软件，系统更新残留和软件缓存也会越攒越多。

按这个顺序来：

1. **清系统列出的临时文件**  
   打开 **设置 → 系统 → 存储 → 临时文件**，等扫描完成。先取消其他勾选，只选“临时文件、缩略图、传递优化文件”清理。  
   **“下载”是你下载的文件，先别勾；回收站先检查；“以前的 Windows 安装”先留着，删掉就失去回退到上一个 Windows 版本的机会。** [微软清理说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

2. **把自己的大文件挪走**  
   看看“下载、桌面、视频”里的安装包、压缩包、视频。要留的先复制到 D 盘或移动硬盘，确认能打开，再删除 C 盘原件、清空对应的回收站项目。[微软操作说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

3. **看看软件到底占了多少**  
   打开 **设置 → 应用 → 已安装的应用**，按大小排序，只卸载你认识且不用的软件。微信、QQ、网盘的缓存和附件，进软件自己的“存储管理”里按内容清。[微软卸载说明](https://support.microsoft.com/zh-cn/windows/experience/performance-optimization/tips-to-improve-pc-performance-in-windows)

**别手动删 `Windows`、`Program Files`，也别把 `AppData` 整个清空。** 尤其 `Windows\WinSxS`，交给系统工具处理，手动删可能损坏系统。[微软说明](https://learn.microsoft.com/zh-tw/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)

先做第 1 步。清完如果空间还是很少，把“存储”页面各分类占用多少 GB 发我，我帮你挑下一处。

### 试验版（没有发布）

有。**最稳的是先用 Windows 自带工具清缓存，再处理自己的大文件。** 更新残留、下载文件、聊天缓存，积起来也会把 C 盘撑满。

按这个顺序来：

1. **先看空间花在哪。** 按 `Win + I` → **系统 → 存储**，等它统计完，看看“临时文件”“已安装的应用”“系统和保留”分别占多少。

2. **清临时文件，别全选。** 进入“临时文件”，先清“临时文件、缩略图、传递优化文件、DirectX 着色器缓存”等缓存项。**“下载”先别勾；“回收站”先检查内容；“以前的 Windows 安装”先留着**，删掉它会失去回退到上一版 Windows 的功能。[微软清理说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

3. **处理自己的大文件。** 到“下载”“视频”等文件夹，按大小排序。不要的安装包、压缩包可以删；要留的文件先复制到 D 盘或移动硬盘，确认能打开，再删除 C 盘原件并清空对应的回收站项目。软件占得多就从“设置 → 应用”卸载，别直接删安装目录。

4. **以后用存储感知清缓存。** 在“系统 → 存储 → 存储感知”里开启自动清理，把“下载文件夹”的自动删除设成 **“从不”**；回收站也可以先设“从不”，自己检查后再清。[微软设置说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense)

**别手动清空 `C:\Windows`、`WinSxS`、`Installer` 或整个 `AppData`。** 尤其 `WinSxS`，微软明确提醒，手动删里面的文件可能导致无法启动。[微软说明](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)

先做前两步，看看能腾出多少。还不够的话，把“存储”里几项占用的数字发我，我帮你挑下一步该清哪里。

## 第 3 遍

### 本仓库 + AGENTS.md

有，**先用 Win11 自带的清理功能，再处理自己的大文件，比较稳。** 更新留下的文件、下载内容和软件缓存，也会慢慢吃掉空间。

按这个顺序来：

1. **清临时文件。** 按 `Win + I` → **系统 → 存储 → 临时文件**，等扫描完成。优先选“临时文件、缩略图、传递优化文件、Windows 更新清理”，再点“删除文件”。**“下载”先别勾，回收站先看一眼内容。** [微软清理说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

2. **“以前的 Windows 安装”先留着。** 这项删掉后，就失去了回退到上一个 Windows 版本的选项。[微软说明](https://support.microsoft.com/zh-cn/windows/deployment/install-upgrade/delete-your-previous-version-of-windows)

3. **清完还很挤，就看谁占得最多。** 回到“存储”页面，查看各项大小。自己的视频、安装包可以移到 D 盘或移动硬盘；软件通过“设置 → 应用 → 已安装的应用”卸载。[微软说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

**别直接删 `C:\Windows`、`Program Files` 或整个 `AppData`。** 这些地方交给系统或软件自带的清理功能处理。

你把“存储”页面里各项占用发来，我可以帮你挑下一步最值得清的地方。

### 本仓库（只装 skill）

有，**先用 Win11 自带的清理功能，比较稳。** 没装大软件，更新留下的文件、缓存和下载附件也会慢慢占满 C 盘。

按这个顺序来：

1. **先清系统认得的临时文件。**  
   按 `Win + I` → **系统 → 存储 → 临时文件**，等扫描完。先勾选“临时文件”“缩略图”“传递优化文件”这些缓存，再点“删除文件”。**别一键全选：“下载”先不勾，回收站先检查；“以前的 Windows 安装”先留着，删掉会失去回退到上一版本的入口。** [微软清理说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

2. **再处理自己的大文件。**  
   看看下载、桌面、视频里有没有旧安装包、压缩包、录屏。有 D 盘或移动硬盘就先复制过去，确认能打开，再删 C 盘那份。微信、QQ 的缓存从软件自己的设置里清，别直接把聊天数据文件夹整包删掉。

3. **最后设置自动清缓存。**  
   在 **系统 → 存储 → 存储感知**里开启清理临时文件，把“下载文件夹”和“回收站”的自动删除都设为“从不”，先自己管理。[微软设置说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense)

**别手动删 `C:\Windows`、`Program Files`，也别整包清空 `AppData`。** 尤其 `Windows\WinSxS`，强删确实可能导致开不了机。[微软提醒](https://learn.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)

先争取把可用空间腾到 **20GB 左右**。如果第一步只清出一点点，可以发张“系统 → 存储”的占用截图，我帮你找真正占地方的那块。

### 原版（不加 skill）

有。**先看占用，再用 Windows 自带功能清理**，这套比较稳。没装大软件，也可能被更新残留、临时文件和下载文件占满。

按这个顺序来，每做完一步就看看腾出了多少空间：

1. **先查谁占空间。**  
   按 `Win + I` → **系统 → 存储**，等统计完成，看看“临时文件”“安装的应用”“系统和保留”“其他”各占多少。先不用删东西。

2. **清理系统识别出的临时文件。**  
   进入 **存储 → 临时文件**，先选“临时文件”“缩略图”等缓存项目，再点“删除文件”。**别直接全选**：“下载”里可能有你自己的资料；回收站先检查；“以前的 Windows 安装”先留着，删除后就不能用它回退到上一版本了。[微软清理说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

3. **处理你认识的大文件。**  
   看看“下载”、桌面、视频里的安装包、压缩包和录像。有 D 盘或移动硬盘的话，先复制过去，确认能打开，再删 C 盘原件。软件通过“设置 → 应用 → 安装的应用”卸载，别直接搬或删软件文件夹。

4. **设置后续自动清理。**  
   在“存储感知”里启用临时文件清理，把“下载文件夹”的自动删除设为**从不**；回收站也可以先设为“从不”，自己检查后再清。[微软设置说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense)

**不要手动清空 `Windows`、`Program Files`、`ProgramData` 或整个 `AppData`，也别直接删除 `pagefile.sys`、`hiberfil.sys`。** 尤其 `Windows\WinSxS`，微软明确提醒，手动删其中的文件可能导致无法启动。[微软提醒](https://learn.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)

你可以先发一张“系统 → 存储”的占用截图，我帮你判断哪一块值得清、哪些先留着。

### talk-normal

有，**先用 Win11 自带的清理功能，再处理确认用途的个人文件**，这是比较稳的顺序。更新残留、软件缓存、聊天附件和网盘本地文件都会慢慢占空间。

1. **先看空间用在哪。**  
   按 `Win + I` →「系统」→「存储」，等统计完成，看「临时文件」「已安装的应用」「其他」「系统和保留」哪项最大。

2. **清理低风险的临时文件。**  
   进入「临时文件」，优先选：临时文件、缩略图、DirectX 着色器缓存、传递优化文件。「Windows 更新清理」放在更新完成、重启且运行正常后处理。[微软清理指南](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

   **「下载」保持未勾选**，里面可能有你保存的资料；回收站先查看内容再清空；「以前的 Windows 安装」第一轮先保留，它关联升级后的回退功能。

3. **再处理个人文件和软件缓存。**  
   下载目录里的旧安装包、压缩包可以逐个确认；视频和资料可以转移到 D 盘或移动硬盘，打开确认完整后再删除 C 盘原件。微信、QQ、浏览器缓存通过各自软件的设置清理，聊天记录和附件按需要保留。

4. **开启「存储感知」防止继续堆积。**  
   自动清理下载文件的选项设为「从不」；回收站也可设为「从不」，由你手动确认。[微软设置说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense)

**系统目录保持原状**：尤其是 `C:\Windows\WinSxS`、`C:\Windows\Installer`；整个 `AppData` 也要保留，`pagefile.sys` 继续交给系统管理。WinSxS 和 Installer 中的文件涉及启动、更新及软件修复。[微软组件清理说明](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)、[Installer 缓存说明](https://learn.microsoft.com/en-us/troubleshoot/windows-client/application-management/missing-windows-installer-cache)

先做第 1、2 步，清完查看剩余容量；建议先争取留出 **20GB 左右**，给更新和日常运行留些余量。

### 试验版 + AGENTS.md（没有发布）

有，**先用 Windows 自带工具清缓存，再挪自己的大文件，比较稳。** 更新残留、下载文件和软件缓存都会慢慢占空间，没装大软件也会满。

按这个顺序来：

1. **先看空间花在哪。**  
   按 `Win + I` → **系统 → 存储**，等统计完成，看“临时文件”“已安装的应用”“系统和保留”各占多少。

2. **清“临时文件”，别直接全选。**  
   可以先选“临时文件、缩略图、传递优化文件、DirectX 着色器缓存”，再点“删除文件”。这是 Windows 自带的清理入口。[微软操作说明](https://support.microsoft.com/en-us/windows/experience/performance-optimization/tips-to-improve-pc-performance-in-windows)  
   **“下载”先别勾**，里面是你下载的真实文件；回收站先打开看一遍再清。“以前的 Windows 安装”先留着，删了就失去回退到升级前版本的功能。[微软说明](https://support.microsoft.com/zh-cn/windows/deployment/install-upgrade/delete-your-previous-version-of-windows)

3. **处理自己的文件和软件。**  
   下载、桌面里的视频、压缩包、安装包，可以挪到有空余的 D 盘或移动硬盘。微信、QQ、网盘缓存从各自软件的设置里清；不用的软件从 **设置 → 应用 → 已安装的应用** 卸载。

**别手动删 `C:\Windows` 里的文件，尤其是 `WinSxS`、`Installer`，也别把 `AppData` 整个当垃圾清掉。** 系统文件交给自带工具处理。[WinSxS 说明](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11)、[Installer 说明](https://learn.microsoft.com/en-us/troubleshoot/windows-client/application-management/missing-windows-installer-cache)

建议尽量留出 **20～30GB**，给更新和日常缓存留余地。你把“存储”页面的占用分类截张图发来，我帮你看下一步清哪里最划算。

### 试验版（没有发布）

有。**先用 Windows 自带的清理功能，再挪自己的大文件，比较稳。** 没装大软件，更新残留和缓存也能慢慢把 C 盘塞满。

按这个顺序来：

1. **清临时文件**  
   按 `Win + I` → **系统 → 存储 → 临时文件**，等扫描完成，别直接全选。先选“临时文件、缩略图、传递优化文件”；系统更新完成、重启后使用正常，再清“Windows 更新清理”。  
   **“下载”先取消勾选**，里面是你自己下载的文件；“回收站”先检查；“以前的 Windows 安装”先留着，删后就失去回退到上一版本的入口。[微软清理说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

2. **搬走自己的大文件**  
   看“下载、桌面、视频”里的安装包、压缩包、录像。有 D 盘或移动硬盘，就先复制过去，确认能打开，再删除 C 盘那份。删完检查回收站并清空，才会真正释放空间。[微软文件迁移说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)

3. **设置后续自动清理**  
   在“存储感知”里开启临时文件清理，把**下载、回收站和云内容的自动清理设成“从不”**，自己的文件留给自己决定。[微软设置说明](https://support.microsoft.com/zh-cn/windows/experience/storage-filemanagement/manage-drive-space-with-storage-sense)

**别手动删 `C:\Windows`、`WinSxS`、`Installer`，也别整块删除 `AppData`。** 软件缓存尽量从软件自己的设置里清。

先做第一步。如果腾出来的空间很少，把“存储”页面里各项占用的大小发我，我帮你找下一处该清哪里。

# 109 · 电脑或软件问题

> 用户：我用 pandas 读 CSV，手机号前面那个 0 读完就没了，保存回去也没了……怎么让它老老实实按文本读啊？

## 第 1 遍

### 本仓库 + AGENTS.md

在 `read_csv` 里指定 `dtype`，把手机号列按字符串读，前面的 0 就会保留。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("原始.csv", dtype={"手机号": str})
df.to_csv("结果.csv", index=False)
```

把 `"手机号"` 换成你的实际列名。**所有列都想按文本读**，就写：

```python
df = pd.read_csv("原始.csv", dtype=str)
```

记得从还带着 0 的原始文件或备份重新读。读完再 `astype(str)`，只会把 `123` 变成 `"123"`，补不回前面的 0。

### 本仓库（只装 skill）

在 **`read_csv` 时指定 `dtype`**，手机号就会按字符串读，前面的 `0` 也会保留。[pandas 官方文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("input.csv", dtype={"手机号": str})
df.to_csv("output.csv", index=False)
```

把 `"手机号"` 换成你的实际列名。想让**所有列**都按文本读，用：

```python
df = pd.read_csv("input.csv", dtype=str, keep_default_na=False)
```

`keep_default_na=False` 会把空字段保留成空字符串，也保留 `"NA"` 这类原文。

你现在已经丢了 `0` 的那份，要重新读原始 CSV；读完再 `astype(str)`，丢掉的 `0` 补不回来。

### 原版（不加 skill）

在 `read_csv` 时指定手机号列的 `dtype=str`，就能保留前导 `0`。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

# “手机号”换成你的实际列名
df = pd.read_csv("input.csv", dtype={"手机号": str})

df.to_csv("output.csv", index=False)
```

如果**所有列都要按文本读**，并保留空字符串、`NA` 等原始文本：

```python
df = pd.read_csv("input.csv", dtype=str, keep_default_na=False)
```

已经丢掉的 `0`，事后用 `astype(str)` 转字符串也补不回来，需要从仍保留 `0` 的原文件重新读取。CSV 不记录列类型，下次读保存后的文件时，也要指定 `dtype`。

### talk-normal

在 `read_csv` 时给手机号列指定 `dtype=str`，就能保留前导 `0`。[pandas 官方文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("input.csv", dtype={"手机号": str})
df.to_csv("output.csv", index=False)
```

把 `"手机号"` 换成你的实际列名。整张表都按文本读，可以这样写，空字段也会保留为 `""`：

```python
df = pd.read_csv("input.csv", dtype=str, keep_default_na=False)
```

已经丢失的 `0` 需要从仍保留它的原始 CSV 重新读取；以后再读保存后的 CSV，也要指定 `dtype`。

### 试验版 + AGENTS.md（没有发布）

在 `read_csv` 里指定 `dtype={"手机号": str}`，就会按文本读，保住开头的 0。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("input.csv", dtype={"手机号": str})
df.to_csv("output.csv", index=False)
```

把 `"手机号"` 换成你的实际列名就行，`0912345678` 读入再保存还是 `0912345678`。

如果**所有列都要按文本读**：

```python
df = pd.read_csv("input.csv", dtype=str, keep_default_na=False)
```

`keep_default_na=False` 会让空字符串、`"NA"` 等也保留原样。

你现在已经读丢的 0，要从**原始 CSV 重新读**；事后 `.astype(str)` 补不回来。

### 试验版（没有发布）

在 **读取时** 指定 `dtype` 就行，把 `"手机号"` 换成你的实际列名：[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)。

```python
import pandas as pd

df = pd.read_csv(
    "原始.csv",
    dtype={"手机号": str},
    keep_default_na=False,  # 空白保留为 ""，不转成 NaN
)

df.to_csv("输出.csv", index=False)
```

这样 `0912345678` 读进来、保存出去都会保留开头的 `0`。

如果想让**所有列都按文本读**：

```python
df = pd.read_csv("原始.csv", dtype=str, keep_default_na=False)
```

已经丢掉的 `0`，读完再 `astype(str)` 也补不回来，要从还保留 `0` 的原始 CSV 重新读。

## 第 2 遍

### 本仓库 + AGENTS.md

在 **`read_csv` 读取时指定 `dtype`** 就行，手机号会按文本读，保存时也会保留开头的 0：

```python
import pandas as pd

df = pd.read_csv("原始.csv", dtype={"手机号": str})
df.to_csv("输出.csv", index=False)
```

把 `"手机号"` 换成你的实际列名。想让**所有列**都按文本读，就用 `pd.read_csv("原始.csv", dtype=str)`。[pandas 参数说明](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

已经丢了 0 的那份，要从保留着 0 的原 CSV 重新读；读完再 `astype(str)`，丢掉的 0 补不回来。

### 本仓库（只装 skill）

在 `read_csv` 里指定 `dtype`，手机号就会按文本读，前面的 `0` 也会保留。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

# “手机号”换成你 CSV 里的实际列名
df = pd.read_csv("input.csv", dtype={"手机号": str})

df.to_csv("output.csv", index=False)
```

想让**所有列都按文本读**，就写：

```python
df = pd.read_csv("input.csv", dtype=str)
```

空白单元格也想保留成空字符串，再加 `keep_default_na=False`。

**已经丢掉的 `0` 得从原始 CSV 重新读**，读完再 `.astype(str)` 补不回来。

### 原版（不加 skill）

在 `read_csv` 时就指定手机号列为字符串，前面的 `0` 就能保住。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv(
    "原始.csv",
    dtype={"手机号": str},   # 换成你的实际列名
    keep_default_na=False,  # 空字段保留为 ""，而不是 NaN
)

df.to_csv("输出.csv", index=False)
```

如果想让**所有列都按文本读**，把 `dtype={"手机号": str}` 换成 `dtype=str`。

已经读成数字后再用 `.astype(str)`，丢掉的 `0` 不会回来；需要用上面的写法重新读取原始 CSV。

### talk-normal

在 `read_csv` 时指定手机号列为字符串，就能保留前面的 `0`：

```python
import pandas as pd

df = pd.read_csv(
    "input.csv",
    dtype={"手机号": str},
    keep_default_na=False,  # 空字段也保持为空字符串
)
df.to_csv("output.csv", index=False)
```

把 `手机号` 换成实际列名。整张表都按文本读，就用 `dtype=str`。[pandas 官方文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

已经丢掉的 `0`，需要用这段代码从原始 CSV 重新读取。

### 试验版 + AGENTS.md（没有发布）

在 `read_csv` 里指定手机号列为文本就行，前面的 0 就会保留。[pandas 参数说明](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("原始.csv", dtype={"手机号": "string"})
df.to_csv("输出.csv", index=False)
```

把 `"手机号"` 换成你的实际列名。想**所有列都按文本读**，就用 `dtype="string"`。

你这次得找还保留着 0 的原始 CSV 重读；读完再 `astype(str)`，已经丢掉的 0 补不回来。

### 试验版（没有发布）

在 **读取时** 指定 `dtype` 就行，手机号开头的 `0` 就能保住。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv(
    "input.csv",
    dtype={"手机号": str},  # 换成你的实际列名
    keep_default_na=False,  # 空白保留为 ""，不转成 NaN
)

df.to_csv("output.csv", index=False)
```

如果想让 **所有列都按文本读**：

```python
df = pd.read_csv("input.csv", dtype=str, keep_default_na=False)
```

已经丢掉的 `0`，读完再 `.astype(str)` 也补不回来；得用上面的写法重新读还带着 `0` 的原始 CSV。

## 第 3 遍

### 本仓库 + AGENTS.md

在 `read_csv` 里用 `dtype` 把手机号列指定成文本，前面的 `0` 就会保住。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("input.csv", dtype={"手机号": "string"})
df.to_csv("output.csv", index=False)
```

把 `"手机号"` 换成你的实际列名。想让**所有列**都按文本读，就用：

```python
df = pd.read_csv("input.csv", dtype="string")
```

已经丢了 `0` 的那份，得从原始 CSV 重新读；读完再 `astype(str)`，丢掉的 `0` 补不回来。

### 本仓库（只装 skill）

在 `read_csv` 里给手机号列指定 `dtype` 就行，前面的 0 会保留下来。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("input.csv", dtype={"手机号": "string"})
df.to_csv("output.csv", index=False)
```

把 `"手机号"` 换成你的实际列名。整张表都想按文本读，就用：

```python
df = pd.read_csv("input.csv", dtype="string")
```

**要在读取时指定**：读完再 `.astype(str)`，已经丢掉的 0 补不回来，得从原 CSV 重新读。以后再读保存的 CSV，也要指定 `dtype`。

### 原版（不加 skill）

在 **读取时** 用 `dtype` 指定手机号列为字符串，开头的 `0` 就能保留。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("input.csv", dtype={"手机号": str})
df.to_csv("output.csv", index=False)
```

把 `"手机号"` 换成你 CSV 里的实际列名。如果**所有列都要按文本读**：

```python
df = pd.read_csv("input.csv", dtype=str)
```

已经读成数字后，再用 `astype(str)` **补不回丢掉的 `0`**，需要从仍保留 `0` 的原始 CSV 重新读取。

### talk-normal

在 `read_csv` 时用 `dtype` 指定手机号列为文本，前导 `0` 就会保留。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

# “手机号”换成你的实际列名
df = pd.read_csv("input.csv", dtype={"手机号": str})
df.to_csv("output.csv", index=False)
```

整张表都按文本读取，可以用：

```python
df = pd.read_csv("input.csv", dtype=str)
```

已经丢失的 `0`，需要从保留完整号码的原始 CSV 重新读取。

### 试验版 + AGENTS.md（没有发布）

在 **`read_csv` 读取时就指定字符串类型**，前面的 `0` 就能保住。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("input.csv", dtype={"手机号": str})
df.to_csv("output.csv", index=False)
```

把 `"手机号"` 换成你的实际列名。整张表都想按文本读，就用：

```python
df = pd.read_csv("input.csv", dtype=str)
```

已经读丢了 `0` 的数据，要从原始 CSV 重新读；事后用 `.astype(str)` 补不回来。

### 试验版（没有发布）

在 **`read_csv` 的时候指定 `dtype`** 就行，让手机号按文本读。[pandas 官方文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("input.csv", dtype={"手机号": "string"})
df.to_csv("output.csv", index=False)
```

把 `"手机号"` 换成你的实际列名。这样 `0912345678` 读入、写回都会保留开头的 `0`。

如果想让**所有列都按文本读**：

```python
df = pd.read_csv("input.csv", dtype="string")
```

已经丢掉的 `0`，事后用 `astype(str)` 转字符串也补不回来，得从还保留着 `0` 的原始 CSV 重新读。

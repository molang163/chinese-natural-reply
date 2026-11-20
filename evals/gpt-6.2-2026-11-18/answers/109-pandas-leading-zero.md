# 109 · 电脑或软件问题

> 用户：我用 pandas 读 CSV，手机号前面那个 0 读完就没了，保存回去也没了……怎么让它老老实实按文本读啊？

## GPT-6.2 Sol

### 本仓库 + AGENTS.md

在 `read_csv` 里加 `dtype={"手机号": str}`，pandas 就会把这列当文本读，开头的 `0` 写回 CSV 时也会保留。

```python
import pandas as pd

df = pd.read_csv("input.csv", dtype={"手机号": str})
df.to_csv("output.csv", index=False)
```

把 `手机号` 换成 CSV 里的实际列名。

如果手上的 CSV 已经丢了开头的 `0`，有原始文件就重新读。如果确定号码都是 10 位，可以在保存前用 `df["手机号"] = df["手机号"].str.zfill(10)` 补齐。

### 本仓库（只装 skill）

在 `pd.read_csv()` 里用 `dtype` 指定手机号那列按字符串读，开头的 `0` 就会保留下来。 [pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("原始.csv", dtype={"手机号": "string"})
df.to_csv("输出.csv", index=False)
```

把 `"手机号"` 换成你 CSV 里的实际列名。比如 `0123456789`，读进来和写回 CSV 都还是 `0123456789`。

如果 `0` 已经在上一次读取时丢了，就用这段代码从还带 `0` 的原始文件或备份重读一遍。

### talk-normal

用 `dtype={"手机号": "string"}` 指定手机号列按文本读取，前导 `0` 会保留，写回 CSV 时也会保留。

```python
import pandas as pd

df = pd.read_csv("input.csv", dtype={"手机号": "string"})
df.to_csv("output.csv", index=False)
```

把 `手机号` 换成 CSV 里的实际列名。如果已经读丢了 `0`，用这段代码重新读取仍保留前导 `0` 的原始文件或备份。

### 原版（不加 skill）

在 `read_csv()` 时用 `dtype` 把手机号列指定为字符串。这样 `0912345678` 读进来和写回去都会保留开头的 `0`。 [pandas 读取文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) · [保存文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)

```python
import pandas as pd

df = pd.read_csv("input.csv", dtype={"手机号": "string"})
df.to_csv("output.csv", index=False)
```

把 `"手机号"` 换成 CSV 里的实际列名。已经读丢了 `0` 的话，用这段代码从原始 CSV 重新读一遍。以后再用 pandas 读 `output.csv`，也加上同样的 `dtype`。

## GPT-6.2 Astra

### 本仓库 + AGENTS.md

从还带 `0` 的原始 CSV 重新读一次，用 `dtype` 把手机号这列指定为文本，保存时开头的 `0` 就会保留。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("原始.csv", dtype={"手机号": "string"})
df.to_csv("输出.csv", index=False)
```

把 `"手机号"` 换成你文件里的实际列名。下次用 pandas 读 `输出.csv` 时，也带上同一个 `dtype`。

### 本仓库（只装 skill）

在 `pd.read_csv()` 里加 `dtype={"手机号": str}`，把 `手机号` 换成你 CSV 里的实际列名。这样 `0912345678` 就会按文本读，写回 CSV 时开头的 `0` 也会保留。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("原始.csv", dtype={"手机号": str})
df.to_csv("输出.csv", index=False)
```

如果已经读成了数字 `912345678`，再用 `astype(str)` 只会得到 `"912345678"`，得用上面的写法重读那份还带 `0` 的原始文件。下次读 `输出.csv` 时也带上同样的 `dtype`。

### talk-normal

在 `read_csv` 时用 `dtype` 把手机号列指定为 `str`，这样 `0912345678` 读进来、写回 CSV 都会保留开头的 `0`。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("input.csv", dtype={"手机号": str})  # 换成 CSV 里的实际列名
df.to_csv("output.csv", index=False)
```

如果已经读成了数字，就从仍带 `0` 的原始文件或备份重新读。下次读取 `output.csv` 时也带上同样的 `dtype`。

### 原版（不加 skill）

在 `read_csv` 时用 `dtype={"手机号": str}`，就能保留开头的 `0`。把 `手机号` 换成 CSV 里的实际列名即可。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("input.csv", dtype={"手机号": str})
df.to_csv("output.csv", index=False)
```

这样原文件里的 `0912345678` 写回去还是 `0912345678`。下次读 `output.csv` 时也要带上同样的 `dtype`，因为 CSV 本身只保存字段内容。

如果已经读成了 `912345678`，再用 `astype(str)` 只会得到 `"912345678"`，需要从还保留前导 `0` 的原文件重新读。

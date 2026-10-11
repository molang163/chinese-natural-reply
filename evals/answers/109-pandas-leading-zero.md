# 109 · 电脑或软件问题

> 用户：我用 pandas 读 CSV，手机号前面那个 0 读完就没了，保存回去也没了……怎么让它老老实实按文本读啊？

出题人：GPT（不知道评分标准）

## 本仓库（发布版）

在 **`read_csv` 时就指定手机号列为字符串**，前面的 `0` 就会保留。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("input.csv", dtype={"手机号": str})
df.to_csv("output.csv", index=False)
```

把 `"手机号"` 换成你的实际列名，像 `0912345678` 就会原样读入、保存。

如果想**所有列都按文本读**：

```python
df = pd.read_csv("input.csv", dtype=str, keep_default_na=False)
```

这里 `keep_default_na=False` 会让空白字段保留为 `""`，也让 `"NA"` 等文本保留原样。

已经读丢的 `0`，再用 `astype(str)` 补不回来，得从原始 CSV 重新读。

## 测试版（发布前的同一份规则，例子里还有个人信息）

在 **`read_csv` 时指定 `dtype`**，手机号就会按字符串读取，保留开头的 `0`。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv(
    "input.csv",
    dtype={"手机号": str},    # 换成你的实际列名
    keep_default_na=False,   # 空字段保留为 ""，不转成 NaN
)

df.to_csv("output.csv", index=False)
```

如果**所有列都要按文本读**：

```python
df = pd.read_csv("input.csv", dtype=str, keep_default_na=False)
```

已经丢掉的 `0`，读完再 `astype(str)` 也补不回来。要用上面的写法，重新读取仍保留 `0` 的原始 CSV。

## 原版（不加 skill）

在 **读取时就用 `dtype` 指定手机号列为字符串**，前导 `0` 就能保住。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv(
    "input.csv",
    dtype={"手机号": str},  # 换成你的实际列名
    keep_default_na=False,  # 可选：空值保留为 ""，不转成 NaN
)

df.to_csv("output.csv", index=False)
```

如果想让**所有列都按文本读**：

```python
df = pd.read_csv("input.csv", dtype=str, keep_default_na=False)
```

已经丢了 `0` 再用 `astype(str)` 也救不回来，需要从原始 CSV 重读。CSV 不记录列类型，下次读取保存的文件时，也要指定 `dtype`。

## talk-normal

在 **`read_csv` 时指定 `dtype`**，手机号就会按文本读取，保留前导 `0`：

```python
import pandas as pd

df = pd.read_csv(
    "input.csv",
    dtype={"手机号": str},  # 换成你的实际列名
    keep_default_na=False,  # 空字段保留为空字符串
)

df.to_csv("output.csv", index=False)
```

`dtype` 可以按列指定；`keep_default_na=False` 会在整张表中保留空字符串及 `"NA"` 等原始文本。[pandas 官方文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

整张表都要按文本读，可以用：

```python
df = pd.read_csv("input.csv", dtype=str, keep_default_na=False)
```

已经读丢 `0` 的数据，需要从仍保留完整号码的原始 CSV 重新读取。

## 好好说话 haohao-shuohua

**在 `read_csv` 时就指定字符串类型**，手机号前面的 `0` 就能保住。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("input.csv", dtype={"手机号": str})
df.to_csv("output.csv", index=False)
```

把 `"手机号"` 换成你的实际列名。

如果**整张表都要按文本读**，空字段也想保留为 `""`，用：

```python
df = pd.read_csv("input.csv", dtype=str, keep_default_na=False)
```

已经读丢的 `0`，事后再用 `astype(str)` 也补不回来，得从仍保留 `0` 的原始 CSV 重新读。

## Humanizer-zh

**在 `read_csv` 时就指定手机号列为字符串，前导 `0` 就能保住。** [pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv(
    "input.csv",
    dtype={"手机号": str},  # 换成你的实际列名
    keep_default_na=False  # 空字段保留为 ""，"NA" 等也按原文本保留
)

df.to_csv("output.csv", index=False)
```

如果**所有列都要按文本读**，把 `dtype={"手机号": str}` 改成 `dtype=str`。

已经读成数字、丢掉的 `0`，再用 `.astype(str)` 也补不回来，需要重新读取仍保留 `0` 的原始 CSV。

如果保存后用 **Excel** 打开又看不到 `0`，可能是 Excel 自动转成了数字；通过“数据 → 从文本/CSV”导入，并把手机号列设为“文本”。[微软说明](https://support.microsoft.com/en-us/excel/keeping-leading-zeros-and-large-numbers)

## humanizer（英文原版）

在 `read_csv()` 时指定手机号列为字符串，就能保留前面的 `0`。[pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv("input.csv", dtype={"手机号": str})
df.to_csv("output.csv", index=False)
```

把 `"手机号"` 换成你的实际列名。

如果**所有列都要按文本读**：

```python
df = pd.read_csv("input.csv", dtype=str, keep_default_na=False)
```

`keep_default_na=False` 会让空字符串、`"NA"` 等也保留原样，不自动变成缺失值。

要在**读入时**设置：读完再 `.astype(str)`，只能把 `123` 变成 `"123"`，恢复不了已经丢掉的 `0`。需要从仍保留前导零的原始 CSV 重新读取。

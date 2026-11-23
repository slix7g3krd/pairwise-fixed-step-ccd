# pairwise-fixed-step-ccd

## 领域

游戏、图形与多媒体

## 主题

固定步长与连续碰撞

## 说明

累加器上限、子步拆分与回调重入保护。

初始状态下 `gameplay/fixed_step_ccd.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。

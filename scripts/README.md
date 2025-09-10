放置一次性或分析型脚本 (如 cleaning / hoc_first / hourofcode / tag / top_acc / 2_10_trace 等)。

后续可将根目录对应脚本迁移至此，并在其顶部添加 `if __name__ == "__main__":` 保护，避免作为库导入时执行。

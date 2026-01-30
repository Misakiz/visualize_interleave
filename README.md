# Video Interleave Visualization

本项目包含一个基于 Python 的工具，用于分析和可视化音频和视频流在媒体文件（MP4）中的交错情况。该工具使用 `ffprobe` 提取相关视频流信息，并将数据处理后生成交错的可视化图。

## 前提条件

- **ffmpeg**：您需要在系统上安装 `ffmpeg` 才能运行 `ffprobe`。
- **Python 3**：该工具需要 Python 3 环境来运行可视化脚本。

您可以通过以下命令安装 `ffmpeg`：
```bash
brew install ffmpeg  # 在 MacOS 上使用 Homebrew 安装

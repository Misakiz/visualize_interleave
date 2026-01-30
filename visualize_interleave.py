import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys
import re
 
# 从标准输入读取数据
data_str = sys.stdin.read().strip()
 
# 解析数据 - 更灵活的方式
packets = []
 
# 先提取所有的stream_index, pts_time, dts_time, pos
stream_indices = re.findall(r'stream_index=(\d+)', data_str)
pts_times = re.findall(r'pts_time=([-\d.]+)', data_str)
dts_times = re.findall(r'dts_time=([-\d.]+)', data_str)
positions = re.findall(r'pos=(\d+)', data_str)
 
# 配对数据
min_len = min(len(stream_indices), len(pts_times), len(dts_times), len(positions))
 
if min_len > 0:
    for i in range(min_len):
        packets.append({
            'stream_index': int(stream_indices[i]),
            'pts_time': float(pts_times[i]),
            'dts_time': float(dts_times[i]),
            'pos': int(positions[i])
        })
else:
    sys.exit(1)
 
try:
    # 创建一张大图，显示packet在文件中的分布
    fig, ax = plt.subplots(figsize=(20, 6))
     
    # 按文件位置排序
    sorted_packets = sorted(packets, key=lambda p: p['pos'])
     
    # 提取数据
    positions = np.array([p['pos'] for p in sorted_packets])
    streams = np.array([p['stream_index'] for p in sorted_packets])
     
    # 绘制：X轴是文件位置，Y轴是stream类型
    # 用条形图显示每个packet
    colors = ['#FF6B6B' if s == 0 else '#4ECDC4' for s in streams]
     
    for i, (pos, stream, color) in enumerate(zip(positions, streams, colors)):
        ax.bar(i, 1, width=1, color=color, edgecolor='none', alpha=0.8)
     
    ax.set_xlabel('Packet Index (sorted by file position)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Stream Type', fontsize=12, fontweight='bold')
    ax.set_title('Packet Interleaving Pattern in File\nRed=Video(0), Cyan=Audio(1)\nGood=alternating colors, Bad=large blocks',
                 fontsize=13, fontweight='bold')
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['Video (0)', 'Audio (1)'])
    ax.set_ylim(0, 1.2)
    ax.grid(axis='y', alpha=0.3)
     
    plt.tight_layout()
    plt.savefig('interleave_analysis.png', dpi=100, bbox_inches='tight')
     
except Exception as e:
    pass
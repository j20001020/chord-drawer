def draw_chord(chord_name, frets, start_fret=0):
    """
    繪製吉他和弦圖
    
    :param chord_name: 和弦名稱 (str)
    :param frets: 每條弦按的品數 (list, 6 個數字，0 表示空弦，-1 表示不彈)
    :param start_fret: 起始品數 (int, 預設為 0)
    """
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots(figsize=(3, 4))
    
    # 設定琴頸格線
    for i in range(5):  # 畫 5 條橫線 (品數)
        if i == 4:
            ax.plot([0, 5], [i, i], 'k', lw=7)  # 加粗第一條橫線
        else:
            ax.plot([0, 5], [i, i], 'k', lw=2)
    for i in range(6):  # 畫 6 條直線 (琴弦)
        ax.plot([i, i], [0, 4], 'k', lw=1)
    
    # 標示按弦點
    for string, fret in enumerate(frets):
        if fret > 0:  # 有按弦
            ax.scatter(string, 4 - fret + 0.5, s=500, c='black', edgecolors='white', zorder=3)

    # 標示 X（不彈）或 O（空弦）
    for string, fret in enumerate(frets):
        if fret == 0:  # 空弦
            ax.text(string, 4.3, '○', ha='center', va='center', fontsize=18, fontweight='bold')
        elif fret == -1:  # 不彈
            ax.text(string, 4.3, '✕', ha='center', va='center', fontsize=18, fontweight='bold')

    # 標題
    ax.set_title(chord_name, fontsize=22, fontweight='bold')

    # 顯示起始品數
    if start_fret > 0:
        ax.text(-0.5, 4, str(start_fret), ha='right', va='center', fontsize=22, fontweight='bold')

    # 隱藏軸標籤
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(-0.5, 4.8)
    ax.axis('off')

    plt.show()
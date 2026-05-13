# MP3 音乐网站

一个简单的MP3音乐播放网站，托管于GitHub Pages。

## 功能

- 播放MP3歌曲（鱼虾·岭南水墨）
- 每5小时50分钟自动更新最后更新时间
- 可通过二维码扫码访问

## 项目结构

```
MP3player/
├── index.html          # 音乐播放网页
├── 鱼虾·岭南水墨.mp3   # MP3歌曲文件
├── qrcode.png          # 网站二维码
├── generate_qrcode.py  # 二维码生成脚本
├── .github/
│   └── workflows/
│       └── main.yml    # GitHub Actions 自动部署配置
├── .gitignore
├── .gitattributes
└── README.md
```

## 使用说明

1. 将 `MP3player/` 目录推送到GitHub仓库
2. 在仓库 Settings → Pages 中设置：
   - Source: **Deploy from a branch**
   - Branch: **gh-pages** / **/(root)**
3. 网站即可通过 `https://<你的用户名>.github.io/<仓库名>/` 访问

## 自动更新

通过 GitHub Actions 实现每5小时50分钟自动更新 `index.html` 中的时间戳，并部署到 `gh-pages` 分支。

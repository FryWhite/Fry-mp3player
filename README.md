# MP3 音乐网站

一个简单的MP3音乐播放网站，托管于GitHub Pages。

## 功能

- 播放MP3歌曲
- 每5小时自动更新最后更新时间
- 可通过二维码扫码访问

## 使用说明

1. 将 `mp3-website/` 目录下的文件推送到GitHub仓库
2. 在仓库设置中启用 GitHub Pages (Source: main branch, folder: / (root))
3. 网站即可通过 `https://<你的用户名>.github.io/<仓库名>/` 访问

## 自动更新

通过 GitHub Actions 实现每5小时自动更新 `index.html` 中的时间戳。

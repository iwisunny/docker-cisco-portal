# Docker Development Environment for cisco portal

## Usage
1. 确保你已经接入互联网.
- 安装 docker.
- `touch` 一个 `.env` 文件, 将 `.env.example` 中的配置复制到 `.env` 中, 修改其中的源代码路径和 logs 输出路径, logs 路径不要包含在源代码路径中.
- 如果你设置的源代码路径和 logs 输出路径不在 `/Users/` `/Volumes/` `/private/` 和 `/tmp/` 下，需要在 docker => Perferences... => File Sharing 中增加一个 mount point。
- 如果你的 80 端口已经被占用可以修改 `NGINX_PORT` 为其他值.
- 执行 `docker-compose build && docker-compose up -d`


## About I18n

我们的很多项目都用到了 Django 的 compilemessages, 目前这部分功能还无法在 container 中完成, 所以本机也需要安装 Django.



<p align="center">
  <img src="http://cdn.moyusoldier.cloud/8B7C336065F6A936D01285E96EFA7BD2.png" width="50" height="50" alt="nonebot">
</p>


<div align="center">

# 为了「聊的燚燚 N」而努力！

_✨ NoneBot2 续火花 ✨_

</div>

## 功能💻
实现在两个用户间每天自动发送消息，保证火花不会灭

- 每天0时向指定用户发送"/echo 花花"
- 发送前随机延时1～10秒，避免脚本被检测

> 注意：
1. 本插件为Server端，您需要再自行配置一个Nonebot机器人作为Client端，以实现对"/echo"命令的响应及返回消息"花花"，完成整个续火花的过程。
2. 使用大号作为QQ机器人带来的风险请自行承担。


## 安装💿

1. 安装[定时任务](https://v2.nonebot.dev/docs/advanced/scheduler)插件

2. `pip install nonebot-plugin-fire`

在 `.env.*`中做出如下配置：

```
fire_user_id=1234567 #与该QQ号续火花
```

## 导入📲
在**bot.py** 导入，语句：
`nonebot.load_plugin("nonebot_plugin_fire")`

## 截图🖼
<p align="center">
  <img src="http://cdn.moyusoldier.cloud/截屏2022-03-07 上午10.38.56.png"
>
</p>



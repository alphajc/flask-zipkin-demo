# Flask Zipkin Demo

本项目基于 [Flask Microservice Demo](https://github.com/michaellitherland/flask-microservice-demo) 改造，结合 Zipkin 实现一个简单的分布式链路追踪的例子。使用 `flask-zipkin`实现。有关业务逻辑请查阅[原文档](https://github.com/michaellitherland/flask-microservice-demo)

# 简要说明

- Zipkin 服务端：mysql、prometheus、zipkin
- 微服务：aggregate、backend、items、orders
'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  api_root: '"//127.0.0.1/8000/api"',/*j后台接口地址*/
  user_name: '""',/*账号*/
  pass_wd: '""'/*密码*/
})

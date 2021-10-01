<template>
  <div class="login">
    <div class="box">
      <i class="el-icon-close" @click="close_login"></i>
      <div class="content">
        <div class="nav">
                    <span :class="{active: login_method === 'is_pwd'}"
                          @click="change_login_method('is_pwd')">密码登录</span>
          <span :class="{active: login_method === 'is_sms'}"
                @click="change_login_method('is_sms')">短信登录</span>
        </div>
        <el-form v-if="login_method === 'is_pwd'">
          <el-input
              placeholder="用户名/手机号/邮箱"
              prefix-icon="el-icon-user"
              v-model="username"
              clearable>
          </el-input>
          <el-input
              placeholder="密码"
              prefix-icon="el-icon-key"
              v-model="password"
              clearable
              show-password>
          </el-input>
          <el-button type="primary" @click="login">登录</el-button>
        </el-form>
        <el-form v-if="login_method === 'is_sms'">
          <el-input
              placeholder="手机号"
              prefix-icon="el-icon-phone-outline"
              v-model="mobile"
              clearable
              @blur="check_mobile">
          </el-input>
          <el-input
              placeholder="验证码"
              prefix-icon="el-icon-chat-line-round"
              v-model="sms"
              clearable>
            <template slot="append">
              <span class="sms" @click="send_sms">{{ sms_interval }}</span>
            </template>
          </el-input>
          <el-button type="primary" @click="smsLogin">登录</el-button>
        </el-form>
        <div class="foot">
          <span @click="goRegister">立即注册</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "Login",
  data() {
    return {
      username: '',
      password: '',
      mobile: '',
      sms: '',
      login_method: 'is_pwd',
      sms_interval: '获取验证码',
      is_send: false,
    }
  },
  methods: {
    close_login() {
      this.$emit('close')
    },
    goRegister() {
      this.$emit('go')
    },
    change_login_method(method) {
      this.login_method = method;
    },
    check_mobile() {
      if (!this.mobile) return;
      if (!this.mobile.match(/^1[3-9][0-9]{9}$/)) {
        this.$message({
          message: '手机号有误',
          type: 'warning',
          duration: 1000,
          onClose: () => {
            this.mobile = '';
          }
        });
        return false;
      }
      this.$axios.post(this.$url + 'user/mobile/', {'mobile': this.mobile}).then(res => {
            if (res.data.code === 200) {
              this.$message({
                message: '请获取验证码',
                type: 'success',
                duration: 1000,
                onClose: () => {
                  this.is_send = true  // 通过 is_send 来标志, 能否发送验证码
                }
              })
            } else {
              this.$message({
                message: '该手机号未注册, 请先注册',
                type: 'error',
                duration: 1000,
                onClose: () => {
                  this.mobile = ''
                  this.is_send = false
                }
              });
            }
          }
      )
    },
    send_sms() {
      if (!this.is_send) return;
      this.is_send = false;
      let sms_interval_time = 60;
      this.sms_interval = "发送中...";
      let timer = setInterval(() => {
        if (sms_interval_time <= 1) {
          clearInterval(timer);
          this.sms_interval = "获取验证码";
          this.is_send = true; // 重新回复点击发送功能的条件
        } else {
          sms_interval_time -= 1;
          this.sms_interval = `${sms_interval_time}秒后再发`;
        }
      }, 1000);
      this.$axios.get(this.$url + 'user/sms/?mobile=' + this.mobile).then(res => {
        if (res.data.code === 200) {
          this.$message({
            message: res.data.msg,
            type: 'success',
          });
        } else {
          this.$message({
            message: res.data.msg,
            type: 'error',
          });
        }
      })
    }
    ,  // 密码登录
    login() {
      if (this.username && this.password) {
        this.$axios.post(this.$url + 'user/login/', {
          username: this.username,
          password: this.password
        }).then(res => {
          if (res.data.code === 200) {
            // 登录成功, 将 token 和 username 存入 cookies
            this.$cookies.set('token', res.data.token, '7d')
            this.$cookies.set('username', res.data.username, '7d')
            // 关闭登录窗口
            this.$message({
              message: res.data.msg,
              type: 'success',
              duration: 1000,
            });
            this.$emit('close')
          } else {
            this.$message({
              message: res.data.msg[0],
              type: 'error',
              duration: 1000,
            });
          }
        })
      } else {
        this.$message({
          message: '请输入用户名或密码',
          type: 'error',
          duration: 1000,
        });
      }
    }
    ,  // 验证码登录
    smsLogin() {
      if (this.mobile && this.sms) {
        this.$axios.post(this.$url + 'user/mlogin/', {
          mobile: this.mobile,
          code: this.sms
        }).then(res => {
          if (res.data.code === 200) {
            // 登录成功, 将 token 和 username 存入 cookies
            this.$cookies.set('token', res.data.token, '7d')
            this.$cookies.set('username', res.data.username, '7d')
            this.$message({
              message: '登录成功',
              type: 'success',
              duration: 1000,
            });
            // 关闭登录窗口
            this.$emit('close')
          } else {
            this.$message({
              message: res.data.msg[0],
              type: 'error',
              duration: 1000,
            });
          }
        })
      }
    }
    ,
  }
}
</script>

<style scoped>
.login {
  width: 100vw;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 10;
  background-color: rgba(0, 0, 0, 0.3);
}

.box {
  width: 400px;
  height: 420px;
  background-color: white;
  border-radius: 10px;
  position: relative;
  top: calc(50vh - 210px);
  left: calc(50vw - 200px);
}

.el-icon-close {
  position: absolute;
  font-weight: bold;
  font-size: 20px;
  top: 10px;
  right: 10px;
  cursor: pointer;
}

.el-icon-close:hover {
  color: darkred;
}

.content {
  position: absolute;
  top: 40px;
  width: 280px;
  left: 60px;
}

.nav {
  font-size: 20px;
  height: 38px;
  border-bottom: 2px solid darkgrey;
}

.nav > span {
  margin: 0 20px 0 35px;
  color: darkgrey;
  user-select: none;
  cursor: pointer;
  padding-bottom: 10px;
  border-bottom: 2px solid darkgrey;
}

.nav > span.active {
  color: black;
  border-bottom: 3px solid black;
  padding-bottom: 9px;
}

.el-input, .el-button {
  margin-top: 40px;
}

.el-button {
  width: 100%;
  font-size: 18px;
}

.foot > span {
  float: right;
  margin-top: 20px;
  color: orange;
  cursor: pointer;
}

.sms {
  color: orange;
  cursor: pointer;
  display: inline-block;
  width: 70px;
  text-align: center;
  user-select: none;
}
</style>
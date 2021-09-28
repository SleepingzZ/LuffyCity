<template>
  <div class="header">
    <div class="slogan">
      <p>老男孩IT教育 | 帮助有志向的年轻人通过努力学习获得体面的工作和生活</p>
    </div>
    <div class="nav">
      <ul class="left-part">
        <li class="logo">
          <router-link to="/">
            <img src="../assets/img/head-logo.svg" alt="">
          </router-link>
        </li>
        <li class="ele">
          <span @click="goPage('/free-course')" :class="{active: url_path === '/free-course'}">免费课</span>
        </li>
        <li class="ele">
          <span @click="goPage('/actual-course')" :class="{active: url_path === '/actual-course'}">实战课</span>
        </li>
        <li class="ele">
          <span @click="goPage('/light-course')" :class="{active: url_path === '/light-course'}">轻课</span>
        </li>
      </ul>

      <div class="right-part">
        <div>
          <span @click="popLogin">登录</span>
          <span class="line">|</span>
          <span @click="popRegister">注册</span>
        </div>
      </div>
      <Login v-if="loginInterface" @close="closeLogin" @go="popRegister"></Login>
      <Register v-if="registerInterface" @close="closeRegister" @go="popLogin" />
    </div>
  </div>
</template>

<script>
import Login from "./Login";
import Register from "./Register";
  export default {
    name: "Header",
    data() {
      return {
        url_path: sessionStorage.url_path || '/',
        loginInterface: false,
        registerInterface: false,
      }
    },
    methods: {
      goPage(url_path) {
        // 已经是当前路由就没有必要重新跳转
        if (this.url_path !== url_path) {
          this.$router.push(url_path);
        }
        sessionStorage.url_path = url_path;
      },
      popLogin() {
        this.loginInterface = true;
        this.registerInterface = false;
      },
      popRegister() {
        this.loginInterface = false;
        this.registerInterface = true;
      },
      closeLogin() {
        this.loginInterface = false;
      },
      closeRegister() {
        this.registerInterface = false;
      }
    },
    components:{
      Login,
      Register,
    },
    created() {
      // 前端存储数据： 1、cookies -- 存储有时效；2、sessionStorage -- 临时存储，页面刷新或关闭即失效；3、localStorage -- 永久保存，清除缓存即消失
      sessionStorage.url_path = this.$route.path;
      this.url_path = this.$route.path;
    }
  }
</script>

<style scoped>
.header {
  background-color: white;
  box-shadow: 0 0 5px 0 #aaa;
}

.header:after {
  content: "";
  display: block;
  clear: both;
}

.slogan {
  background-color: #eee;
  height: 40px;
}

.slogan p {
  width: 1200px;
  margin: 0 auto;
  color: #aaa;
  font-size: 13px;
  line-height: 40px;
}

.nav {
  background-color: white;
  user-select: none;
  width: 1200px;
  margin: 0 auto;

}

.nav ul {
  padding: 15px 0;
  float: left;
}

.nav ul:after {
  clear: both;
  content: '';
  display: block;
}

.nav ul li {
  float: left;
}

.logo {
  margin-right: 20px;
}

.ele {
  margin: 0 20px;
}

.ele span {
  display: block;
  font: 15px/36px '微软雅黑';
  border-bottom: 2px solid transparent;
  cursor: pointer;
}

.ele span:hover {
  border-bottom-color: orange;
}

.ele span.active {
  color: orange;
  border-bottom-color: orange;
}

.right-part {
  float: right;
}

.right-part .line {
  margin: 0 10px;
}

.right-part span {
  line-height: 68px;
  cursor: pointer;
}
</style>